/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { ActionLog, AlarmItem, LearningTrack, Mission, MissionResult, ScadaState } from '../types';
import { computeMissionXP, computeStarsFromScore, formatNumberID } from '../utils/gamification';

export const INITIAL_SCADA_STATE: ScadaState = {
  intakePump1Running: true,
  intakePump2Running: false,
  intakePumpDuty: 1,
  intakePumpTripped: false,
  rawWaterFlow: 100,
  rawWaterTurbidity: 20.0,

  coagulantDoseSetpoint: 20,
  coagulantActualDose: 20,
  waterPh: 7.2,
  flashMixerRunning: true,

  flocculatorMixerRunning: true,
  flocculatorRpm: 18,
  flocQualityScore: 88,

  clarifierBlowdownOpen: false,
  sludgeLevelPercent: 28,
  settledWaterTurbidity: 2.0,

  filter1Active: true,
  filter2Active: true,
  filter1Headloss: 0.8,
  filter2Headloss: 0.9,
  filter1Backwashing: false,
  filter2Backwashing: false,
  filteredWaterTurbidity: 1.1,

  chlorineDoseSetpoint: 1.5,
  freeResidualChlorine: 0.35,

  reservoirInletOpen: true,
  reservoirOutletOpen: true,
  reservoirLevelMeters: 4.2,
  reservoirLevelPercent: 84,

  distPump1Running: true,
  distPump2Running: false,
  distPumpDuty: 1,
  distPumpTripped: false,
  distDischargePressure: 4.1,
  distTotalFlow: 45,

  valveZone1Open: true,
  valveZone2Open: true,
  valveIsolasiBocorOpen: true,
  prvSetpointBar: 2.5,
  zone1Pressure: 2.4,
  zone2Pressure: 2.2,
  zone1Flow: 28,
  zone2Flow: 19,
  pipeLeakActive: false,
  leakFlowSurge: 0,
  zoneChlorineEnd: 0.26,
};

export function createInitialScadaState(mission: Mission): ScadaState {
  const base: ScadaState = { ...INITIAL_SCADA_STATE };

  // Kondisi awal normal sesuai misi (selalu mulai 00:00 tanpa alarm aktif)
  switch (mission.code) {
    case 'IPA-02':
      base.intakePump1Running = false;
      base.rawWaterFlow = 0;
      break;
    case 'IPA-04':
      base.filter1Headloss = 1.85;
      break;
    case 'DST-02':
      base.distPump1Running = false;
      base.distDischargePressure = 0.5;
      base.distTotalFlow = 0;
      base.zone1Pressure = 0.6;
      base.zone2Pressure = 0.5;
      break;
    case 'DST-04':
      base.chlorineDoseSetpoint = 1.25;
      base.freeResidualChlorine = 0.23;
      base.zoneChlorineEnd = 0.14;
      break;
    default:
      break;
  }

  return base;
}

export function formatSimTime(sec: number): string {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

export function tickSimulation(
  current: ScadaState,
  mission: Mission,
  elapsedSec: number,
  existingAlarms: AlarmItem[],
  _actionLogs: ActionLog[],
  turbidityStableCount: number,
  chlorineStableCount: number,
  pressureStableCount: number,
  simTrack: LearningTrack = 'terpadu'
): {
  nextScada: ScadaState;
  alarms: AlarmItem[];
  nextTurbidityStableCount: number;
  nextChlorineStableCount: number;
  nextPressureStableCount: number;
  isParameterStable: boolean;
} {
  const next: ScadaState = { ...current };
  let alarms = existingAlarms.map((a) => ({ ...a }));

  const allowIpaAlarms = simTrack === 'ipa' || simTrack === 'terpadu';
  const allowDistAlarms = simTrack === 'distribusi' || simTrack === 'terpadu';

  const triggerTurbiditySpike = (sec: number) => {
    if (!allowIpaAlarms) return;
    next.rawWaterTurbidity = 185.0;
    if (!alarms.some((a) => a.id === 'alarm-intake-turb')) {
      const snap = formatNumberID(185.0, 1, 'NTU');
      alarms.push({
        id: 'alarm-intake-turb',
        timestamp: formatSimTime(sec),
        timestampSec: sec,
        priority: 'sedang',
        controlPointId: 'intake',
        controlPointName: 'Intake Air Baku',
        message: `Kekeruhan air baku tinggi (${snap}, ambang normal ≤ 50 NTU)`,
        triggerSnapshotValue: snap,
        status: 'aktif_belum_diakui',
        clearMethod: 'auto',
      });
    }
  };

  const triggerPipeLeak = (sec: number) => {
    if (!allowDistAlarms) return;
    next.pipeLeakActive = true;
    if (!alarms.some((a) => a.id === 'alarm-leak')) {
      const flowSnap = formatNumberID(next.valveZone1Open ? 48 : 20, 0, 'L/s');
      const pressSnap = formatNumberID(Math.max(0.6, next.prvSetpointBar - 1.3), 2, 'bar');
      const snap = `Debit ${flowSnap} · Tekanan ${pressSnap}`;
      alarms.push({
        id: 'alarm-leak',
        timestamp: formatSimTime(sec),
        timestampSec: sec,
        priority: 'tinggi',
        controlPointId: 'valve_prv',
        controlPointName: 'Valve Zona & PRV',
        message: `Pipa Distribusi Zona 1 Bocor! Debit saat kejadian: ${flowSnap} · Tekanan: ${pressSnap}`,
        triggerSnapshotValue: snap,
        status: 'aktif_belum_diakui',
        clearMethod: 'auto',
      });
    }
  };

  // 1. Trigger scenario disturbances at exact triggerTimeSec
  mission.disturbances.forEach((dist) => {
    if (elapsedSec === dist.triggerTimeSec) {
      if (dist.type === 'kekeruhan_lonjakan') {
        triggerTurbiditySpike(elapsedSec);
      }

      if (dist.type === 'pompa_trip') {
        if (simTrack === 'distribusi') {
          next.distPump1Running = false;
          next.distPumpTripped = true;
          const distFlowAtTrip = next.distPump2Running ? 45 : 0;
          if (!alarms.some((a) => a.id === 'alarm-dist-trip')) {
            const snap = `Aliran ${formatNumberID(distFlowAtTrip, 0, 'L/s')}`;
            alarms.push({
              id: 'alarm-dist-trip',
              timestamp: formatSimTime(elapsedSec),
              timestampSec: elapsedSec,
              priority: 'kritis',
              controlPointId: 'pompa_distribusi',
              controlPointName: 'Pompa Distribusi',
              message: `Pompa Distribusi P-101 Trip Overload! Aliran saat kejadian: ${formatNumberID(distFlowAtTrip, 0, 'L/s')}`,
              triggerSnapshotValue: snap,
              status: 'aktif_belum_diakui',
              isLatched: true,
              latchedResetDone: false,
              clearMethod: 'manual',
            });
          }
        } else if (allowIpaAlarms) {
          next.intakePump1Running = false;
          next.intakePumpTripped = true;
          next.rawWaterFlow = next.intakePump2Running ? 100 : 0;
          if (!alarms.some((a) => a.id === 'alarm-intake-trip')) {
            const snap = `Aliran ${formatNumberID(next.rawWaterFlow, 0, 'L/s')}`;
            alarms.push({
              id: 'alarm-intake-trip',
              timestamp: formatSimTime(elapsedSec),
              timestampSec: elapsedSec,
              priority: 'kritis',
              controlPointId: 'intake',
              controlPointName: 'Intake & Pompa Air Baku',
              message: `Pompa Intake P1 Trip Overload! Aliran saat kejadian: ${formatNumberID(next.rawWaterFlow, 0, 'L/s')}`,
              triggerSnapshotValue: snap,
              status: 'aktif_belum_diakui',
              isLatched: true,
              latchedResetDone: false,
              clearMethod: 'manual',
            });
          }
        }
      }

      if (dist.type === 'klor_salah' && allowIpaAlarms) {
        next.chlorineDoseSetpoint = 0.4;
        next.freeResidualChlorine = 0.08;
        if (!alarms.some((a) => a.id === 'alarm-cl-low')) {
          const snap = formatNumberID(next.freeResidualChlorine, 2, 'mg/L');
          alarms.push({
            id: 'alarm-cl-low',
            timestamp: formatSimTime(elapsedSec),
            timestampSec: elapsedSec,
            priority: 'kritis',
            controlPointId: 'desinfeksi',
            controlPointName: 'Desinfeksi (Klorinasi)',
            message: `Sisa klor bebas < 0,20 mg/L (Terukur saat kejadian: ${snap})! Periksa pompa dosing klor.`,
            triggerSnapshotValue: snap,
            status: 'aktif_belum_diakui',
            clearMethod: 'auto',
          });
        }
      }

      if (dist.type === 'pipa_bocor') {
        triggerPipeLeak(elapsedSec);
      }

      if (dist.type === 'tekanan_drop' && allowDistAlarms) {
        next.prvSetpointBar = 1.4;
        next.zone1Pressure = 1.3;
        if (!alarms.some((a) => a.id === 'alarm-pdrop')) {
          const snap = formatNumberID(next.zone1Pressure, 2, 'bar');
          alarms.push({
            id: 'alarm-pdrop',
            timestamp: formatSimTime(elapsedSec),
            timestampSec: elapsedSec,
            priority: 'tinggi',
            controlPointId: 'titik_pantau_jaringan',
            controlPointName: 'Titik Pantau Jaringan',
            message: `Tekanan zona di bawah batas layanan (< 2,00 bar · Terukur saat kejadian: ${snap})!`,
            triggerSnapshotValue: snap,
            status: 'aktif_belum_diakui',
            clearMethod: 'auto',
          });
        }
      }

      if (dist.type === 'hulu_hilir') {
        triggerTurbiditySpike(elapsedSec);
        triggerPipeLeak(elapsedSec);
      }
    }
  });

  // 2. Continuous Physics & Process Mass Balance calculations
  // Intake Flow (preserve manual flow adjustments when at least 1 pump is running)
  const intakePumpsActive = (next.intakePump1Running ? 1 : 0) + (next.intakePump2Running ? 1 : 0);
  if (intakePumpsActive === 0) {
    next.rawWaterFlow = 0;
  } else if (current.rawWaterFlow === 0) {
    next.rawWaterFlow = 100;
  }

  // Coagulation Chemistry Response
  // Normal 20 NTU needs ~18–25 mg/L PAC; 185 NTU flood needs ~45–52 mg/L PAC
  const targetPac = next.rawWaterTurbidity <= 35 ? 20 : Math.max(20, next.rawWaterTurbidity * 0.22 + 8);
  const pacRatio = next.coagulantActualDose / targetPac;
  const retentionBonus = next.rawWaterFlow <= 80 && next.rawWaterFlow > 0 ? 0.1 : 0;

  if (next.flashMixerRunning) {
    if (intakePumpsActive > 0) {
      if (pacRatio + retentionBonus >= 0.85 && pacRatio <= 2.6) {
        next.flocQualityScore = Math.min(95, next.flocQualityScore + 3);
      } else {
        next.flocQualityScore = Math.max(25, next.flocQualityScore - 5);
      }
    } else {
      // Saat pompa intake berhenti sementara (misal trip/transisi ke P2),
      // perubahan debit tidak boleh menjatuhkan mutu koagulasi bila air baku & PAC normal.
      if (next.rawWaterTurbidity > 35 && pacRatio < 0.85) {
        next.flocQualityScore = Math.max(25, next.flocQualityScore - 2);
      }
    }
  } else {
    next.flocQualityScore = Math.max(15, next.flocQualityScore - 4);
  }

  // Sedimentation settling
  if (next.flocQualityScore >= 70 && next.flocculatorMixerRunning && next.waterPh >= 6.5 && next.waterPh <= 8.5) {
    const settleRate = next.rawWaterFlow <= 80 ? 0.84 : 0.9;
    next.settledWaterTurbidity = Math.max(1.5, next.settledWaterTurbidity * settleRate + 1.5 * (1 - settleRate));
  } else if (intakePumpsActive > 0 || next.rawWaterTurbidity > 35) {
    next.settledWaterTurbidity = Math.min(18.0, next.settledWaterTurbidity + 0.9);
  }

  // Filtration performance
  if (next.filter1Backwashing) {
    next.filter1Headloss = Math.max(0.5, next.filter1Headloss - 0.15);
    if (next.filter1Headloss <= 0.55) {
      next.filter1Backwashing = false;
    }
  } else {
    next.filter1Headloss = Math.min(3.0, next.filter1Headloss + 0.001);
  }

  if (next.filter2Backwashing) {
    next.filter2Headloss = Math.max(0.5, next.filter2Headloss - 0.15);
    if (next.filter2Headloss <= 0.55) {
      next.filter2Backwashing = false;
    }
  } else {
    next.filter2Headloss = Math.min(3.0, next.filter2Headloss + 0.001);
  }

  // Filtered water turbidity
  const filterClogged = next.filter1Headloss > 2.2 || next.filter2Headloss > 2.2;
  if (next.settledWaterTurbidity < 4.5 && !filterClogged) {
    const recoveryFactor = next.rawWaterFlow <= 80 ? 0.82 : 0.88;
    next.filteredWaterTurbidity = Math.max(
      0.9,
      next.filteredWaterTurbidity * recoveryFactor + 1.0 * (1 - recoveryFactor)
    );
  } else if (intakePumpsActive > 0 || next.rawWaterTurbidity > 35 || filterClogged) {
    next.filteredWaterTurbidity = Math.min(8.0, next.filteredWaterTurbidity + 0.25);
  }

  // Raise high turbidity alarm on filtrasi whenever treated water >= 3,0 NTU (IPA/Terpadu only)
  if (allowIpaAlarms && next.filteredWaterTurbidity >= 3.0) {
    if (!alarms.some((a) => a.id === 'alarm-filt-turb' && a.status !== 'clear')) {
      const existingCleared = alarms.find((a) => a.id === 'alarm-filt-turb');
      if (!existingCleared) {
        const snap = formatNumberID(next.filteredWaterTurbidity, 2, 'NTU');
        alarms.push({
          id: 'alarm-filt-turb',
          timestamp: formatSimTime(elapsedSec),
          timestampSec: elapsedSec,
          priority: 'tinggi',
          controlPointId: 'filtrasi',
          controlPointName: 'Filtrasi (Air Olahan)',
          message: `Kekeruhan air olahan ≥ 3,0 NTU (Terukur saat kejadian: ${snap})`,
          triggerSnapshotValue: snap,
          status: 'aktif_belum_diakui',
          clearMethod: 'auto',
        });
      }
    }
  }

  // Disinfection residual (Permenkes 0,2 - 0,5 mg/L)
  // setpoint 1.5 -> 0.35 mg/L; setpoint 1.6 -> 0.40 mg/L; setpoint 0.4 -> 0.08 mg/L
  const calculatedResidual = Math.max(0.08, (next.chlorineDoseSetpoint - 1.0) * 0.5 + 0.1);
  next.freeResidualChlorine = Math.max(
    0.05,
    Math.min(1.2, next.freeResidualChlorine * 0.78 + calculatedResidual * 0.22)
  );

  // Reservoir Level Balance
  const inflowRate = (next.intakePump1Running || next.intakePump2Running) && next.reservoirInletOpen ? 50 : 0;
  const distPumpsActive = (next.distPump1Running ? 1 : 0) + (next.distPump2Running ? 1 : 0);
  const outflowRate = next.reservoirOutletOpen ? distPumpsActive * 25 : 0;
  const netFlow = inflowRate - outflowRate;

  next.reservoirLevelMeters = Math.max(0.5, Math.min(5.0, next.reservoirLevelMeters + netFlow * 0.0005));
  next.reservoirLevelPercent = Math.round((next.reservoirLevelMeters / 5.0) * 100);

  // Distribution Hydraulics (L/s)
  if (distPumpsActive === 0) {
    next.distDischargePressure = 0.5;
    next.distTotalFlow = 0;
  } else if (distPumpsActive === 1) {
    next.distDischargePressure = 4.1;
    next.distTotalFlow = 45;
  } else {
    next.distDischargePressure = 4.6;
    next.distTotalFlow = 64;
  }

  // Zone pressures & leak physics (both PRV setpoint and extra pump boost affect zone pressure)
  const pumpBoost = distPumpsActive >= 2 ? 0.8 : distPumpsActive === 0 ? -1.8 : 0;
  let leakFlow = 0;
  if (next.pipeLeakActive && next.valveIsolasiBocorOpen) {
    leakFlow = 20;
    next.zone1Pressure = Math.max(0.6, Number((next.prvSetpointBar - 1.3 + pumpBoost).toFixed(2)));
    next.zone2Pressure = Math.max(0.8, Number((next.prvSetpointBar - 0.9 + pumpBoost).toFixed(2)));
  } else {
    next.zone1Pressure = next.valveZone1Open
      ? Math.max(0.4, Math.min(3.5, Number((next.prvSetpointBar - 0.1 + pumpBoost).toFixed(2))))
      : 0;
    next.zone2Pressure = next.valveZone2Open
      ? Math.max(0.4, Math.min(3.2, Number((next.prvSetpointBar - 0.3 + pumpBoost).toFixed(2))))
      : 0;
  }

  next.zone1Flow = (next.valveZone1Open ? 28 : 0) + (next.pipeLeakActive && next.valveIsolasiBocorOpen ? leakFlow : 0);
  next.zone2Flow = next.valveZone2Open ? 19 : 0;
  next.leakFlowSurge = leakFlow;
  next.zoneChlorineEnd = Math.max(0.05, Number((next.freeResidualChlorine - 0.09).toFixed(2)));

  // 3. Automated Alarm Auto-Clear with stability deadband (PRD §10)
  let nextTurbidityCount = turbidityStableCount;
  let nextChlorineCount = chlorineStableCount;
  let nextPressureCount = pressureStableCount;

  // Turbidity auto-clear (<= 2,7 NTU for 10 consecutive seconds)
  if (next.filteredWaterTurbidity <= 2.7) {
    nextTurbidityCount += 1;
  } else {
    nextTurbidityCount = 0;
  }

  if (nextTurbidityCount >= 10) {
    alarms = alarms.map((a) => {
      if ((a.controlPointId === 'filtrasi' || a.controlPointId === 'koagulasi') && a.status !== 'clear') {
        return {
          ...a,
          status: 'clear',
          clearMethod: 'auto',
          clearedAtSec: elapsedSec,
          clearedTimestamp: formatSimTime(elapsedSec),
          clearNote: `Pulih otomatis: kekeruhan air olahan ≤ 2,7 NTU stabil 10 detik (saat clear: ${formatNumberID(next.filteredWaterTurbidity, 2, 'NTU')})`,
        };
      }
      return a;
    });

    // Once treated water has stabilized for 10s, upstream turbidity flood begins receding
    if (next.rawWaterTurbidity > 35 && next.coagulantActualDose >= 42) {
      next.rawWaterTurbidity = Math.max(25, next.rawWaterTurbidity - 15);
    }
  }

  if (next.rawWaterTurbidity <= 50) {
    alarms = alarms.map((a) => {
      if (a.id === 'alarm-intake-turb' && a.status !== 'clear') {
        return {
          ...a,
          status: 'clear',
          clearMethod: 'auto',
          clearedAtSec: elapsedSec,
          clearedTimestamp: formatSimTime(elapsedSec),
          clearNote: `Pulih otomatis: kekeruhan air baku kembali normal (saat clear: ${formatNumberID(next.rawWaterTurbidity, 1, 'NTU')})`,
        };
      }
      return a;
    });
  }

  // Chlorine auto-clear (0,20 - 0,50 mg/L for 10 consecutive seconds)
  if (next.freeResidualChlorine >= 0.2 && next.freeResidualChlorine <= 0.5) {
    nextChlorineCount += 1;
  } else {
    nextChlorineCount = 0;
  }

  if (nextChlorineCount >= 10) {
    alarms = alarms.map((a) => {
      if (a.controlPointId === 'desinfeksi' && a.status !== 'clear') {
        return {
          ...a,
          status: 'clear',
          clearMethod: 'auto',
          clearedAtSec: elapsedSec,
          clearedTimestamp: formatSimTime(elapsedSec),
          clearNote: `Pulih otomatis: sisa klor kembali dalam rentang 0,20–0,50 mg/L selama 10 detik (saat clear: ${formatNumberID(next.freeResidualChlorine, 2, 'mg/L')})`,
        };
      }
      return a;
    });
  }

  // Zone pressure / leak auto-clear (pressure in service range >= 2,00 bar for 10 consecutive seconds)
  if (next.zone1Pressure >= 2.0 && (!next.pipeLeakActive || !next.valveIsolasiBocorOpen)) {
    nextPressureCount += 1;
  } else {
    nextPressureCount = 0;
  }

  if (nextPressureCount >= 10) {
    alarms = alarms.map((a) => {
      if ((a.controlPointId === 'valve_prv' || a.controlPointId === 'titik_pantau_jaringan') && a.status !== 'clear') {
        return {
          ...a,
          status: 'clear',
          clearMethod: 'auto',
          clearedAtSec: elapsedSec,
          clearedTimestamp: formatSimTime(elapsedSec),
          clearNote: `Pulih otomatis: tekanan layanan jaringan kembali normal (saat clear: ${formatNumberID(next.zone1Pressure, 2, 'bar')})`,
        };
      }
      return a;
    });
  }

  // Latched Pump Trip Alarm state check
  alarms = alarms.map((a) => {
    if (a.isLatched && a.status !== 'clear') {
      if (a.controlPointId === 'intake' && !next.intakePumpTripped) {
        return { ...a, status: 'pulih_belum_clear', latchedResetDone: true };
      }
      if (a.controlPointId === 'pompa_distribusi' && !next.distPumpTripped) {
        return { ...a, status: 'pulih_belum_clear', latchedResetDone: true };
      }
    }
    return a;
  });

  // Catatan: message & triggerSnapshotValue dipertahankan sebagai snapshot tepat saat kejadian alarm
  // (PRD §10 Pencatatan: log tidak menimpa nilai historis kejadian dengan nilai proses terkini).

  const isParameterStable =
    (!allowIpaAlarms ||
      (next.filteredWaterTurbidity < 3.0 &&
        next.freeResidualChlorine >= 0.2 &&
        next.freeResidualChlorine <= 0.5)) &&
    (!allowDistAlarms || next.zone1Pressure >= 2.0);

  return {
    nextScada: next,
    alarms,
    nextTurbidityStableCount: nextTurbidityCount,
    nextChlorineStableCount: nextChlorineCount,
    nextPressureStableCount: nextPressureCount,
    isParameterStable,
  };
}

export function evaluateMissionScore(
  mission: Mission,
  durationSec: number,
  actionLogs: ActionLog[],
  alarmLogs: AlarmItem[],
  stabilityHistoryCount: { stable: number; total: number },
  hintsUsedCount: number,
  userId: string,
  tenantId: string,
  track: LearningTrack,
  trendHistory: Array<any>,
  timedOut = false
): MissionResult {
  // Pisahkan percobaan Clear prematur ("Penyebab belum ditangani") dari tindakan kontrol/SOP lain
  // dan dari Tindakan Tidak Aman (-15 Poin).
  const prematureClearErrors = actionLogs.filter(
    (a) => a.isCorrect === false && a.action.includes('Percobaan Clear Alarm')
  ).length;
  const operationalActions = actionLogs.filter(
    (a) => !a.action.includes('Percobaan Clear Alarm')
  );

  // 1. Ketepatan tindakan (40%)
  const correctActions = operationalActions.filter((a) => a.isCorrect !== false).length;
  const totalActions = Math.max(1, operationalActions.length);
  const scoreTindakan =
    operationalActions.length === 0 && alarmLogs.length > 0
      ? 20
      : Math.min(40, Math.round((correctActions / totalActions) * 40));

  // 2. Waktu respons (25%)
  const targetTime = mission.durationLimitSec || 300;
  let scoreWaktuRespons = 25;
  if (durationSec > targetTime) {
    const overSec = durationSec - targetTime;
    scoreWaktuRespons = Math.max(10, Math.round(25 - (overSec / targetTime) * 15));
  } else if (timedOut) {
    scoreWaktuRespons = 12;
  }

  // 3. Stabilitas parameter (20%)
  const stabilityRatio =
    stabilityHistoryCount.total > 0 ? stabilityHistoryCount.stable / stabilityHistoryCount.total : 0.85;
  const scoreStabilitas = Math.min(20, Math.round(stabilityRatio * 20));

  // 4. Penanganan alarm (15%) — termasuk pengurangan poin akibat Clear sebelum penyebab ditangani
  const allAlarms = alarmLogs;
  const handledAlarms = allAlarms.filter((a) => a.status === 'clear' || a.status === 'pulih_belum_clear').length;
  const totalAlarms = Math.max(1, allAlarms.length);
  const baseAlarmScore = allAlarms.length === 0 ? 15 : Math.min(15, Math.round((handledAlarms / totalAlarms) * 15));
  const scoreAlarm = Math.max(0, baseAlarmScore - prematureClearErrors * 4);

  // Deductions: -5 per hint used, -15 per unsafe action (strictly NOT premature Clear)
  const unsafeDeduction =
    actionLogs.filter(
      (a) =>
        a.isCorrect === false &&
        !a.action.includes('Percobaan Clear Alarm') &&
        (a.action.includes('Tidak Aman') || Boolean(a.feedback?.includes('Tindakan Tidak Aman')))
    ).length * 15;
  const hintDeduction = hintsUsedCount * 5;
  const scoreDeductions = unsafeDeduction + hintDeduction;

  const rawTotal = scoreTindakan + scoreWaktuRespons + scoreStabilitas + scoreAlarm - scoreDeductions;
  let totalScore = Math.max(0, Math.min(100, rawTotal));

  // Passing criteria (PRD §8: Graduation exam ALWAYS fails when time expires)
  const passScore = mission.passScore || 70;
  let isPassed = totalScore >= passScore;
  if (mission.level === 5 && timedOut) {
    isPassed = false;
    totalScore = Math.min(totalScore, passScore - 1);
  }

  const stars = computeStarsFromScore(totalScore, passScore);
  const xpEarned = computeMissionXP(mission, totalScore, isPassed);

  // Enrich alarmLogs with actionSummary from corrective actions if missing
  const enrichedAlarmLogs: AlarmItem[] = alarmLogs.map((a) => {
    if (a.actionSummary) return a;
    const endSec = a.clearedAtSec ?? durationSec;
    const related = operationalActions.filter(
      (l) =>
        l.isCorrect !== false &&
        l.timestampSec >= a.timestampSec &&
        l.timestampSec <= endSec &&
        !l.action.startsWith('Acknowledge') &&
        !l.action.startsWith('Manual Clear')
    );
    const summary =
      related.length > 0
        ? related.map((r) => `${r.action}${r.value !== undefined && r.value !== 'RESET_OK' ? ` (${r.value})` : ''}`).join('; ')
        : a.status === 'clear'
        ? a.clearMethod === 'auto'
          ? 'Parameter proses pulih ke rentang aman'
          : 'Penanganan selesai'
        : 'Belum ada tindakan koreksi';
    return {
      ...a,
      actionSummary: summary,
    };
  });

  return {
    id: `result-${Date.now()}`,
    userId,
    tenantId,
    missionCode: mission.code,
    track,
    completedAt: new Date().toISOString(),
    durationSec,
    scoreTindakan,
    scoreWaktuRespons,
    scoreStabilitas,
    scoreAlarm,
    scoreDeductions,
    totalScore,
    stars,
    xpEarned,
    hintsUsedCount,
    isPassed,
    actionLogs,
    alarmLogs: enrichedAlarmLogs,
    trendHistory,
  };
}

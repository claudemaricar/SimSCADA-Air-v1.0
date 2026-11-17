/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { ActionLog, AlarmItem, AlarmPriority, LearningTrack, Mission, MissionResult, ScadaState } from '../../types';
import { useApp } from '../../context/AppContext';
import { CONTROL_POINTS } from '../../data/seedData';
import {
  createInitialScadaState,
  evaluateMissionScore,
  formatSimTime,
  tickSimulation,
} from '../../engine/simulationEngine';
import { ScadaMimic } from '../simulator/ScadaMimic';
import { ControlPanel } from '../simulator/ControlPanel';
import { AlarmPanel } from '../simulator/AlarmPanel';
import { TrendChart, TrendParamKey } from '../simulator/TrendChart';
import { NarrativeModal } from '../simulator/NarrativeModal';
import { scadaAudio } from '../../utils/audio';
import {
  Building2,
  Check,
  Lightbulb,
  StopCircle,
} from 'lucide-react';

interface ScadaSimulatorProps {
  mission: Mission;
  onFinishMission: (result: MissionResult) => void;
  onExit: () => void;
}

const PRIORITY_RANK: Record<AlarmPriority, number> = {
  kritis: 4,
  tinggi: 3,
  sedang: 2,
  info: 1,
};

const getRecoveryHintForAlarm = (alarm: AlarmItem): string => {
  switch (alarm.id) {
    case 'alarm-intake-trip':
      return 'Jalankan P2 (Standby), Reset Proteksi Trip di Intake, lalu Clear Manual';
    case 'alarm-dist-trip':
      return 'Jalankan P-102 (Standby), Reset Proteksi Trip Pompa Distribusi, lalu Clear Manual';
    case 'alarm-filt-turb':
      return 'Auto-Clear aktif setelah kekeruhan air olahan ≤ 2,7 NTU stabil 10 dtk';
    case 'alarm-intake-turb':
      return 'Auto-Clear aktif setelah kekeruhan air baku kembali ≤ 50 NTU';
    case 'alarm-cl-low':
      return 'Auto-Clear aktif setelah sisa klor kembali di 0,20–0,50 mg/L stabil 10 dtk';
    case 'alarm-leak':
      return 'Tutup Valve Isolasi Ruas Bocor & pulihkan tekanan ≥ 2,00 bar';
    case 'alarm-pdrop':
      return 'Pulihkan tekanan zona ≥ 2,00 bar (atur PRV atau tambah P-102)';
    default:
      return alarm.isLatched
        ? 'Reset proteksi di panel kontrol lalu tekan Clear Manual'
        : 'Pulihkan parameter ke rentang aman untuk Auto-Clear';
  }
};

export const L5_ScadaSimulator: React.FC<ScadaSimulatorProps> = ({
  mission,
  onFinishMission,
}) => {
  const { currentUser, currentTenant, activeTrack, saveMissionResult, showTechnicalRefs } = useApp();

  // Tentukan jalur aktif sesi simulasi berdasarkan akun dan kode misi
  const userTrack = currentUser?.track || activeTrack;
  const simTrack: LearningTrack = useMemo(() => {
    if (userTrack === 'terpadu') return 'terpadu';
    if (mission.code.startsWith('DST-')) return 'distribusi';
    if (mission.code.startsWith('IPA-')) return 'ipa';
    return userTrack;
  }, [userTrack, mission.code]);

  const initialUnit = simTrack === 'distribusi' || mission.code.startsWith('DST-') ? 'reservoir' : 'intake';
  const durationLimitSec = mission.durationLimitSec || 300;
  const isExamMission = mission.level === 5;

  const initialScada = useMemo(() => createInitialScadaState(mission), [mission]);

  const [scada, setScada] = useState<ScadaState>(initialScada);
  const [elapsedSec, setElapsedSec] = useState<number>(0);
  const [selectedUnit, setSelectedUnit] = useState<string>(initialUnit);
  const [hintsUsedCount, setHintsUsedCount] = useState<number>(0);
  const [showHintModal, setShowHintModal] = useState<boolean>(false);
  const [currentNarrativeUnit, setCurrentNarrativeUnit] = useState<string | null>(null);
  const [alarms, setAlarms] = useState<AlarmItem[]>([]);
  const [actionLogs, setActionLogs] = useState<ActionLog[]>([]);
  const [ackTimeMap, setAckTimeMap] = useState<Record<string, string>>({});
  const [stableTicks, setStableTicks] = useState<number>(0);
  const [trendHistory, setTrendHistory] = useState<Array<{
    timeSec: number;
    turbidity: number;
    settledTurbidity: number;
    freeChlorine: number;
    reservoirLevel: number;
    zonePressure: number;
    zoneFlow: number;
  }>>(() => [
    {
      timeSec: 0,
      turbidity: initialScada.filteredWaterTurbidity,
      settledTurbidity: initialScada.settledWaterTurbidity,
      freeChlorine: initialScada.freeResidualChlorine,
      reservoirLevel: initialScada.reservoirLevelMeters,
      zonePressure: initialScada.zone1Pressure,
      zoneFlow: initialScada.zone1Flow,
    },
  ]);

  // Mutable refs for 1 Hz simulation loop without stale closures
  const scadaRef = useRef<ScadaState>(initialScada);
  const elapsedSecRef = useRef<number>(0);
  const alarmsRef = useRef<AlarmItem[]>([]);
  const actionLogsRef = useRef<ActionLog[]>([]);
  const turbidityStableRef = useRef<number>(0);
  const chlorineStableRef = useRef<number>(0);
  const pressureStableRef = useRef<number>(0);
  const stableTicksRef = useRef<number>(0);
  const hintsUsedRef = useRef<number>(0);
  const trendHistoryRef = useRef(trendHistory);
  const isRunningRef = useRef<boolean>(true);
  const isFinishedRef = useRef<boolean>(false);

  const finishSession = useCallback(
    (finalSec: number, timedOut = false) => {
      if (isFinishedRef.current) return;
      isFinishedRef.current = true;
      isRunningRef.current = false;
      scadaAudio.stopAlarmSound();

      const result = evaluateMissionScore(
        mission,
        finalSec,
        actionLogsRef.current,
        alarmsRef.current,
        { stable: stableTicksRef.current, total: Math.max(1, finalSec) },
        hintsUsedRef.current,
        currentUser?.id || 'user-peserta-ipa',
        currentTenant.id,
        simTrack,
        trendHistoryRef.current,
        timedOut
      );

      saveMissionResult(result);
      onFinishMission(result);
    },
    [mission, currentUser?.id, currentTenant.id, simTrack, saveMissionResult, onFinishMission]
  );

  // Reset entire session state when mission or user changes
  useEffect(() => {
    const fresh = createInitialScadaState(mission);
    const freshTrend = [
      {
        timeSec: 0,
        turbidity: fresh.filteredWaterTurbidity,
        settledTurbidity: fresh.settledWaterTurbidity,
        freeChlorine: fresh.freeResidualChlorine,
        reservoirLevel: fresh.reservoirLevelMeters,
        zonePressure: fresh.zone1Pressure,
        zoneFlow: fresh.zone1Flow,
      },
    ];

    scadaRef.current = fresh;
    elapsedSecRef.current = 0;
    alarmsRef.current = [];
    actionLogsRef.current = [];
    turbidityStableRef.current = 0;
    chlorineStableRef.current = 0;
    pressureStableRef.current = 0;
    stableTicksRef.current = 0;
    hintsUsedRef.current = 0;
    trendHistoryRef.current = freshTrend;
    isRunningRef.current = true;
    isFinishedRef.current = false;

    setScada(fresh);
    setElapsedSec(0);
    setSelectedUnit(initialUnit);
    setAlarms([]);
    setActionLogs([]);
    setAckTimeMap({});
    setHintsUsedCount(0);
    setShowHintModal(false);
    setCurrentNarrativeUnit(null);
    setStableTicks(0);
    setTrendHistory(freshTrend);
    scadaAudio.stopAlarmSound();
  }, [mission, currentUser?.id, initialUnit]);

  // 1-Hz Real-Time Simulation Loop
  useEffect(() => {
    const timer = window.setInterval(() => {
      if (!isRunningRef.current || isFinishedRef.current) return;

      const nextSec = elapsedSecRef.current + 1;
      const simRes = tickSimulation(
        scadaRef.current,
        mission,
        nextSec,
        alarmsRef.current,
        actionLogsRef.current,
        turbidityStableRef.current,
        chlorineStableRef.current,
        pressureStableRef.current,
        simTrack
      );

      scadaRef.current = simRes.nextScada;
      alarmsRef.current = simRes.alarms;
      elapsedSecRef.current = nextSec;
      turbidityStableRef.current = simRes.nextTurbidityStableCount;
      chlorineStableRef.current = simRes.nextChlorineStableCount;
      pressureStableRef.current = simRes.nextPressureStableCount;

      if (simRes.isParameterStable) {
        stableTicksRef.current += 1;
        setStableTicks(stableTicksRef.current);
      }

      const newTrendPoint = {
        timeSec: nextSec,
        turbidity: simRes.nextScada.filteredWaterTurbidity,
        settledTurbidity: simRes.nextScada.settledWaterTurbidity,
        freeChlorine: simRes.nextScada.freeResidualChlorine,
        reservoirLevel: simRes.nextScada.reservoirLevelMeters,
        zonePressure: simRes.nextScada.zone1Pressure,
        zoneFlow: simRes.nextScada.zone1Flow,
      };
      const nextTrend = [...trendHistoryRef.current.slice(-119), newTrendPoint];
      trendHistoryRef.current = nextTrend;

      setScada(simRes.nextScada);
      setAlarms(simRes.alarms);
      setElapsedSec(nextSec);
      setTrendHistory(nextTrend);

      if (nextSec >= durationLimitSec) {
        finishSession(durationLimitSec, true);
      }
    }, 1000);

    return () => {
      window.clearInterval(timer);
      scadaAudio.stopAlarmSound();
    };
  }, [mission, simTrack, durationLimitSec, finishSession]);

  // Sync alarm audio with unacknowledged alarms
  const unackCount = useMemo(
    () => alarms.filter((a) => a.status === 'aktif_belum_diakui').length,
    [alarms]
  );
  const prevUnackCountRef = useRef<number>(0);

  useEffect(() => {
    if (unackCount > prevUnackCountRef.current) {
      const hasKritis = alarms.some(
        (a) => a.status === 'aktif_belum_diakui' && a.priority === 'kritis'
      );
      const hasTinggi = alarms.some(
        (a) => a.status === 'aktif_belum_diakui' && a.priority === 'tinggi'
      );
      scadaAudio.playAlarmBeep(hasKritis ? 'kritis' : hasTinggi ? 'tinggi' : 'sedang');
    } else if (unackCount === 0) {
      scadaAudio.stopAlarmSound();
    }
    prevUnackCountRef.current = unackCount;
  }, [unackCount, alarms]);

  // Handle Control Panel user action
  const handleUpdateScada = (
    updates: Partial<ScadaState>,
    actionName: string,
    value: string | number
  ) => {
    const updated = { ...scadaRef.current, ...updates };
    scadaRef.current = updated;
    setScada(updated);

    let isCorrect = true;
    let feedback = 'Tindakan dicatat';

    if (updates.distPump1Running === false && !scadaRef.current.distPump2Running && actionName.includes('Stop')) {
      isCorrect = false;
      feedback = 'Tindakan Tidak Aman: Menghentikan seluruh pompa pasokan mendadak (-15 Poin)';
    }

    const newLog: ActionLog = {
      timestampSec: elapsedSecRef.current,
      controlPointId: selectedUnit,
      action: actionName,
      value,
      isCorrect,
      feedback,
    };

    const nextLogs = [...actionLogsRef.current, newLog];
    actionLogsRef.current = nextLogs;
    setActionLogs(nextLogs);
  };

  // Reset Pump Trip Action
  const handleResetPumpTrip = () => {
    scadaAudio.playAcknowledgeChime();

    const updatedScada: ScadaState = {
      ...scadaRef.current,
      intakePumpTripped: false,
      distPumpTripped: false,
    };
    scadaRef.current = updatedScada;
    setScada(updatedScada);

    const updatedAlarms = alarmsRef.current.map((a) => {
      if (a.isLatched && a.status !== 'clear') {
        return {
          ...a,
          status: 'pulih_belum_clear' as const,
          latchedResetDone: true,
          clearNote: 'Thermal breaker telah di-reset oleh operator. Siap di-clear.',
        };
      }
      return a;
    });
    alarmsRef.current = updatedAlarms;
    setAlarms(updatedAlarms);

    const nextLogs: ActionLog[] = [
      ...actionLogsRef.current,
      {
        timestampSec: elapsedSecRef.current,
        controlPointId: selectedUnit,
        action: 'Reset Proteksi Trip Pompa (Electrical Reset)',
        value: 'RESET_OK',
        isCorrect: true,
        feedback: 'Reset trip pompa berhasil dilakukan sesuai SOP.',
      },
    ];
    actionLogsRef.current = nextLogs;
    setActionLogs(nextLogs);
  };

  // Alarm Acknowledge
  const handleAcknowledgeAlarm = (alarmId: string) => {
    scadaAudio.playAcknowledgeChime();
    const ackTimeStr = formatSimTime(elapsedSecRef.current);

    const updatedAlarms = alarmsRef.current.map((a) =>
      a.id === alarmId ? { ...a, status: 'aktif_diakui' as const } : a
    );
    alarmsRef.current = updatedAlarms;
    setAlarms(updatedAlarms);
    setAckTimeMap((prev) => ({ ...prev, [alarmId]: ackTimeStr }));

    const targetAlarm = alarmsRef.current.find((a) => a.id === alarmId);
    const nextLogs: ActionLog[] = [
      ...actionLogsRef.current,
      {
        timestampSec: elapsedSecRef.current,
        controlPointId: targetAlarm?.controlPointId || selectedUnit,
        action: `Acknowledge (Akui) Alarm ${targetAlarm?.controlPointName || 'SCADA'}`,
        value: 'ACK',
        isCorrect: true,
      },
    ];
    actionLogsRef.current = nextLogs;
    setActionLogs(nextLogs);
  };

  // Alarm Manual Clear with SOP Guard (PRD §10)
  const handleClearAlarm = (alarmId: string): { success: boolean; message: string } => {
    const alarm = alarmsRef.current.find((a) => a.id === alarmId);
    if (!alarm) return { success: false, message: 'Alarm tidak ditemukan' };

    const curr = scadaRef.current;

    const recordRejection = (actionText: string, feedbackText: string, rejectMsg: string) => {
      const nextLogs: ActionLog[] = [
        ...actionLogsRef.current,
        {
          timestampSec: elapsedSecRef.current,
          controlPointId: alarm.controlPointId,
          action: actionText,
          value: 'REJECTED',
          isCorrect: false,
          feedback: feedbackText,
        },
      ];
      actionLogsRef.current = nextLogs;
      setActionLogs(nextLogs);
      return { success: false, message: rejectMsg };
    };

    // Rejection 1: Latched Pump Trip not reset
    if (alarm.isLatched && !alarm.latchedResetDone) {
      return recordRejection(
        'Percobaan Clear Alarm Sebelum Reset Trip (Ditolak)',
        'Pelanggaran SOP: Alarm pompa trip wajib di-reset di panel kontrol sebelum di-clear! (-15 Poin)',
        'Penyebab belum ditangani: Pompa trip harus di-reset terlebih dahulu!'
      );
    }

    // Rejection 2: Latched Pump Trip without active replacement/running pump
    if (alarm.id === 'alarm-intake-trip' && !curr.intakePump1Running && !curr.intakePump2Running) {
      return recordRejection(
        'Percobaan Clear Alarm Intake Trip Tanpa Pompa Aktif (Ditolak)',
        'Pelanggaran SOP: Jalankan Pompa Intake 2 (Standby) terlebih dahulu agar aliran air baku pulih! (-15 Poin)',
        'Penyebab belum ditangani: Jalankan Pompa Intake 2 (Standby) sebelum Clear!'
      );
    }

    if (alarm.id === 'alarm-dist-trip' && !curr.distPump1Running && !curr.distPump2Running) {
      return recordRejection(
        'Percobaan Clear Alarm Distribusi Trip Tanpa Pompa Aktif (Ditolak)',
        'Pelanggaran SOP: Jalankan Pompa Distribusi P-102 (Standby) terlebih dahulu! (-15 Poin)',
        'Penyebab belum ditangani: Jalankan Pompa P-102 (Standby) sebelum Clear!'
      );
    }

    // Rejection 3: Filtrasi turbidity still >= 3.0 NTU
    if (alarm.controlPointId === 'filtrasi' && curr.filteredWaterTurbidity >= 3.0) {
      return recordRejection(
        'Percobaan Clear Alarm Kekeruhan Tinggi Saat Masih Abnormal (Ditolak)',
        'Pelanggaran SOP: Tombol Clear ditekan saat kekeruhan air olahan masih ≥ 3,0 NTU! (-15 Poin)',
        `Penyebab belum ditangani: Kekeruhan air olahan ${curr.filteredWaterTurbidity.toFixed(2)} NTU ≥ 3,0 NTU!`
      );
    }

    // Rejection 4: Intake turbidity still > 50 NTU
    if (alarm.id === 'alarm-intake-turb' && curr.rawWaterTurbidity > 50) {
      return recordRejection(
        'Percobaan Clear Alarm Kekeruhan Baku Saat Masih Tinggi (Ditolak)',
        'Pelanggaran SOP: Kekeruhan air baku masih di atas ambang 50 NTU!',
        `Penyebab belum ditangani: Kekeruhan air baku ${curr.rawWaterTurbidity.toFixed(0)} NTU masih di atas ambang!`
      );
    }

    // Rejection 5: Chlorine residual out of range
    if (alarm.controlPointId === 'desinfeksi' && (curr.freeResidualChlorine < 0.2 || curr.freeResidualChlorine > 0.5)) {
      return recordRejection(
        'Percobaan Clear Alarm Klorin Saat Sisa Klor Masih Abnormal (Ditolak)',
        'Pelanggaran SOP: Sisa klor bebas masih di luar rentang 0,20–0,50 mg/L! (-15 Poin)',
        `Penyebab belum ditangani: Sisa klor ${curr.freeResidualChlorine.toFixed(2)} mg/L belum di rentang 0,20–0,50 mg/L!`
      );
    }

    // Rejection 6: Pipe leak not isolated
    if (alarm.controlPointId === 'valve_prv' && curr.pipeLeakActive && curr.valveIsolasiBocorOpen) {
      return recordRejection(
        'Percobaan Clear Alarm Kebocoran Sebelum Isolasi Valve (Ditolak)',
        'Pelanggaran SOP: Valve Isolasi Ruas Bocor belum ditutup! (-15 Poin)',
        'Penyebab belum ditangani: Tutup Valve Isolasi Kebocoran terlebih dahulu!'
      );
    }

    // Rejection 7: Zone pressure still < 2.0 bar
    if (alarm.controlPointId === 'titik_pantau_jaringan' && curr.zone1Pressure < 2.0) {
      return recordRejection(
        'Percobaan Clear Alarm Tekanan Drop Saat Masih Rendah (Ditolak)',
        'Pelanggaran SOP: Tekanan zona masih < 2,00 bar! (-15 Poin)',
        `Penyebab belum ditangani: Tekanan zona ${curr.zone1Pressure.toFixed(2)} bar masih < 2,00 bar!`
      );
    }

    // Allowed Clear
    scadaAudio.playSuccessFanfare();
    const updatedAlarms = alarmsRef.current.map((a) =>
      a.id === alarmId ? { ...a, status: 'clear' as const, clearMethod: 'manual' as const } : a
    );
    alarmsRef.current = updatedAlarms;
    setAlarms(updatedAlarms);

    const nextLogs: ActionLog[] = [
      ...actionLogsRef.current,
      {
        timestampSec: elapsedSecRef.current,
        controlPointId: alarm.controlPointId,
        action: `Manual Clear Alarm (${alarm.controlPointName})`,
        value: 'CLEAR',
        isCorrect: true,
      },
    ];
    actionLogsRef.current = nextLogs;
    setActionLogs(nextLogs);

    return {
      success: true,
      message: 'Alarm berhasil di-clear oleh operator.',
    };
  };

  const handleUseHint = () => {
    if (isExamMission) return;
    const nextCount = hintsUsedRef.current + 1;
    hintsUsedRef.current = nextCount;
    setHintsUsedCount(nextCount);
    setShowHintModal(true);

    const nextLogs: ActionLog[] = [
      ...actionLogsRef.current,
      {
        timestampSec: elapsedSecRef.current,
        controlPointId: selectedUnit,
        action: 'Operator Membuka Bantuan Petunjuk (−5 Poin)',
        value: `Hint #${nextCount}`,
        isCorrect: true,
        feedback: 'Pengurangan nilai -5 Poin diterapkan.',
      },
    ];
    actionLogsRef.current = nextLogs;
    setActionLogs(nextLogs);
  };

  const handleFinish = () => {
    finishSession(elapsedSecRef.current, false);
  };

  // Compute live score dynamically
  const liveScore = useMemo(() => {
    if (alarms.length === 0 && actionLogs.length === 0) {
      return Math.max(0, 100 - hintsUsedCount * 5);
    }
    return evaluateMissionScore(
      mission,
      Math.max(1, elapsedSec),
      actionLogs,
      alarms,
      { stable: stableTicks, total: Math.max(1, elapsedSec) },
      hintsUsedCount,
      currentUser?.id || 'user-peserta-ipa',
      currentTenant.id,
      simTrack,
      trendHistory,
      false
    ).totalScore;
  }, [mission, elapsedSec, actionLogs, alarms, stableTicks, hintsUsedCount, currentUser?.id, currentTenant.id, simTrack, trendHistory]);

  // Select highest-priority active alarm for top banner
  const activeAlarm = useMemo(() => {
    const active = alarms.filter((a) => a.status !== 'clear');
    if (active.length === 0) return undefined;
    return [...active].sort((a, b) => PRIORITY_RANK[b.priority] - PRIORITY_RANK[a.priority])[0];
  }, [alarms]);

  // Default trend parameter based on mission
  const initialTrendParam: TrendParamKey = useMemo(() => {
    if (mission.code === 'IPA-08') return 'freeChlorine';
    if (mission.code.startsWith('DST-') || simTrack === 'distribusi') return 'zonePressure';
    return 'turbidity';
  }, [mission.code, simTrack]);

  // Banner style matching activeAlarm priority
  const bannerStyle = useMemo(() => {
    if (!activeAlarm) return null;
    switch (activeAlarm.priority) {
      case 'kritis':
        return {
          wrapper: 'bg-rose-950/50 border-rose-500/70 text-rose-100',
          dot: 'bg-rose-500',
          label: 'text-rose-300',
          hint: 'text-rose-300',
        };
      case 'tinggi':
        return {
          wrapper: 'bg-amber-950/40 border-amber-500/60 text-amber-100',
          dot: 'bg-amber-400',
          label: 'text-amber-300',
          hint: 'text-amber-300',
        };
      case 'sedang':
        return {
          wrapper: 'bg-sky-950/40 border-sky-500/60 text-sky-100',
          dot: 'bg-sky-400',
          label: 'text-sky-300',
          hint: 'text-sky-300',
        };
      default:
        return {
          wrapper: 'bg-slate-900/60 border-slate-500/50 text-slate-200',
          dot: 'bg-slate-400',
          label: 'text-slate-300',
          hint: 'text-slate-300',
        };
    }
  }, [activeAlarm]);

  const trackLabel =
    simTrack === 'ipa'
      ? 'INSTALASI PENGOLAHAN AIR (IPA) AKTIF'
      : simTrack === 'distribusi'
      ? 'JARINGAN PIPA DISTRIBUSI AKTIF'
      : 'SISTEM TERPADU HULU-HILIR (IPA + DISTRIBUSI) AKTIF';

  const trackBadgeLabel =
    simTrack === 'ipa'
      ? 'JALUR IPA · SIKLUS REAL-TIME 1 HZ'
      : simTrack === 'distribusi'
      ? 'JALUR DISTRIBUSI · SIKLUS REAL-TIME 1 HZ'
      : 'JALUR TERPADU · SIKLUS REAL-TIME 1 HZ';

  const remainingSec = Math.max(0, durationLimitSec - elapsedSec);

  return (
    <div className="max-w-[1720px] mx-auto px-3 sm:px-6 py-4 font-sans text-slate-100 space-y-4 select-none">

      {/* Top Header Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3.5 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-lg">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-sky-600/20 border border-sky-500/40 text-sky-400 flex items-center justify-center font-bold">
            <Building2 className="w-5 h-5 text-sky-400" />
          </div>
          <div>
            <div className="text-xs font-bold text-sky-400 uppercase tracking-wider">
              MISI: {mission.code} {mission.name}
            </div>
            <div className="text-[11px] text-slate-400">
              {currentTenant.name} · Operator: <strong className="text-white">{currentUser?.fullName}</strong> ({currentUser?.role})
            </div>
          </div>
        </div>

        {/* Center Timer & Score */}
        <div className="flex items-center gap-3 font-mono">
          <div className="px-3.5 py-1.5 rounded-xl bg-[#0b1120] border border-[#1e293b] text-xs">
            <span className="text-slate-400 mr-2 font-sans font-semibold">⏱ WAKTU:</span>
            <span className={`font-bold text-sm ${remainingSec <= 30 ? 'text-rose-400 animate-pulse' : 'text-white'}`}>
              {formatSimTime(elapsedSec)}
            </span>
            <span className="text-slate-500 text-xs"> / {formatSimTime(durationLimitSec)}</span>
          </div>

          <div className="px-3.5 py-1.5 rounded-xl bg-[#0b1120] border border-[#1e293b] text-xs">
            <span className="text-slate-400 mr-2 font-sans font-semibold">SKOR SEMENTARA:</span>
            <span className={`font-bold text-sm ${liveScore >= (mission.passScore || 70) ? 'text-emerald-400' : 'text-amber-400'}`}>
              {liveScore}
            </span>
          </div>
        </div>

        {/* Buttons: Hint & Finish */}
        <div className="flex items-center gap-2">
          <button
            type="button"
            disabled={isExamMission}
            onClick={handleUseHint}
            title={isExamMission ? `Petunjuk dinonaktifkan pada Misi Kelulusan Ujian${showTechnicalRefs ? ' (PRD §8)' : ''}` : 'Buka bantuan petunjuk (-5 poin)'}
            className={`px-3.5 py-1.5 rounded-xl border font-bold text-xs transition-all flex items-center gap-1.5 ${
              isExamMission
                ? 'bg-slate-800/60 border-slate-700 text-slate-500 cursor-not-allowed'
                : 'bg-amber-500/20 hover:bg-amber-500/30 border-amber-500/40 text-amber-300 cursor-pointer'
            }`}
          >
            <Lightbulb className="w-3.5 h-3.5 text-amber-400" />
            <span>{isExamMission ? 'Petunjuk Nonaktif (Ujian)' : 'Petunjuk (−5 Poin)'}</span>
          </button>

          <button
            type="button"
            onClick={handleFinish}
            className="px-4 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-md shadow-rose-950/50 flex items-center gap-1.5 cursor-pointer"
          >
            <StopCircle className="w-3.5 h-3.5" />
            <span>SELESAI SIMULASI</span>
          </button>
        </div>
      </div>

      {/* Live Alarm Warning Banner Synced with Active Highest-Priority Alarm */}
      {activeAlarm && bannerStyle && (
        <div className={`p-3.5 rounded-xl border text-xs flex flex-col md:flex-row md:items-center justify-between gap-2 shadow-md ${bannerStyle.wrapper}`}>
          <div className="flex items-center gap-2.5 min-w-0">
            <div className={`w-3 h-3 rounded-full animate-ping shrink-0 ${bannerStyle.dot}`} />
            <span className={`font-bold uppercase tracking-wider shrink-0 ${bannerStyle.label}`}>
              ▲ ALARM {activeAlarm.priority.toUpperCase()}:
            </span>
            <span className="truncate text-slate-100 font-medium">
              {activeAlarm.controlPointName} — {activeAlarm.message} · Status:{' '}
              {activeAlarm.status === 'aktif_belum_diakui'
                ? 'Aktif, Belum Diakui'
                : activeAlarm.status === 'pulih_belum_clear'
                ? 'Pulih, Siap di-Clear'
                : `Diakui (ACK pada ${ackTimeMap[activeAlarm.id] || activeAlarm.timestamp})`}
            </span>
          </div>
          <div className="flex items-center gap-2.5 shrink-0">
            <span className={`text-[10px] font-mono font-semibold ${bannerStyle.hint}`}>
              {getRecoveryHintForAlarm(activeAlarm)}
            </span>
            {activeAlarm.status === 'aktif_belum_diakui' && (
              <button
                type="button"
                onClick={() => {
                  handleAcknowledgeAlarm(activeAlarm.id);
                  setSelectedUnit(activeAlarm.controlPointId);
                }}
                className="px-2.5 py-1 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-[10px] flex items-center gap-1 cursor-pointer shadow-xs"
              >
                <Check className="w-3 h-3" />
                <span>Akui (ACK)</span>
              </button>
            )}
          </div>
        </div>
      )}

      {/* Main SCADA Workspace Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">

        {/* LEFT AREA: SCADA Mimic + Trend Chart */}
        <div className="lg:col-span-9 space-y-4">
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-3 shadow-xl relative overflow-hidden">
            <div className="flex items-center justify-between px-2 pb-2 mb-1 border-b border-[#1e293b] text-xs">
              <span className="font-bold text-slate-300 uppercase tracking-wider text-[11px]">
                DIAGRAM MIMIC PROSES: {trackLabel}
              </span>
              <span className="text-[10px] px-2 py-0.5 rounded-full bg-sky-950 border border-sky-500/30 text-sky-400 font-mono font-bold">
                {trackBadgeLabel}
              </span>
            </div>

            <ScadaMimic
              scada={scada}
              track={simTrack}
              selectedUnit={selectedUnit}
              onSelectUnit={setSelectedUnit}
              onOpenNarrative={setCurrentNarrativeUnit}
              activeAlarms={alarms}
            />
          </div>

          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-4 shadow-xl space-y-2">
            <div className="flex items-center justify-between text-xs">
              <span className="font-bold text-slate-300 uppercase tracking-wider text-[11px]">
                TREN PARAMETER PROSES (REAL-TIME 1 HZ):
              </span>
              <span className="text-[10px] text-slate-400 font-mono">
                {simTrack === 'distribusi'
                  ? 'Tekanan Layanan: 2,0–2,8 bar · Sisa Klor Ujung ≥ 0,20 mg/L'
                  : 'Kekeruhan < 3,0 NTU (Deadband ≤ 2,7 NTU) · Sisa Klor: 0,20–0,50 mg/L'}
              </span>
            </div>

            <TrendChart trendHistory={trendHistory} initialParam={initialTrendParam} />
          </div>
        </div>

        {/* RIGHT AREA: Control Panel */}
        <div className="lg:col-span-3 bg-[#0f172a] rounded-2xl border border-[#24324d] p-4 shadow-xl">
          <ControlPanel
            selectedUnit={selectedUnit}
            scada={scada}
            simTrack={simTrack}
            onUpdateScada={handleUpdateScada}
            onOpenNarrative={setCurrentNarrativeUnit}
            onResetPumpTrip={handleResetPumpTrip}
          />
        </div>

      </div>

      {/* Bottom Area: Alarm Panel Table */}
      <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-4 shadow-xl">
        <div className="flex items-center justify-between pb-2 mb-2 border-b border-[#1e293b] text-xs">
          <span className="font-bold text-slate-300 uppercase tracking-wider text-[11px]">
            DAFTAR ALARM SISTEM ({showTechnicalRefs ? '4 STATUS STANDAR PRD §10' : '4 STATUS STANDAR'}: AKTIF BLM DIAKUI · AKTIF DIAKUI · PULIH BLM CLEAR · CLEAR)
          </span>
          <span className="text-[10px] text-slate-400 font-mono">
            {alarms.filter((a) => a.status !== 'clear').length} Alarm Memerlukan Perhatian
          </span>
        </div>

        <AlarmPanel
          alarms={alarms}
          onAcknowledge={handleAcknowledgeAlarm}
          onClear={handleClearAlarm}
          onSelectControlPoint={setSelectedUnit}
        />
      </div>

      {/* Educational Narrative Pop-up Modal (L5a) */}
      {currentNarrativeUnit && (
        <NarrativeModal
          controlPoint={
            CONTROL_POINTS.find((cp) => cp.id === currentNarrativeUnit) || CONTROL_POINTS[0]
          }
          scada={scada}
          hasActiveAlarm={alarms.some(
            (a) => a.controlPointId === currentNarrativeUnit && a.status !== 'clear'
          )}
          onClose={() => setCurrentNarrativeUnit(null)}
        />
      )}

      {/* Mission-Specific Hint Modal (-5 Poin) */}
      {showHintModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-[#0f172a] rounded-2xl border border-amber-500/40 p-6 max-w-md w-full space-y-4 shadow-2xl">
            <div className="flex items-center gap-2.5 text-amber-400">
              <Lightbulb className="w-5 h-5" />
              <h3 className="text-sm font-bold uppercase tracking-wider text-white">
                Petunjuk Misi {mission.code} (−5 Poin)
              </h3>
            </div>

            <div className="p-3.5 rounded-xl bg-amber-950/30 border border-amber-500/30 text-xs text-slate-200 leading-relaxed space-y-2">
              {mission.hints.length > 0 ? (
                mission.hints.map((h, i) => (
                  <p key={i}>
                    {i + 1}. {h}
                  </p>
                ))
              ) : (
                <p>Ikuti prosedur standar operasi (SOP) untuk menjaga seluruh parameter dalam batas aman.</p>
              )}
            </div>

            <div className="text-[10px] text-slate-500 italic">
              Pengurangan skor −5 Poin telah dicatat pada sistem penilaian misi.
            </div>

            <button
              type="button"
              onClick={() => setShowHintModal(false)}
              className="w-full py-2.5 bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs rounded-xl shadow-sm transition-colors cursor-pointer"
            >
              Kembali ke Workspace SCADA
            </button>
          </div>
        </div>
      )}

    </div>
  );
};

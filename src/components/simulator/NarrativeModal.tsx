/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect } from 'react';
import { ControlPointDef, ScadaState } from '../../types';
import { useApp } from '../../context/AppContext';
import { formatNumberID } from '../../utils/gamification';
import { 
  AlertTriangle, 
  ArrowDownRight, 
  BookOpen, 
  CheckCircle2, 
  FileText, 
  Info, 
  SlidersHorizontal, 
  X,
  Compass,
  Building2
} from 'lucide-react';

interface NarrativeModalProps {
  controlPoint: ControlPointDef;
  scada: ScadaState;
  hasActiveAlarm: boolean;
  onClose: () => void;
}

export const NarrativeModal: React.FC<NarrativeModalProps> = ({
  controlPoint,
  scada,
  hasActiveAlarm,
  onClose,
}) => {
  const { currentTenant, markNarrativeOpened, showTechnicalRefs } = useApp();

  useEffect(() => {
    // Automatically register that participant has opened this educational narrative
    // Does NOT deduct score!
    markNarrativeOpened(controlPoint.id);
  }, [controlPoint.id, markNarrativeOpened]);

  const localSopNote =
    currentTenant.config.localSopNotes?.[controlPoint.id] ||
    `Di instalasi latih ${currentTenant.shortName}, operator wajib memantau ${controlPoint.name} secara berkala dan mengikuti SOP standar: ${controlPoint.narrative.gangguanUmumDanSop}`;

  const renderLiveTelemetryRows = () => {
    switch (controlPoint.id) {
      case 'intake':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Debit Air Baku:</span>
              <span className="text-sky-300 font-bold font-mono">{formatNumberID(scada.rawWaterFlow, 0, 'L/s')} (Target: 75–100 L/s)</span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Kekeruhan Air Baku:</span>
              <span className={`font-bold font-mono ${scada.rawWaterTurbidity > 50 ? 'text-amber-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.rawWaterTurbidity, 1, 'NTU')}
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Status Pompa Intake:</span>
              <span className={`font-bold font-mono ${scada.intakePumpTripped ? 'text-rose-400' : 'text-emerald-400'}`}>
                {scada.intakePumpTripped ? 'P1 TRIP' : scada.intakePump1Running ? 'P1 RUN' : 'P1 STOP'} / {scada.intakePump2Running ? 'P2 RUN' : 'P2 STANDBY'}
              </span>
            </div>
          </>
        );
      case 'koagulasi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Kekeruhan Baku:</span>
              <span className={`font-bold font-mono ${scada.rawWaterTurbidity > 50 ? 'text-amber-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.rawWaterTurbidity, 1, 'NTU')} {scada.rawWaterTurbidity > 50 ? '(Tinggi!)' : '(Normal)'}
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Dosis Koagulan PAC:</span>
              <span className="text-sky-300 font-bold font-mono">
                {formatNumberID(scada.coagulantActualDose, 1, 'mg/L')}
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Derajat pH:</span>
              <span className={`font-bold font-mono ${scada.waterPh < 6.5 || scada.waterPh > 8.5 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.waterPh, 2)} pH ({scada.waterPh >= 6.5 && scada.waterPh <= 8.5 ? 'Normal ✓' : 'Koreksi'})
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Motor Flash Mixer:</span>
              <span className={`font-bold font-mono ${scada.flashMixerRunning ? 'text-sky-400' : 'text-rose-400'}`}>
                {scada.flashMixerRunning ? '120 RPM (Aktif)' : 'OFF'}
              </span>
            </div>
          </>
        );
      case 'flokulasi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Kecepatan Pengaduk:</span>
              <span className="text-sky-300 font-bold font-mono">{formatNumberID(scada.flocculatorRpm, 0, 'RPM')}</span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Indeks Pembentukan Flok:</span>
              <span className={`font-bold font-mono ${scada.flocQualityScore >= 75 ? 'text-emerald-400' : 'text-amber-400'}`}>
                {formatNumberID(scada.flocQualityScore, 0)}%
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Status Pengaduk Lambat:</span>
              <span className={`font-bold font-mono ${scada.flocculatorMixerRunning ? 'text-emerald-400' : 'text-rose-400'}`}>
                {scada.flocculatorMixerRunning ? 'AKTIF' : 'OFF'}
              </span>
            </div>
          </>
        );
      case 'sedimentasi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Kekeruhan Air Mengendap:</span>
              <span className={`font-bold font-mono ${scada.settledWaterTurbidity > 5 ? 'text-amber-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.settledWaterTurbidity, 1, 'NTU')}
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Selimut Lumpur (Sludge):</span>
              <span className={`font-bold font-mono ${scada.sludgeLevelPercent > 60 ? 'text-amber-400' : 'text-sky-300'}`}>
                {formatNumberID(scada.sludgeLevelPercent, 0)}%
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Katup Blowdown Lumpur:</span>
              <span className="text-sky-300 font-bold font-mono">
                {scada.clarifierBlowdownOpen ? 'OPEN (Membuang)' : 'CLOSED'}
              </span>
            </div>
          </>
        );
      case 'filtrasi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Kekeruhan Air Olahan:</span>
              <span className={`font-bold font-mono ${scada.filteredWaterTurbidity >= 3.0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.filteredWaterTurbidity, 2, 'NTU')} (Target &lt; 3,0)
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Headloss Filter 1 / 2:</span>
              <span className="text-sky-300 font-bold font-mono">
                {formatNumberID(scada.filter1Headloss, 2, 'm')} / {formatNumberID(scada.filter2Headloss, 2, 'm')}
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Status Backwash:</span>
              <span className="text-sky-300 font-bold font-mono">
                {scada.filter1Backwashing ? 'Filter 1 Backwash' : scada.filter2Backwashing ? 'Filter 2 Backwash' : 'Filtrasi Normal'}
              </span>
            </div>
          </>
        );
      case 'desinfeksi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Setpoint Dosis Klor:</span>
              <span className="text-sky-300 font-bold font-mono">{formatNumberID(scada.chlorineDoseSetpoint, 2, 'mg/L')}</span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Sisa Klor Bebas:</span>
              <span className={`font-bold font-mono ${scada.freeResidualChlorine < 0.2 || scada.freeResidualChlorine > 0.5 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.freeResidualChlorine, 2, 'mg/L')} (0,20–0,50)
              </span>
            </div>
          </>
        );
      case 'reservoir':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Level Reservoir:</span>
              <span className="text-sky-300 font-bold font-mono">
                {formatNumberID(scada.reservoirLevelMeters, 2, 'm')} ({formatNumberID(scada.reservoirLevelPercent, 0)}%)
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Sisa Klor Bebas:</span>
              <span className={`font-bold font-mono ${scada.freeResidualChlorine < 0.2 || scada.freeResidualChlorine > 0.5 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.freeResidualChlorine, 2, 'mg/L')}
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Katup Inlet / Outlet:</span>
              <span className="text-emerald-400 font-bold font-mono">
                {scada.reservoirInletOpen ? 'OPEN' : 'CLOSED'} / {scada.reservoirOutletOpen ? 'OPEN' : 'CLOSED'}
              </span>
            </div>
          </>
        );
      case 'pompa_distribusi':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Tekanan Keluar (Discharge):</span>
              <span className={`font-bold font-mono ${scada.distDischargePressure < 3.0 ? 'text-rose-400' : 'text-sky-300'}`}>
                {formatNumberID(scada.distDischargePressure, 2, 'bar')}
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Total Debit Distribusi:</span>
              <span className="text-sky-300 font-bold font-mono">{formatNumberID(scada.distTotalFlow, 0, 'L/s')}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Status Pompa P-101 / P-102:</span>
              <span className={`font-bold font-mono ${scada.distPumpTripped ? 'text-rose-400' : 'text-emerald-400'}`}>
                {scada.distPumpTripped ? 'P-101 TRIP' : scada.distPump1Running ? 'P-101 RUN' : 'P-101 STOP'} / {scada.distPump2Running ? 'P-102 RUN' : 'STANDBY'}
              </span>
            </div>
          </>
        );
      case 'valve_prv':
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Setpoint Tekanan PRV:</span>
              <span className="text-amber-400 font-bold font-mono">{formatNumberID(scada.prvSetpointBar, 2, 'bar')}</span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Valve Isolasi Ruas Bocor:</span>
              <span className={`font-bold font-mono ${scada.pipeLeakActive && scada.valveIsolasiBocorOpen ? 'text-rose-400' : 'text-emerald-400'}`}>
                {scada.valveIsolasiBocorOpen ? 'OPEN (TERBUKA)' : 'CLOSED (TERISOLASI)'}
              </span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Valve Zona 1 / Zona 2:</span>
              <span className="text-sky-300 font-bold font-mono">
                {scada.valveZone1Open ? 'OPEN' : 'CLOSED'} / {scada.valveZone2Open ? 'OPEN' : 'CLOSED'}
              </span>
            </div>
          </>
        );
      case 'titik_pantau_jaringan':
      default:
        return (
          <>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Tekanan Zona 1 / Zona 2:</span>
              <span className={`font-bold font-mono ${scada.zone1Pressure < 2.0 || scada.zone2Pressure < 2.0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.zone1Pressure, 2)} / {formatNumberID(scada.zone2Pressure, 2, 'bar')} (Target 2,0–2,8)
              </span>
            </div>
            <div className="flex justify-between border-b border-[#1e293b] pb-1">
              <span className="text-slate-400">Debit Zona 1 / Zona 2:</span>
              <span className="text-sky-300 font-bold font-mono">{formatNumberID(scada.zone1Flow, 0)} / {formatNumberID(scada.zone2Flow, 0, 'L/s')}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-slate-400">Sisa Klor Ujung Jaringan:</span>
              <span className={`font-bold font-mono ${scada.zoneChlorineEnd < 0.2 ? 'text-rose-400' : 'text-emerald-400'}`}>
                {formatNumberID(scada.zoneChlorineEnd, 2, 'mg/L')}
              </span>
            </div>
          </>
        );
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/75 backdrop-blur-xs p-4 animate-fade-in font-sans">
      <div className="bg-[#0f172a] rounded-2xl shadow-2xl border border-[#24324d] w-full max-w-4xl max-h-[92vh] flex flex-col overflow-hidden text-slate-100">
        
        {/* Header */}
        <div className="px-6 py-4 bg-[#0b1120] border-b border-[#1e293b] flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-sky-600/20 border border-sky-500/40 flex items-center justify-center text-sky-400 font-bold">
              <Info className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white leading-tight">
                Narasi Detail Titik Kontrol: {controlPoint.name}
              </h2>
              <span className="text-[11px] text-sky-400 font-medium">
                {controlPoint.category === 'ipa'
                  ? 'Unit Operasi Instalasi Pengolahan Air (IPA)'
                  : 'Unit Operasi Jaringan Pipa Distribusi'}
                {showTechnicalRefs ? ' (PRD §9)' : ''}
              </span>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-[#1e293b] transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Alarm Banner if currently active */}
        {hasActiveAlarm && (
          <div className="px-6 py-2.5 bg-amber-950/40 border-b border-amber-500/40 text-amber-200 text-xs flex items-center gap-2">
            <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0" />
            <span>Peringatan: Titik kontrol ini sedang memiliki alarm aktif. Tinjau Bagian 5 (Gangguan Umum &amp; SOP Singkat) di bawah.</span>
          </div>
        )}

        {/* Content Body: 6 Sections */}
        <div className="px-6 py-5 overflow-y-auto space-y-4 text-xs text-slate-300 leading-relaxed">
          
          {/* Top 2 Columns: (1. Apa Ini) & (4. Dampak ke Hilir) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            {/* 1. Apa Ini & Fungsinya */}
            <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2">
              <span className="text-[11px] font-bold text-sky-400 uppercase tracking-wider block">
                1. APA INI &amp; FUNGSINYA (DESKRIPSI PROSES):
              </span>
              <p className="text-slate-300 text-xs leading-relaxed">
                {controlPoint.narrative.apaIni}
              </p>
              <div className="p-2.5 bg-[#0f172a] rounded-lg border border-[#1e293b] text-center text-[10px] text-sky-300 font-mono">
                Unit: {controlPoint.name} · Parameter Pantau: {controlPoint.monitoredParams.join(', ')}
              </div>
            </div>

            {/* 4. Dampak ke Hilir */}
            <div className="p-4 rounded-xl bg-amber-950/20 border border-amber-500/30 space-y-2 text-xs">
              <span className="text-[11px] font-bold text-amber-400 uppercase tracking-wider block">
                4. DAMPAK KE HILIR (DOWNSTREAM IMPACT):
              </span>
              <p className="text-[11px] text-slate-300 leading-relaxed">
                {controlPoint.narrative.dampakKeHilir}
              </p>
            </div>
          </div>

          {/* Middle 2 Columns: (2. Yang Dipantau) & (5. Gangguan Umum & SOP) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            {/* 2. Yang Dipantau */}
            <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-xs">
              <span className="text-[11px] font-bold text-sky-400 uppercase tracking-wider block">
                2. YANG DIPANTAU (TELEMETRI REAL-TIME):
              </span>
              <div className="space-y-1.5 text-[11px]">
                {renderLiveTelemetryRows()}
              </div>
              <p className="text-[10px] text-slate-400 pt-1 border-t border-[#1e293b]">
                {controlPoint.narrative.yangDipantau}
              </p>
            </div>

            {/* 5. Gangguan Umum & SOP Singkat */}
            <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-xs">
              <span className="text-[11px] font-bold text-sky-400 uppercase tracking-wider block">
                5. GANGGUAN UMUM &amp; SOP SINGKAT{showTechnicalRefs ? ' (PRD §9 & §10)' : ''}:
              </span>
              <p className="text-[11px] text-slate-300 leading-relaxed">
                {controlPoint.narrative.gangguanUmumDanSop}
              </p>
            </div>
          </div>

          {/* Bottom 2 Columns: (3. Controls) & (6. Pelajari Lebih Lanjut) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* 3. Controls */}
            <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1.5 text-xs">
              <span className="text-[11px] font-bold text-sky-400 uppercase tracking-wider block">
                3. YANG BISA DIKENDALIKAN (CONTROLS):
              </span>
              <p className="text-[11px] text-slate-300 leading-relaxed">
                {controlPoint.narrative.yangBisaDikendalikan}
              </p>
            </div>

            {/* 6. Pelajari Lebih Lanjut */}
            <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1.5 text-xs">
              <span className="text-[11px] font-bold text-sky-400 uppercase tracking-wider block">
                6. PELAJARI LEBIH LANJUT:
              </span>
              <p className="text-[11px] text-sky-300 leading-relaxed">
                {controlPoint.narrative.pelajariLebihLanjut}
              </p>
            </div>
          </div>

          {/* Catatan SOP Lokal Lembaga Box */}
          <div className="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/40 text-xs space-y-1">
            <span className="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block">
              CATATAN SOP LOKAL LEMBAGA ({currentTenant.name.toUpperCase()}):
            </span>
            <p className="text-emerald-200 text-xs leading-relaxed font-mono">
              "{localSopNote}"
            </p>
            <span className="text-[9px] text-slate-400 block pt-0.5">
              Dikonfigurasi oleh Admin Lembaga di Pengaturan Lembaga{showTechnicalRefs ? ' (Layar L13)' : ''}.
            </span>
          </div>

        </div>

        {/* Footer */}
        <div className="px-6 py-3.5 bg-[#0b1120] border-t border-[#1e293b] flex items-center justify-between shrink-0">
          <div className="text-[11px] text-slate-400 flex items-center gap-1.5">
            <Compass className="w-3.5 h-3.5 text-sky-400" />
            <span>
              Membuka narasi ini dicatat dalam sistem untuk syarat perolehan Lencana &quot;Penjelajah Titik Kontrol&quot;
              {showTechnicalRefs ? ' (PRD §8)' : ''}.
            </span>
          </div>
          <button
            onClick={onClose}
            className="px-5 py-2 bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs rounded-xl shadow-sm transition-all cursor-pointer"
          >
            KEMBALI KE WORKSPACE
          </button>
        </div>

      </div>
    </div>
  );
};

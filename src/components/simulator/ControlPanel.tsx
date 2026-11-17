/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { LearningTrack, ScadaState } from '../../types';
import {
  AlertCircle,
  Droplets,
  Gauge,
  Info,
  Power,
  RefreshCw,
  ShieldAlert,
  Sliders,
  Wrench,
} from 'lucide-react';

interface ControlPanelProps {
  selectedUnit: string;
  scada: ScadaState;
  simTrack?: LearningTrack;
  onUpdateScada: (updates: Partial<ScadaState>, actionName: string, value: string | number) => void;
  onOpenNarrative: (unitId: string) => void;
  onResetPumpTrip: () => void;
}

export const ControlPanel: React.FC<ControlPanelProps> = ({
  selectedUnit,
  scada,
  simTrack = 'terpadu',
  onUpdateScada,
  onOpenNarrative,
  onResetPumpTrip,
}) => {
  const [kapurDose, setKapurDose] = useState<number>(8.5);
  const [chlorinePumpInspected, setChlorinePumpInspected] = useState<boolean>(false);

  const isChlorineSafe = scada.freeResidualChlorine >= 0.2 && scada.freeResidualChlorine <= 0.5;
  const isIpaUnit = ['intake', 'koagulasi', 'flokulasi', 'sedimentasi', 'filtrasi', 'desinfeksi'].includes(selectedUnit);
  const isDistUnit = ['pompa_distribusi', 'valve_prv', 'titik_pantau_jaringan'].includes(selectedUnit);
  const isUnitDisabledForTrack =
    (simTrack === 'ipa' && isDistUnit) || (simTrack === 'distribusi' && isIpaUnit);

  return (
    <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-4 flex flex-col h-full font-sans text-slate-100 select-none shadow-lg">
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-[#1e293b] mb-3">
        <div className="flex items-center gap-2">
          <Sliders className="w-4 h-4 text-sky-400" />
          <h3 className="text-xs font-bold text-white uppercase tracking-wider">
            PANEL KENDALI TITIK KONTROL
          </h3>
        </div>
        <span className="text-[10px] text-sky-400 font-mono font-bold capitalize">
          {selectedUnit.replace(/_/g, ' ')}
        </span>
      </div>

      <div className="flex-1 overflow-y-auto space-y-4 pr-1 text-xs">
        {isUnitDisabledForTrack && (
          <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-700 text-[11px] text-slate-400">
            Titik kontrol ini dinonaktifkan pada sesi jalur{' '}
            <strong className="text-slate-200 uppercase">{simTrack}</strong>. Pilih unit yang aktif pada diagram mimic.
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: KOAGULASI                                          */}
        {/* ======================================================== */}
        {selectedUnit === 'koagulasi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Flash Mixer Koagulasi</strong>
            </div>

            {/* Slider 1: Setpoint Dosis PAC */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider">
                  SETPOINT DOSIS KOAGULAN (PAC):
                </span>
                <span className="text-xs font-black text-sky-400 font-mono">
                  {scada.coagulantDoseSetpoint.toFixed(1)} mg/L
                </span>
              </div>
              <input
                type="range"
                min="10"
                max="80"
                step="1"
                value={scada.coagulantDoseSetpoint}
                onChange={(e) => {
                  const val = Number(e.target.value);
                  onUpdateScada(
                    { coagulantDoseSetpoint: val, coagulantActualDose: val },
                    'Ubah Setpoint Dosis Koagulan PAC',
                    `${val} mg/L`
                  );
                }}
                className="w-full accent-sky-500 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
              />
              <div className="flex justify-between text-[9px] text-slate-500 font-mono">
                <span>Normal: 20 mg/L</span>
                <span className="text-emerald-400 font-bold">SOP Banjir: 45–50 mg/L</span>
                <span>Max: 80 mg/L</span>
              </div>
            </div>

            {/* Slider 2: Dosis Penyesuai pH Kapur */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider">
                  DOSIS PENYESUAI pH (KAPUR):
                </span>
                <span className="text-xs font-black text-emerald-400 font-mono">
                  {kapurDose.toFixed(1).replace('.', ',')} mg/L
                </span>
              </div>
              <input
                type="range"
                min="0"
                max="20"
                step="0.5"
                value={kapurDose}
                onChange={(e) => {
                  const val = Number(e.target.value);
                  setKapurDose(val);
                  const adjustedPh = Number((6.6 + (val / 20) * 1.4).toFixed(2));
                  onUpdateScada(
                    { waterPh: adjustedPh },
                    'Koreksi Dosis Penyesuai pH Kapur',
                    `${val} mg/L`
                  );
                }}
                className="w-full accent-emerald-500 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
              />
              <div className="flex justify-between text-[9px] text-slate-500 font-mono">
                <span>pH Terukur: {scada.waterPh.toFixed(2)} (Aman: 6,5–8,5)</span>
              </div>
            </div>

            {/* Flash Mixer Motor Buttons */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2">
              <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider block">
                MOTOR FLASH MIXER:
              </span>
              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { flashMixerRunning: true },
                      'Nyalakan Flash Mixer Koagulasi',
                      'ON (120 RPM)'
                    )
                  }
                  className={`py-2 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                    scada.flashMixerRunning
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white'
                  }`}
                >
                  ON (120 RPM)
                </button>
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { flashMixerRunning: false },
                      'Matikan Flash Mixer Koagulasi',
                      'OFF'
                    )
                  }
                  className={`py-2 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                    !scada.flashMixerRunning
                      ? 'bg-rose-600 text-white shadow-xs'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white'
                  }`}
                >
                  OFF (STOP)
                </button>
              </div>
            </div>

            {/* Dosing Klorin (Live Telemetry) */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-1">
              <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider block">
                TELEMETRI DESINFEKSI KLORIN:
              </span>
              <div className="flex items-center justify-between text-xs font-mono">
                <span className={isChlorineSafe ? 'text-sky-300 font-bold' : 'text-rose-400 font-bold'}>
                  {scada.chlorineDoseSetpoint.toFixed(2).replace('.', ',')} mg/L (Sisa: {scada.freeResidualChlorine.toFixed(2).replace('.', ',')} mg/L)
                </span>
                <span className={`text-[10px] font-bold ${isChlorineSafe ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {isChlorineSafe ? 'Aman ✓' : 'Kritis!'}
                </span>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('koagulasi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Titik Kontrol Koagulasi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: INTAKE & POMPA AIR BAKU                            */}
        {/* ======================================================== */}
        {selectedUnit === 'intake' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Intake &amp; Pompa Air Baku</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider block">
                Kontrol Pompa Intake (Air Baku):
              </span>

              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { intakePump1Running: !scada.intakePump1Running },
                      scada.intakePump1Running ? 'Stop Pompa Intake 1' : 'Start Pompa Intake 1',
                      scada.intakePump1Running ? 'STOP' : 'RUN'
                    )
                  }
                  disabled={scada.intakePumpTripped}
                  className={`py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all ${
                    scada.intakePumpTripped
                      ? 'bg-rose-950/40 text-rose-400 border border-rose-500/40 cursor-not-allowed'
                      : scada.intakePump1Running
                      ? 'bg-emerald-600 text-white shadow-xs cursor-pointer'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white cursor-pointer'
                  }`}
                >
                  <Power className="w-3.5 h-3.5" />
                  P1: {scada.intakePumpTripped ? 'TRIP' : scada.intakePump1Running ? 'RUN' : 'STOP'}
                </button>

                <button
                  type="button"
                  onClick={() => {
                    const nextP2 = !scada.intakePump2Running;
                    onUpdateScada(
                      {
                        intakePump2Running: nextP2,
                        rawWaterFlow: nextP2 && scada.rawWaterFlow === 0 ? 100 : scada.rawWaterFlow,
                      },
                      nextP2 ? 'Start Pompa Intake 2 (Standby)' : 'Stop Pompa Intake 2',
                      nextP2 ? 'RUN' : 'STOP'
                    );
                  }}
                  className={`py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all cursor-pointer ${
                    scada.intakePump2Running
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white'
                  }`}
                >
                  <Power className="w-3.5 h-3.5" />
                  P2: {scada.intakePump2Running ? 'RUN' : 'STANDBY'}
                </button>
              </div>

              {scada.intakePumpTripped && (
                <div className="p-2.5 bg-rose-950/30 border border-rose-500/40 rounded-xl space-y-1.5">
                  <div className="flex items-center gap-1.5 text-xs font-bold text-rose-300">
                    <AlertCircle className="w-4 h-4 text-rose-400" />
                    <span>Pompa 1 Overload Trip!</span>
                  </div>
                  <p className="text-[10px] text-rose-200/80">
                    SOP: Jalankan Pompa 2 (Standby), kemudian tekan Reset Proteksi Trip sebelum Clear Alarm.
                  </p>
                  <button
                    type="button"
                    onClick={onResetPumpTrip}
                    className="w-full py-1.5 px-3 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs rounded-lg transition-colors flex items-center justify-center gap-1.5 cursor-pointer"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    <span>Reset Proteksi Trip Pompa Intake</span>
                  </button>
                </div>
              )}

              {/* Debit Intake Slider */}
              <div className="space-y-1 pt-1">
                <div className="flex items-center justify-between text-xs">
                  <span className="text-slate-400">Debit Intake:</span>
                  <span className="text-sky-400 font-mono font-bold">{scada.rawWaterFlow.toFixed(0)} L/s</span>
                </div>
                <input
                  type="range"
                  min="50"
                  max="120"
                  step="5"
                  value={Math.max(50, scada.rawWaterFlow)}
                  disabled={!scada.intakePump1Running && !scada.intakePump2Running}
                  onChange={(e) => {
                    const val = Number(e.target.value);
                    onUpdateScada({ rawWaterFlow: val }, 'Ubah Debit Intake', `${val} L/s`);
                  }}
                  className="w-full accent-sky-500 cursor-pointer h-2 bg-[#1e293b] rounded-lg disabled:opacity-40"
                />
                <div className="flex justify-between text-[9px] text-slate-500 font-mono">
                  <span>Kekeruhan Air Baku: {scada.rawWaterTurbidity.toFixed(1)} NTU</span>
                </div>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('intake')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Titik Kontrol Intake</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: FLOKULASI                                          */}
        {/* ======================================================== */}
        {selectedUnit === 'flokulasi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Flokulator 3 Kompartemen</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Kecepatan Pengaduk Lambat:</span>
                <span className="text-sky-400 font-mono font-bold">{scada.flocculatorRpm.toFixed(0)} RPM</span>
              </div>
              <input
                type="range"
                min="10"
                max="40"
                step="1"
                value={scada.flocculatorRpm}
                onChange={(e) => {
                  const val = Number(e.target.value);
                  onUpdateScada({ flocculatorRpm: val }, 'Atur Kecepatan Flokulator', `${val} RPM`);
                }}
                className="w-full accent-sky-500 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
              />
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Indeks Pembentukan Flok:</span>
                <span className="text-emerald-400 font-mono font-bold">{scada.flocQualityScore.toFixed(0)}%</span>
              </div>
              <button
                type="button"
                onClick={() =>
                  onUpdateScada(
                    { flocculatorMixerRunning: !scada.flocculatorMixerRunning },
                    scada.flocculatorMixerRunning ? 'Matikan Pengaduk Flokulasi' : 'Nyalakan Pengaduk Flokulasi',
                    scada.flocculatorMixerRunning ? 'OFF' : 'ON'
                  )
                }
                className={`w-full py-2 px-3 rounded-xl text-xs font-bold cursor-pointer ${
                  scada.flocculatorMixerRunning ? 'bg-emerald-600 text-white' : 'bg-rose-600 text-white'
                }`}
              >
                Motor Flokulator: {scada.flocculatorMixerRunning ? 'ON' : 'OFF'}
              </button>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('flokulasi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Flokulasi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: SEDIMENTASI                                        */}
        {/* ======================================================== */}
        {selectedUnit === 'sedimentasi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Sedimentasi (Plate Settler)</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Kekeruhan Keluar Bak:</span>
                <span className="text-sky-400 font-mono font-bold">{scada.settledWaterTurbidity.toFixed(1)} NTU</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Selimut Lumpur:</span>
                <span className="text-amber-400 font-mono font-bold">{scada.sludgeLevelPercent.toFixed(0)}%</span>
              </div>
              <button
                type="button"
                onClick={() =>
                  onUpdateScada(
                    {
                      clarifierBlowdownOpen: !scada.clarifierBlowdownOpen,
                      sludgeLevelPercent: !scada.clarifierBlowdownOpen
                        ? Math.max(15, scada.sludgeLevelPercent - 10)
                        : scada.sludgeLevelPercent,
                    },
                    'Ubah Valve Blowdown Lumpur Sedimentasi',
                    !scada.clarifierBlowdownOpen ? 'OPEN' : 'CLOSED'
                  )
                }
                className={`w-full py-2 px-3 rounded-xl text-xs font-bold cursor-pointer ${
                  scada.clarifierBlowdownOpen ? 'bg-emerald-600 text-white' : 'bg-[#1e293b] text-slate-300'
                }`}
              >
                Valve Blowdown Lumpur: {scada.clarifierBlowdownOpen ? 'OPEN (BUANG)' : 'CLOSED'}
              </button>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('sedimentasi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Sedimentasi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: FILTRASI                                           */}
        {/* ======================================================== */}
        {selectedUnit === 'filtrasi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Filtrasi Pasir Cepat</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Headloss Filter 1:</span>
                <span className={`font-mono font-bold ${scada.filter1Headloss > 2.0 ? 'text-rose-400' : 'text-amber-400'}`}>
                  {scada.filter1Headloss.toFixed(2)} m
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Kekeruhan Olahan:</span>
                <span className={`font-mono font-bold ${scada.filteredWaterTurbidity >= 3.0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                  {scada.filteredWaterTurbidity.toFixed(2)} NTU
                </span>
              </div>

              <div className="pt-2 space-y-1.5">
                <button
                  type="button"
                  disabled={scada.filter1Backwashing}
                  onClick={() => {
                    onUpdateScada(
                      { filter1Backwashing: true },
                      'Mulai Backwash Filter 1',
                      'BACKWASH'
                    );
                  }}
                  className={`w-full py-2 px-3 font-bold text-xs rounded-xl shadow-xs transition-colors ${
                    scada.filter1Backwashing
                      ? 'bg-sky-900/50 text-sky-300 border border-sky-500/40 cursor-wait'
                      : 'bg-sky-600 hover:bg-sky-500 text-white cursor-pointer'
                  }`}
                >
                  {scada.filter1Backwashing ? 'Sedang Proses Backwash Filter 1...' : 'Pencucian Balik (Backwash Filter 1)'}
                </button>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('filtrasi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Filtrasi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: DESINFEKSI (KLORINASI)                             */}
        {/* ======================================================== */}
        {selectedUnit === 'desinfeksi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Desinfeksi (Injeksi Klorin)</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Sisa Klor Bebas Terukur:</span>
                <span className={`font-mono font-black ${isChlorineSafe ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {scada.freeResidualChlorine.toFixed(2).replace('.', ',')} mg/L
                </span>
              </div>
              <div className="flex items-center justify-between text-[11px]">
                <span className="text-slate-400">Target Baku Mutu:</span>
                <span className="text-sky-300 font-mono font-semibold">0,20 – 0,50 mg/L</span>
              </div>

              <button
                type="button"
                onClick={() => {
                  setChlorinePumpInspected(true);
                  onUpdateScada(
                    {},
                    'Periksa & Pulihkan Pompa Dosing Klor',
                    'INSPECT_OK'
                  );
                }}
                className={`w-full py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all cursor-pointer ${
                  chlorinePumpInspected
                    ? 'bg-emerald-950/50 border border-emerald-500/40 text-emerald-300'
                    : 'bg-amber-600 hover:bg-amber-500 text-white'
                }`}
              >
                <Wrench className="w-3.5 h-3.5" />
                <span>
                  {chlorinePumpInspected
                    ? 'Pompa Dosing Klor Diperiksa ✓'
                    : 'Periksa Pompa Dosing Klor'}
                </span>
              </button>

              <div className="space-y-1.5 pt-1 border-t border-[#1e293b]">
                <div className="flex items-center justify-between">
                  <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider">
                    SETPOINT DOSIS KLORIN:
                  </span>
                  <span className="text-xs font-black text-cyan-400 font-mono">
                    {scada.chlorineDoseSetpoint.toFixed(2).replace('.', ',')} mg/L
                  </span>
                </div>
                <input
                  type="range"
                  min="0.2"
                  max="2.5"
                  step="0.05"
                  value={scada.chlorineDoseSetpoint}
                  onChange={(e) => {
                    const val = Number(e.target.value);
                    onUpdateScada(
                      { chlorineDoseSetpoint: val },
                      'Atur Setpoint Dosis Klorin',
                      `${val.toFixed(2)} mg/L`
                    );
                  }}
                  className="w-full accent-cyan-400 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
                />
                <div className="flex justify-between text-[9px] text-slate-500 font-mono">
                  <span>0,2 mg/L</span>
                  <span className="text-emerald-400 font-bold">SOP: 1,50–1,60 mg/L</span>
                  <span>2,5 mg/L</span>
                </div>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('desinfeksi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Desinfeksi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: RESERVOIR                                          */}
        {/* ======================================================== */}
        {selectedUnit === 'reservoir' && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Reservoir Air Bersih &amp; Klorinasi</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Level Air:</span>
                <span className="text-sky-400 font-mono font-bold">
                  {scada.reservoirLevelMeters.toFixed(2)} m ({scada.reservoirLevelPercent.toFixed(0)}%)
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Sisa Klorin:</span>
                <span className={`font-mono font-bold ${isChlorineSafe ? 'text-emerald-400' : 'text-rose-400'}`}>
                  {scada.freeResidualChlorine.toFixed(2).replace('.', ',')} mg/L
                </span>
              </div>

              <div className="space-y-1 pt-1 border-t border-[#1e293b]">
                <div className="flex items-center justify-between text-xs">
                  <span className="text-slate-400">Setpoint Dosis Klorin:</span>
                  <span className="text-cyan-400 font-mono font-bold">
                    {scada.chlorineDoseSetpoint.toFixed(2).replace('.', ',')} mg/L
                  </span>
                </div>
                <input
                  type="range"
                  min="0.2"
                  max="2.5"
                  step="0.05"
                  value={scada.chlorineDoseSetpoint}
                  onChange={(e) => {
                    const val = Number(e.target.value);
                    onUpdateScada(
                      { chlorineDoseSetpoint: val },
                      'Atur Setpoint Dosis Klorin (Reservoir)',
                      `${val.toFixed(2)} mg/L`
                    );
                  }}
                  className="w-full accent-cyan-400 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
                />
              </div>

              <div className="grid grid-cols-2 gap-2 pt-1">
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { reservoirInletOpen: !scada.reservoirInletOpen },
                      'Katup Inlet Reservoir',
                      scada.reservoirInletOpen ? 'TUTUP' : 'BUKA'
                    )
                  }
                  className={`py-1.5 px-2 rounded-lg text-xs font-bold cursor-pointer ${
                    scada.reservoirInletOpen ? 'bg-emerald-600 text-white' : 'bg-[#1e293b] text-slate-400'
                  }`}
                >
                  Katup Masuk: {scada.reservoirInletOpen ? 'BUKA' : 'TUTUP'}
                </button>
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { reservoirOutletOpen: !scada.reservoirOutletOpen },
                      'Katup Outlet Reservoir',
                      scada.reservoirOutletOpen ? 'TUTUP' : 'BUKA'
                    )
                  }
                  className={`py-1.5 px-2 rounded-lg text-xs font-bold cursor-pointer ${
                    scada.reservoirOutletOpen ? 'bg-emerald-600 text-white' : 'bg-[#1e293b] text-slate-400'
                  }`}
                >
                  Katup Keluar: {scada.reservoirOutletOpen ? 'BUKA' : 'TUTUP'}
                </button>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('reservoir')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Reservoir</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: POMPA DISTRIBUSI                                   */}
        {/* ======================================================== */}
        {selectedUnit === 'pompa_distribusi' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Stasiun Pompa Distribusi</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Tekanan Keluar (Discharge):</span>
                <span className={`font-mono font-bold ${scada.distDischargePressure < 3.0 ? 'text-rose-400' : 'text-sky-400'}`}>
                  {scada.distDischargePressure.toFixed(2)} bar
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Total Debit Distribusi:</span>
                <span className="text-emerald-400 font-mono font-bold">{scada.distTotalFlow.toFixed(0)} L/s</span>
              </div>

              <div className="grid grid-cols-2 gap-2 pt-1">
                <button
                  type="button"
                  disabled={scada.distPumpTripped}
                  onClick={() =>
                    onUpdateScada(
                      { distPump1Running: !scada.distPump1Running },
                      scada.distPump1Running ? 'Stop Pompa Distribusi P-101' : 'Start Pompa Distribusi P-101',
                      scada.distPump1Running ? 'STOP' : 'RUN'
                    )
                  }
                  className={`py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all ${
                    scada.distPumpTripped
                      ? 'bg-rose-950/40 text-rose-400 border border-rose-500/40 cursor-not-allowed'
                      : scada.distPump1Running
                      ? 'bg-emerald-600 text-white shadow-xs cursor-pointer'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white cursor-pointer'
                  }`}
                >
                  <Power className="w-3.5 h-3.5" />
                  P-101: {scada.distPumpTripped ? 'TRIP' : scada.distPump1Running ? 'RUN' : 'STOP'}
                </button>

                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { distPump2Running: !scada.distPump2Running },
                      scada.distPump2Running ? 'Stop Pompa Distribusi P-102' : 'Start Pompa Distribusi P-102 (Paralel/Cadangan)',
                      scada.distPump2Running ? 'STOP' : 'RUN'
                    )
                  }
                  className={`py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all cursor-pointer ${
                    scada.distPump2Running
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : 'bg-[#1e293b] text-slate-400 hover:text-white'
                  }`}
                >
                  <Power className="w-3.5 h-3.5" />
                  P-102: {scada.distPump2Running ? 'RUN' : 'STANDBY'}
                </button>
              </div>

              {scada.distPumpTripped && (
                <button
                  type="button"
                  onClick={onResetPumpTrip}
                  className="w-full py-2 px-3 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs rounded-xl transition-colors flex items-center justify-center gap-1.5 cursor-pointer"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  <span>Reset Proteksi Trip Pompa Distribusi</span>
                </button>
              )}
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('pompa_distribusi')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Pompa Distribusi</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: VALVE ZONA & PRV                                   */}
        {/* ======================================================== */}
        {selectedUnit === 'valve_prv' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Valve Zona &amp; PRV</strong>
            </div>

            {/* Leak Isolation Control */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider">
                  VALVE ISOLASI RUAS BOCOR:
                </span>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  scada.valveIsolasiBocorOpen ? 'bg-amber-500/20 text-amber-300' : 'bg-emerald-500/20 text-emerald-300'
                }`}>
                  {scada.valveIsolasiBocorOpen ? 'TERBUKA' : 'TERISOLASI ✓'}
                </span>
              </div>

              {scada.pipeLeakActive && scada.valveIsolasiBocorOpen && (
                <div className="p-2 rounded-lg bg-rose-950/40 border border-rose-500/40 text-[10px] text-rose-300 flex items-center gap-1.5">
                  <ShieldAlert className="w-4 h-4 shrink-0 text-rose-400" />
                  <span>Kebocoran pipa aktif (+{scada.leakFlowSurge} L/s)! Tutup katup isolasi segera.</span>
                </div>
              )}

              <button
                type="button"
                onClick={() =>
                  onUpdateScada(
                    { valveIsolasiBocorOpen: !scada.valveIsolasiBocorOpen },
                    scada.valveIsolasiBocorOpen ? 'Tutup Valve Isolasi Ruas Bocor' : 'Buka Valve Isolasi Ruas Bocor',
                    scada.valveIsolasiBocorOpen ? 'CLOSED (ISOLATED)' : 'OPEN'
                  )
                }
                className={`w-full py-2 px-3 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                  scada.valveIsolasiBocorOpen
                    ? 'bg-rose-600 hover:bg-rose-500 text-white'
                    : 'bg-emerald-600 hover:bg-emerald-500 text-white'
                }`}
              >
                {scada.valveIsolasiBocorOpen
                  ? 'Tutup Valve Isolasi Kebocoran'
                  : 'Valve Tertutup (Klik untuk Buka Kembali)'}
              </button>
            </div>

            {/* PRV Setpoint Slider */}
            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold text-slate-300 uppercase tracking-wider">
                  SETPOINT PRV (TEKANAN):
                </span>
                <span className="text-xs font-black text-amber-400 font-mono">
                  {scada.prvSetpointBar.toFixed(2).replace('.', ',')} bar
                </span>
              </div>
              <input
                type="range"
                min="1.2"
                max="3.2"
                step="0.1"
                value={scada.prvSetpointBar}
                onChange={(e) => {
                  const val = Number(e.target.value);
                  onUpdateScada({ prvSetpointBar: val }, 'Ubah Setpoint PRV', `${val.toFixed(1)} bar`);
                }}
                className="w-full accent-amber-500 cursor-pointer h-2 bg-[#1e293b] rounded-lg"
              />
              <div className="flex justify-between text-[9px] text-slate-500 font-mono">
                <span>1,2 bar</span>
                <span className="text-emerald-400 font-bold">Standar: 2,5 bar</span>
                <span>3,2 bar</span>
              </div>

              <div className="grid grid-cols-2 gap-2 pt-1 border-t border-[#1e293b]">
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { valveZone1Open: !scada.valveZone1Open },
                      'Ubah Valve Zona 1',
                      !scada.valveZone1Open ? 'OPEN' : 'CLOSED'
                    )
                  }
                  className={`py-1.5 px-2 rounded-lg text-[11px] font-bold cursor-pointer ${
                    scada.valveZone1Open ? 'bg-emerald-600 text-white' : 'bg-[#1e293b] text-slate-400'
                  }`}
                >
                  Z1: {scada.valveZone1Open ? 'OPEN' : 'CLOSED'}
                </button>
                <button
                  type="button"
                  onClick={() =>
                    onUpdateScada(
                      { valveZone2Open: !scada.valveZone2Open },
                      'Ubah Valve Zona 2',
                      !scada.valveZone2Open ? 'OPEN' : 'CLOSED'
                    )
                  }
                  className={`py-1.5 px-2 rounded-lg text-[11px] font-bold cursor-pointer ${
                    scada.valveZone2Open ? 'bg-emerald-600 text-white' : 'bg-[#1e293b] text-slate-400'
                  }`}
                >
                  Z2: {scada.valveZone2Open ? 'OPEN' : 'CLOSED'}
                </button>
              </div>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('valve_prv')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Valve &amp; PRV</span>
            </button>
          </div>
        )}

        {/* ======================================================== */}
        {/* UNIT: TITIK PANTAU JARINGAN                              */}
        {/* ======================================================== */}
        {selectedUnit === 'titik_pantau_jaringan' && !isUnitDisabledForTrack && (
          <div className="space-y-3.5">
            <div className="text-[11px] text-slate-400 font-semibold">
              Unit Terpilih: <strong className="text-sky-400">Titik Pantau Telemetri Jaringan</strong>
            </div>

            <div className="p-3 bg-[#0b1120] rounded-xl border border-[#1e293b] space-y-2.5">
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Tekanan Zona 1:</span>
                <span className={`font-mono font-bold ${scada.zone1Pressure < 2.0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                  {scada.zone1Pressure.toFixed(2).replace('.', ',')} bar
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Debit Zona 1:</span>
                <span className={`font-mono font-bold ${scada.zone1Flow > 36 ? 'text-rose-400' : 'text-sky-400'}`}>
                  {scada.zone1Flow.toFixed(0)} L/s
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Tekanan Zona 2:</span>
                <span className={`font-mono font-bold ${scada.zone2Pressure < 2.0 ? 'text-rose-400' : 'text-emerald-400'}`}>
                  {scada.zone2Pressure.toFixed(2).replace('.', ',')} bar
                </span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-slate-400">Sisa Klor Ujung Jaringan:</span>
                <span className={`font-mono font-bold ${scada.zoneChlorineEnd < 0.2 ? 'text-amber-400' : 'text-emerald-400'}`}>
                  {scada.zoneChlorineEnd.toFixed(2).replace('.', ',')} mg/L
                </span>
              </div>
              <p className="text-[10px] text-slate-400 pt-1 border-t border-[#1e293b]">
                Telemetri bersifat baca-saja (read-only). Untuk mengatur tekanan atau menutup kebocoran, buka panel{' '}
                <strong className="text-sky-300">Valve Zona &amp; PRV</strong> atau{' '}
                <strong className="text-sky-300">Pompa Distribusi</strong>.
              </p>
            </div>

            <button
              type="button"
              onClick={() => onOpenNarrative('titik_pantau_jaringan')}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-950/40 hover:bg-sky-900/50 border border-sky-500/40 text-sky-300 font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer"
            >
              <Info className="w-4 h-4 text-sky-400" />
              <span>Buka Narasi Titik Pantau Jaringan</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

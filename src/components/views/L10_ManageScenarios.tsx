/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useState } from 'react';
import { useApp } from '../../context/AppContext';
import {
  CheckCircle2,
  Copy,
  Edit3,
} from 'lucide-react';

export const L10_ManageScenarios: React.FC = () => {
  const { currentTenant, getVisibleGroups, showTechnicalRefs } = useApp();
  const visibleGroups = getVisibleGroups();
  const hasDistribusi = currentTenant.license.packageTracks.includes('distribusi');
  const hasTerpadu = currentTenant.license.packageTracks.includes('terpadu');

  const [title, setTitle] = useState(
    hasDistribusi
      ? 'Simulasi Kebocoran Pipa Distribusi Zona 2 saat Jam Puncak Pagi'
      : 'Simulasi Lonjakan Kekeruhan Air Baku & Penyesuaian Dosis PAC'
  );
  const [difficulty, setDifficulty] = useState<'1' | '2' | '3' | '4' | '5'>('3');
  const [track, setTrack] = useState(hasDistribusi ? 'distribusi' : 'ipa');
  const [targetPoint, setTargetPoint] = useState(hasDistribusi ? 'valve_prv' : 'koagulasi');
  const [triggerSec, setTriggerSec] = useState('90');
  const [targetTimeSec, setTargetTimeSec] = useState('60');
  const [deviationThreshold, setDeviationThreshold] = useState(
    hasDistribusi ? 'Tekanan < 2,0 bar & Debit > 40 L/s' : 'Kekeruhan Olahan ≥ 3,0 NTU'
  );
  const [assignedGroup, setAssignedGroup] = useState(visibleGroups[0]?.id || '');
  const [feedbackMsg, setFeedbackMsg] = useState<string | null>(null);

  useEffect(() => {
    const groupsNow = getVisibleGroups();
    setAssignedGroup(groupsNow[0]?.id || '');
    const allowDist = currentTenant.license.packageTracks.includes('distribusi');
    setTrack(allowDist ? 'distribusi' : 'ipa');
    setTargetPoint(allowDist ? 'valve_prv' : 'koagulasi');
    setTitle(
      allowDist
        ? 'Simulasi Kebocoran Pipa Distribusi Zona 2 saat Jam Puncak Pagi'
        : 'Simulasi Lonjakan Kekeruhan Air Baku & Penyesuaian Dosis PAC'
    );
    setDeviationThreshold(
      allowDist ? 'Tekanan < 2,0 bar & Debit > 40 L/s' : 'Kekeruhan Olahan ≥ 3,0 NTU'
    );
    setFeedbackMsg(null);
  }, [currentTenant.id]);

  const selectedGroupObj = visibleGroups.find((g) => g.id === assignedGroup) || visibleGroups[0];

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    setFeedbackMsg(
      `Skenario "${title}" berhasil disimpan dan diterbitkan ke kelompok ${
        selectedGroupObj?.name || currentTenant.name
      }.`
    );
  };

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title Block */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Kelola Skenario Gangguan Kustom · {currentTenant.name}
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Perancang Skenario Gangguan &amp; Pengaturan Tingkat Kesulitan{showTechnicalRefs ? ' (FR-23 · PRD §7)' : ''}
        </p>
      </div>

      {feedbackMsg && (
        <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-between text-xs text-emerald-300">
          <span className="flex items-center gap-2 font-semibold">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            {feedbackMsg}
          </span>
          <button
            type="button"
            onClick={() => setFeedbackMsg(null)}
            className="text-slate-400 hover:text-white font-bold px-2 cursor-pointer"
          >
            ✕
          </button>
        </div>
      )}

      {/* Main Grid: Left = Form Authoring (Width: 60%), Right = Skenario List (Width: 40%) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        {/* LEFT COLUMN: Authoring Form */}
        <div className="lg:col-span-7 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">
              Formulir Perancangan Skenario Baru{showTechnicalRefs ? ' (Authoring Tool FR-23)' : ''}
            </h2>
            <p className="text-xs text-slate-400">
              Rancang skenario kondisi abnormal berbasis hidrolika dan kimia proses air minum
            </p>
          </div>

          <form onSubmit={handleSave} className="space-y-4">
            <div>
              <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                Judul Skenario Gangguan:
              </label>
              <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="w-full px-3.5 py-2.5 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs font-semibold text-white focus:outline-hidden focus:ring-2 focus:ring-sky-500"
              />
            </div>

            {/* Tingkat Kesulitan & Pengali XP */}
            <div>
              <label className="block text-xs font-bold text-amber-400 uppercase tracking-wider mb-1">
                ★ Tingkat Kesulitan &amp; Pengali XP{showTechnicalRefs ? ' (PRD SimSCADA-Air v1.2 §7)' : ''}:
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <select
                  value={difficulty}
                  onChange={(e) => setDifficulty(e.target.value as '1' | '2' | '3' | '4' | '5')}
                  className="w-full px-3.5 py-2.5 bg-[#0b1120] border border-amber-500/50 rounded-xl text-xs font-bold text-amber-300 focus:outline-hidden"
                >
                  <option value="1">Tingkat 1: Mudah (Pengali XP = 1,0x)</option>
                  <option value="2">Tingkat 2: Sedang (Pengali XP = 1,5x)</option>
                  <option value="3">Tingkat 3: Sulit (Pengali XP = 2,0x)</option>
                  <option value="4">Tingkat 4: Sangat Sulit (Pengali XP = 2,5x)</option>
                  <option value="5">Tingkat 5: Ujian (Pengali XP = 3,0x)</option>
                </select>
                <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b] text-[10px] text-slate-400 flex items-center">
                  Pilihan: 1 Mudah (1x) · 2 Sedang (1,5x) · 3 Sulit (2x) · 4 Sangat Sulit (2,5x) · 5 Ujian (3x)
                </div>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                  Jalur Terkait:
                </label>
                <select
                  value={track}
                  onChange={(e) => setTrack(e.target.value)}
                  className="w-full px-3 py-2 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs text-white focus:outline-hidden"
                >
                  <option value="ipa">Operator IPA</option>
                  {hasDistribusi && <option value="distribusi">Operator Distribusi</option>}
                  {hasTerpadu && <option value="terpadu">Air Minum Terpadu</option>}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                  Titik Kontrol Terdampak:
                </label>
                <select
                  value={targetPoint}
                  onChange={(e) => setTargetPoint(e.target.value)}
                  className="w-full px-3 py-2 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs text-white focus:outline-hidden"
                >
                  <option value="koagulasi">Flash Mixer Koagulasi &amp; Dosing PAC</option>
                  <option value="intake">Intake Pompa Air Baku</option>
                  <option value="filtrasi">Filtrasi Pasir Cepat</option>
                  {hasDistribusi && <option value="valve_prv">Valve Isolasi Zona 2 &amp; PRV Distribusi</option>}
                </select>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                  Waktu Pemicu Gangguan (detik):
                </label>
                <input
                  type="text"
                  value={triggerSec}
                  onChange={(e) => setTriggerSec(e.target.value)}
                  placeholder="Detik ke-90 (01:30)"
                  className="w-full px-3 py-2 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs text-white font-mono"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                  Ambang Deviasi Alarm:
                </label>
                <input
                  type="text"
                  value={deviationThreshold}
                  onChange={(e) => setDeviationThreshold(e.target.value)}
                  placeholder={hasDistribusi ? 'Tekanan < 2,0 bar' : 'Kekeruhan ≥ 3,0 NTU'}
                  className="w-full px-3 py-2 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs text-rose-300 font-mono"
                />
              </div>
            </div>

            {/* SOP Scoring Key */}
            <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-xs">
              <span className="text-[10px] font-bold text-sky-400 uppercase tracking-wider block">
                Kunci Penilaian SOP &amp; Ketentuan Penalti:
              </span>
              {track === 'ipa' ? (
                <div className="text-[11px] text-slate-300 space-y-1 font-mono">
                  <p>1. Wajib menyesuaikan dosis PAC &amp; pH dalam target {targetTimeSec} detik (Bobot Respons 25%).</p>
                  <p>2. Mematikan seluruh pompa intake saat air baku tinggi dianggap tidak aman (-15 poin penalti{showTechnicalRefs ? ' PRD §8' : ''}).</p>
                  <p>3. Alarm clear otomatis saat kekeruhan air olahan ≤ 2,7 NTU stabil selama 10 detik.</p>
                </div>
              ) : (
                <div className="text-[11px] text-slate-300 space-y-1 font-mono">
                  <p>1. Wajib menutup valve isolasi V-Z2 dalam waktu target {targetTimeSec} detik (Bobot Respons 25%).</p>
                  <p>2. Mematikan semua pompa distribusi dianggap tindakan tidak aman (-15 poin penalti{showTechnicalRefs ? ' PRD §8' : ''}).</p>
                  <p>3. Alarm clear otomatis saat tekanan zona pulih di rentang 2,0–2,8 bar selama 10 detik.</p>
                </div>
              )}
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
                Tugaskan ke Kelompok / Angkatan:
              </label>
              <select
                value={assignedGroup}
                onChange={(e) => setAssignedGroup(e.target.value)}
                className="w-full px-3.5 py-2.5 bg-[#0b1120] border border-[#24324d] rounded-xl text-xs font-bold text-sky-400 focus:outline-hidden"
              >
                {visibleGroups.map((grp) => (
                  <option key={grp.id} value={grp.id}>
                    {grp.name} · {currentTenant.name}
                  </option>
                ))}
              </select>
            </div>

            <button
              type="submit"
              className="w-full py-3 px-4 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-md shadow-sky-950/50 flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>Simpan &amp; Terbitkan Skenario ke Kelas →</span>
            </button>
          </form>
        </div>

        {/* RIGHT COLUMN: Skenario List */}
        <div className="lg:col-span-5 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">Daftar Skenario Lembaga ({currentTenant.code})</h2>
            <p className="text-xs text-slate-400">Pustaka Baku Super Admin (Read-Only) + Skenario Kustom</p>
          </div>

          <div className="space-y-3">
            {/* Standard Scenario 1: IPA-06 */}
            <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1">
              <div className="flex items-center justify-between">
                <span className="text-[9px] px-2 py-0.5 rounded-md bg-slate-800 text-slate-400 font-bold uppercase tracking-wider">
                  BAKU SA
                </span>
                <span className="text-[10px] text-slate-500 font-mono">Tingkat 3 Sulit (2,0x)</span>
              </div>
              <div className="text-xs font-bold text-white">IPA-06: Lonjakan Kekeruhan Air Baku</div>
              <div className="text-[10px] text-slate-400">Kekeruhan air baku 185 NTU · Jalur IPA</div>
              <div className="text-[10px] text-slate-500 italic pt-1 flex items-center justify-between">
                <span>Dipakai di Sesi Latihan Utama</span>
                <span className="text-slate-400">Tidak dapat diubah (Terkunci)</span>
              </div>
            </div>

            {/* Standard Scenario 2: DST-05 if Distribusi licensed, else IPA-07 */}
            {hasDistribusi ? (
              <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1">
                <div className="flex items-center justify-between">
                  <span className="text-[9px] px-2 py-0.5 rounded-md bg-slate-800 text-slate-400 font-bold uppercase tracking-wider">
                    BAKU SA
                  </span>
                  <span className="text-[10px] text-slate-500 font-mono">Tingkat 3 Sulit (2,0x)</span>
                </div>
                <div className="text-xs font-bold text-white">DST-05: Gangguan Kebocoran Pipa</div>
                <div className="text-[10px] text-slate-400">Tekanan drop &amp; debit melonjak · Jalur Distribusi</div>
                <div className="text-[10px] text-slate-500 italic pt-1 flex items-center justify-between">
                  <span>Dipakai di Jalur Distribusi</span>
                  <span className="text-slate-400">Tidak dapat diubah</span>
                </div>
              </div>
            ) : (
              <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1">
                <div className="flex items-center justify-between">
                  <span className="text-[9px] px-2 py-0.5 rounded-md bg-slate-800 text-slate-400 font-bold uppercase tracking-wider">
                    BAKU SA
                  </span>
                  <span className="text-[10px] text-slate-500 font-mono">Tingkat 3 Sulit (2,0x)</span>
                </div>
                <div className="text-xs font-bold text-white">IPA-07: Gangguan Pompa Intake Trip</div>
                <div className="text-[10px] text-slate-400">Alih ke pompa standby &amp; reset trip · Jalur IPA</div>
                <div className="text-[10px] text-slate-500 italic pt-1 flex items-center justify-between">
                  <span>Dipakai di Jalur IPA</span>
                  <span className="text-slate-400">Tidak dapat diubah</span>
                </div>
              </div>
            )}

            {/* Custom Scenario strictly owned by currentTenant */}
            <div className="p-3.5 rounded-xl bg-sky-950/20 border border-sky-500/40 space-y-1.5 shadow-xs">
              <div className="flex items-center justify-between">
                <span className="text-[9px] px-2 py-0.5 rounded-md bg-sky-500/20 text-sky-300 font-bold uppercase tracking-wider border border-sky-500/30">
                  KUSTOM {currentTenant.code}
                </span>
                <span className="text-[10px] text-amber-400 font-mono font-bold">Tingkat 3 Sulit (2,0x)</span>
              </div>
              <div className="text-xs font-bold text-white">
                {hasDistribusi
                  ? 'Simulasi Kebocoran Zona 2 Puncak'
                  : 'Simulasi Kalibrasi Dosing PAC Musim Hujan'}
              </div>
              <div className="text-[10px] text-slate-400">
                Dibuat oleh {currentTenant.signers.instructorName} · Ditugaskan ke:{' '}
                {visibleGroups[0]?.name || 'Kelompok Aktif'}
              </div>
              <div className="flex items-center gap-2 pt-2">
                <button
                  type="button"
                  onClick={() =>
                    setFeedbackMsg(`Mode sunting skenario kustom ${currentTenant.code} dibuka pada formulir kiri.`)
                  }
                  className="px-2.5 py-1 rounded-lg bg-[#1e293b] hover:bg-[#334155] text-slate-300 text-[10px] font-semibold flex items-center gap-1 cursor-pointer"
                >
                  <Edit3 className="w-3 h-3" /> Edit
                </button>
                <button
                  type="button"
                  onClick={() =>
                    setFeedbackMsg(`Salinan skenario kustom ${currentTenant.code} berhasil dibuat.`)
                  }
                  className="px-2.5 py-1 rounded-lg bg-[#1e293b] hover:bg-[#334155] text-slate-300 text-[10px] font-semibold flex items-center gap-1 cursor-pointer"
                >
                  <Copy className="w-3 h-3" /> Duplikasi
                </button>
              </div>
            </div>
          </div>

          {/* Tenant Isolation Policy */}
          <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] text-[10px] text-slate-400 space-y-1">
            <span className="font-bold text-sky-400 uppercase tracking-wider text-[10px] block">
              Kebijakan Konten Multi-Tenant{showTechnicalRefs ? ' (PRD §6)' : ''}:
            </span>
            <p>
              Skenario kustom yang dibuat hanya dapat diakses oleh peserta {currentTenant.name} dan tidak akan terlihat oleh lembaga lain. Misi baku tetap menjadi acuan kelulusan.
            </p>
          </div>
        </div>

      </div>
    </div>
  );
};

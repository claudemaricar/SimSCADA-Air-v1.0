/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { formatDecimalID, formatIntegerID } from '../../utils/gamification';
import { 
  FileSpreadsheet, 
  FileText, 
  CheckCircle2,
} from 'lucide-react';

export const L14_TenantEvaluationDashboard: React.FC = () => {
  const { currentTenant, getTenantMetrics, getVisibleGroups, getVisibleUsers } = useApp();

  const [period, setPeriod] = useState('6_months');
  const [trackFilter, setTrackFilter] = useState('all');
  const [groupFilter, setGroupFilter] = useState('all');
  const [instructorFilter, setInstructorFilter] = useState('all');
  const [exportFeedback, setExportFeedback] = useState<string | null>(null);

  useEffect(() => {
    setTrackFilter('all');
    setGroupFilter('all');
    setInstructorFilter('all');
    setExportFeedback(null);
  }, [currentTenant.id]);

  // Dynamically computed metrics and lists for current tenant
  const metrics = getTenantMetrics(currentTenant.id);
  const tenantGroups = getVisibleGroups();
  const tenantUsers = getVisibleUsers();
  const tenantInstructors = tenantUsers.filter((u) => u.role === 'instruktur');
  const allowedTracks = currentTenant.license.packageTracks;
  const isIpaOnly = !allowedTracks.includes('distribusi') && !allowedTracks.includes('terpadu');

  const trackLabelMap: Record<string, string> = {
    ipa: 'Operator IPA',
    distribusi: 'Operator Distribusi',
    terpadu: 'Air Minum Terpadu',
  };

  const handleExportExcel = () => {
    setExportFeedback(`Laporan Evaluasi Pelatihan ${currentTenant.name} siap diunduh dalam format Excel (.xlsx).`);
    setTimeout(() => setExportFeedback(null), 5000);
  };

  const handleExportPdf = () => {
    window.print();
  };

  const hardestMissions = isIpaOnly
    ? [
        { title: '1. IPA-06 Gangguan Lonjakan Kekeruhan Air Baku', rate: 39, color: 'text-rose-400', bar: 'bg-rose-500' },
        { title: '2. IPA-07 Gangguan Pompa Intake Trip', rate: 34, color: 'text-amber-400', bar: 'bg-amber-500' },
        { title: '3. IPA-08 Gangguan Dosis Klorin Drop', rate: 29, color: 'text-amber-400', bar: 'bg-amber-500' },
        { title: '4. IPA-04 Operasi Normal: Penyesuaian Dosis Koagulan', rate: 24, color: 'text-sky-400', bar: 'bg-sky-500' },
        { title: '5. IPA-09 Misi Kelulusan: Pengolahan Air Lengkap', rate: 22, color: 'text-emerald-400', bar: 'bg-emerald-500' },
      ]
    : [
        { title: '1. IPA-06 Gangguan Lonjakan Kekeruhan Air Baku', rate: 42, color: 'text-rose-400', bar: 'bg-rose-500' },
        { title: '2. DST-05 Gangguan Kebocoran Pipa Distribusi', rate: 38, color: 'text-amber-400', bar: 'bg-amber-500' },
        { title: '3. TRP-01 Gangguan Berantai Hulu ke Hilir', rate: 35, color: 'text-amber-400', bar: 'bg-amber-500' },
        { title: '4. DST-06 Gangguan Tekanan Jaringan Drop', rate: 31, color: 'text-sky-400', bar: 'bg-sky-500' },
        { title: '5. IPA-07 Gangguan Pompa Intake Trip', rate: 28, color: 'text-emerald-400', bar: 'bg-emerald-500' },
      ];

  const frequentErrors = isIpaOnly
    ? [
        {
          title: '1. Terlambat Naikkan Koagulan saat Lonjakan Baku (19 Kejadian)',
          detail: 'Rata-rata respons terlambat 26 detik dari target awal.',
          wrapperClass: 'bg-rose-950/20 border-rose-500/30 text-rose-300',
          titleClass: '',
        },
        {
          title: '2. Menekan Tombol Clear saat Kondisi Masih Abnormal (14 Kejadian)',
          detail: 'Sistem menolak dengan pesan "Penyebab belum ditangani".',
          wrapperClass: 'bg-amber-950/20 border-amber-500/30 text-amber-300',
          titleClass: '',
        },
        {
          title: '3. Lupa Koreksi Dosis Kapur saat pH Air Olahan Turun (11 Kejadian)',
          detail: 'Menyebabkan pH efluen turun di bawah 6,5 saat injeksi PAC tinggi.',
          wrapperClass: 'bg-[#0b1120] border-[#1e293b] text-slate-300',
          titleClass: 'text-sky-400',
        },
      ]
    : [
        {
          title: '1. Terlambat Naikkan Koagulan saat Lonjakan Baku (34 Kejadian)',
          detail: 'Rata-rata respons terlambat 28 detik dari target awal.',
          wrapperClass: 'bg-rose-950/20 border-rose-500/30 text-rose-300',
          titleClass: '',
        },
        {
          title: '2. Menekan Tombol Clear saat Kondisi Masih Abnormal (26 Kejadian)',
          detail: 'Sistem menolak dengan pesan "Penyebab belum ditangani".',
          wrapperClass: 'bg-amber-950/20 border-amber-500/30 text-amber-300',
          titleClass: '',
        },
        {
          title: '3. Menutup Valve Isolasi yang Salah pada Kebocoran (18 Kejadian)',
          detail: 'Mengakibatkan tekanan drop merembet ke zona pelanggan aktif.',
          wrapperClass: 'bg-[#0b1120] border-[#1e293b] text-slate-300',
          titleClass: 'text-sky-400',
        },
      ];

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Dasbor Evaluasi Lembaga & ROI Pelatihan
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          {currentTenant.name} ({currentTenant.code}) · 4 Metrik Kunci Keberhasilan (T1–T4 PRD §3) · Kartu Pemakaian Lisensi & Ekspor Laporan (PRD §12)
        </p>
      </div>

      {/* Filter & Action Controls Bar */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3 p-3.5 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-sm">
        <div className="flex flex-wrap items-center gap-2.5 text-xs">
          <div className="flex items-center gap-1.5">
            <span className="text-slate-400 font-semibold">Periode:</span>
            <select
              value={period}
              onChange={(e) => setPeriod(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-2.5 py-1 text-slate-200 text-xs font-semibold focus:outline-hidden"
            >
              <option value="6_months">6 Bulan Terakhir</option>
              <option value="1_year">1 Tahun Penuh</option>
              <option value="3_months">Kuartal Ini (Q3/Q4)</option>
            </select>
          </div>

          <div className="flex items-center gap-1.5">
            <span className="text-slate-400 font-semibold">Jalur:</span>
            <select
              value={trackFilter}
              onChange={(e) => setTrackFilter(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-2.5 py-1 text-slate-200 text-xs font-semibold focus:outline-hidden"
            >
              <option value="all">Semua Jalur Paket</option>
              {allowedTracks.map((t) => (
                <option key={t} value={t}>
                  {trackLabelMap[t] || t}
                </option>
              ))}
            </select>
          </div>

          <div className="flex items-center gap-1.5">
            <span className="text-slate-400 font-semibold">Kelompok:</span>
            <select
              value={groupFilter}
              onChange={(e) => setGroupFilter(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-2.5 py-1 text-slate-200 text-xs font-semibold focus:outline-hidden"
            >
              <option value="all">
                {tenantGroups.length > 1 ? `Semua Kelompok (${tenantGroups.length})` : tenantGroups[0]?.name || 'Semua Kelompok'}
              </option>
              {tenantGroups.map((grp) => (
                <option key={grp.id} value={grp.id}>
                  {grp.name}
                </option>
              ))}
            </select>
          </div>

          <div className="flex items-center gap-1.5">
            <span className="text-slate-400 font-semibold">Instruktur:</span>
            <select
              value={instructorFilter}
              onChange={(e) => setInstructorFilter(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-2.5 py-1 text-slate-200 text-xs font-semibold focus:outline-hidden"
            >
              <option value="all">Semua Instruktur</option>
              {tenantInstructors.length > 0 ? (
                tenantInstructors.map((inst) => (
                  <option key={inst.id} value={inst.id}>
                    {inst.fullName}
                  </option>
                ))
              ) : (
                <option value="default">{currentTenant.signers.instructorName}</option>
              )}
            </select>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleExportExcel}
            className="px-3 py-1.5 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 text-xs font-semibold transition-all flex items-center gap-1.5"
          >
            <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-400" />
            <span>Ekspor Excel (.xlsx)</span>
          </button>

          <button
            onClick={handleExportPdf}
            className="px-3.5 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center gap-1.5 shadow-md shadow-sky-950/50"
          >
            <FileText className="w-3.5 h-3.5" />
            <span>Ekspor PDF Berkop</span>
          </button>
        </div>
      </div>

      {exportFeedback && (
        <div className="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-300 text-xs font-semibold flex items-center gap-2">
          <CheckCircle2 className="w-4 h-4 shrink-0" />
          <span>{exportFeedback}</span>
        </div>
      )}

      {/* 4 Cards Metrik Kunci Keberhasilan (T1–T4 PRD §3) matching SVG L14 */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* T1: Peningkatan Kompetensi */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-emerald-500/40 shadow-lg space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              T1: PENINGKATAN KOMPETENSI (PRD §3):
            </span>
            <span className="px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 font-bold text-[9px] border border-emerald-500/30">
              TARGET: ≥ 25% (LULUS)
            </span>
          </div>
          <div className="text-3xl font-black text-emerald-400 font-mono">
            +{formatDecimalID(metrics.t1ImprovementPercent, 1)}%
          </div>
          <div className="text-[11px] text-slate-300">
            Pre-Test Rata-Rata: {formatDecimalID(metrics.t1PreAverage, 1)} | Post-Test: {formatDecimalID(metrics.t1PostAverage, 1)}
          </div>
          <div className="text-[10px] text-slate-500 font-mono">
            Formula: (({formatDecimalID(metrics.t1PostAverage, 1)} − {formatDecimalID(metrics.t1PreAverage, 1)}) ÷ {formatDecimalID(metrics.t1PreAverage, 1)}) × 100% = +{formatDecimalID(metrics.t1ImprovementPercent, 1)}%
          </div>
        </div>

        {/* T2: Penguasaan Gangguan Utama */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-sky-500/40 shadow-lg space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              {isIpaOnly ? 'T2: PENGUASAAN GANGGUAN UTAMA IPA:' : 'T2: PENGUASAAN 5 GANGGUAN UTAMA:'}
            </span>
            <span className="px-2 py-0.5 rounded-md bg-sky-500/20 text-sky-300 font-bold text-[9px] border border-sky-500/30">
              TARGET: ≥ 80% (LULUS)
            </span>
          </div>
          <div className="text-3xl font-black text-sky-400 font-mono">
            {formatDecimalID(metrics.t2PassingRatePercent, 1)}%
          </div>
          <div className="text-[11px] text-slate-300">
            {isIpaOnly ? 'Lulus IPA-06, 07, 08 (≥1★)' : 'Lulus IPA-06, 07, 08 & DST-05, 06 (≥1★)'}
          </div>
          <div className="text-[10px] text-slate-500 font-mono">
            {metrics.t2PassedCount} dari {metrics.activeParticipantsCount} peserta aktif lulus {isIpaOnly ? 'gangguan utama IPA' : 'ke-5 gangguan'}
          </div>
        </div>

        {/* T3: Waktu Menuju Kelulusan */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-amber-500/40 shadow-lg space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              T3: WAKTU MENUJU KELULUSAN:
            </span>
            <span className="px-2 py-0.5 rounded-md bg-amber-500/20 text-amber-300 font-bold text-[9px] border border-amber-500/30">
              ±2 BULAN (TARGET T3)
            </span>
          </div>
          <div className="text-3xl font-black text-amber-400 font-mono">
            {metrics.t3MedianDays} Hari
          </div>
          <div className="text-[11px] text-slate-300">
            Median mulai jalur hingga piagam terbit
          </div>
          <div className="text-[10px] text-slate-500 font-mono">
            Turun dari orientasi konvensional (±90 hari)
          </div>
        </div>

        {/* T4: Penyelesaian Jalur (Kelulusan) */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-purple-500/40 shadow-lg space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              T4: PENYELESAIAN JALUR (KELULUSAN):
            </span>
            <span className="px-2 py-0.5 rounded-md bg-purple-500/20 text-purple-300 font-bold text-[9px] border border-purple-500/30">
              TARGET: ≥ 70% (LULUS)
            </span>
          </div>
          <div className="text-3xl font-black text-purple-400 font-mono">
            {formatDecimalID(metrics.t4GraduationRatePercent, 1)}%
          </div>
          <div className="text-[11px] text-slate-300">
            {metrics.t4GraduatesCount} Piagam Terbit ÷ {metrics.activeParticipantsCount} Peserta Aktif
          </div>
          <div className="text-[10px] text-slate-500 font-mono">
            Peserta aktif = login 14 hari terakhir
          </div>
        </div>

      </div>

      {/* Kartu Pemakaian Lisensi & Nilai Investasi (ROI Diklat PRD §12) */}
      <div className="p-5 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-lg space-y-3">
        <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block">
          KARTU PEMAKAIAN LISENSI & NILAI INVESTASI (ROI DIKLAT PRD §12):
        </span>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center sm:text-left">
          <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Kursi Lisensi Terpakai:</span>
            <div className="text-xl font-black text-white font-mono mt-0.5">
              {metrics.usedSeats} / {metrics.quotaSeats} <span className="text-xs text-amber-400 font-bold">({metrics.usedSeatsPercent}% Terpakai)</span>
            </div>
          </div>

          <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Sisa Masa Berlaku Lisensi:</span>
            <div className="text-xl font-black text-emerald-400 font-mono mt-0.5">
              {metrics.remainingDays} Hari Tersisa
            </div>
          </div>

          <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Total Waktu Simulasi SCADA:</span>
            <div className="text-xl font-black text-sky-400 font-mono mt-0.5">
              {formatIntegerID(metrics.totalSimulationHours)} Jam Praktik
            </div>
          </div>

          <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Peserta Aktif (14 Hari Terakhir):</span>
            <div className="text-xl font-black text-purple-400 font-mono mt-0.5">
              {metrics.activeParticipantsCount} Peserta Aktif
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Grid: 5 Misi Paling Sulit + Analisis Kesalahan Tersering */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* 5 Misi Paling Sulit */}
        <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
          <div>
            <h2 className="text-sm font-bold text-white">5 Misi Paling Sulit (Tingkat Gagal Percobaan Pertama PRD §12):</h2>
            <p className="text-[11px] text-slate-400">Bahan evaluasi materi pengajaran bagi instruktur {currentTenant.shortName}</p>
          </div>

          <div className="space-y-3 text-xs">
            {hardestMissions.map((item) => (
              <div key={item.title}>
                <div className="flex justify-between text-slate-300 mb-1">
                  <span>{item.title}</span>
                  <span className={`font-bold ${item.color}`}>{item.rate}% Gagal Percobaan 1</span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div className={`h-full ${item.bar} rounded-full`} style={{ width: `${item.rate}%` }} />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Analisis Kesalahan Tersering & Komparasi Kelompok */}
        <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
          <div>
            <h2 className="text-sm font-bold text-white">Analisis Kesalahan Tersering & Performa Kelompok (PRD §12):</h2>
            <p className="text-[11px] text-slate-400">Bahan penyempurnaan SOP operasional dan kurikulum kelas {currentTenant.shortName}</p>
          </div>

          <div className="space-y-2 text-xs">
            {frequentErrors.map((err) => (
              <div key={err.title} className={`p-3 rounded-xl border space-y-0.5 ${err.wrapperClass}`}>
                <span className={`font-bold ${err.titleClass}`}>{err.title}</span>
                <p className="text-[10px] text-slate-400">{err.detail}</p>
              </div>
            ))}
          </div>

          {/* Komparasi / Performa Kelompok Lembaga */}
          <div className="pt-2 border-t border-[#1e293b] space-y-2">
            <span className="text-[10px] font-bold text-sky-400 uppercase tracking-wider block">
              {tenantGroups.length > 1
                ? `KOMPARASI KELOMPOK ${currentTenant.shortName.toUpperCase()}:`
                : `RINGKASAN KELOMPOK ${currentTenant.shortName.toUpperCase()}:`}
            </span>
            <div className={`grid ${tenantGroups.length > 1 ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1'} gap-3 text-xs`}>
              {tenantGroups.map((grp, idx) => {
                const instUser = tenantUsers.find((u) => u.id === grp.instructorId);
                const instructorLabel = instUser ? instUser.fullName.split(',')[0] : currentTenant.signers.instructorName.split(',')[0];
                const avgScore =
                  currentTenant.id === 'tirta'
                    ? 82.4
                    : idx === 0
                    ? 84.2
                    : 81.0;
                const gradRate =
                  currentTenant.id === 'tirta'
                    ? metrics.t4GraduationRatePercent
                    : idx === 0
                    ? 79
                    : 71;

                return (
                  <div key={grp.id} className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                    <div className="font-bold text-white text-[11px]">
                      {grp.name} ({instructorLabel})
                    </div>
                    <div className={`text-[10px] mt-1 font-mono ${idx === 0 ? 'text-emerald-400' : 'text-sky-400'}`}>
                      Rata-Rata Skor: {formatDecimalID(avgScore, 1)} · Kelulusan: {formatDecimalID(gradRate, 1)}%
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

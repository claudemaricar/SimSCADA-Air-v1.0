/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useRef, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { MISSIONS_LIST } from '../../data/seedData';
import { formatDecimalID } from '../../utils/gamification';
import {
  Building2,
  CheckCircle2,
  Clock,
  Download,
  ExternalLink,
  FileCheck2,
  Lock,
  QrCode,
  Share2,
} from 'lucide-react';

interface CertificateProps {
  onOpenPublicVerification: (certNo?: string) => void;
}

export const L8_MyCertificate: React.FC<CertificateProps> = ({ onOpenPublicVerification }) => {
  const {
    currentUser,
    currentTenant,
    tenants,
    users,
    groups,
    getVisibleCertificates,
    getBestMissionResult,
    userPrePostTests,
    userMissionResults,
    verificationCertNo,
    setCurrentView,
  } = useApp();
  const certRef = useRef<HTMLDivElement>(null);
  const [selectedCertId, setSelectedCertId] = useState<string>('');
  const [copiedLink, setCopiedLink] = useState<boolean>(false);

  const visibleCerts = getVisibleCertificates();
  const issuedVisibleCerts = visibleCerts.filter(
    (c) => c.status === 'valid' && c.instructorApproved
  );

  useEffect(() => {
    if (currentUser?.role !== 'peserta') {
      const fromNav = issuedVisibleCerts.find(
        (c) => c.certificateNumber === verificationCertNo
      );
      if (fromNav) {
        setSelectedCertId(fromNav.id);
      } else if (
        issuedVisibleCerts.length > 0 &&
        !issuedVisibleCerts.some((c) => c.id === selectedCertId)
      ) {
        setSelectedCertId(issuedVisibleCerts[0].id);
      }
    }
  }, [currentTenant.id, currentUser?.role, verificationCertNo, issuedVisibleCerts.length]);

  const handlePrint = () => {
    window.print();
  };

  if (!currentUser) return null;

  // For peserta: strictly show only their OWN issued certificate, or their real unissued progress checklist
  if (currentUser.role === 'peserta') {
    const myIssuedCert = issuedVisibleCerts.find((c) => c.userId === currentUser.id);

    if (!myIssuedCert) {
      const myPendingCert = visibleCerts.find(
        (c) => c.userId === currentUser.id && c.status === 'valid' && !c.instructorApproved
      );
      const userTrack = currentUser.track || currentTenant.license.packageTracks[0] || 'ipa';
      const trackMissions = MISSIONS_LIST.filter((m) => m.track.includes(userTrack));
      const passedCount = trackMissions.filter((m) => {
        const r = getBestMissionResult(currentUser.id, m.code);
        return Boolean(r && r.isPassed);
      }).length;
      const gradCode =
        userTrack === 'ipa' ? 'IPA-09' : userTrack === 'distribusi' ? 'DST-07' : 'TRP-02';
      const gradRes = getBestMissionResult(currentUser.id, gradCode);
      const threshold = currentTenant.config.graduationThresholdScore || 80;
      const postTest = userPrePostTests.find(
        (t) => t.userId === currentUser.id && t.type === 'post'
      );
      const allMissionsPassed = passedCount === trackMissions.length && trackMissions.length > 0;
      const gradPassed = Boolean(gradRes && gradRes.totalScore >= threshold);
      const postPassed = Boolean(postTest && postTest.score >= 70);

      return (
        <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
          <div className="pb-2 border-b border-[#1e293b]">
            <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
              Piagam Kelulusan Saya · {currentUser.fullName} ({currentUser.username})
            </h1>
            <p className="text-xs text-slate-400 mt-0.5">
              {currentTenant.name} ({currentTenant.code}) · Syarat Penerbitan Piagam PRD §13
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <div className="lg:col-span-7 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-4 shadow-lg">
              <div className="flex items-start gap-3 p-4 rounded-xl bg-amber-950/25 border border-amber-500/40">
                {myPendingCert ? (
                  <Clock className="w-6 h-6 text-amber-400 shrink-0 mt-0.5" />
                ) : (
                  <Lock className="w-6 h-6 text-amber-400 shrink-0 mt-0.5" />
                )}
                <div className="space-y-1">
                  <h2 className="text-sm font-bold text-amber-300 uppercase tracking-wider">
                    {myPendingCert
                      ? `Piagam Menunggu Persetujuan Instruktur (${myPendingCert.certificateNumber})`
                      : 'Piagam Kelulusan Belum Terbit'}
                  </h2>
                  <p className="text-xs text-slate-300 leading-relaxed">
                    {myPendingCert
                      ? `Seluruh misi dan Post-Test Anda telah lulus. Menunggu verifikasi dari instruktur ${currentTenant.signers.instructorName} sebelum piagam dapat diunduh.`
                      : `Piagam kelulusan ${currentTenant.name} baru diterbitkan secara otomatis setelah seluruh 4 syarat wajib pada jalur belajar Anda terpenuhi.`}
                  </p>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div
                  className={`p-3.5 rounded-xl border ${
                    allMissionsPassed
                      ? 'bg-emerald-950/25 border-emerald-500/40'
                      : 'bg-[#0b1120] border-[#1e293b]'
                  }`}
                >
                  <div className="font-bold text-white flex items-center gap-1.5">
                    {allMissionsPassed ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    ) : (
                      <Clock className="w-4 h-4 text-amber-400" />
                    )}
                    <span>1. Semua Misi Jalur Lulus</span>
                  </div>
                  <div className="text-[11px] text-slate-400 mt-1">
                    Capaian saat ini: <strong className="text-white">{passedCount} dari {trackMissions.length} misi</strong> lulus.
                  </div>
                </div>

                <div
                  className={`p-3.5 rounded-xl border ${
                    gradPassed
                      ? 'bg-emerald-950/25 border-emerald-500/40'
                      : 'bg-[#0b1120] border-[#1e293b]'
                  }`}
                >
                  <div className="font-bold text-white flex items-center gap-1.5">
                    {gradPassed ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    ) : (
                      <Lock className="w-4 h-4 text-slate-500" />
                    )}
                    <span>2. Misi Kelulusan ({gradCode}) ≥ {threshold}</span>
                  </div>
                  <div className="text-[11px] text-slate-400 mt-1">
                    {gradRes
                      ? `Skor terbaik: ${gradRes.totalScore} / 100`
                      : 'Belum dikerjakan'}
                  </div>
                </div>

                <div
                  className={`p-3.5 rounded-xl border ${
                    postPassed
                      ? 'bg-emerald-950/25 border-emerald-500/40'
                      : 'bg-[#0b1120] border-[#1e293b]'
                  }`}
                >
                  <div className="font-bold text-white flex items-center gap-1.5">
                    {postPassed ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                    ) : (
                      <Lock className="w-4 h-4 text-slate-500" />
                    )}
                    <span>3. Post-Test Akhir ≥ 70</span>
                  </div>
                  <div className="text-[11px] text-slate-400 mt-1">
                    {postTest ? `Skor Post-Test: ${postTest.score} / 100` : 'Terbuka setelah semua misi jalur selesai'}
                  </div>
                </div>

                <div
                  className={`p-3.5 rounded-xl border ${
                    myPendingCert?.instructorApproved
                      ? 'bg-emerald-950/25 border-emerald-500/40'
                      : 'bg-[#0b1120] border-[#1e293b]'
                  }`}
                >
                  <div className="font-bold text-white flex items-center gap-1.5">
                    <Clock className="w-4 h-4 text-slate-500" />
                    <span>4. Persetujuan Instruktur</span>
                  </div>
                  <div className="text-[11px] text-slate-400 mt-1">
                    Penilai: {currentTenant.signers.instructorName}
                  </div>
                </div>
              </div>

              <div className="pt-2 flex flex-wrap gap-2">
                <button
                  type="button"
                  onClick={() => setCurrentView('home')}
                  className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all cursor-pointer"
                >
                  Kembali ke Peta Misi (L2)
                </button>
                <button
                  type="button"
                  onClick={() => onOpenPublicVerification('')}
                  className="px-4 py-2 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 font-semibold text-xs transition-all cursor-pointer"
                >
                  Portal Verifikasi Publik (L16)
                </button>
              </div>
            </div>

            <div className="lg:col-span-5 bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-3 shadow-lg text-xs">
              <h3 className="text-sm font-bold text-white flex items-center gap-2">
                <FileCheck2 className="w-4 h-4 text-sky-400" />
                <span>Informasi Piagam {currentTenant.name}</span>
              </h3>
              <p className="text-slate-400 leading-relaxed">
                Penanda tangan piagam resmi di lembaga Anda:
              </p>
              <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2">
                <div>
                  <span className="text-[10px] text-slate-500 uppercase font-bold block">Instruktur Penilai</span>
                  <span className="text-white font-semibold">{currentTenant.signers.instructorName}</span>
                  <span className="text-[11px] text-slate-400 block">{currentTenant.signers.instructorTitle}</span>
                </div>
                <div className="pt-2 border-t border-[#1e293b]">
                  <span className="text-[10px] text-slate-500 uppercase font-bold block">Pimpinan Lembaga</span>
                  <span className="text-white font-semibold">{currentTenant.signers.leaderName}</span>
                  <span className="text-[11px] text-slate-400 block">{currentTenant.signers.leaderTitle}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    }
  }

  // Pick certificate to render (for graduated peserta or admin/instruktur/pimpinan reviewing tenant certificates)
  const cert =
    currentUser.role === 'peserta'
      ? issuedVisibleCerts.find((c) => c.userId === currentUser.id)!
      : issuedVisibleCerts.find((c) => c.id === selectedCertId) ||
        issuedVisibleCerts[0] ||
        visibleCerts[0];

  if (!cert) {
    return (
      <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-4">
        <h1 className="text-xl font-bold text-white">Daftar Piagam Kelulusan · {currentTenant.name}</h1>
        <div className="p-6 rounded-2xl bg-[#0f172a] border border-[#24324d] text-xs text-slate-400">
          Belum ada piagam kelulusan yang diterbitkan di {currentTenant.name}.
        </div>
      </div>
    );
  }

  const certTenant = tenants.find((t) => t.id === cert.tenantId) || currentTenant;
  const certUser = users.find((u) => u.id === cert.userId);
  const certGroup = groups.find((g) => g.id === certUser?.groupId);
  const certGroupLabel = certGroup
    ? certGroup.name.replace(/\s*\(\d+\s*Peserta\)/i, '')
    : groups.find((g) => g.tenantId === certTenant.id)?.name.replace(/\s*\(\d+\s*Peserta\)/i, '') || 'Angkatan 1';

  const trackMissions = MISSIONS_LIST.filter((m) => m.track.includes(cert.track));
  const trackMissionTotal = trackMissions.length || 9;
  const gradMissionCode = cert.track === 'ipa' ? 'IPA-09' : cert.track === 'distribusi' ? 'DST-07' : 'TRP-02';
  const gradResult = getBestMissionResult(cert.userId, gradMissionCode);
  const gradScore = gradResult?.totalScore ?? cert.averageScore;

  const computedStars = trackMissions.reduce((acc, m) => {
    const res = getBestMissionResult(cert.userId, m.code);
    return acc + (res?.isPassed ? res.stars : 0);
  }, 0);
  const displayStars = (userMissionResults[cert.userId] || []).length > 0 ? computedStars : cert.starsCount;

  const preTest = userPrePostTests.find((t) => t.userId === cert.userId && t.type === 'pre');
  const postTest = userPrePostTests.find((t) => t.userId === cert.userId && t.type === 'post');
  const preScore = preTest?.score ?? 55;
  const postScore = postTest?.score ?? 74;
  const gainPct =
    preScore > 0 ? formatDecimalID(((postScore - preScore) / preScore) * 100, 1) : '0,0';

  const shortSignatureName = (fullName: string) =>
    fullName.replace(/^(Dr\.|Ir\.|Hj\.|H\.)\s+/gi, '').split(',')[0].trim();

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title Block */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-3 pb-2 border-b border-[#1e293b]">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
            {currentUser.role === 'peserta'
              ? `Piagam Kelulusan Terbit · ${cert.userName} (${currentUser.username})`
              : `Arsip Piagam Terbit (${issuedVisibleCerts.length}) · ${currentTenant.name}`}
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Format Baku Cetak A4 Landscape · Sesuai Ketentuan Ketat PRD SimSCADA-Air §13
          </p>
        </div>

        {currentUser.role !== 'peserta' && issuedVisibleCerts.length > 0 && (
          <div className="flex items-center gap-2">
            <span className="text-xs text-slate-400 font-semibold">Pilih Piagam {currentTenant.code}:</span>
            <select
              value={cert.id}
              onChange={(e) => setSelectedCertId(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-3 py-1.5 text-xs font-semibold text-sky-400 focus:outline-hidden"
            >
              {issuedVisibleCerts.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.certificateNumber} — {c.userName}
                </option>
              ))}
            </select>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        {/* LEFT COLUMN: THE OFFICIAL A4 CERTIFICATE (Width: 8 cols) */}
        <div className="lg:col-span-8 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 shadow-xl">
          {/* Certificate Container with Guilloche styling */}
          <div 
            ref={certRef}
            className="bg-white text-slate-900 rounded-xl p-8 sm:p-10 border-4 border-amber-600/80 shadow-2xl relative overflow-hidden space-y-6 print:border-none print:shadow-none"
          >
            {/* Inner dashed frame */}
            <div className="absolute inset-2 border-2 border-dashed border-amber-700/30 rounded-lg pointer-events-none" />

            {/* Header: Tenant Logo & Title */}
            <div className="flex items-center justify-between pb-4 border-b-2 border-slate-900 relative">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-sky-600 text-white flex items-center justify-center font-bold">
                  <Building2 className="w-7 h-7" />
                </div>
                <div>
                  <h2 className="text-lg font-black tracking-tight text-slate-900 uppercase">
                    {cert.tenantName}
                  </h2>
                  <p className="text-[11px] text-slate-600 uppercase tracking-widest font-semibold">
                    LEMBAGA PELATIHAN OPERATOR SISTEM PENYEDIAAN AIR MINUM
                  </p>
                </div>
              </div>

              <div className="px-3.5 py-1.5 bg-slate-900 text-white font-mono text-xs font-bold rounded-lg tracking-wider">
                {cert.certificateNumber}
              </div>
            </div>

            {/* Certificate Core Statement */}
            <div className="text-center space-y-3 py-4">
              <h3 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-wider uppercase font-serif">
                PIAGAM KELULUSAN
              </h3>
              <div className="text-xs font-bold text-sky-800 tracking-widest uppercase">
                {cert.trackName}
              </div>

              <p className="text-xs text-slate-600 italic">
                Diberikan dengan bangga kepada:
              </p>

              <div className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-wide font-serif py-1">
                {cert.userName.toUpperCase()}
              </div>
              <div className="text-xs font-medium text-slate-600">
                {certGroupLabel} · {cert.tenantName}
              </div>

              <p className="text-xs text-slate-700 max-w-xl mx-auto leading-relaxed pt-2">
                Telah menyelesaikan seluruh rangkaian pelatihan berbasis simulator SCADA pada jalur terkait, memenuhi seluruh kriteria kompetensi penanganan gangguan dan dinyatakan:
              </p>

              <div className="pt-2">
                <span className="inline-block px-6 py-2 rounded-xl bg-amber-500 text-slate-950 font-black text-sm uppercase tracking-wider shadow-sm">
                  PREDIKAT: {cert.predicate.toUpperCase()}
                </span>
              </div>
            </div>

            {/* Achievement Matrix */}
            <div className="grid grid-cols-3 gap-3 text-center py-2 px-4 bg-slate-50 border border-slate-200 rounded-xl">
              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-wider block">Tanggal Lulus:</span>
                <span className="text-xs font-bold text-slate-900">{cert.issueDate}</span>
              </div>
              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-wider block">Level Kompetensi:</span>
                <span className="text-xs font-bold text-purple-900">{cert.operatorLevel}</span>
              </div>
              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-wider block">Capaian Bintang:</span>
                <span className="text-xs font-bold text-amber-600">{displayStars} Bintang ({trackMissionTotal} Misi)</span>
              </div>
            </div>

            {/* Signatures & QR Code */}
            <div className="grid grid-cols-3 gap-4 items-end pt-4 pb-2">
              {/* Left Signer */}
              <div className="text-center space-y-1">
                <span className="text-[11px] text-slate-600 block">Instruktur Penilai,</span>
                <div className="h-10 flex items-center justify-center">
                  <span className="font-serif italic text-base text-sky-800 font-bold border-b border-slate-400 px-4">
                    {shortSignatureName(certTenant.signers.instructorName)}
                  </span>
                </div>
                <div className="font-bold text-xs text-slate-900 leading-tight">
                  {certTenant.signers.instructorName}
                </div>
                <div className="text-[10px] text-slate-500">
                  {certTenant.signers.instructorTitle}
                </div>
              </div>

              {/* Center QR Code */}
              <div className="flex flex-col items-center justify-center text-center">
                <div 
                  onClick={() => onOpenPublicVerification(cert.certificateNumber)}
                  className="p-2 border border-slate-300 rounded-lg bg-white shadow-2xs cursor-pointer hover:border-sky-500 transition-colors"
                  title="Klik untuk verifikasi publik"
                >
                  <QrCode className="w-14 h-14 text-slate-900" />
                </div>
                <span className="text-[9px] text-slate-500 mt-1 font-mono">Scan Validasi L16</span>
              </div>

              {/* Right Signer */}
              <div className="text-center space-y-1">
                <span className="text-[11px] text-slate-600 block">Pimpinan Lembaga,</span>
                <div className="h-10 flex items-center justify-center">
                  <span className="font-serif italic text-base text-amber-800 font-bold border-b border-slate-400 px-4">
                    {shortSignatureName(certTenant.signers.leaderName)}
                  </span>
                </div>
                <div className="font-bold text-xs text-slate-900 leading-tight">
                  {certTenant.signers.leaderName}
                </div>
                <div className="text-[10px] text-slate-500">
                  {certTenant.signers.leaderTitle}
                </div>
              </div>
            </div>

            {/* Mandatory Footnote (PRD §13) */}
            <div className="pt-3 border-t border-slate-200 text-center space-y-0.5">
              <p className="text-[10px] text-slate-600 font-semibold italic">
                "Piagam ini menyatakan penyelesaian pelatihan berbasis simulator dan bukan sertifikat kompetensi resmi."
              </p>
              <p className="text-[9px] text-slate-500 font-mono">
                Simulator: SimSCADA-Air · Kode Verifikasi: {cert.certificateNumber} · Validasi di portal publik tanpa login
              </p>
            </div>
          </div>
        </div>

        {/* RIGHT COLUMN: VERIFIKASI SYARAT & AKSI UNDUH (Width: 4 cols) */}
        <div className="lg:col-span-4 space-y-6">
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
            <div>
              <h2 className="text-sm font-bold text-white">Verifikasi Syarat Kelulusan Jalur</h2>
              <p className="text-[11px] text-slate-400">Standar Kelulusan PRD SimSCADA-Air §13</p>
            </div>

            {/* 4 Checklist Criteria */}
            <div className="space-y-2.5 text-xs">
              <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-emerald-300 flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-white">1. Semua Misi Wajib Lulus</div>
                  <div className="text-[11px] text-emerald-300/80">{trackMissionTotal} dari {trackMissionTotal} Misi Diselesaikan (100% Lulus)</div>
                </div>
              </div>

              <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-emerald-300 flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-white">2. Misi Kelulusan Skor ≥ 80</div>
                  <div className="text-[11px] text-emerald-300/80">Skor {gradMissionCode}: {gradScore} / 100 (ambang ≥ 80 tercapai)</div>
                </div>
              </div>

              <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-emerald-300 flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-white">3. Post-Test Akhir ≥ 70</div>
                  <div className="text-[11px] text-emerald-300/80">Post-test {postScore} / 100 (pre-test {preScore} → +{gainPct}%)</div>
                </div>
              </div>

              <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-emerald-300 flex items-start gap-2.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <div className="font-bold text-white">4. Persetujuan Instruktur</div>
                  <div className="text-[11px] text-emerald-300/80">Disetujui {certTenant.signers.instructorName} · {cert.issueDate}</div>
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="space-y-2 pt-2 border-t border-[#1e293b]">
              <button
                onClick={handlePrint}
                className="w-full py-3 px-4 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-md shadow-sky-950/50 cursor-pointer"
              >
                <Download className="w-4 h-4" />
                <span>Unduh Piagam (PDF) ⎙</span>
              </button>

              <button
                onClick={() => onOpenPublicVerification(cert.certificateNumber)}
                className="w-full py-2.5 px-3 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 hover:text-white font-semibold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
              >
                <ExternalLink className="w-3.5 h-3.5 text-sky-400" />
                <span>Verifikasi di Portal Publik (L16)</span>
              </button>

              <button
                onClick={() => {
                  navigator.clipboard?.writeText(cert.qrVerificationUrl);
                  setCopiedLink(true);
                  setTimeout(() => setCopiedLink(false), 3000);
                }}
                className="w-full py-2 px-3 rounded-xl bg-[#0b1120] hover:bg-[#1e293b] border border-[#1e293b] text-slate-400 hover:text-slate-200 font-medium text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
              >
                <Share2 className="w-3.5 h-3.5" />
                <span>{copiedLink ? 'Tautan Verifikasi Disalin ✓' : 'Bagikan ke LinkedIn / Rekruter'}</span>
              </button>
            </div>

            {/* PRD Legal Note */}
            <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b] text-[10px] text-slate-400 space-y-1">
              <span className="font-bold text-slate-300 block uppercase tracking-wider text-[10px]">
                Catatan Ketentuan Hukum (PRD §13):
              </span>
              <p>
                Piagam tidak memuat NIP aparatur atau rincian nilai angka untuk menjaga privasi peserta. Piagam dapat dicabut oleh Admin Lembaga jika ditemukan pelanggaran.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

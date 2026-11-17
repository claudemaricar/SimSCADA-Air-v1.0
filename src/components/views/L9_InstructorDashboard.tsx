/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { MISSIONS_LIST } from '../../data/seedData';
import { computeStarsFromScore, computeUserTotalStarsAndXP } from '../../utils/gamification';
import { LearningTrack, MissionResult, User } from '../../types';
import {
  AlertTriangle,
  FileCheck2,
  History,
  MessageSquare,
  Unlock,
} from 'lucide-react';

interface InstructorDashboardProps {
  onViewReplay: (userId: string) => void;
  onNavigateScenarios: () => void;
}

const PRIORITY_ORDER = [
  'user-peserta-ipa',
  'user-peserta-baru',
  'user-peserta-distribusi',
  'user-peserta-lulus',
  'user-eko-prasetyo',
  'user-rian-hidayat',
  'user-peserta-tirta',
];

const renderStarsLabel = (stars: number): string => {
  return '★'.repeat(stars) + '☆'.repeat(Math.max(0, 3 - stars));
};

const getTrackShortLabel = (track: LearningTrack): string => {
  if (track === 'ipa') return 'Operator IPA (9 Misi)';
  if (track === 'distribusi') return 'Operator Distribusi (7 Misi)';
  return 'Air Minum Terpadu (16 Misi)';
};

const formatLastActivity = (iso: string): string => {
  if (!iso) return '–';
  if (iso.startsWith('2026-10-28')) return 'Hari ini';
  if (iso.startsWith('2026-10-26')) return '2 hari lalu';
  if (iso.startsWith('2026-10-25')) return '3 hari lalu';
  return new Date(iso).toLocaleDateString('id-ID', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
  });
};

export const L9_InstructorDashboard: React.FC<InstructorDashboardProps> = ({
  onViewReplay,
  onNavigateScenarios,
}) => {
  const {
    currentTenant,
    users,
    certificates,
    approveCertificate,
    unlockMissionForUser,
    setCurrentView,
    setVerificationCertNo,
    userMissionResults,
    userPrePostTests,
    getVisibleGroups,
    getUserOperatorLevel,
    getBestMissionResult,
    isMissionUnlocked,
  } = useApp();

  const visibleGroups = getVisibleGroups();
  const [selectedGroup, setSelectedGroup] = useState<string>(
    visibleGroups[0]?.id || ''
  );
  const [selectedTrackFilter, setSelectedTrackFilter] = useState<string>('all');
  const [unlockedEko, setUnlockedEko] = useState<boolean>(false);
  const [actionBanner, setActionBanner] = useState<string | null>(null);

  useEffect(() => {
    if (visibleGroups.length > 0 && !visibleGroups.some((g) => g.id === selectedGroup)) {
      setSelectedGroup(visibleGroups[0].id);
    }
    setSelectedTrackFilter('all');
    setActionBanner(null);
  }, [currentTenant.id, visibleGroups, selectedGroup]);

  // Check pending certificate within current tenant
  const pendingCert = certificates.find(
    (c) =>
      c.tenantId === currentTenant.id &&
      c.status === 'valid' &&
      !c.instructorApproved
  );

  const handleApprovePending = () => {
    if (pendingCert) {
      approveCertificate(pendingCert.id);
      setActionBanner(
        `Piagam ${pendingCert.certificateNumber} atas nama ${pendingCert.userName} berhasil disetujui dan diterbitkan.`
      );
    }
  };

  const handleUnlockEko = () => {
    const hasEko = users.some(
      (u) => u.id === 'user-eko-prasetyo' && u.tenantId === currentTenant.id
    );
    if (hasEko) {
      unlockMissionForUser('user-eko-prasetyo', 'IPA-07');
      unlockMissionForUser('user-eko-prasetyo', 'IPA-08');
      setUnlockedEko(true);
      setActionBanner(
        'Kunci Misi IPA-07 dan IPA-08 untuk Eko Prasetyo berhasil dibuka oleh instruktur.'
      );
      return;
    }
    const firstParticipant = groupParticipants[0];
    if (firstParticipant) {
      const nextLocked = MISSIONS_LIST.find(
        (m) =>
          m.track.includes(firstParticipant.track || 'ipa') &&
          !isMissionUnlocked(firstParticipant.id, m.code)
      );
      if (nextLocked) {
        unlockMissionForUser(firstParticipant.id, nextLocked.code);
        setActionBanner(
          `Misi ${nextLocked.code} untuk ${firstParticipant.fullName} berhasil dibuka secara manual.`
        );
        return;
      }
    }
    setActionBanner('Seluruh misi aktif peserta pada kelompok ini sudah terbuka.');
  };

  // All participants in current tenant & selected group (including peserta.baru & all Angkatan 1 accounts)
  const groupParticipants = users
    .filter(
      (u) =>
        u.tenantId === currentTenant.id &&
        u.role === 'peserta' &&
        (!selectedGroup || u.groupId === selectedGroup) &&
        (selectedTrackFilter === 'all' || (u.track || 'ipa') === selectedTrackFilter)
    )
    .sort((a: User, b: User) => {
      const idxA = PRIORITY_ORDER.indexOf(a.id);
      const idxB = PRIORITY_ORDER.indexOf(b.id);
      if (idxA !== -1 && idxB !== -1) return idxA - idxB;
      if (idxA !== -1) return -1;
      if (idxB !== -1) return 1;
      return a.username.localeCompare(b.username, undefined, { numeric: true });
    });

  const getLatestAttempt = (userId: string): MissionResult | null => {
    const raw = userMissionResults[userId] || [];
    if (raw.length === 0) return null;
    const sorted = [...raw].sort((a, b) => {
      const diff = new Date(b.completedAt).getTime() - new Date(a.completedAt).getTime();
      if (diff !== 0) return diff;
      return raw.indexOf(b) - raw.indexOf(a);
    });
    return sorted[0];
  };

  const showEkoLaggingAlert = groupParticipants.some((u) => u.id === 'user-eko-prasetyo');

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-5">
      {/* Page Title */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Dasbor Pengawasan Kelas Instruktur
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Matriks Kemajuan Peserta × Misi · Deteksi Otomatis Peserta Tertinggal (Lagging Alerts) (PRD §12)
        </p>
      </div>

      {/* Control Bar: Filters & Action Buttons */}
      <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3 p-3.5 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-sm">
        <div className="flex flex-wrap items-center gap-3">
          <div className="flex items-center gap-2">
            <span className="text-xs text-slate-400 font-semibold">Kelompok Binaan:</span>
            <select
              value={selectedGroup}
              onChange={(e) => setSelectedGroup(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-3 py-1.5 text-xs font-bold text-sky-400 focus:outline-hidden"
            >
              {visibleGroups.map((grp) => (
                <option key={grp.id} value={grp.id}>
                  {grp.name}
                </option>
              ))}
            </select>
          </div>

          <div className="flex items-center gap-2">
            <span className="text-xs text-slate-400 font-semibold">Jalur Belajar:</span>
            <select
              value={selectedTrackFilter}
              onChange={(e) => setSelectedTrackFilter(e.target.value)}
              className="bg-[#0b1120] border border-[#334155] rounded-xl px-3 py-1.5 text-xs text-slate-200 focus:outline-hidden"
            >
              <option value="all">Semua Jalur</option>
              {currentTenant.license.packageTracks.includes('ipa') && (
                <option value="ipa">Operator IPA</option>
              )}
              {currentTenant.license.packageTracks.includes('distribusi') && (
                <option value="distribusi">Operator Distribusi</option>
              )}
              {currentTenant.license.packageTracks.includes('terpadu') && (
                <option value="terpadu">Air Minum Terpadu</option>
              )}
            </select>
          </div>

          <span className="text-[11px] px-2.5 py-1 rounded-lg bg-[#0b1120] border border-[#1e293b] text-slate-300 font-mono">
            {groupParticipants.length} Peserta
          </span>
        </div>

        {/* Action Buttons Matching SVG L9 */}
        <div className="flex flex-wrap items-center gap-2">
          <button
            onClick={onNavigateScenarios}
            className="px-3 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center gap-1.5 shadow-sm cursor-pointer"
          >
            <span>+ Tugaskan Skenario</span>
          </button>

          <button
            onClick={handleUnlockEko}
            className="px-3 py-1.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <Unlock className="w-3.5 h-3.5" />
            <span>Buka Kunci</span>
          </button>

          {pendingCert && (
            <button
              onClick={handleApprovePending}
              className="px-3 py-1.5 rounded-xl bg-purple-700 hover:bg-purple-600 text-white font-bold text-xs transition-all flex items-center gap-1.5 shadow-sm cursor-pointer"
            >
              <FileCheck2 className="w-3.5 h-3.5" />
              <span>Setujui Piagam (1)</span>
            </button>
          )}

          <button
            onClick={() => {
              const firstWithHistory = groupParticipants.find(
                (p) => (userMissionResults[p.id] || []).length > 0
              );
              onViewReplay(firstWithHistory?.id || groupParticipants[0]?.id || '');
            }}
            className="px-3 py-1.5 rounded-xl bg-amber-700 hover:bg-amber-600 text-white font-bold text-xs transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <History className="w-3.5 h-3.5" />
            <span>Putar Ulang (L11)</span>
          </button>

          <button
            onClick={() =>
              setActionBanner(
                `Mode Catatan Evaluasi aktif untuk ${currentTenant.name}. Catatan instruktur tampil di ringkasan peserta.`
              )
            }
            className="px-3 py-1.5 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-300 text-xs font-semibold transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <MessageSquare className="w-3.5 h-3.5" />
            <span>Beri Catatan Evaluasi</span>
          </button>
        </div>
      </div>

      {actionBanner && (
        <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-emerald-300 text-xs flex items-center justify-between gap-3">
          <span>{actionBanner}</span>
          <button
            type="button"
            onClick={() => setActionBanner(null)}
            className="text-emerald-200 hover:text-white font-bold cursor-pointer"
          >
            ✕
          </button>
        </div>
      )}

      {/* Lagging Student Alert (PRD §12 Alert) */}
      {showEkoLaggingAlert && (
        <div className="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/50 text-rose-200 text-xs flex items-center gap-2.5 shadow-sm">
          <AlertTriangle className="w-4 h-4 text-rose-400 shrink-0" />
          <div className="leading-snug">
            <strong className="text-rose-300 uppercase tracking-wider">
              PERINGATAN PESERTA TERTINGGAL (PRD §12):
            </strong>{' '}
            Eko Prasetyo (eko.prasetyo) tidak lulus IPA-07 (Pompa Trip) 3 kali berturut-turut.
            Disarankan bimbingan atau buka kunci.
          </div>
        </div>
      )}

      {/* Main Roster Matrix Table */}
      <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] overflow-hidden shadow-lg">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-[#0b1120] text-slate-400 text-[10px] uppercase tracking-wider border-b border-[#1e293b] font-bold">
              <tr>
                <th className="py-3 px-4">Nama Peserta / Akun</th>
                <th className="py-3 px-3">Misi Aktif</th>
                <th className="py-3 px-3 text-center">Skor Terakhir</th>
                <th className="py-3 px-3 text-center">Bintang</th>
                <th className="py-3 px-3">Aktivitas</th>
                <th className="py-3 px-3">Status Peserta</th>
                <th className="py-3 px-3">Matriks Progres Misi Jalur</th>
                <th className="py-3 px-4 text-right">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1e293b] font-sans">
              {groupParticipants.map((participant) => {
                const userTrack: LearningTrack = participant.track || 'ipa';
                const trackMissions = MISSIONS_LIST.filter((m) => m.track.includes(userTrack));
                const rawResults = userMissionResults[participant.id] || [];
                const stats = computeUserTotalStarsAndXP(rawResults, MISSIONS_LIST);
                const opLevel = getUserOperatorLevel(participant.id);
                const latestAttempt = getLatestAttempt(participant.id);
                const latestMissionDef = latestAttempt
                  ? MISSIONS_LIST.find((m) => m.code === latestAttempt.missionCode)
                  : undefined;
                const latestStars = latestAttempt
                  ? computeStarsFromScore(
                      latestAttempt.totalScore,
                      latestMissionDef?.passScore ?? 70
                    )
                  : 0;

                const hasPreTest = userPrePostTests.some(
                  (t) => t.userId === participant.id && t.type === 'pre'
                );
                const postTest = userPrePostTests.find(
                  (t) => t.userId === participant.id && t.type === 'post'
                );
                const userCert = certificates.find(
                  (c) => c.userId === participant.id && c.status === 'valid'
                );

                // Count passed missions in active track
                const passedInTrack = trackMissions.filter((m) => {
                  const best = getBestMissionResult(participant.id, m.code);
                  return Boolean(best && best.isPassed);
                }).length;

                // Determine active mission
                const nextMission = trackMissions.find((m) => {
                  const best = getBestMissionResult(participant.id, m.code);
                  return !best || !best.isPassed;
                });

                const isLagging = participant.id === 'user-eko-prasetyo';
                const isPendingCert = Boolean(userCert && !userCert.instructorApproved);
                const isIssuedCert = Boolean(userCert && userCert.instructorApproved);
                const isNotStarted = !hasPreTest && rawResults.length === 0;

                let activeMissionTitle = '';
                let activeMissionSubtitle = '';
                if (isNotStarted) {
                  activeMissionTitle = 'Belum Mulai · Pre-Test';
                  activeMissionSubtitle = `${getTrackShortLabel(userTrack)} · 0/${trackMissions.length} Misi`;
                } else if (nextMission) {
                  activeMissionTitle = `${nextMission.code}: ${nextMission.name}`;
                  activeMissionSubtitle = `${getTrackShortLabel(userTrack)}`;
                } else {
                  const lastMission = trackMissions[trackMissions.length - 1];
                  activeMissionTitle = lastMission
                    ? `${lastMission.code}: ${lastMission.name}`
                    : 'Semua Misi Selesai';
                  activeMissionSubtitle = `Semua ${trackMissions.length} Misi Lulus${
                    postTest ? ` · Post-test ${postTest.score}` : ''
                  }`;
                }

                const activityLabel = formatLastActivity(participant.lastLoginAt);

                return (
                  <tr
                    key={participant.id}
                    className={`hover:bg-[#1e293b]/40 transition-colors ${
                      isLagging
                        ? 'bg-rose-950/10'
                        : isPendingCert
                        ? 'bg-amber-950/15'
                        : ''
                    }`}
                  >
                    {/* Nama Peserta / Akun */}
                    <td className="py-3.5 px-4">
                      <div className="font-bold text-white text-xs">{participant.fullName}</div>
                      <div
                        className={`text-[10px] font-mono ${
                          isIssuedCert
                            ? 'text-emerald-400'
                            : isLagging
                            ? 'text-rose-400'
                            : isPendingCert
                            ? 'text-purple-300'
                            : isNotStarted
                            ? 'text-slate-400'
                            : 'text-sky-400'
                        }`}
                      >
                        {participant.username} · {opLevel.level} ({stats.totalXP.toLocaleString('id-ID')} XP)
                      </div>
                    </td>

                    {/* Misi Aktif */}
                    <td className="py-3 px-3">
                      <div
                        className={`font-semibold text-xs ${
                          isNotStarted
                            ? 'text-amber-300'
                            : isLagging
                            ? 'text-rose-300'
                            : isIssuedCert
                            ? 'text-purple-300'
                            : 'text-sky-300'
                        }`}
                      >
                        {activeMissionTitle}
                      </div>
                      <div className="text-[10px] text-slate-400">{activeMissionSubtitle}</div>
                    </td>

                    {/* Skor Terakhir (diambil dinamis dari data peserta) */}
                    <td className="py-3 px-3 text-center font-mono font-bold">
                      {latestAttempt ? (
                        <span
                          className={
                            !latestAttempt.isPassed
                              ? 'text-rose-400'
                              : latestAttempt.totalScore >= 95
                              ? 'text-emerald-400'
                              : 'text-sky-400'
                          }
                        >
                          {latestAttempt.totalScore}{' '}
                          <span className="text-[10px] text-slate-500 font-normal">/ 100</span>
                          <span className="block text-[9px] text-slate-400 font-normal">
                            {latestAttempt.missionCode}
                          </span>
                        </span>
                      ) : (
                        <span className="text-slate-500">–</span>
                      )}
                    </td>

                    {/* Bintang (dari skor terakhir) */}
                    <td className="py-3 px-3 text-center">
                      <span
                        className={`font-bold ${
                          latestAttempt && latestStars > 0 ? 'text-amber-400' : 'text-slate-500'
                        }`}
                      >
                        {renderStarsLabel(latestStars)}
                      </span>
                      <span className="block text-[9px] text-slate-400 font-mono">
                        Total {stats.totalStars}★
                      </span>
                    </td>

                    {/* Aktivitas */}
                    <td
                      className={`py-3 px-3 text-[11px] ${
                        activityLabel === 'Hari ini'
                          ? 'text-emerald-400 font-semibold'
                          : 'text-slate-400'
                      }`}
                    >
                      {activityLabel}
                    </td>

                    {/* Status Peserta */}
                    <td className="py-3 px-3">
                      {isIssuedCert ? (
                        <span className="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[10px] font-bold">
                          Piagam Terbit ✓
                        </span>
                      ) : isPendingCert ? (
                        <span className="px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[10px] font-bold">
                          Menunggu Persetujuan
                        </span>
                      ) : isLagging ? (
                        <span className="px-2 py-0.5 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/40 text-[10px] font-bold">
                          {unlockedEko ? 'Kunci Dibuka Instruktur' : 'TERTINGGAL (3X GAGAL)'}
                        </span>
                      ) : isNotStarted ? (
                        <span className="px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30 text-[10px] font-bold">
                          Belum Mulai (Pre-Test)
                        </span>
                      ) : latestAttempt?.isPassed ? (
                        <span className="px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30 text-[10px] font-bold">
                          Lulus {latestAttempt.missionCode} ✓
                        </span>
                      ) : (
                        <span className="px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 text-[10px] font-bold">
                          Pre-Test Selesai
                        </span>
                      )}
                    </td>

                    {/* Matriks Progres Misi Jalur */}
                    <td className="py-3 px-3">
                      {isIssuedCert ? (
                        <span className="px-2.5 py-1 rounded-lg bg-emerald-950/60 border border-emerald-500/40 text-emerald-300 font-bold text-[10px]">
                          ✓ SEMUA {trackMissions.length} MISI LULUS ({stats.totalStars} BINTANG)
                        </span>
                      ) : isPendingCert && userCert ? (
                        <span className="text-[11px] text-emerald-300 font-semibold">
                          Semua syarat terpenuhi · {userCert.certificateNumber} dicadangkan
                        </span>
                      ) : isNotStarted ? (
                        <span className="text-[11px] text-slate-400 font-mono">
                          Pre-Test belum selesai · 0 / {trackMissions.length} Misi ({getTrackShortLabel(userTrack)})
                        </span>
                      ) : trackMissions.length <= 9 ? (
                        <div className="flex items-center flex-wrap gap-1 font-mono text-[9px] font-bold">
                          {trackMissions.map((m) => {
                            const best = getBestMissionResult(participant.id, m.code);
                            const unlocked = isMissionUnlocked(participant.id, m.code);
                            const shortCode = m.code.split('-')[1];
                            const isFailedTarget = isLagging && m.code === 'IPA-07' && !best?.isPassed;
                            if (best && best.isPassed) {
                              return (
                                <span
                                  key={m.code}
                                  className={`px-1.5 py-0.5 rounded text-white ${
                                    best.stars === 3
                                      ? 'bg-emerald-700'
                                      : best.stars === 2
                                      ? 'bg-sky-700'
                                      : 'bg-amber-600'
                                  }`}
                                  title={`${m.code} (${best.totalScore} · ${best.stars}★)`}
                                >
                                  {shortCode} ({best.stars}★)
                                </span>
                              );
                            }
                            if (isFailedTarget) {
                              return (
                                <span
                                  key={m.code}
                                  className="px-1.5 py-0.5 rounded bg-rose-700 text-white animate-pulse"
                                  title={`${m.code} Gagal 3x`}
                                >
                                  {shortCode} ✕
                                </span>
                              );
                            }
                            if (unlocked) {
                              return (
                                <span
                                  key={m.code}
                                  className="px-1.5 py-0.5 rounded bg-sky-950 border border-sky-500 text-sky-300"
                                  title={`${m.code} (Terbuka)`}
                                >
                                  {shortCode} ⏳
                                </span>
                              );
                            }
                            return (
                              <span
                                key={m.code}
                                className="px-1.5 py-0.5 rounded bg-[#1e293b] text-slate-500"
                                title={`${m.code} (Terkunci)`}
                              >
                                {shortCode} 🔒
                              </span>
                            );
                          })}
                        </div>
                      ) : (
                        <span className="text-[11px] font-mono text-slate-300">
                          {passedInTrack} / {trackMissions.length} Misi Lulus ({stats.totalStars}★)
                        </span>
                      )}
                    </td>

                    {/* Aksi */}
                    <td className="py-3 px-4 text-right">
                      {isPendingCert ? (
                        <button
                          onClick={handleApprovePending}
                          className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider transition-all shadow-md shadow-emerald-950/50 cursor-pointer"
                        >
                          SETUJUI PIAGAM
                        </button>
                      ) : isIssuedCert && userCert ? (
                        <button
                          onClick={() => {
                            setVerificationCertNo(userCert.certificateNumber);
                            setCurrentView('certificate');
                          }}
                          className="px-2.5 py-1 rounded-lg bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 font-semibold text-[11px] transition-all cursor-pointer"
                        >
                          Lihat Piagam
                        </button>
                      ) : isLagging ? (
                        <button
                          onClick={handleUnlockEko}
                          className="px-2.5 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-[11px] transition-all cursor-pointer"
                        >
                          Buka Kunci
                        </button>
                      ) : rawResults.length > 0 ? (
                        <button
                          onClick={() => onViewReplay(participant.id)}
                          className="px-2.5 py-1 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-[11px] transition-all cursor-pointer"
                        >
                          Replay (L11)
                        </button>
                      ) : (
                        <span className="text-[11px] text-slate-500">Menunggu Pre-Test</span>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

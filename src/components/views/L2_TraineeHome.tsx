/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { useApp } from '../../context/AppContext';
import {
  Award,
  CheckCircle2,
  ClipboardCheck,
  Compass,
  Droplets,
  FileCheck2,
  Gauge,
  GitFork,
  History,
  Lock,
  Play,
  ShieldCheck,
  Sparkles,
  Star,
  Zap,
} from 'lucide-react';
import { BADGES_LIST } from '../../data/seedData';
import { LearningTrack, Mission, MissionResult } from '../../types';

interface TraineeHomeProps {
  onSelectMission: (missionCode: string) => void;
  onOpenPreTest: () => void;
  onOpenPostTest: () => void;
  onViewCertificates: () => void;
  onNavigateTrackSelect: () => void;
  onViewBadges: () => void;
}

const getInitials = (name: string): string => {
  const parts = name.trim().split(/\s+/);
  if (parts.length >= 2) {
    return `${parts[0].charAt(0)}${parts[1].charAt(0)}`.toUpperCase();
  }
  return name.slice(0, 2).toUpperCase();
};

const getTrackDisplayName = (track: LearningTrack): string => {
  if (track === 'ipa') return 'Operator IPA';
  if (track === 'distribusi') return 'Operator Distribusi';
  return 'Air Minum Terpadu';
};

const getNextLevelLabel = (level: string): string => {
  switch (level) {
    case 'Operator Magang':
      return 'Muda';
    case 'Operator Muda':
      return 'Madya';
    case 'Operator Madya':
      return 'Utama';
    case 'Operator Utama':
      return 'Ahli';
    default:
      return 'Maksimum';
  }
};

const getBadgeIconSmall = (id: string) => {
  switch (id) {
    case 'b-penjelajah':
      return <Compass className="w-3 h-3" />;
    case 'b-respons-kilat':
      return <Zap className="w-3 h-3" />;
    case 'b-tanpa-alarm-terlewat':
      return <CheckCircle2 className="w-3 h-3" />;
    case 'b-penjaga-mutu':
      return <Droplets className="w-3 h-3" />;
    case 'b-penjaga-tekanan':
      return <Gauge className="w-3 h-3" />;
    case 'b-tiga-bintang':
      return <Star className="w-3 h-3" />;
    case 'b-hulu-ke-hilir':
      return <GitFork className="w-3 h-3" />;
    default:
      return <Award className="w-3 h-3" />;
  }
};

const renderStars = (stars: number) => {
  return '★'.repeat(stars) + '☆'.repeat(Math.max(0, 3 - stars));
};

export const L2_TraineeHome: React.FC<TraineeHomeProps> = ({
  onSelectMission,
  onOpenPreTest,
  onOpenPostTest,
  onViewCertificates,
  onNavigateTrackSelect,
  onViewBadges,
}) => {
  const {
    currentUser,
    currentTenant,
    users,
    groups,
    activeTrack,
    getMissionsForTrack,
    isMissionUnlocked,
    getBestMissionResult,
    getUserXP,
    getUserOperatorLevel,
    userMissionResults,
    userBadges,
    userPrePostTests,
    certificates,
  } = useApp();

  if (!currentUser) return null;

  const userTrack: LearningTrack = currentUser.track || activeTrack || 'ipa';
  const trackLabel = getTrackDisplayName(userTrack);
  const trackMissions = getMissionsForTrack(userTrack);
  const xp = getUserXP(currentUser.id);
  const operatorLevel = getUserOperatorLevel(currentUser.id);
  const myBadges = userBadges[currentUser.id] || [];
  const myRawResults = userMissionResults[currentUser.id] || [];

  // Best result per mission in active track
  const trackResults: Array<{ mission: Mission; result: MissionResult }> = [];
  let passedCount = 0;
  let totalStars = 0;
  trackMissions.forEach((m) => {
    const res = getBestMissionResult(currentUser.id, m.code);
    if (res) {
      trackResults.push({ mission: m, result: res });
      if (res.isPassed) {
        passedCount += 1;
        totalStars += res.stars;
      }
    }
  });

  // Certificates
  const validCert = certificates.find(
    (c) => c.userId === currentUser.id && c.status === 'valid' && c.instructorApproved
  );
  const pendingCert = certificates.find(
    (c) => c.userId === currentUser.id && c.status === 'valid' && !c.instructorApproved
  );

  // Pre-test & Post-test status
  const preTest = userPrePostTests.find((t) => t.userId === currentUser.id && t.type === 'pre');
  const postTest = userPrePostTests.find((t) => t.userId === currentUser.id && t.type === 'post');

  const gradMissionCode =
    userTrack === 'ipa' ? 'IPA-09' : userTrack === 'distribusi' ? 'DST-07' : 'TRP-02';
  const gradMissionResult = getBestMissionResult(currentUser.id, gradMissionCode);
  const gradThreshold = currentTenant.config.graduationThresholdScore || 80;
  const allMissionsPassed = trackMissions.length > 0 && passedCount === trackMissions.length;
  const gradMissionPassed = Boolean(gradMissionResult && gradMissionResult.totalScore >= gradThreshold);
  const canTakePostTest = Boolean(preTest) && allMissionsPassed && gradMissionPassed;

  // Dynamic Leaderboard Rank within Tenant
  const tenantPeserta = users.filter(
    (u) => u.tenantId === currentTenant.id && u.role === 'peserta'
  );
  const sortedByXP = [...tenantPeserta].sort((a, b) => getUserXP(b.id) - getUserXP(a.id));
  const rankIdx = sortedByXP.findIndex((u) => u.id === currentUser.id);
  const rankLabel = !currentTenant.config.leaderboardEnabled
    ? 'Off'
    : rankIdx >= 0
    ? `#${rankIdx + 1}`
    : '-';

  // Group name
  const userGroup = groups.find((g) => g.id === currentUser.groupId);
  const groupShortName = userGroup
    ? userGroup.name.replace(/\s*\(\d+\s*Peserta\)/i, '')
    : 'Mandiri';

  // Next playable mission
  const nextPlayableMission =
    trackMissions.find((m) => {
      const res = getBestMissionResult(currentUser.id, m.code);
      return (!res || !res.isPassed) && isMissionUnlocked(currentUser.id, m.code);
    }) ||
    trackMissions.find((m) => {
      const res = getBestMissionResult(currentUser.id, m.code);
      return !res || !res.isPassed;
    });

  // Dynamic Competency Radar (5 Competencies PRD §11)
  const avgPercentFromCodes = (codes: string[]): number | null => {
    const matched = myRawResults.filter((r) => codes.includes(r.missionCode));
    if (matched.length === 0) return null;
    const sum = matched.reduce((acc, r) => acc + r.totalScore, 0);
    return Math.round(sum / matched.length);
  };

  const comp1NormalIpa =
    userTrack === 'distribusi'
      ? null
      : avgPercentFromCodes(['IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05']);

  const comp2MutuAir = avgPercentFromCodes(['IPA-03', 'IPA-05', 'IPA-06', 'IPA-08', 'DST-04']);

  const disturbanceResults = myRawResults.filter((r) =>
    ['IPA-06', 'IPA-07', 'IPA-08', 'IPA-09', 'DST-05', 'DST-06', 'DST-07', 'TRP-01', 'TRP-02'].includes(
      r.missionCode
    )
  );
  const comp3ResponsGangguan =
    disturbanceResults.length > 0
      ? Math.round(
          (disturbanceResults.reduce((acc, r) => acc + (r.scoreWaktuRespons / 25) * 100, 0) /
            disturbanceResults.length)
        )
      : null;

  const comp4Alarm =
    myRawResults.length > 0
      ? Math.round(
          (myRawResults.reduce((acc, r) => acc + (r.scoreAlarm / 15) * 100, 0) /
            myRawResults.length)
        )
      : null;

  const comp5Hidrolika =
    userTrack === 'ipa'
      ? null
      : avgPercentFromCodes(['DST-01', 'DST-02', 'DST-03', 'DST-04', 'DST-05', 'DST-06', 'DST-07']);

  // Score Trend & Attempt History (real user results only)
  const sortedResults = [...myRawResults].sort(
    (a, b) => new Date(a.completedAt).getTime() - new Date(b.completedAt).getTime()
  );
  const recentAttempts = [...sortedResults].reverse().slice(0, 5);

  // Weakest passed mission for smart advice
  const lowestResult =
    myRawResults.length > 0
      ? [...myRawResults].sort((a, b) => a.totalScore - b.totalScore)[0]
      : null;

  // XP progress display
  const xpProgressPercent =
    operatorLevel.level === 'Operator Ahli'
      ? 100
      : Math.min(100, Math.max(0, Math.round((xp / operatorLevel.nextXP) * 100)));
  const xpRemaining = Math.max(0, operatorLevel.nextXP - xp);

  // Post-test improvement %
  const t1Improvement =
    preTest && postTest && preTest.score > 0
      ? (((postTest.score - preTest.score) / preTest.score) * 100).toFixed(1)
      : null;

  // Group trackMissions by level 1..5
  const level1Missions = trackMissions.filter((m) => m.level === 1);
  const level2Missions = trackMissions.filter((m) => m.level === 2);
  const level3Missions = trackMissions.filter((m) => m.level === 3);
  const level4Missions = trackMissions.filter((m) => m.level === 4);
  const level5Missions = trackMissions.filter((m) => m.level === 5);

  const terpaduTotalCount = getMissionsForTrack('terpadu').length || 16;

  // Remaining missions for certificate message
  const remainingMissions = trackMissions.filter((m) => {
    const res = getBestMissionResult(currentUser.id, m.code);
    return !res || !res.isPassed;
  });

  const renderMissionCard = (m: Mission) => {
    const res = getBestMissionResult(currentUser.id, m.code);
    const unlocked = isMissionUnlocked(currentUser.id, m.code);
    const isPassed = Boolean(res && res.isPassed);
    const isNext = nextPlayableMission?.code === m.code && unlocked && !isPassed;
    const isFirstLockedPreTest =
      !unlocked && (m.code === 'IPA-01' || m.code === 'DST-01') && !preTest;

    return (
      <div
        key={m.code}
        className={`p-3 rounded-xl border flex flex-col justify-between gap-2 transition-all ${
          isPassed
            ? m.level === 3
              ? 'border-amber-500/40 bg-amber-950/20'
              : m.level >= 4
              ? 'border-purple-500/40 bg-purple-950/20'
              : 'border-emerald-500/30 bg-emerald-950/20'
            : isNext
            ? 'border-sky-500 bg-sky-950/40 ring-1 ring-sky-500/50'
            : unlocked
            ? 'border-[#334155] bg-[#0b1120] hover:border-sky-500/60'
            : 'border-[#1e293b] bg-[#0b1120]/70 opacity-75'
        }`}
      >
        <div className="flex items-start justify-between gap-2">
          <div>
            <div className="flex items-center gap-1.5 flex-wrap">
              {isPassed ? (
                <span className="text-[9px] px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-bold uppercase">
                  Lulus
                </span>
              ) : isNext ? (
                <span className="text-[9px] px-1.5 py-0.5 rounded-full bg-sky-500 text-white font-bold uppercase">
                  Misi Berikut
                </span>
              ) : unlocked ? (
                <span className="text-[9px] px-1.5 py-0.5 rounded-full bg-sky-500/20 text-sky-300 font-bold uppercase">
                  Terbuka
                </span>
              ) : (
                <span className="text-[9px] px-1.5 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold uppercase flex items-center gap-1">
                  <Lock className="w-2.5 h-2.5" /> Terkunci
                </span>
              )}
              <span className="text-[10px] font-mono text-slate-400">{m.code}</span>
            </div>
            <div className="text-xs font-bold text-white mt-1 leading-snug">
              {m.code}: {m.name}
            </div>
            <div className="text-[10px] text-slate-400 mt-0.5 line-clamp-2">{m.trainingFocus}</div>
          </div>
          {isPassed && res ? (
            <span className="text-amber-400 text-xs font-bold shrink-0">
              {renderStars(res.stars)}
            </span>
          ) : !unlocked ? (
            <Lock className="w-3.5 h-3.5 text-slate-500 shrink-0 mt-0.5" />
          ) : null}
        </div>

        <div className="pt-1 border-t border-[#1e293b]/80 flex items-center justify-between gap-2">
          {isPassed && res ? (
            <>
              <div className="text-[10px] text-sky-300 font-mono">
                Skor: <strong>{res.totalScore}</strong> ({res.stars}★) · +{res.xpEarned} XP
              </div>
              <button
                onClick={() => onSelectMission(m.code)}
                className="px-2 py-1 rounded-lg bg-[#1e293b] hover:bg-sky-600 text-slate-300 hover:text-white text-[10px] font-semibold transition-all shrink-0 cursor-pointer"
              >
                Ulangi
              </button>
            </>
          ) : unlocked ? (
            <button
              onClick={() => onSelectMission(m.code)}
              className="w-full py-1.5 px-2 bg-sky-600 hover:bg-sky-500 text-white font-bold text-[11px] rounded-lg transition-all flex items-center justify-center gap-1 shadow-sm cursor-pointer"
            >
              <Play className="w-3 h-3" />
              <span>Mulai Misi Ini →</span>
            </button>
          ) : (
            <div className="w-full flex items-center justify-between gap-2 text-[10px] text-slate-500">
              <span>
                {isFirstLockedPreTest
                  ? 'Selesaikan Pre-Test dahulu untuk membuka'
                  : 'Lulus misi sebelumnya terlebih dahulu'}
              </span>
              {isFirstLockedPreTest && (
                <button
                  onClick={onOpenPreTest}
                  className="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 font-bold shrink-0 cursor-pointer"
                >
                  Pre-Test →
                </button>
              )}
            </div>
          )}
        </div>
      </div>
    );
  };

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Page Title Block */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-2 border-b border-[#1e293b]">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
            Beranda Peserta &amp; Peta Misi Jalur {trackLabel}
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Jalur Aktif:{' '}
            <span className="text-sky-400 font-semibold">
              {trackLabel} ({trackMissions.length} Misi)
            </span>{' '}
            · {passedCount} Misi Lulus · {totalStars} Bintang · {xp.toLocaleString('id-ID')} XP (PRD §7, §8, §11)
          </p>
        </div>
        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={onNavigateTrackSelect}
            className="px-3.5 py-1.5 rounded-xl border border-[#334155] bg-[#1e293b]/70 hover:bg-[#1e293b] text-slate-300 hover:text-white text-xs font-semibold transition-all cursor-pointer"
          >
            Ganti Jalur Pembelajaran
          </button>
        </div>
      </div>

      {/* Prominent First-Time Pre-Test Onboarding Prompt when Pre-Test is not completed */}
      {!preTest && (
        <div className="p-4 rounded-2xl bg-amber-950/30 border border-amber-500/50 flex flex-col md:flex-row md:items-center justify-between gap-4 shadow-lg">
          <div className="flex items-start gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 text-amber-300 flex items-center justify-center shrink-0">
              <ClipboardCheck className="w-5 h-5" />
            </div>
            <div className="space-y-1">
              <div className="text-xs font-bold text-amber-300 uppercase tracking-wider">
                Langkah Pertama Wajib · Pre-Test Diagnostik (FR-09)
              </div>
              <p className="text-xs text-slate-200 leading-relaxed">
                Halo <strong>{currentUser.fullName}</strong>, Anda belum mengerjakan{' '}
                <strong>Pre-Test</strong>. Kerjakan Pre-Test (20 soal pilihan ganda, 30 menit) terlebih dahulu untuk mencatat nilai awal kompetensi (Metrik T1) dan membuka misi pertama{' '}
                <strong className="text-sky-300">{trackMissions[0]?.code || 'IPA-01'}</strong>.
              </p>
            </div>
          </div>
          <button
            onClick={onOpenPreTest}
            className="px-4 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-xs uppercase tracking-wider transition-all shrink-0 shadow-md cursor-pointer"
          >
            Kerjakan Pre-Test Sekarang (L4a) →
          </button>
        </div>
      )}

      {/* Main Grid: Left Column (Profile & Competency) + Right Column (Pre/Post Cards + Mission Roadmap) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* LEFT COLUMN */}
        <div className="lg:col-span-4 space-y-6">
          {/* Card 1: Profile & Gamification Stats */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-5 shadow-lg">
            <div className="flex items-center gap-3.5">
              <div className="w-14 h-14 rounded-2xl bg-sky-600 text-white font-extrabold text-xl flex items-center justify-center shadow-md shrink-0">
                {getInitials(currentUser.fullName)}
              </div>
              <div className="space-y-0.5 min-w-0">
                <h2 className="text-base font-bold text-white leading-tight truncate">
                  {currentUser.fullName}
                </h2>
                <div className="text-xs text-slate-400 truncate">{currentTenant.name}</div>
                <div className="text-[11px] text-sky-400 font-medium">
                  {groupShortName} · ID: <span className="font-mono">{currentUser.username}</span>
                </div>
              </div>
            </div>

            {/* Level & XP Progress Bar */}
            <div className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2">
              <div className="flex items-center justify-between text-xs font-semibold">
                <span className="text-slate-400 text-[11px] uppercase tracking-wider">
                  Level Operator (PRD §8):
                </span>
                <span className="text-sky-400 font-bold font-mono">
                  TOTAL XP: {xp.toLocaleString('id-ID')} XP
                </span>
              </div>

              <div className="flex items-center justify-between gap-2 flex-wrap">
                <span className="px-3 py-1 rounded-lg bg-sky-500/20 text-sky-300 border border-sky-500/40 font-bold text-xs">
                  {operatorLevel.level}
                </span>
                <span className="text-[11px] text-slate-400 font-mono">
                  {operatorLevel.level === 'Operator Ahli'
                    ? `${xp.toLocaleString('id-ID')} XP (Level Maksimum)`
                    : `${xp.toLocaleString('id-ID')} / ${operatorLevel.nextXP.toLocaleString(
                        'id-ID'
                      )} XP (sisa ${xpRemaining.toLocaleString('id-ID')} ke ${getNextLevelLabel(
                        operatorLevel.level
                      )})`}
                </span>
              </div>

              <div className="w-full h-2 rounded-full bg-[#1e293b] overflow-hidden">
                <div
                  className="h-full bg-linear-to-r from-sky-500 to-cyan-400 rounded-full transition-all duration-500"
                  style={{ width: `${xpProgressPercent}%` }}
                />
              </div>
            </div>

            {/* Stats Row */}
            <div className="grid grid-cols-4 gap-2 text-center">
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Misi Lulus</div>
                <div className="text-base font-extrabold text-white mt-0.5">
                  {passedCount} / {trackMissions.length}
                </div>
              </div>
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Bintang</div>
                <div className="text-base font-extrabold text-amber-400 mt-0.5">
                  {totalStars} ★
                </div>
              </div>
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Lencana</div>
                <div className="text-base font-extrabold text-emerald-400 mt-0.5">
                  {myBadges.length} / {BADGES_LIST.length}
                </div>
              </div>
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Peringkat</div>
                <div className="text-base font-extrabold text-sky-400 mt-0.5">{rankLabel}</div>
              </div>
            </div>

            {/* Pre-Test & Post-Test Summary Badge */}
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Nilai Pre-Test (T1)</div>
                <div className="text-sm font-extrabold mt-0.5 font-mono">
                  {preTest ? (
                    <span className="text-sky-400">{preTest.score} / 100</span>
                  ) : (
                    <span className="text-amber-400">Belum dikerjakan</span>
                  )}
                </div>
              </div>
              <div className="p-2.5 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Nilai Post-Test</div>
                <div className="text-sm font-extrabold mt-0.5 font-mono">
                  {postTest ? (
                    <span className="text-emerald-400">
                      {postTest.score} / 100 {t1Improvement ? `(+${t1Improvement}%)` : ''}
                    </span>
                  ) : canTakePostTest ? (
                    <span className="text-emerald-300">Siap dikerjakan</span>
                  ) : (
                    <span className="text-slate-500">Terkunci</span>
                  )}
                </div>
              </div>
            </div>

            {/* Certificate Status Box */}
            {validCert ? (
              <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-xs flex items-center justify-between gap-2">
                <div>
                  <span className="text-[10px] text-emerald-400 font-bold uppercase tracking-wider block">
                    Status Piagam Kelulusan:
                  </span>
                  <span className="text-emerald-200 font-semibold">
                    Terbit · {validCert.certificateNumber} ({validCert.predicate})
                  </span>
                </div>
                <button
                  onClick={onViewCertificates}
                  className="px-2.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-[11px] shrink-0 cursor-pointer"
                >
                  Lihat Piagam
                </button>
              </div>
            ) : pendingCert ? (
              <div className="p-3 rounded-xl bg-amber-950/30 border border-amber-500/40 text-xs flex items-center justify-between gap-2">
                <div>
                  <span className="text-[10px] text-amber-400 font-bold uppercase tracking-wider block">
                    Status Piagam Kelulusan:
                  </span>
                  <span className="text-amber-200 font-semibold">
                    Menunggu Persetujuan Instruktur ({pendingCert.certificateNumber})
                  </span>
                </div>
                <button
                  onClick={onViewCertificates}
                  className="px-2.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-[11px] shrink-0 cursor-pointer"
                >
                  Cek Status
                </button>
              </div>
            ) : (
              <div className="p-3 rounded-xl bg-purple-950/20 border border-purple-500/30 text-xs flex items-center justify-between">
                <div>
                  <span className="text-[10px] text-purple-400 font-bold uppercase tracking-wider block">
                    Status Piagam Kelulusan:
                  </span>
                  <span className="text-purple-200 font-semibold">
                    Belum memenuhi{' '}
                    {!preTest
                      ? '(Kerjakan Pre-Test & seluruh misi jalur)'
                      : remainingMissions.length > 0
                      ? `(Sisa ${remainingMissions.length} misi jalur ${trackLabel})`
                      : !postTest || postTest.score < 70
                      ? '(Selesaikan Post-Test ≥ 70)'
                      : '(Menunggu verifikasi)'}
                  </span>
                </div>
                <Lock className="w-4 h-4 text-purple-400 shrink-0 ml-2" />
              </div>
            )}
          </div>

          {/* Card 2: Competency Radar & Score Trend & Attempt History */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold uppercase tracking-wider text-slate-200">
                Peta Kompetensi (5 Kompetensi PRD §11)
              </h3>
              <span className="text-[10px] text-slate-500">Evaluasi Mesin</span>
            </div>

            <div className="space-y-3 text-xs">
              <div>
                <div className="flex justify-between text-slate-300 mb-1">
                  <span>1. Operasi Normal IPA</span>
                  <span className="font-bold text-sky-400">
                    {userTrack === 'distribusi'
                      ? '– (bukan jalur Distribusi)'
                      : comp1NormalIpa !== null
                      ? `${comp1NormalIpa}%`
                      : '0%'}
                  </span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div
                    className="h-full bg-sky-500 rounded-full transition-all"
                    style={{ width: `${comp1NormalIpa ?? 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-slate-300 mb-1">
                  <span>2. Mutu Air (Kekeruhan &amp; Klor)</span>
                  <span className="font-bold text-emerald-400">
                    {comp2MutuAir !== null ? `${comp2MutuAir}%` : '0%'}
                  </span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div
                    className="h-full bg-emerald-500 rounded-full transition-all"
                    style={{ width: `${comp2MutuAir ?? 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-slate-300 mb-1">
                  <span>3. Respons Gangguan &amp; Darurat</span>
                  <span className="font-bold text-amber-400">
                    {comp3ResponsGangguan !== null ? `${comp3ResponsGangguan}%` : '0%'}
                  </span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div
                    className="h-full bg-amber-500 rounded-full transition-all"
                    style={{ width: `${comp3ResponsGangguan ?? 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-slate-300 mb-1">
                  <span>4. Penanganan Alarm ISA-18.2</span>
                  <span className="font-bold text-cyan-400">
                    {comp4Alarm !== null ? `${comp4Alarm}%` : '0%'}
                  </span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div
                    className="h-full bg-cyan-400 rounded-full transition-all"
                    style={{ width: `${comp4Alarm ?? 0}%` }}
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between text-slate-400 mb-1">
                  <span>5. Hidrolika Distribusi</span>
                  <span className="font-bold text-slate-400">
                    {userTrack === 'ipa'
                      ? '– (bukan jalur IPA)'
                      : comp5Hidrolika !== null
                      ? `${comp5Hidrolika}%`
                      : '0%'}
                  </span>
                </div>
                <div className="w-full h-1.5 rounded-full bg-[#1e293b]">
                  <div
                    className="h-full bg-indigo-500 rounded-full transition-all"
                    style={{ width: `${comp5Hidrolika ?? 0}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Score Trend Sparkline */}
            <div className="pt-3 border-t border-[#1e293b]">
              <div className="text-[11px] font-semibold text-slate-400 mb-2">
                Tren Skor Misi ({sortedResults.length} Percobaan):
              </div>
              {sortedResults.length === 0 ? (
                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b] text-center text-[11px] text-slate-500">
                  Belum ada percobaan misi
                </div>
              ) : (
                <div className="flex items-end gap-1.5 h-16 pt-2 px-1">
                  {sortedResults.slice(-8).map((item, idx) => (
                    <div key={`${item.id}-${idx}`} className="flex-1 flex flex-col items-center gap-1">
                      <span className="text-[9px] text-slate-400 font-mono">{item.totalScore}</span>
                      <div
                        className={`w-full rounded-t-sm transition-all ${
                          item.totalScore >= 95
                            ? 'bg-amber-400'
                            : item.totalScore >= 85
                            ? 'bg-sky-400'
                            : item.totalScore >= 70
                            ? 'bg-emerald-500'
                            : 'bg-rose-500'
                        }`}
                        style={{ height: `${Math.max(4, (item.totalScore / 100) * 36)}px` }}
                      />
                      <span className="text-[8px] text-slate-500 font-mono truncate max-w-full">
                        {item.missionCode.replace('IPA-', 'I').replace('DST-', 'D').replace('TRP-', 'T')}
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Attempt History */}
            <div className="pt-3 border-t border-[#1e293b] space-y-2">
              <div className="text-[11px] font-semibold text-slate-400 flex items-center gap-1.5">
                <History className="w-3.5 h-3.5 text-slate-400" />
                <span>Riwayat Percobaan Terbaru:</span>
              </div>
              {recentAttempts.length === 0 ? (
                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b] text-center text-[11px] text-slate-500">
                  Belum ada percobaan misi
                </div>
              ) : (
                <div className="space-y-1.5">
                  {recentAttempts.map((att) => (
                    <div
                      key={att.id}
                      className="px-2.5 py-1.5 rounded-lg bg-[#0b1120] border border-[#1e293b] flex items-center justify-between text-[11px]"
                    >
                      <span className="font-mono font-bold text-slate-200">{att.missionCode}</span>
                      <span className="text-slate-400">
                        Skor <strong className="text-white">{att.totalScore}</strong> ·{' '}
                        <span className="text-amber-400">{renderStars(att.stars)}</span>
                      </span>
                      <span className="text-sky-400 font-mono">+{att.xpEarned} XP</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Card 3: Automated Learning Advice (PRD §11) */}
          <div className="p-4 rounded-2xl bg-sky-950/30 border border-sky-500/40 text-xs space-y-2.5 shadow-md">
            <div className="flex items-center gap-2 text-sky-400 font-bold">
              <Sparkles className="w-4 h-4 text-sky-400" />
              <span>Saran Belajar Otomatis (PRD §11):</span>
            </div>

            {!preTest ? (
              <>
                <p className="text-slate-300 leading-relaxed text-[11px]">
                  "Anda berada di awal {trackLabel}. Selesaikan Pre-Test terlebih dahulu untuk memetakan kompetensi dasar Anda sebelum masuk ke misi pertama."
                </p>
                <button
                  onClick={onOpenPreTest}
                  className="w-full py-2 px-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
                >
                  <span>Mulai Pre-Test (L4a) →</span>
                </button>
              </>
            ) : allMissionsPassed && !postTest ? (
              <>
                <p className="text-slate-300 leading-relaxed text-[11px]">
                  "Seluruh misi jalur {trackLabel} telah lulus! Kerjakan Post-Test Kelulusan (≥ 70) untuk memenuhi syarat penerbitan piagam."
                </p>
                <button
                  onClick={onOpenPostTest}
                  className="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
                >
                  <span>Kerjakan Post-Test Sekarang →</span>
                </button>
              </>
            ) : allMissionsPassed && postTest ? (
              <>
                <p className="text-slate-300 leading-relaxed text-[11px]">
                  "Selamat! Seluruh misi {trackLabel} dan Post-Test telah selesai. Anda dapat melihat piagam kelulusan atau mengulang simulasi untuk skor sempurna."
                </p>
                <button
                  onClick={onViewCertificates}
                  className="w-full py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
                >
                  <span>Lihat Piagam Saya (L8) →</span>
                </button>
              </>
            ) : lowestResult && lowestResult.totalScore < 80 ? (
              <>
                <p className="text-slate-300 leading-relaxed text-[11px]">
                  "Skor terendah Anda saat ini pada {lowestResult.missionCode} ({lowestResult.totalScore}/100). Ulangi latihan atau lanjutkan misi berikutnya ({nextPlayableMission?.code})."
                </p>
                <button
                  onClick={() => onSelectMission(lowestResult.missionCode)}
                  className="w-full py-2 px-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
                >
                  <span>Latihan Ulang: {lowestResult.missionCode} →</span>
                </button>
              </>
            ) : (
              <>
                <p className="text-slate-300 leading-relaxed text-[11px]">
                  "Langkah selanjutnya: lanjutkan misi {nextPlayableMission?.code} ({nextPlayableMission?.name}) untuk menambah XP dan membuka tingkat berikutnya."
                </p>
                {nextPlayableMission && (
                  <button
                    onClick={() => onSelectMission(nextPlayableMission.code)}
                    className="w-full py-2 px-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
                  >
                    <span>Mulai {nextPlayableMission.code} →</span>
                  </button>
                )}
              </>
            )}
          </div>
        </div>

        {/* RIGHT COLUMN */}
        <div className="lg:col-span-8 space-y-6">
          {/* Pre-Test & Post-Test Dedicated Access Cards (FR-09) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Kartu Pre-Test */}
            <div
              className={`p-4 rounded-2xl border flex flex-col justify-between gap-3 shadow-md ${
                preTest
                  ? 'bg-[#0f172a] border-[#24324d]'
                  : 'bg-amber-950/20 border-amber-500/50 ring-1 ring-amber-500/30'
              }`}
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider ${
                      preTest
                        ? 'bg-emerald-500/20 text-emerald-300'
                        : 'bg-amber-500/20 text-amber-300'
                    }`}
                  >
                    {preTest ? 'Pre-Test Selesai ✓' : 'Wajib Sebelum Misi 1'}
                  </span>
                  <h3 className="text-sm font-bold text-white mt-1.5">
                    Pre-Test Diagnostik Awal (T1)
                  </h3>
                  <p className="text-[11px] text-slate-400 mt-0.5">
                    {preTest
                      ? `Baseline kompetensi awal tersimpan: ${preTest.score} / 100.`
                      : '20 soal pilihan ganda (30 menit). Membuka kunci misi pertama jalur Anda.'}
                  </p>
                </div>
                {preTest && (
                  <div className="text-right shrink-0">
                    <div className="text-xl font-black text-sky-400 font-mono">
                      {preTest.score}
                    </div>
                    <div className="text-[9px] text-slate-500">/ 100</div>
                  </div>
                )}
              </div>

              <button
                onClick={onOpenPreTest}
                className={`w-full py-2 px-3 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1.5 cursor-pointer ${
                  preTest
                    ? 'bg-[#1e293b] hover:bg-[#334155] text-slate-200 border border-[#334155]'
                    : 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-sm'
                }`}
              >
                <ClipboardCheck className="w-3.5 h-3.5" />
                <span>{preTest ? 'Lihat Hasil Pre-Test (L4a)' : 'Mulai Pre-Test Sekarang →'}</span>
              </button>
            </div>

            {/* Kartu Post-Test */}
            <div
              className={`p-4 rounded-2xl border flex flex-col justify-between gap-3 shadow-md ${
                postTest
                  ? 'bg-emerald-950/20 border-emerald-500/40'
                  : canTakePostTest
                  ? 'bg-purple-950/30 border-purple-500/50 ring-1 ring-purple-500/40'
                  : 'bg-[#0f172a] border-[#1e293b] opacity-85'
              }`}
            >
              <div className="flex items-start justify-between gap-2">
                <div>
                  <span
                    className={`text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider ${
                      postTest
                        ? 'bg-emerald-500/20 text-emerald-300'
                        : canTakePostTest
                        ? 'bg-purple-500/20 text-purple-300'
                        : 'bg-slate-800 text-slate-400'
                    }`}
                  >
                    {postTest
                      ? 'Post-Test Lulus ✓'
                      : canTakePostTest
                      ? 'Syarat Terpenuhi · Aktif'
                      : 'Terkunci'}
                  </span>
                  <h3 className="text-sm font-bold text-white mt-1.5">
                    Post-Test Kelulusan Jalur
                  </h3>
                  <p className="text-[11px] text-slate-400 mt-0.5">
                    {postTest
                      ? `Skor akhir: ${postTest.score}/100 (KKM ≥ 70)${
                          t1Improvement ? ` · Naik +${t1Improvement}%` : ''
                        }.`
                      : canTakePostTest
                      ? `Semua ${trackMissions.length} misi & ${gradMissionCode} ≥ ${gradThreshold} lulus. Siap uji Post-Test.`
                      : `Terbuka setelah semua ${trackMissions.length} misi jalur & ${gradMissionCode} (≥ ${gradThreshold}) lulus.`}
                  </p>
                </div>
                {postTest ? (
                  <div className="text-right shrink-0">
                    <div className="text-xl font-black text-emerald-400 font-mono">
                      {postTest.score}
                    </div>
                    <div className="text-[9px] text-slate-500">/ 100</div>
                  </div>
                ) : !canTakePostTest ? (
                  <Lock className="w-4 h-4 text-slate-500 shrink-0 mt-1" />
                ) : null}
              </div>

              <button
                onClick={onOpenPostTest}
                disabled={!canTakePostTest && !postTest}
                className={`w-full py-2 px-3 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1.5 ${
                  postTest
                    ? 'bg-emerald-600 hover:bg-emerald-500 text-white cursor-pointer'
                    : canTakePostTest
                    ? 'bg-purple-600 hover:bg-purple-500 text-white shadow-sm cursor-pointer'
                    : 'bg-[#1e293b] text-slate-500 border border-[#334155] cursor-not-allowed'
                }`}
              >
                <FileCheck2 className="w-3.5 h-3.5" />
                <span>
                  {postTest
                    ? 'Lihat Perbandingan Pre vs Post (L4a)'
                    : canTakePostTest
                    ? 'Kerjakan Post-Test Sekarang →'
                    : `Selesaikan ${trackMissions.length} Misi untuk Membuka`}
                </span>
              </button>
            </div>
          </div>

          {/* Peta Misi Dinamis */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-6 shadow-lg">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e293b] gap-3 flex-wrap">
              <div>
                <h3 className="text-base font-bold text-white">
                  Peta Misi Jalur {trackLabel} ({trackMissions.length} Misi Berjenjang)
                </h3>
                <p className="text-xs text-slate-400">
                  Aturan Bintang: &lt;70 Belum Lulus · 70–84 (1★) · 85–94 (2★) · ≥95 (3★). Misi Kelulusan lulus jika skor ≥80.
                </p>
              </div>
              <span className="text-xs font-mono text-sky-400 font-bold px-2.5 py-1 rounded-lg bg-sky-950/40 border border-sky-500/30">
                Katalog PRD §7
              </span>
            </div>

            {/* TINGKAT 1: PENGENALAN */}
            {level1Missions.length > 0 && (
              <div className="space-y-2">
                <div className="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-emerald-400" />
                  <span>Tingkat 1: Pengenalan (Mudah · 1,0x XP · Tanpa Gangguan)</span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {level1Missions.map(renderMissionCard)}
                </div>
              </div>
            )}

            {/* TINGKAT 2: OPERASI NORMAL */}
            {level2Missions.length > 0 && (
              <div className="space-y-2">
                <div className="text-xs font-bold text-sky-400 uppercase tracking-wider flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-sky-400" />
                  <span>Tingkat 2: Operasi Normal (Mudah 1,0x · Sedang 1,5x XP)</span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {level2Missions.map(renderMissionCard)}
                </div>
              </div>
            )}

            {/* TINGKAT 3: GANGGUAN TUNGGAL */}
            {level3Missions.length > 0 && (
              <div className="space-y-2">
                <div className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-amber-400" />
                  <span>Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP · 5 Gangguan Utama PRD §7)</span>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  {level3Missions.map(renderMissionCard)}
                </div>
              </div>
            )}

            {/* TINGKAT 4: GANGGUAN BERANTAI */}
            {level4Missions.length > 0 ? (
              <div className="space-y-2">
                <div className="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-purple-400" />
                  <span>Tingkat 4: Gangguan Berantai (Sangat Sulit · 2,5x XP · Khusus Jalur Terpadu)</span>
                </div>
                <div className="grid grid-cols-1 gap-3">
                  {level4Missions.map(renderMissionCard)}
                </div>
              </div>
            ) : (
              <div className="p-3.5 rounded-xl border border-[#24324d] bg-[#0b1120] text-xs space-y-1">
                <div className="text-slate-400 font-bold uppercase tracking-wider text-[11px]">
                  Tingkat 4: Gangguan Berantai (Sangat Sulit · Khusus Jalur Terpadu TRP-01)
                </div>
                <p className="text-slate-400 text-[11px]">
                  Jalur {trackLabel} melompat langsung dari Tingkat 3 ke Misi Kelulusan Ujian ({gradMissionCode}). Misi TRP-01 "Hulu ke Hilir" hanya tersedia di{' '}
                  <span className="text-sky-400 font-semibold">
                    Jalur Air Minum Terpadu ({terpaduTotalCount} Misi)
                  </span>.
                </p>
              </div>
            )}

            {/* TINGKAT 5: MISI KELULUSAN */}
            {level5Missions.length > 0 && (
              <div className="space-y-2">
                <div className="text-xs font-bold text-purple-300 uppercase tracking-wider flex items-center gap-1.5">
                  <span className="w-2 h-2 rounded-full bg-purple-400" />
                  <span>
                    Tingkat 5: Misi Kelulusan Jalur {trackLabel} (Ujian Akhir · Batas Waktu &amp; Tanpa Petunjuk · 3,0x XP)
                  </span>
                </div>
                <div className="grid grid-cols-1 gap-3">
                  {level5Missions.map(renderMissionCard)}
                </div>
              </div>
            )}

            {/* BADGES GALLERY PREVIEW */}
            <div className="pt-2 border-t border-[#1e293b] flex items-center justify-between flex-wrap gap-2 text-xs">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="font-bold text-slate-300">
                  Lencana {currentUser.fullName.split(' ')[0]} ({myBadges.length} dari {BADGES_LIST.length} PRD §8):
                </span>
                {myBadges.length === 0 ? (
                  <span className="text-slate-500 text-[11px]">
                    Belum ada lencana terbuka — selesaikan misi dan jelajahi titik kontrol.
                  </span>
                ) : (
                  myBadges.slice(0, 4).map((bId) => {
                    const badge = BADGES_LIST.find((b) => b.id === bId);
                    if (!badge) return null;
                    return (
                      <span
                        key={bId}
                        className="px-2 py-0.5 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30 text-[11px] flex items-center gap-1"
                      >
                        {getBadgeIconSmall(bId)} {badge.name}
                      </span>
                    );
                  })
                )}
              </div>
              <button
                type="button"
                onClick={onViewBadges}
                className="text-sky-400 hover:text-sky-300 underline font-semibold text-[11px] cursor-pointer"
              >
                {BADGES_LIST.length - myBadges.length > 0
                  ? `+ ${BADGES_LIST.length - myBadges.length} Lencana Terkunci (Lihat di L7)`
                  : 'Semua 8 Lencana Terbuka! (Lihat di L7)'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

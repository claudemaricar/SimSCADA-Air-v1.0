/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { useApp } from '../../context/AppContext';
import { 
  Award, 
  Check, 
  CheckCircle2, 
  Compass, 
  Droplets, 
  Gauge, 
  GitFork, 
  Lock, 
  ShieldCheck, 
  Sparkles, 
  Star, 
  Trophy, 
  Users, 
  Zap,
  Info
} from 'lucide-react';
import { BADGES_LIST, MISSIONS_LIST } from '../../data/seedData';
import { computeBestPassedResults } from '../../utils/gamification';

export const L7_BadgesLeaderboard: React.FC = () => {
  const { currentUser, currentTenant, users, getUserXP, getUserOperatorLevel, userBadges, userMissionResults } = useApp();
  const [scopeTab, setScopeTab] = useState<'kelompok' | 'lembaga'>('kelompok');
  const [timeTab, setTimeTab] = useState<'all_time' | 'weekly'>('all_time');

  if (!currentUser) return null;

  // Filter users strictly within current tenant (ISOLASI DATA PRD §5 & FR-21)
  const tenantParticipants = users.filter((u) => u.tenantId === currentTenant.id && u.role === 'peserta');

  // Filter by group if scope is 'kelompok'
  const filteredUsers = scopeTab === 'kelompok' && currentUser.groupId
    ? tenantParticipants.filter((u) => u.groupId === currentUser.groupId)
    : tenantParticipants;

  // Sort by XP descending
  const rankedUsers = [...filteredUsers].sort((a, b) => getUserXP(b.id) - getUserXP(a.id));

  // 8 Official Badges mapping for current logged-in user
  const myBadgeIds = userBadges[currentUser.id] || [];
  const unlockedCount = myBadgeIds.length;
  const lockedCount = Math.max(0, BADGES_LIST.length - unlockedCount);

  const getBadgeIcon = (id: string, isUnlocked: boolean) => {
    const colorClass = isUnlocked ? 'text-emerald-400' : 'text-slate-400';
    switch (id) {
      case 'b-penjelajah': return <Compass className={`w-5 h-5 ${colorClass}`} />;
      case 'b-respons-kilat': return <Zap className={`w-5 h-5 ${colorClass}`} />;
      case 'b-tanpa-alarm-terlewat': return <ShieldCheck className={`w-5 h-5 ${colorClass}`} />;
      case 'b-penjaga-mutu': return <Droplets className={`w-5 h-5 ${colorClass}`} />;
      case 'b-penjaga-tekanan': return <Gauge className={`w-5 h-5 ${colorClass}`} />;
      case 'b-tiga-bintang': return <Star className={`w-5 h-5 ${colorClass}`} />;
      case 'b-hulu-ke-hilir': return <GitFork className={`w-5 h-5 ${colorClass}`} />;
      case 'b-tanpa-petunjuk': return <Award className={`w-5 h-5 ${colorClass}`} />;
      default: return <Award className={`w-5 h-5 ${colorClass}`} />;
    }
  };

  const getBadgeDetail = (id: string, unlocked: boolean) => {
    if (unlocked) {
      switch (id) {
        case 'b-penjelajah': return 'Capaian: Seluruh Narasi Titik Kontrol Dibuka';
        case 'b-respons-kilat': return 'Diraih: Respons < 50% Target Waktu Skenario';
        case 'b-tanpa-alarm-terlewat': return 'Capaian: 100% Alarm Diakui & Clear Tepat';
        default: return 'Lencana Diraih ✓';
      }
    }
    switch (id) {
      case 'b-penjelajah': return 'Buka semua narasi titik kontrol (i) di simulator';
      case 'b-respons-kilat': return 'Atasi gangguan dalam < 50% target waktu skenario';
      case 'b-tanpa-alarm-terlewat': return 'Akui dan selesaikan semua alarm dalam 1 sesi gangguan';
      case 'b-penjaga-mutu': return 'Kekeruhan dan sisa klor di rentang normal sepanjang misi IPA';
      case 'b-penjaga-tekanan': return 'Tekanan semua zona di rentang layanan sepanjang misi distribusi';
      case 'b-tiga-bintang': return 'Raih minimal 3 bintang (≥95) pada 3 misi';
      case 'b-hulu-ke-hilir': return 'Selesaikan skenario Tingkat 4 TRP-01 (Khusus Terpadu)';
      case 'b-tanpa-petunjuk': return 'Lulus Misi Kelulusan tanpa membuka petunjuk';
      default: return 'Terkunci';
    }
  };

  const getUserMissionStats = (userId: string) => {
    const res = userMissionResults[userId] || [];
    const bestPassed = computeBestPassedResults(res, MISSIONS_LIST);
    const totalStars = bestPassed.reduce((acc, r) => acc + r.stars, 0);
    return { passedCount: bestPassed.length, totalStars };
  };

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Galeri Lencana &amp; Papan Peringkat Kompetensi
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          8 Lencana PRD SimSCADA-Air §8 · Papan Peringkat Terisolasi Antar-Lembaga (FR-20, FR-21)
        </p>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        {/* LEFT COLUMN: 8 LENCANA RESMI PRD §8 */}
        <div className="lg:col-span-7 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">
              8 Lencana Prestasi Operator (PRD SimSCADA-Air v1.1 §8)
            </h2>
            <p className="text-xs text-slate-400">
              Koleksi pencapaian {currentUser.fullName} · {unlockedCount} Lencana Terbuka, {lockedCount} Terkunci
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            {BADGES_LIST.map((badge) => {
              const unlocked = myBadgeIds.includes(badge.id);
              const detail = getBadgeDetail(badge.id, unlocked);
              return (
                <div
                  key={badge.id}
                  className={`p-3.5 rounded-xl border transition-all ${
                    unlocked
                      ? 'bg-emerald-950/20 border-emerald-500/40'
                      : 'bg-[#0b1120] border-[#1e293b] opacity-75'
                  }`}
                >
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <div className="flex items-center gap-2.5">
                      <div className={`w-9 h-9 rounded-lg flex items-center justify-center shrink-0 ${
                        unlocked ? 'bg-emerald-500/20 border border-emerald-500/30' : 'bg-[#1e293b]'
                      }`}>
                        {getBadgeIcon(badge.id, unlocked)}
                      </div>
                      <div>
                        <div className="text-xs font-bold text-white leading-tight">
                          {badge.name}
                        </div>
                        <div className="text-[10px] text-sky-400 font-medium">Syarat PRD §8:</div>
                      </div>
                    </div>

                    <span className={`text-[9px] px-2 py-0.5 rounded-md font-bold uppercase tracking-wider shrink-0 ${
                      unlocked
                        ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                        : 'bg-slate-800 text-slate-400'
                    }`}>
                      {unlocked ? 'TERBUKA ✓' : 'TERKUNCI'}
                    </span>
                  </div>

                  <p className="text-[11px] text-slate-300 leading-snug">
                    {badge.description}
                  </p>

                  <div className="mt-2 pt-2 border-t border-[#1e293b] text-[10px] text-slate-400">
                    <span className={unlocked ? 'text-emerald-400 font-medium' : 'text-slate-500'}>
                      {detail}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* RIGHT COLUMN: PAPAN PERINGKAT TERISOLASI ANTAR-LEMBAGA */}
        <div className="lg:col-span-5 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">
              Papan Peringkat Kompetensi (PRD §8)
            </h2>
            <p className="text-xs text-slate-400">
              Terisolasi dalam {currentTenant.name}
            </p>
          </div>

          {/* Toggle Check: if leaderboard is disabled by admin in L13 */}
          {!currentTenant.config.leaderboardEnabled ? (
            <div className="p-6 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <Info className="w-8 h-8 text-slate-500 mx-auto" />
              <div className="text-xs font-bold text-slate-300">Papan Peringkat Dinonaktifkan</div>
              <p className="text-[11px] text-slate-500">
                Admin Lembaga menonaktifkan fitur papan peringkat demi menjaga fokus pembelajaran mandiri (FR-21).
              </p>
            </div>
          ) : (
            <>
              {/* Filter Tabs */}
              <div className="space-y-2">
                <div className="grid grid-cols-2 gap-1.5 p-1 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <button
                    onClick={() => setScopeTab('kelompok')}
                    className={`py-1.5 px-3 rounded-lg text-xs font-bold transition-all ${
                      scopeTab === 'kelompok'
                        ? 'bg-sky-600 text-white shadow-xs'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    TAB: KELOMPOK (ANGKATAN 1)
                  </button>
                  <button
                    onClick={() => setScopeTab('lembaga')}
                    className={`py-1.5 px-3 rounded-lg text-xs font-bold transition-all ${
                      scopeTab === 'lembaga'
                        ? 'bg-sky-600 text-white shadow-xs'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    LEMBAGA (SELURUH NUSANTARA)
                  </button>
                </div>

                <div className="grid grid-cols-2 gap-1.5 p-1 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <button
                    onClick={() => setTimeTab('weekly')}
                    className={`py-1.5 px-3 rounded-lg text-xs font-semibold transition-all ${
                      timeTab === 'weekly'
                        ? 'bg-[#1e293b] text-white shadow-xs'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    Mingguan
                  </button>
                  <button
                    onClick={() => setTimeTab('all_time')}
                    className={`py-1.5 px-3 rounded-lg text-xs font-bold transition-all ${
                      timeTab === 'all_time'
                        ? 'bg-emerald-600 text-white shadow-xs'
                        : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    Sepanjang Waktu (All-Time) ✓
                  </button>
                </div>
              </div>

              {/* Roster of Ranked Users */}
              <div className="space-y-2 max-h-[420px] overflow-y-auto pr-1">
                {rankedUsers.slice(0, 8).map((user, idx) => {
                  const userXp = getUserXP(user.id);
                  const isCurrent = user.id === currentUser.id;
                  const isAndi = user.username === 'peserta.lulus';
                  const stats = getUserMissionStats(user.id);

                  return (
                    <div
                      key={user.id}
                      className={`p-3 rounded-xl border flex items-center justify-between gap-3 transition-all ${
                        isCurrent
                          ? 'border-sky-500 bg-sky-950/30 ring-1 ring-sky-500/40'
                          : isAndi
                          ? 'border-amber-500/40 bg-amber-950/20'
                          : 'border-[#1e293b] bg-[#0b1120]'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <span className={`w-6 text-center font-mono font-bold text-sm ${
                          idx === 0 ? 'text-amber-400' : idx === 1 ? 'text-sky-400' : idx === 2 ? 'text-amber-600' : 'text-slate-500'
                        }`}>
                          {idx + 1}
                        </span>
                        
                        <div className="w-8 h-8 rounded-lg bg-[#1e293b] text-slate-200 font-bold flex items-center justify-center text-xs">
                          {user.fullName.substring(0, 2).toUpperCase()}
                        </div>

                        <div>
                          <div className="text-xs font-bold text-white flex items-center gap-1.5">
                            <span>{user.fullName}</span>
                            {isCurrent && <span className="text-sky-400 font-normal">(Anda)</span>}
                          </div>
                          <div className="text-[10px] text-slate-400">
                            {user.username} · {getUserOperatorLevel(user.id).level} {isAndi ? '· Piagam Terbit' : ''}
                          </div>
                        </div>
                      </div>

                      <div className="text-right">
                        <div className="text-xs font-black text-amber-400 font-mono">
                          {userXp.toLocaleString('id-ID')} XP
                        </div>
                        <div className="text-[10px] text-slate-400">
                          {stats.passedCount} Misi Lulus ({stats.totalStars}★)
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Data Isolation Note */}
              <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b] text-[10px] text-slate-400 space-y-1">
                <div className="font-bold text-sky-400 flex items-center gap-1">
                  <ShieldCheck className="w-3.5 h-3.5 text-sky-400" />
                  <span>KEAMANAN & ISOLASI DATA (PRD §8):</span>
                </div>
                <p>
                  Peserta hanya dapat melihat peringkat dalam lembaganya sendiri ({currentTenant.name}). Admin Lembaga dapat mengaktifkan/menonaktifkan papan peringkat ini kapan saja di menu L13.
                </p>
              </div>
            </>
          )}
        </div>

      </div>
    </div>
  );
};

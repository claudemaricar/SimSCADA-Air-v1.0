/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { MISSIONS_LIST } from '../../data/seedData';
import { computeBestPassedResults } from '../../utils/gamification';
import {
  AlertTriangle,
  CheckCircle2,
  FileSpreadsheet,
  Plus,
  Search,
  UserPlus,
} from 'lucide-react';

const ROLE_LABELS: Record<string, { label: string; colorClass: string }> = {
  superadmin: { label: 'Super Admin', colorClass: 'text-indigo-400' },
  admin_lembaga: { label: 'Admin Lembaga', colorClass: 'text-emerald-400' },
  pimpinan_lembaga: { label: 'Pimpinan Lembaga', colorClass: 'text-purple-400' },
  instruktur: { label: 'Instruktur SPAM', colorClass: 'text-amber-400' },
  peserta: { label: 'Peserta Operator', colorClass: 'text-sky-300' },
};

const TRACK_LABELS: Record<string, { label: string; colorClass: string }> = {
  ipa: { label: 'Operator IPA', colorClass: 'text-sky-400' },
  distribusi: { label: 'Operator Distribusi', colorClass: 'text-amber-400' },
  terpadu: { label: 'Air Minum Terpadu', colorClass: 'text-indigo-400' },
};

export const L12_ManageUsersGroups: React.FC = () => {
  const {
    currentUser,
    currentTenant,
    getVisibleUsers,
    getVisibleGroups,
    getVisibleCertificates,
    userMissionResults,
    addUser,
    addGroup,
    archiveGroup,
    resetPreTestForUser,
    userPrePostTests,
    preTestHistory,
    auditLogs,
    setCurrentView,
    setVerificationCertNo,
    showTechnicalRefs,
  } = useApp();

  const isTenantAdmin = currentUser?.role === 'admin_lembaga';

  const [searchQuery, setSearchQuery] = useState('');
  const [showAllParticipants, setShowAllParticipants] = useState(false);
  const [showAddUserModal, setShowAddUserModal] = useState(false);
  const [showAddGroupModal, setShowAddGroupModal] = useState(false);
  const [resetTargetUser, setResetTargetUser] = useState<(ReturnType<typeof getVisibleUsers>[number]) | null>(null);
  const [resetReason, setResetReason] = useState('');
  const [actionFeedback, setActionFeedback] = useState<string | null>(null);
  const [actionFeedbackType, setActionFeedbackType] = useState<'success' | 'error'>('success');

  const visibleUsers = getVisibleUsers().filter((u) => u.role !== 'superadmin');
  const visibleGroups = getVisibleGroups();
  const visibleCertificates = getVisibleCertificates();

  // Form states for new user
  const [newUsername, setNewUsername] = useState('');
  const [newFullName, setNewFullName] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [newRole, setNewRole] = useState<'peserta' | 'instruktur'>('peserta');
  const [newGroup, setNewGroup] = useState(visibleGroups[0]?.id || '');

  // Form states for new group
  const [newGroupName, setNewGroupName] = useState('');

  useEffect(() => {
    setNewGroup(visibleGroups[0]?.id || '');
    setSearchQuery('');
    setShowAllParticipants(false);
    setActionFeedback(null);
  }, [currentTenant.id]);

  const tenantParticipants = visibleUsers.filter((u) => u.role === 'peserta');
  const tenantInstructors = visibleUsers.filter((u) => u.role === 'instruktur');
  const tenantLeaders = visibleUsers.filter((u) => u.role === 'pimpinan_lembaga');
  const defaultInstructor =
    tenantInstructors[0] || visibleUsers.find((u) => u.role === 'admin_lembaga');

  const isBulkParticipant = (id: string) =>
    id.startsWith('user-nus-grp') || id.startsWith('user-trm-');

  const filteredUsers = visibleUsers.filter((u) => {
    const q = searchQuery.trim().toLowerCase();
    if (q) {
      return (
        u.username.toLowerCase().includes(q) ||
        u.fullName.toLowerCase().includes(q) ||
        u.role.toLowerCase().includes(q)
      );
    }
    if (!showAllParticipants && isBulkParticipant(u.id)) {
      return false;
    }
    return true;
  });

  const hiddenBulkCount = visibleUsers.filter((u) => isBulkParticipant(u.id)).length;

  const handleCreateUser = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUsername.trim() || !newFullName.trim()) return;

    const domain =
      currentTenant.id === 'tirta' ? 'tirtamandiri.co.id' : 'diklatnusantara.id';
    const defaultTrack = currentTenant.license.packageTracks[0] || 'ipa';

    const result = addUser({
      username: newUsername.trim(),
      fullName: newFullName.trim(),
      email: newEmail.trim() || `${newUsername.trim()}@${domain}`,
      role: newRole,
      tenantId: currentTenant.id,
      groupId: newGroup || visibleGroups[0]?.id,
      track: newRole === 'peserta' ? defaultTrack : undefined,
    });

    if (!result.success) {
      setActionFeedbackType('error');
      setActionFeedback(result.message || 'Gagal menambahkan pengguna baru.');
      return;
    }

    setActionFeedbackType('success');
    setActionFeedback(
      result.message || `Akun ${newUsername.trim()} berhasil ditambahkan ke ${currentTenant.name}.`
    );
    setShowAddUserModal(false);
    setNewUsername('');
    setNewFullName('');
    setNewEmail('');
  };

  const handleCreateGroup = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newGroupName.trim()) return;

    addGroup({
      name: newGroupName.trim(),
      tenantId: currentTenant.id,
      instructorId: defaultInstructor?.id || currentTenant.id,
      track: currentTenant.license.packageTracks[0] || 'ipa',
    });

    setActionFeedbackType('success');
    setActionFeedback(`Kelompok "${newGroupName.trim()}" berhasil dibuat untuk ${currentTenant.name}.`);
    setShowAddGroupModal(false);
    setNewGroupName('');
  };

  const handleImportCsv = () => {
    setActionFeedbackType('success');
    setActionFeedback(
      `Simulasi Impor CSV${showTechnicalRefs ? ' (FR-05)' : ''}: Berkas template ${currentTenant.code} tervalidasi (siap impor ke ${
        visibleGroups[0]?.name || currentTenant.name
      }).`
    );
  };

  const handleDeactivateUser = (username: string) => {
    setActionFeedbackType('success');
    setActionFeedback(`Status akun ${username} ditandai nonaktif untuk pengujian (${currentTenant.code}).`);
  };

  const handleConfirmResetPreTest = (e: React.FormEvent) => {
    e.preventDefault();
    if (!resetTargetUser) return;
    const res = resetPreTestForUser(resetTargetUser.id, resetReason);
    if (!res.success) {
      setActionFeedbackType('error');
      setActionFeedback(res.message);
      return;
    }
    setActionFeedbackType('success');
    setActionFeedback(res.message);
    setResetTargetUser(null);
    setResetReason('');
  };

  const tenantAuditLogs = auditLogs.filter((log) => log.tenantId === currentTenant.id);

  const getUserSummaryNote = (u: typeof visibleUsers[number]) => {
    if (u.role === 'admin_lembaga') {
      return `${visibleGroups.length} kelompok, ${tenantInstructors.length} instruktur, ${tenantParticipants.length} peserta`;
    }
    if (u.role === 'pimpinan_lembaga') {
      return 'Dashboard evaluasi eksekutif (T1–T4) & penanda tangan piagam';
    }
    if (u.role === 'instruktur') {
      const grp = visibleGroups.find((g) => g.id === u.groupId);
      return `Membina ${grp?.name || currentTenant.name} (Matrix & Approval)`;
    }
    const cert = visibleCertificates.find(
      (c) => c.userId === u.id && c.status === 'valid' && c.instructorApproved
    );
    const pendingCert = visibleCertificates.find(
      (c) => c.userId === u.id && c.status === 'valid' && !c.instructorApproved
    );
    const trackMissions = MISSIONS_LIST.filter((m) => m.track.includes(u.track || 'ipa'));
    const raw = userMissionResults[u.id] || [];
    const passed = computeBestPassedResults(raw, MISSIONS_LIST).filter((r) =>
      trackMissions.some((m) => m.code === r.missionCode)
    );
    const totalStars = passed.reduce((a, b) => a + b.stars, 0);

    if (cert) {
      return `${passed.length} misi lulus · piagam ${cert.certificateNumber} terbit`;
    }
    if (pendingCert) {
      return `Semua misi lulus · menunggu persetujuan ${pendingCert.certificateNumber}`;
    }
    if (passed.length === 0) {
      return 'Belum mulai; menampilkan pre-test dan misi pertama';
    }
    return `Aktif belajar: ${passed.length}/${trackMissions.length} misi lulus, ${totalStars}★`;
  };

  const quotaPct = Math.round(
    (currentTenant.license.seatsUsed / currentTenant.license.seatQuota) * 100
  );
  const isQuotaCritical = quotaPct >= 90;
  const remainingDays = currentTenant.id === 'nusantara' ? 245 : 28;

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Kelola Pengguna, Kelompok &amp; Kuota Kursi · {currentTenant.name}
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Manajemen Akun {currentTenant.name} ({currentTenant.code}) · Kuota {currentTenant.license.seatQuota} Kursi{showTechnicalRefs ? ' (PRD §5 & §18)' : ''}
        </p>
      </div>

      {actionFeedback && (
        <div
          className={`p-3 rounded-xl flex items-center justify-between text-xs border ${
            actionFeedbackType === 'error'
              ? 'bg-rose-500/10 border-rose-500/30 text-rose-300'
              : 'bg-emerald-500/10 border-emerald-500/30 text-emerald-300'
          }`}
        >
          <span className="flex items-center gap-2 font-semibold">
            {actionFeedbackType === 'error' ? (
              <AlertTriangle className="w-4 h-4 shrink-0" />
            ) : (
              <CheckCircle2 className="w-4 h-4 shrink-0" />
            )}
            {actionFeedback}
          </span>
          <button
            type="button"
            onClick={() => setActionFeedback(null)}
            className="text-slate-400 hover:text-white font-bold px-2 cursor-pointer"
          >
            ✕
          </button>
        </div>
      )}

      {/* 3 Top Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Card 1: Seats & License Quota */}
        <div
          className={`p-4 rounded-2xl border shadow-lg space-y-2 ${
            isQuotaCritical ? 'bg-amber-950/20 border-amber-500/40' : 'bg-[#0f172a] border-[#24324d]'
          }`}
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              ALOKASI KURSI LISENSI{showTechnicalRefs ? ' (PRD §5)' : ''}:
            </span>
            <span
              className={`px-2 py-0.5 rounded-md font-bold text-[9px] border ${
                isQuotaCritical
                  ? 'bg-amber-500/20 text-amber-300 border-amber-500/30'
                  : 'bg-sky-500/20 text-sky-300 border-sky-500/30'
              }`}
            >
              {isQuotaCritical ? `KUOTA ${quotaPct}% (≥90%)` : `TERPAKAI ${quotaPct}% · SISA ${remainingDays} HARI`}
            </span>
          </div>
          <div className="text-2xl font-black text-white font-mono">
            {currentTenant.license.seatsUsed}{' '}
            <span className="text-sm font-normal text-slate-400">
              / {currentTenant.license.seatQuota} Kursi Terpakai
            </span>
          </div>
          <div className={`text-[11px] font-medium ${isQuotaCritical ? 'text-amber-400' : 'text-sky-400'}`}>
            Sisa {currentTenant.license.seatQuota - currentTenant.license.seatsUsed} Kursi Kosong · Paket:{' '}
            {currentTenant.license.packageTracks.map((t) => t.toUpperCase()).join(' + ')}
          </div>
        </div>

        {/* Card 2: Active Groups */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-lg space-y-2">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
            KELOMPOK AKTIF{showTechnicalRefs ? ' (PRD §5)' : ''}:
          </span>
          <div className="text-2xl font-black text-sky-400 font-mono">
            {visibleGroups.length} Kelompok
          </div>
          <div className="text-[11px] text-slate-300 truncate">
            {visibleGroups
              .map((g) => {
                const cnt = tenantParticipants.filter((p) => p.groupId === g.id).length;
                return `${g.name} (${cnt} Peserta)`;
              })
              .join(' · ')}
          </div>
        </div>

        {/* Card 3: Faculty & Leadership */}
        <div className="p-4 rounded-2xl bg-[#0f172a] border border-[#24324d] shadow-lg space-y-2">
          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">
            TENAGA PENGAJAR &amp; PIMPINAN:
          </span>
          <div className="text-2xl font-black text-emerald-400 font-mono">
            {Math.max(1, tenantInstructors.length)} Instruktur · {Math.max(1, tenantLeaders.length)} Pimpinan
          </div>
          <div className="text-[11px] text-slate-300 truncate">
            {currentTenant.signers.instructorName} (Instruktur) · {currentTenant.signers.leaderName} (Pimpinan)
          </div>
        </div>
      </div>

      {/* Main Table Container: Users List */}
      <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-4 shadow-xl">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
          <div>
            <h2 className="text-base font-bold text-white">
              Daftar Akun Pengguna {currentTenant.name}{showTechnicalRefs ? ' (PRD SimSCADA-Air v1.2 §5)' : ''}
            </h2>
            <p className="text-xs text-slate-400">
              Menampilkan {visibleUsers.length} akun resmi {currentTenant.name} ({currentTenant.code}) · Data lembaga lain terisolasi penuh
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <div className="relative">
              <Search className="w-3.5 h-3.5 text-slate-500 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Cari username / nama..."
                className="pl-8 pr-3 py-1.5 bg-[#0b1120] border border-[#334155] rounded-xl text-xs text-white focus:outline-hidden focus:ring-1 focus:ring-sky-500"
              />
            </div>

            <button
              onClick={() => setShowAddUserModal(true)}
              className="px-3.5 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center gap-1.5 shadow-md shadow-sky-950/50 cursor-pointer"
            >
              <UserPlus className="w-3.5 h-3.5" />
              <span>+ Tambah Pengguna</span>
            </button>

            <button
              onClick={handleImportCsv}
              className="px-3.5 py-1.5 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 text-xs font-semibold transition-all flex items-center gap-1.5 cursor-pointer"
            >
              <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-400" />
              <span>Impor CSV{showTechnicalRefs ? ' (FR-05)' : ''}</span>
            </button>
          </div>
        </div>

        {/* Users Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-[#0b1120] text-slate-400 text-[10px] uppercase tracking-wider border-b border-[#1e293b] font-bold">
              <tr>
                <th className="py-3 px-3">Username{showTechnicalRefs ? ' (PRD §5)' : ''}</th>
                <th className="py-3 px-3">Nama Lengkap</th>
                <th className="py-3 px-3">Peran Sistem</th>
                <th className="py-3 px-3">Kelompok</th>
                <th className="py-3 px-3">Jalur Belajar</th>
                <th className="py-3 px-3">Kondisi Data Awal{showTechnicalRefs ? ' (PRD §5)' : ''}</th>
                <th className="py-3 px-3 text-right">Aksi</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1e293b] font-sans">
              {filteredUsers.map((u) => {
                const roleInfo = ROLE_LABELS[u.role] || {
                  label: u.role,
                  colorClass: 'text-slate-300',
                };
                const grpObj = visibleGroups.find((g) => g.id === u.groupId);
                const groupLabel =
                  u.role === 'admin_lembaga'
                    ? 'Seluruh Lembaga'
                    : u.role === 'pimpinan_lembaga'
                    ? 'Manajemen Eksekutif'
                    : grpObj?.name || '–';
                const trackInfo = u.track ? TRACK_LABELS[u.track] : null;
                const hasPre =
                  u.role === 'peserta' &&
                  userPrePostTests.some((t) => t.userId === u.id && t.type === 'pre');
                const issuedCert = visibleCertificates.find(
                  (c) => c.userId === u.id && c.status === 'valid' && c.instructorApproved
                );

                return (
                  <tr key={u.id} className="hover:bg-[#1e293b]/40">
                    <td className="py-3 px-3 font-mono font-bold text-sky-400">
                      {u.username}
                    </td>
                    <td className="py-3 px-3 font-semibold text-white">{u.fullName}</td>
                    <td className="py-3 px-3">
                      <span className={`font-semibold ${roleInfo.colorClass}`}>
                        {roleInfo.label}
                      </span>
                    </td>
                    <td className="py-3 px-3 text-slate-300">{groupLabel}</td>
                    <td className="py-3 px-3">
                      {trackInfo ? (
                        <span className={`font-semibold ${trackInfo.colorClass}`}>
                          {trackInfo.label}
                        </span>
                      ) : u.role === 'instruktur' ? (
                        <span className="text-slate-300">
                          {currentTenant.license.packageTracks.length > 1
                            ? 'Semua Jalur'
                            : 'Operator IPA'}
                        </span>
                      ) : (
                        <span className="text-slate-500">–</span>
                      )}
                    </td>
                    <td className="py-3 px-3 text-[11px] text-slate-400">
                      <div>{getUserSummaryNote(u)}</div>
                      {(preTestHistory[u.id] || []).length > 0 && (
                        <div className="text-[10px] text-amber-400/90 font-mono mt-0.5">
                          Riwayat nilai Pre-Test lama: {(preTestHistory[u.id] || []).map((h) => h.score).join(', ')}
                        </div>
                      )}
                    </td>
                    <td className="py-3 px-3 text-right space-x-2 whitespace-nowrap">
                      {issuedCert && (
                        <button
                          type="button"
                          onClick={() => {
                            setVerificationCertNo(issuedCert.certificateNumber);
                            setCurrentView('certificate');
                          }}
                          className="text-emerald-400 hover:underline font-semibold text-[11px] cursor-pointer"
                        >
                          Piagam{showTechnicalRefs ? ' (L8)' : ''}
                        </button>
                      )}
                      {hasPre && isTenantAdmin && (
                        <button
                          type="button"
                          onClick={() => {
                            setResetTargetUser(u);
                            setResetReason('');
                          }}
                          className="text-amber-400 hover:underline font-semibold text-[11px] cursor-pointer"
                        >
                          Reset Pre-Test
                        </button>
                      )}
                      {u.role !== 'admin_lembaga' && (
                        <button
                          type="button"
                          onClick={() => handleDeactivateUser(u.username)}
                          className="text-rose-400 hover:underline text-[11px] cursor-pointer"
                        >
                          Nonaktifkan
                        </button>
                      )}
                      {u.role === 'admin_lembaga' && (
                        <span className="text-sky-400 font-semibold text-[11px]">Aktif</span>
                      )}
                    </td>
                  </tr>
                );
              })}

              {hiddenBulkCount > 0 && !searchQuery.trim() && (
                <tr className="bg-[#0b1120] border-t-2 border-[#1e293b]">
                  <td colSpan={6} className="py-3 px-4 text-slate-400 text-xs">
                    <strong className="text-sky-400">+ {hiddenBulkCount} peserta contoh</strong> di{' '}
                    {currentTenant.name} · Total peserta:{' '}
                    <strong className="text-white">{tenantParticipants.length} peserta</strong> (
                    {currentTenant.license.seatsUsed} / {currentTenant.license.seatQuota} kursi terpakai)
                  </td>
                  <td className="py-3 px-3 text-right">
                    <button
                      type="button"
                      onClick={() => setShowAllParticipants(!showAllParticipants)}
                      className="text-sky-400 font-semibold cursor-pointer hover:underline text-[11px]"
                    >
                      {showAllParticipants
                        ? 'Ringkas daftar'
                        : `Lihat semua (${visibleUsers.length})`}
                    </button>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Group Management Section */}
      <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-4 shadow-xl">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-base font-bold text-white">
              Kelompok Belajar Binaan Lembaga{showTechnicalRefs ? ' (FR-05)' : ''}
            </h2>
            <p className="text-xs text-slate-400">
              Pengelompokan peserta {currentTenant.name} untuk penugasan modul dan pemantauan
            </p>
          </div>
          <button
            onClick={() => setShowAddGroupModal(true)}
            className="px-3.5 py-1.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>+ Buat Kelompok</span>
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {visibleGroups.map((grp) => {
            const count = tenantParticipants.filter((p) => p.groupId === grp.id).length;
            const grpInstructor =
              visibleUsers.find((u) => u.id === grp.instructorId)?.fullName ||
              currentTenant.signers.instructorName;
            return (
              <div
                key={grp.id}
                className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-white">
                    {grp.name} · {count} peserta · Aktif
                  </span>
                  <div className="space-x-2 text-[11px]">
                    <button
                      type="button"
                      onClick={() => {
                        setActionFeedbackType('success');
                        setActionFeedback(`Pengaturan kelompok "${grp.name}" dibuka.`);
                      }}
                      className="text-sky-400 font-semibold cursor-pointer hover:underline"
                    >
                      Ubah
                    </button>
                    <button
                      type="button"
                      onClick={() => archiveGroup(grp.id)}
                      className="text-slate-500 cursor-pointer hover:underline"
                    >
                      Arsip
                    </button>
                  </div>
                </div>
                <div className="text-[11px] text-slate-400">
                  Instruktur: <strong className="text-slate-200">{grpInstructor}</strong> · Paket:{' '}
                  {currentTenant.license.packageTracks.map((t) => t.toUpperCase()).join(' / ')}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Modal Add User */}
      {showAddUserModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-[#0f172a] rounded-2xl border border-[#334155] p-6 max-w-md w-full space-y-4">
            <h3 className="text-base font-bold text-white">Tambah Pengguna Baru ({currentTenant.code})</h3>
            <form onSubmit={handleCreateUser} className="space-y-3 text-xs">
              <div>
                <label className="block text-slate-300 font-semibold mb-1">Username</label>
                <input
                  type="text"
                  value={newUsername}
                  onChange={(e) => setNewUsername(e.target.value)}
                  placeholder={`misal: peserta.${currentTenant.code.toLowerCase()}.baru`}
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white font-mono"
                  required
                />
              </div>
              <div>
                <label className="block text-slate-300 font-semibold mb-1">Nama Lengkap</label>
                <input
                  type="text"
                  value={newFullName}
                  onChange={(e) => setNewFullName(e.target.value)}
                  placeholder="Nama Peserta"
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white"
                  required
                />
              </div>
              <div>
                <label className="block text-slate-300 font-semibold mb-1">Peran</label>
                <select
                  value={newRole}
                  onChange={(e) => setNewRole(e.target.value as 'peserta' | 'instruktur')}
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white"
                >
                  <option value="peserta">Peserta Operator</option>
                  <option value="instruktur">Instruktur</option>
                </select>
              </div>
              <div>
                <label className="block text-slate-300 font-semibold mb-1">Kelompok</label>
                <select
                  value={newGroup}
                  onChange={(e) => setNewGroup(e.target.value)}
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white"
                >
                  {visibleGroups.map((grp) => (
                    <option key={grp.id} value={grp.id}>
                      {grp.name}
                    </option>
                  ))}
                </select>
              </div>
              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowAddUserModal(false)}
                  className="px-4 py-2 bg-[#1e293b] text-slate-300 rounded-xl cursor-pointer"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-sky-600 text-white font-bold rounded-xl cursor-pointer"
                >
                  Simpan Pengguna
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Jejak Audit Reset Pre-Test (NFR-07) */}
      <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-4 shadow-xl">
        <div>
          <h2 className="text-base font-bold text-white">
            Jejak Audit Reset Pre-Test · {currentTenant.name}
          </h2>
          <p className="text-xs text-slate-400">
            Catatan resmi setiap pembukaan ulang Pre-Test oleh Admin Lembaga beserta nilai lama yang tetap tersimpan di riwayat.
          </p>
        </div>

        <div className="overflow-x-auto rounded-xl border border-[#1e293b] bg-[#0b1120]">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-[#0f172a] text-slate-400 text-[10px] uppercase tracking-wider border-b border-[#1e293b] font-bold">
              <tr>
                <th className="py-2.5 px-3">Waktu</th>
                <th className="py-2.5 px-3">Pelaku (Admin)</th>
                <th className="py-2.5 px-3">Peserta</th>
                <th className="py-2.5 px-3">Nilai Lama Tersimpan</th>
                <th className="py-2.5 px-3">Alasan Reset</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1e293b]">
              {tenantAuditLogs.length === 0 ? (
                <tr>
                  <td colSpan={5} className="py-5 px-3 text-center text-slate-500 text-xs">
                    Belum ada catatan reset Pre-Test pada {currentTenant.name}.
                  </td>
                </tr>
              ) : (
                tenantAuditLogs.map((log) => (
                  <tr key={log.id} className="hover:bg-[#1e293b]/40">
                    <td className="py-2.5 px-3 font-mono text-[11px] text-slate-400 whitespace-nowrap">
                      {new Date(log.timestamp).toLocaleString('id-ID', {
                        day: '2-digit',
                        month: 'short',
                        year: 'numeric',
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </td>
                    <td className="py-2.5 px-3 font-mono text-emerald-400 font-semibold">
                      {log.actorUsername}
                    </td>
                    <td className="py-2.5 px-3">
                      <span className="font-semibold text-white">{log.targetName}</span>{' '}
                      <span className="font-mono text-[11px] text-sky-400">({log.targetUsername})</span>
                    </td>
                    <td className="py-2.5 px-3 font-mono font-bold text-amber-400">
                      {log.previousScore !== null ? `${log.previousScore} / 100` : '–'}
                    </td>
                    <td className="py-2.5 px-3 text-slate-200">{log.reason}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal Reset Pre-Test (Admin Lembaga + Alasan Wajib) */}
      {resetTargetUser && isTenantAdmin && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-[#0f172a] rounded-2xl border border-amber-500/40 p-6 max-w-md w-full space-y-4 shadow-2xl">
            <h3 className="text-base font-bold text-white">
              Konfirmasi Reset Pre-Test Peserta
            </h3>
            <div className="p-3 rounded-xl bg-amber-950/30 border border-amber-500/30 text-xs text-slate-200 space-y-1">
              <div>
                Peserta: <strong className="text-white">{resetTargetUser.fullName}</strong> (
                <span className="font-mono text-sky-400">{resetTargetUser.username}</span>)
              </div>
              <div>
                Nilai Pre-Test saat ini:{' '}
                <strong className="text-amber-400 font-mono">
                  {userPrePostTests.find((t) => t.userId === resetTargetUser.id && t.type === 'pre')?.score ?? '–'} / 100
                </strong>
              </div>
              <p className="text-[11px] text-slate-400 pt-1">
                Nilai lama tetap disimpan dalam riwayat dan tercatat di jejak audit. Nilai Pre-Test baru setelah dikerjakan ulang menjadi baseline aktif perhitungan kenaikan kompetensi.
              </p>
            </div>
            <form onSubmit={handleConfirmResetPreTest} className="space-y-3 text-xs">
              <div>
                <label className="block text-slate-300 font-semibold mb-1">
                  Alasan Reset Pre-Test (Wajib Diisi)
                </label>
                <textarea
                  value={resetReason}
                  onChange={(e) => setResetReason(e.target.value)}
                  placeholder="Contoh: Gangguan koneksi listrik saat pengerjaan awal sesuai berita acara kelas."
                  rows={3}
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white"
                  required
                />
              </div>
              <div className="flex justify-end gap-2 pt-1">
                <button
                  type="button"
                  onClick={() => {
                    setResetTargetUser(null);
                    setResetReason('');
                  }}
                  className="px-4 py-2 bg-[#1e293b] text-slate-300 rounded-xl cursor-pointer"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  disabled={!resetReason.trim()}
                  className="px-4 py-2 bg-amber-500 hover:bg-amber-400 disabled:opacity-40 text-slate-950 font-bold rounded-xl cursor-pointer"
                >
                  Konfirmasi Reset &amp; Catat Audit
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Modal Add Group */}
      {showAddGroupModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-[#0f172a] rounded-2xl border border-[#334155] p-6 max-w-md w-full space-y-4">
            <h3 className="text-base font-bold text-white">Buat Kelompok Baru ({currentTenant.name})</h3>
            <form onSubmit={handleCreateGroup} className="space-y-3 text-xs">
              <div>
                <label className="block text-slate-300 font-semibold mb-1">Nama Kelompok</label>
                <input
                  type="text"
                  value={newGroupName}
                  onChange={(e) => setNewGroupName(e.target.value)}
                  placeholder={`Contoh: Angkatan 2 ${currentTenant.shortName}`}
                  className="w-full p-2.5 bg-[#0b1120] border border-[#334155] rounded-xl text-white"
                  required
                />
              </div>
              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowAddGroupModal(false)}
                  className="px-4 py-2 bg-[#1e293b] text-slate-300 rounded-xl cursor-pointer"
                >
                  Batal
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-sky-600 text-white font-bold rounded-xl cursor-pointer"
                >
                  Buat Kelompok
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

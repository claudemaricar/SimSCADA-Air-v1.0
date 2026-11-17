/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useRef, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { MISSIONS_LIST } from '../../data/seedData';
import { computeBestPassedResults } from '../../utils/gamification';
import {
  Award,
  BookOpen,
  Building2,
  ChevronDown,
  FileCheck2,
  History,
  LineChart,
  LogOut,
  Menu,
  MoreHorizontal,
  PlayCircle,
  RotateCcw,
  Settings,
  Shield,
  Sparkles,
  UserCheck,
  Users,
  Volume2,
  VolumeX,
  X,
} from 'lucide-react';
import { scadaAudio } from '../../utils/audio';
import { UserGuideModal } from '../views/UserGuideModal';

interface HeaderProps {
  currentView: string;
  onNavigate: (view: string) => void;
}

interface NavItem {
  id: string;
  label: string;
  shortLabel: string;
  icon?: React.ReactNode;
  secondary?: boolean;
  onClick: () => void;
  isActive: boolean;
}

export const Header: React.FC<HeaderProps> = ({ currentView, onNavigate }) => {
  const {
    currentUser,
    currentTenant,
    logout,
    loginAs,
    getUserXP,
    getUserOperatorLevel,
    userMissionResults,
    resetDemoData,
    setSelectedMissionCode,
  } = useApp();

  const [showSwitchModal, setShowSwitchModal] = useState(false);
  const [showGuideModal, setShowGuideModal] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [moreMenuOpen, setMoreMenuOpen] = useState(false);
  const [isMuted, setIsMuted] = useState(scadaAudio.getIsMuted());
  const moreMenuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (moreMenuRef.current && !moreMenuRef.current.contains(e.target as Node)) {
        setMoreMenuOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleToggleMute = () => {
    const nextMuted = !isMuted;
    scadaAudio.setMuted(nextMuted);
    setIsMuted(nextMuted);
  };

  const handleNavClick = (action: () => void) => {
    action();
    setMobileMenuOpen(false);
    setMoreMenuOpen(false);
  };

  const operatorLevel = currentUser ? getUserOperatorLevel(currentUser.id) : null;

  const getUserStars = (userId: string) =>
    computeBestPassedResults(userMissionResults[userId] || [], MISSIONS_LIST).reduce(
      (sum, r) => sum + r.stars,
      0
    );

  // Build role-based navigation items (shared between desktop, "Lainnya", and hamburger drawer)
  const navItems: NavItem[] = [];

  if (currentUser?.role === 'peserta') {
    navItems.push(
      {
        id: 'home',
        label: 'Beranda & Peta Misi',
        shortLabel: 'Beranda',
        isActive: currentView === 'home',
        onClick: () => onNavigate('home'),
      },
      {
        id: 'track_select',
        label: 'Pilih Jalur (L3)',
        shortLabel: 'Pilih Jalur',
        secondary: true,
        isActive: currentView === 'track_select',
        onClick: () => onNavigate('track_select'),
      },
      {
        id: 'module_quiz',
        label: 'Materi & Kuis (L4)',
        shortLabel: 'Materi & Kuis',
        isActive: currentView === 'module_quiz',
        onClick: () => onNavigate('module_quiz'),
      },
      {
        id: 'pre_post_test',
        label: 'Pre/Post-Test (L4a)',
        shortLabel: 'Pre/Post-Test',
        secondary: true,
        isActive: currentView === 'pre_post_test',
        onClick: () => onNavigate('pre_post_test'),
      },
      {
        id: 'simulator',
        label: 'Simulator SCADA (L5)',
        shortLabel: 'Simulator',
        icon: <PlayCircle className="w-3.5 h-3.5 text-sky-400" />,
        isActive: currentView === 'simulator',
        onClick: () => {
          setSelectedMissionCode('IPA-06');
          onNavigate('simulator');
        },
      },
      {
        id: 'badges',
        label: 'Lencana & Peringkat (L7)',
        shortLabel: 'Lencana',
        icon: <Award className="w-3.5 h-3.5 text-amber-400" />,
        isActive: currentView === 'badges',
        onClick: () => onNavigate('badges'),
      },
      {
        id: 'certificate',
        label: 'Piagam Kelulusan (L8)',
        shortLabel: 'Piagam',
        icon: <FileCheck2 className="w-3.5 h-3.5 text-emerald-400" />,
        isActive: currentView === 'certificate' || currentView === 'certificate_pending',
        onClick: () => onNavigate('certificate'),
      }
    );
  } else if (currentUser?.role === 'instruktur') {
    navItems.push(
      {
        id: 'instructor_dashboard',
        label: 'Dasbor Pengawasan (L9)',
        shortLabel: 'Dasbor (L9)',
        isActive: currentView === 'instructor_dashboard' || currentView === 'home',
        onClick: () => onNavigate('instructor_dashboard'),
      },
      {
        id: 'manage_scenarios',
        label: 'Kelola Skenario (L10)',
        shortLabel: 'Skenario (L10)',
        isActive: currentView === 'manage_scenarios',
        onClick: () => onNavigate('manage_scenarios'),
      },
      {
        id: 'replay',
        label: 'Putar Ulang Sesi (L11)',
        shortLabel: 'Replay (L11)',
        icon: <History className="w-3.5 h-3.5 text-sky-400" />,
        isActive: currentView === 'replay',
        onClick: () => onNavigate('replay'),
      },
      {
        id: 'simulator',
        label: 'Uji Simulator (L5)',
        shortLabel: 'Simulator',
        isActive: currentView === 'simulator',
        onClick: () => {
          setSelectedMissionCode('IPA-06');
          onNavigate('simulator');
        },
      }
    );
  } else if (
    currentUser?.role === 'admin_lembaga' ||
    currentUser?.role === 'pimpinan_lembaga'
  ) {
    navItems.push({
      id: 'evaluation',
      label: 'Evaluasi Lembaga (T1–T4)',
      shortLabel: 'Evaluasi (L14)',
      icon: <LineChart className="w-3.5 h-3.5 text-sky-400" />,
      isActive: currentView === 'evaluation' || currentView === 'home',
      onClick: () => onNavigate('evaluation'),
    });
    if (currentUser.role === 'admin_lembaga') {
      navItems.push(
        {
          id: 'manage_users',
          label: 'Pengguna & Kelompok (L12)',
          shortLabel: 'Pengguna (L12)',
          icon: <Users className="w-3.5 h-3.5 text-emerald-400" />,
          isActive: currentView === 'manage_users',
          onClick: () => onNavigate('manage_users'),
        },
        {
          id: 'tenant_settings',
          label: 'Pengaturan Lembaga (L13)',
          shortLabel: 'Pengaturan (L13)',
          icon: <Settings className="w-3.5 h-3.5 text-amber-400" />,
          isActive: currentView === 'tenant_settings',
          onClick: () => onNavigate('tenant_settings'),
        }
      );
    }
    navItems.push({
      id: 'certificate',
      label: 'Daftar Piagam (L8)',
      shortLabel: 'Piagam (L8)',
      isActive: currentView === 'certificate',
      onClick: () => onNavigate('certificate'),
    });
  } else if (currentUser?.role === 'superadmin') {
    navItems.push(
      {
        id: 'superadmin_dashboard',
        label: 'Konsol Lembaga & Lisensi (L15)',
        shortLabel: 'Konsol Lembaga (L15)',
        icon: <Shield className="w-3.5 h-3.5 text-indigo-400" />,
        isActive: currentView === 'superadmin_dashboard' || currentView === 'home',
        onClick: () => onNavigate('superadmin_dashboard'),
      },
      {
        id: 'simulator',
        label: 'Uji Simulator (L5)',
        shortLabel: 'Simulator',
        isActive: currentView === 'simulator',
        onClick: () => {
          setSelectedMissionCode('IPA-06');
          onNavigate('simulator');
        },
      }
    );
  }

  navItems.push({
    id: 'public_verification',
    label: 'Verifikasi Publik (L16)',
    shortLabel: 'Verifikasi (L16)',
    secondary: currentUser?.role === 'peserta',
    isActive: currentView === 'public_verification',
    onClick: () => onNavigate('public_verification'),
  });

  const primaryItems = navItems.filter((item) => !item.secondary);
  const secondaryItems = navItems.filter((item) => item.secondary);
  const hasActiveSecondary = secondaryItems.some((item) => item.isActive);

  const dimasXP = getUserXP('user-peserta-ipa');
  const dimasStars = getUserStars('user-peserta-ipa');
  const andiXP = getUserXP('user-peserta-lulus');
  const andiStars = getUserStars('user-peserta-lulus');
  const sitiXP = getUserXP('user-peserta-distribusi');
  const sitiStars = getUserStars('user-peserta-distribusi');
  const baruXP = getUserXP('user-peserta-baru');

  return (
    <>
      <header className="sticky top-0 z-40 bg-[#0f172a] border-b border-[#1e293b] shadow-md select-none">
        <div className="max-w-[1720px] mx-auto px-3 sm:px-5">
          <div className="flex items-center justify-between h-16 gap-2 sm:gap-3">
            {/* Zone 1: Hamburger (< 1366px) + Brand & Tenant Identity */}
            <div className="flex items-center gap-2 sm:gap-2.5 min-w-0 shrink-0">
              {currentUser && (
                <button
                  type="button"
                  onClick={() => setMobileMenuOpen((prev) => !prev)}
                  aria-label={mobileMenuOpen ? 'Tutup menu navigasi' : 'Buka menu navigasi'}
                  aria-expanded={mobileMenuOpen}
                  className="min-[1366px]:hidden p-2 rounded-lg border border-[#334155] bg-[#1e293b]/80 hover:bg-[#1e293b] text-slate-200 hover:text-white transition-colors cursor-pointer shrink-0"
                >
                  {mobileMenuOpen ? <X className="w-4 h-4" /> : <Menu className="w-4 h-4" />}
                </button>
              )}

              <div
                onClick={() => handleNavClick(() => onNavigate('home'))}
                className="flex items-center gap-2.5 cursor-pointer group min-w-0"
              >
                <div className="w-9 h-9 rounded-xl bg-sky-600/20 border border-sky-500/40 text-sky-400 flex items-center justify-center font-bold shadow-inner group-hover:bg-sky-600/30 transition-all shrink-0">
                  <Building2 className="w-4 h-4 text-sky-400" />
                </div>
                <div className="flex flex-col min-w-0">
                  <span className="font-bold text-slate-100 text-xs sm:text-sm leading-tight group-hover:text-sky-300 transition-colors whitespace-nowrap">
                    {currentTenant.name}
                  </span>
                  <span className="text-[10px] text-slate-400 font-medium leading-none mt-0.5 whitespace-nowrap hidden sm:block">
                    Didukung <span className="text-sky-400 font-semibold">SimSCADA-Air</span>
                    <span className="hidden 2xl:inline"> · Platform Simulator SCADA Air Minum</span>
                  </span>
                </div>
              </div>
            </div>

            {/* Zone 2: Desktop Role-based Navigation (>= 1366px) */}
            <nav className="hidden min-[1366px]:flex items-center gap-1 min-w-0">
              {primaryItems.map((item) => (
                <button
                  key={item.id}
                  type="button"
                  onClick={() => handleNavClick(item.onClick)}
                  className={`px-2.5 py-1.5 text-xs font-semibold rounded-lg transition-colors flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                    item.isActive
                      ? item.id === 'public_verification'
                        ? 'bg-emerald-600/20 border border-emerald-500/50 text-emerald-300'
                        : item.id === 'superadmin_dashboard'
                        ? 'bg-indigo-600/20 border border-indigo-500/40 text-indigo-300'
                        : 'bg-sky-600/20 border border-sky-500/40 text-sky-300'
                      : item.id === 'public_verification'
                      ? 'border border-[#334155] text-slate-300 hover:text-white hover:bg-slate-800/60'
                      : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                  }`}
                >
                  {item.icon}
                  <span>{item.shortLabel}</span>
                </button>
              ))}

              {/* Secondary items: inline at >= 1536px (2xl), collapsed into "Lainnya ▾" at 1366px..1535px */}
              {secondaryItems.length > 0 && (
                <>
                  <div className="hidden 2xl:flex items-center gap-1">
                    {secondaryItems.map((item) => (
                      <button
                        key={item.id}
                        type="button"
                        onClick={() => handleNavClick(item.onClick)}
                        className={`px-2.5 py-1.5 text-xs font-semibold rounded-lg transition-colors flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                          item.isActive
                            ? item.id === 'public_verification'
                              ? 'bg-emerald-600/20 border border-emerald-500/50 text-emerald-300'
                              : 'bg-sky-600/20 border border-sky-500/40 text-sky-300'
                            : item.id === 'public_verification'
                            ? 'border border-[#334155] text-slate-300 hover:text-white hover:bg-slate-800/60'
                            : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                        }`}
                      >
                        {item.icon}
                        <span>{item.shortLabel}</span>
                      </button>
                    ))}
                  </div>

                  <div ref={moreMenuRef} className="relative 2xl:hidden">
                    <button
                      type="button"
                      onClick={() => setMoreMenuOpen((prev) => !prev)}
                      aria-expanded={moreMenuOpen}
                      className={`px-2.5 py-1.5 text-xs font-semibold rounded-lg transition-colors flex items-center gap-1 whitespace-nowrap border cursor-pointer ${
                        hasActiveSecondary
                          ? 'bg-sky-600/20 border-sky-500/40 text-sky-300'
                          : 'border-[#334155] text-slate-300 hover:text-white hover:bg-slate-800/60'
                      }`}
                    >
                      <MoreHorizontal className="w-3.5 h-3.5" />
                      <span>Lainnya</span>
                      <ChevronDown className="w-3 h-3" />
                    </button>

                    {moreMenuOpen && (
                      <div className="absolute right-0 mt-2 w-56 rounded-xl bg-[#0f172a] border border-[#334155] shadow-2xl p-1.5 z-50 space-y-1">
                        {secondaryItems.map((item) => (
                          <button
                            key={item.id}
                            type="button"
                            onClick={() => handleNavClick(item.onClick)}
                            className={`w-full text-left px-3 py-2 rounded-lg text-xs font-semibold transition-colors flex items-center justify-between cursor-pointer ${
                              item.isActive
                                ? 'bg-sky-600/20 text-sky-300 border border-sky-500/30'
                                : 'text-slate-200 hover:bg-slate-800 hover:text-white'
                            }`}
                          >
                            <span>{item.label}</span>
                          </button>
                        ))}
                      </div>
                    )}
                  </div>
                </>
              )}
            </nav>

            {/* Zone 3: Audio Toggle, Guide, Profile & Keluar */}
            <div className="flex items-center gap-1.5 sm:gap-2 shrink-0">
              <button
                type="button"
                onClick={() => setShowGuideModal(true)}
                title="Buka Dokumen Blueprint & Panduan Pengguna"
                className="px-2 py-1.5 rounded-lg border border-[#334155] bg-[#1e293b]/70 hover:bg-[#1e293b] text-slate-300 hover:text-white transition-colors flex items-center gap-1.5 text-xs font-semibold whitespace-nowrap cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5 text-sky-400" />
                <span className="hidden md:inline">Panduan</span>
              </button>

              <button
                type="button"
                onClick={handleToggleMute}
                title={isMuted ? 'Nyalakan Bunyi Alarm SCADA' : 'Matikan Suara (Mute)'}
                className={`p-2 rounded-lg border transition-colors cursor-pointer ${
                  isMuted
                    ? 'bg-amber-500/10 border-amber-500/30 text-amber-400 hover:bg-amber-500/20'
                    : 'bg-[#1e293b]/70 border-[#334155] text-slate-300 hover:text-white hover:bg-[#1e293b]'
                }`}
              >
                {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
              </button>

              {currentUser ? (
                <div className="flex items-center gap-1.5 sm:gap-2">
                  <button
                    type="button"
                    onClick={() => setShowSwitchModal(true)}
                    className="flex items-center gap-2 px-2 py-1 rounded-xl border border-[#334155] bg-[#1e293b]/80 hover:bg-[#1e293b] transition-all text-left cursor-pointer"
                  >
                    <div className="w-7 h-7 rounded-lg bg-sky-600 text-white font-bold flex items-center justify-center text-xs shadow-inner shrink-0">
                      {currentUser.fullName.charAt(0)}
                    </div>
                    <div className="hidden sm:flex flex-col">
                      <span className="text-xs font-semibold text-slate-100 leading-tight whitespace-nowrap">
                        {currentUser.fullName}
                      </span>
                      <span className="text-[10px] text-sky-400 font-medium whitespace-nowrap">
                        {currentUser.role === 'peserta'
                          ? operatorLevel?.level || 'Operator Magang'
                          : currentUser.role === 'instruktur'
                          ? 'Instruktur'
                          : currentUser.role === 'admin_lembaga'
                          ? 'Admin Lembaga'
                          : currentUser.role === 'pimpinan_lembaga'
                          ? 'Pimpinan Lembaga'
                          : 'Super Admin'}
                      </span>
                    </div>
                    <ChevronDown className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                  </button>

                  <button
                    type="button"
                    onClick={() => logout()}
                    title="Keluar (Logout)"
                    className="px-2.5 py-1.5 rounded-lg border border-[#334155] text-slate-300 hover:text-rose-300 hover:bg-rose-500/10 hover:border-rose-500/30 transition-colors flex items-center gap-1.5 text-xs font-semibold whitespace-nowrap cursor-pointer"
                  >
                    <LogOut className="w-3.5 h-3.5 shrink-0" />
                    <span className="hidden sm:inline">Keluar</span>
                  </button>
                </div>
              ) : (
                <button
                  type="button"
                  onClick={() => onNavigate('login')}
                  className="px-4 py-2 text-xs font-semibold text-white bg-sky-600 hover:bg-sky-500 rounded-lg shadow-sm transition-colors whitespace-nowrap cursor-pointer"
                >
                  Masuk ke Portal
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Responsive Hamburger Drawer (< 1366px) */}
        {mobileMenuOpen && currentUser && (
          <div className="min-[1366px]:hidden border-t border-[#1e293b] bg-[#0b1120] px-4 py-3 shadow-2xl">
            <div className="max-w-[1720px] mx-auto space-y-2">
              <div className="text-[10px] font-bold uppercase tracking-wider text-slate-400 px-1">
                Menu Navigasi ({currentUser.fullName})
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
                {navItems.map((item) => (
                  <button
                    key={item.id}
                    type="button"
                    onClick={() => handleNavClick(item.onClick)}
                    className={`w-full text-left px-3 py-2.5 rounded-xl text-xs font-semibold border transition-colors flex items-center gap-2 cursor-pointer ${
                      item.isActive
                        ? 'bg-sky-600/20 border-sky-500/40 text-sky-300'
                        : 'bg-[#0f172a] border-[#1e293b] text-slate-200 hover:bg-[#1e293b] hover:text-white'
                    }`}
                  >
                    {item.icon}
                    <span>{item.label}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </header>

      {/* Quick Demo Switcher Modal (10 Akun Demo PRD §5) */}
      {showSwitchModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-xs p-4">
          <div className="bg-[#0f172a] rounded-2xl shadow-2xl border border-[#334155] w-full max-w-xl p-6 text-slate-200">
            <div className="flex items-center justify-between pb-3 border-b border-[#1e293b] mb-4">
              <div className="flex items-center gap-2.5">
                <div className="p-2 rounded-lg bg-sky-500/10 border border-sky-500/20 text-sky-400">
                  <Sparkles className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-bold text-white">
                    Pilih Akun Demo Prototipe (PRD §5)
                  </h3>
                  <p className="text-[11px] text-slate-400">
                    Sandi semua akun demo: <code className="text-sky-400 font-mono font-bold">Demo#2026</code>
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowSwitchModal(false)}
                className="text-slate-400 hover:text-white text-sm font-semibold p-1 cursor-pointer"
              >
                ✕
              </button>
            </div>

            <div className="space-y-2.5 max-h-[420px] overflow-y-auto pr-1">
              <div className="text-[11px] font-bold text-sky-400 uppercase tracking-wider px-1">
                Balai Diklat Air Minum Nusantara (NUS - 50 Kursi)
              </div>

              <button
                type="button"
                onClick={() => { loginAs('peserta.ipa'); onNavigate('home'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-sky-500/40 bg-sky-950/30 hover:bg-sky-900/40 transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-sky-300">
                    peserta.ipa · Dimas Wahyu Pratama
                  </div>
                  <div className="text-[11px] text-sky-300/80">
                    Angkatan 1 · Operator Madya · {dimasXP.toLocaleString('id-ID')} XP · {dimasStars}★ (7/9 Misi Lulus)
                  </div>
                </div>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30">
                  Sesi Contoh L5/L6
                </span>
              </button>

              <button
                type="button"
                onClick={() => { loginAs('peserta.lulus'); onNavigate('certificate'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-emerald-500/40 bg-emerald-950/30 hover:bg-emerald-900/40 transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-emerald-300">
                    peserta.lulus · Andi Kurniawan
                  </div>
                  <div className="text-[11px] text-emerald-300/80">
                    Jalur Terpadu (16 Misi Lulus · {andiStars}★) · {andiXP.toLocaleString('id-ID')} XP · Operator Ahli · Piagam SSA/NUS/2026/0001 Terbit
                  </div>
                </div>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  Piagam Terbit
                </span>
              </button>

              <button
                type="button"
                onClick={() => { loginAs('peserta.distribusi'); onNavigate('home'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-[#1e293b] bg-[#1e293b]/40 hover:bg-[#1e293b] transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-sky-300">
                    peserta.distribusi · Siti Rahmawati
                  </div>
                  <div className="text-[11px] text-slate-400">
                    Jalur Distribusi · {sitiXP.toLocaleString('id-ID')} XP · Operator Muda (DST-01..05 Lulus {sitiStars}★)
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-slate-400 group-hover:text-sky-400" />
              </button>

              <button
                type="button"
                onClick={() => { loginAs('peserta.baru'); onNavigate('home'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-[#1e293b] bg-[#1e293b]/40 hover:bg-[#1e293b] transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-sky-300">
                    peserta.baru · Budi Baru
                  </div>
                  <div className="text-[11px] text-slate-400">
                    Jalur Terpadu · Operator Magang · {baruXP.toLocaleString('id-ID')} XP · Belum mulai
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-slate-400 group-hover:text-sky-400" />
              </button>

              <button
                type="button"
                onClick={() => { loginAs('instruktur.nusantara'); onNavigate('instructor_dashboard'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-[#1e293b] bg-[#1e293b]/40 hover:bg-[#1e293b] transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-amber-300">
                    instruktur.nusantara · Budi Santoso, S.T.
                  </div>
                  <div className="text-[11px] text-slate-400">
                    Instruktur Pembina Angkatan 1 · Monitoring, approval piagam, buka kunci
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-amber-400" />
              </button>

              <button
                type="button"
                onClick={() => { loginAs('admin.nusantara'); onNavigate('evaluation'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-[#1e293b] bg-[#1e293b]/40 hover:bg-[#1e293b] transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-emerald-300">
                    admin.nusantara · Rina Oktaviani
                  </div>
                  <div className="text-[11px] text-slate-400">
                    Admin Lembaga Nusantara · Kelola akun (46/50 kursi), KKM, pengaturan
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-emerald-400" />
              </button>

              <button
                type="button"
                onClick={() => { loginAs('pimpinan.nusantara'); onNavigate('evaluation'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-[#1e293b] bg-[#1e293b]/40 hover:bg-[#1e293b] transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-sky-300">
                    pimpinan.nusantara · Dr. Ir. Bambang Sutrisno, M.Eng.
                  </div>
                  <div className="text-[11px] text-slate-400">
                    Pimpinan Balai Diklat · Dasbor Eksekutif (T1–T4) &amp; Penanda Tangan Piagam
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-sky-400" />
              </button>

              <div className="text-[11px] font-bold text-teal-400 uppercase tracking-wider px-1 pt-2">
                Pusat Pelatihan Tirta Mandiri (TRM - Uji Isolasi Data Multi-Tenant)
              </div>

              <button
                type="button"
                onClick={() => { loginAs('admin.tirta'); onNavigate('evaluation'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-teal-500/30 bg-teal-950/20 hover:bg-teal-900/30 transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-teal-300">
                    admin.tirta · Hj. Dewi Anggraini
                  </div>
                  <div className="text-[11px] text-teal-300/80">
                    Admin Lembaga Tirta Mandiri · Isolasi tenant mandiri (1 kelompok, 12 piagam)
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-teal-400" />
              </button>

              <button
                type="button"
                onClick={() => { loginAs('peserta.tirta'); onNavigate('home'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-teal-500/30 bg-teal-950/20 hover:bg-teal-900/30 transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-teal-300">
                    peserta.tirta · Siti Aminah
                  </div>
                  <div className="text-[11px] text-teal-300/80">
                    Peserta Tirta Mandiri · Jalur IPA · Angkatan 1 Tirta Mandiri
                  </div>
                </div>
                <UserCheck className="w-4 h-4 text-teal-400" />
              </button>

              <div className="text-[11px] font-bold text-indigo-400 uppercase tracking-wider px-1 pt-2">
                Super Admin Platform
              </div>

              <button
                type="button"
                onClick={() => { loginAs('superadmin'); onNavigate('superadmin_dashboard'); setShowSwitchModal(false); }}
                className="w-full text-left p-2.5 rounded-xl border border-indigo-500/40 bg-indigo-950/30 hover:bg-indigo-900/40 transition-all flex items-center justify-between group cursor-pointer"
              >
                <div>
                  <div className="text-xs font-bold text-white group-hover:text-indigo-300">
                    superadmin · Super Admin Platform
                  </div>
                  <div className="text-[11px] text-indigo-300/80">
                    Konsol pengelola tenant multi-lembaga, paket lisensi, dan kuota global
                  </div>
                </div>
                <Shield className="w-4 h-4 text-indigo-400" />
              </button>
            </div>

            <div className="pt-4 border-t border-[#1e293b] mt-4 flex items-center justify-between">
              <button
                type="button"
                onClick={() => {
                  if (confirm('Kembalikan semua data latihan ke kondisi bawaan prototipe PRD §5?')) {
                    resetDemoData();
                    setShowSwitchModal(false);
                    onNavigate('home');
                  }
                }}
                className="inline-flex items-center gap-1.5 text-xs text-rose-400 hover:text-rose-300 font-semibold cursor-pointer"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                Reset Data Demo
              </button>
              <button
                type="button"
                onClick={() => setShowSwitchModal(false)}
                className="px-4 py-2 text-xs font-semibold rounded-xl bg-[#1e293b] text-slate-200 hover:bg-[#334155] transition-colors cursor-pointer"
              >
                Tutup
              </button>
            </div>
          </div>
        </div>
      )}

      {showGuideModal && <UserGuideModal onClose={() => setShowGuideModal(false)} />}
    </>
  );
};

/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useState } from 'react';
import { useApp } from '../../context/AppContext';
import { PRE_POST_TEST_QUESTIONS } from '../../data/seedData';
import {
  ArrowLeft,
  ArrowRight,
  Check,
  CheckCircle2,
  ClipboardCheck,
  Clock,
  FileCheck2,
  Lock,
  Play,
  TrendingUp,
} from 'lucide-react';
import { LearningTrack } from '../../types';

interface PrePostTestProps {
  initialMode?: 'auto' | 'pre' | 'post';
  onBack: () => void;
  onViewCertificate: () => void;
  onStartFirstMission?: (missionCode: string) => void;
}

const getTrackDisplayName = (track: LearningTrack): string => {
  if (track === 'ipa') return 'Operator IPA';
  if (track === 'distribusi') return 'Operator Distribusi';
  return 'Air Minum Terpadu';
};

export const L4a_PrePostTest: React.FC<PrePostTestProps> = ({
  initialMode = 'auto',
  onBack,
  onViewCertificate,
  onStartFirstMission,
}) => {
  const {
    currentUser,
    currentTenant,
    activeTrack,
    getMissionsForTrack,
    getBestMissionResult,
    userPrePostTests,
    savePrePostTest,
    certificates,
  } = useApp();

  if (!currentUser) return null;

  const userTrack: LearningTrack = currentUser.track || activeTrack || 'ipa';
  const trackLabel = getTrackDisplayName(userTrack);
  const trackMissions = getMissionsForTrack(userTrack);
  const gradMissionCode =
    userTrack === 'ipa' ? 'IPA-09' : userTrack === 'distribusi' ? 'DST-07' : 'TRP-02';
  const gradThreshold = currentTenant.config.graduationThresholdScore || 80;

  let passedCount = 0;
  trackMissions.forEach((m) => {
    const res = getBestMissionResult(currentUser.id, m.code);
    if (res && res.isPassed) passedCount += 1;
  });
  const gradResult = getBestMissionResult(currentUser.id, gradMissionCode);
  const allMissionsPassed = trackMissions.length > 0 && passedCount === trackMissions.length;
  const gradPassed = Boolean(gradResult && gradResult.totalScore >= gradThreshold);

  const preTest = userPrePostTests.find((t) => t.userId === currentUser.id && t.type === 'pre');
  const postTest = userPrePostTests.find((t) => t.userId === currentUser.id && t.type === 'post');
  const canTakePostTest = Boolean(preTest) && allMissionsPassed && gradPassed;

  const validCert = certificates.find(
    (c) => c.userId === currentUser.id && c.status === 'valid' && c.instructorApproved
  );

  const resolveInitialTab = (): 'pre' | 'post' => {
    if (initialMode === 'pre') return 'pre';
    if (initialMode === 'post') return 'post';
    if (!preTest) return 'pre';
    if (canTakePostTest || postTest) return 'post';
    return 'pre';
  };

  const [activeTab, setActiveTab] = useState<'pre' | 'post'>(resolveInitialTab);
  const [isExamActive, setIsExamActive] = useState<boolean>(() => {
    const tab = resolveInitialTab();
    if (tab === 'pre' && !preTest) return true;
    if (tab === 'post' && canTakePostTest && !postTest) return true;
    return false;
  });
  const [activeQuestionIdx, setActiveQuestionIdx] = useState<number>(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, number>>({});
  const [secondsLeft, setSecondsLeft] = useState<number>(30 * 60); // 30 minutes
  const [justSubmittedType, setJustSubmittedType] = useState<'pre' | 'post' | null>(null);

  // Reset exam state when switching logged-in user or initialMode
  useEffect(() => {
    const tab = resolveInitialTab();
    setActiveTab(tab);
    setSelectedAnswers({});
    setActiveQuestionIdx(0);
    setSecondsLeft(30 * 60);
    setJustSubmittedType(null);
    if (tab === 'pre' && !preTest) {
      setIsExamActive(true);
    } else if (tab === 'post' && canTakePostTest && !postTest) {
      setIsExamActive(true);
    } else {
      setIsExamActive(false);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentUser.id, initialMode]);

  const handleSubmitExam = () => {
    let correct = 0;
    PRE_POST_TEST_QUESTIONS.forEach((q, idx) => {
      if (selectedAnswers[idx] === q.correctIndex) {
        correct += 1;
      }
    });
    const score = Math.round((correct / PRE_POST_TEST_QUESTIONS.length) * 100);
    savePrePostTest({
      userId: currentUser.id,
      tenantId: currentTenant.id,
      type: activeTab,
      score,
      completedAt: new Date().toISOString(),
    });
    setIsExamActive(false);
    setJustSubmittedType(activeTab);
  };

  // Live 30-minute countdown timer
  useEffect(() => {
    if (!isExamActive) return;
    const timer = setInterval(() => {
      setSecondsLeft((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmitExam();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isExamActive, activeTab, selectedAnswers]);

  const startExam = (type: 'pre' | 'post') => {
    if (type === 'pre' && preTest) {
      return;
    }
    setActiveTab(type);
    setSelectedAnswers({});
    setActiveQuestionIdx(0);
    setSecondsLeft(30 * 60);
    setJustSubmittedType(null);
    setIsExamActive(true);
  };

  const switchTab = (tab: 'pre' | 'post') => {
    setActiveTab(tab);
    setSelectedAnswers({});
    setActiveQuestionIdx(0);
    setSecondsLeft(30 * 60);
    setJustSubmittedType(null);
    if (tab === 'pre' && !preTest) {
      setIsExamActive(true);
    } else if (tab === 'post' && canTakePostTest && !postTest) {
      setIsExamActive(true);
    } else {
      setIsExamActive(false);
    }
  };

  const formatTimer = (sec: number): string => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  };

  const answeredCount = Object.keys(selectedAnswers).length;
  const currentQuestion = PRE_POST_TEST_QUESTIONS[activeQuestionIdx] || PRE_POST_TEST_QUESTIONS[0];

  const t1Diff = preTest && postTest ? postTest.score - preTest.score : null;
  const t1Pct =
    preTest && postTest && preTest.score > 0
      ? (((postTest.score - preTest.score) / preTest.score) * 100).toFixed(1)
      : null;

  const firstMissionCode = trackMissions[0]?.code || 'IPA-01';

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-[#1e293b]">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
            Pre-Test &amp; Post-Test Evaluasi Kompetensi (L4a)
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Peserta Aktif: <strong className="text-sky-400">{currentUser.fullName}</strong> ({currentUser.username}) · Jalur {trackLabel} ({trackMissions.length} Misi) · Metrik T1 (PRD §3 &amp; §11)
          </p>
        </div>
        <button
          onClick={onBack}
          className="px-3.5 py-1.5 rounded-xl border border-[#334155] bg-[#1e293b]/70 hover:bg-[#1e293b] text-slate-300 hover:text-white text-xs font-semibold flex items-center gap-1.5 transition-all w-fit cursor-pointer"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Kembali ke Beranda</span>
        </button>
      </div>

      {/* Metric T1 Banner */}
      <div className="p-4 rounded-xl bg-purple-950/20 border border-purple-500/40 text-xs flex flex-col md:flex-row md:items-center justify-between gap-3 shadow-md">
        <div>
          <div className="font-bold text-purple-300 uppercase tracking-wider text-[11px] mb-0.5">
            METRIK KEBERHASILAN T1 (PRD §3): FORMULA KENAIKAN KOMPETENSI PELATIHAN
          </div>
          <div className="text-slate-300 font-mono text-xs">
            Peningkatan Nilai (%) = ((Post − Pre) ÷ Pre) × 100% ·{' '}
            <span className="text-emerald-400 font-semibold font-sans">
              Target PRD: Kenaikan ≥ 25% · KKM Post-Test: ≥ 70
            </span>
          </div>
        </div>
        <div className="flex items-center gap-2 shrink-0">
          <button
            onClick={() => switchTab('pre')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'pre'
                ? 'bg-sky-600 text-white shadow-sm'
                : 'bg-[#1e293b] text-slate-300 hover:text-white'
            }`}
          >
            Pre-Test {preTest ? `(${preTest.score})` : '(Wajib)'}
          </button>
          <button
            onClick={() => switchTab('post')}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === 'post'
                ? 'bg-emerald-600 text-white shadow-sm'
                : 'bg-[#1e293b] text-slate-300 hover:text-white'
            }`}
          >
            Post-Test {postTest ? `(${postTest.score})` : canTakePostTest ? '(Aktif)' : '(Terkunci)'}
          </button>
        </div>
      </div>

      {/* Submission Confirmation Banner */}
      {justSubmittedType && (
        <div className="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/50 text-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2.5">
            <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
            <div>
              <div className="font-bold text-emerald-300">
                {justSubmittedType === 'pre'
                  ? `Pre-Test Berhasil Disimpan! Nilai Awal (T1): ${preTest?.score ?? 0} / 100`
                  : `Post-Test Berhasil Disimpan! Nilai Akhir: ${postTest?.score ?? 0} / 100`}
              </div>
              <div className="text-slate-300 mt-0.5">
                {justSubmittedType === 'pre'
                  ? `Misi pertama ${firstMissionCode} sekarang sudah terbuka dan siap dikerjakan.`
                  : (postTest?.score ?? 0) >= 70
                  ? 'Selamat! Anda memenuhi nilai minimal Post-Test (≥ 70) untuk syarat kelulusan.'
                  : 'Nilai Post-Test belum mencapai KKM 70. Anda dapat mengulang Post-Test.'}
              </div>
            </div>
          </div>
          {justSubmittedType === 'pre' && onStartFirstMission && (
            <button
              onClick={() => onStartFirstMission(firstMissionCode)}
              className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs shrink-0 cursor-pointer"
            >
              Mulai Misi {firstMissionCode} →
            </button>
          )}
        </div>
      )}

      {/* Main 12-Column Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* LEFT COLUMN (4 cols): User Pre-Test Status Card */}
        <div className="lg:col-span-4 bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
          <div className="flex items-center justify-between pb-2 border-b border-[#1e293b]">
            <div>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-500/20 text-amber-400 uppercase tracking-wider">
                Tahap Awal (T1)
              </span>
              <h2 className="text-sm font-bold text-white mt-1.5">Pre-Test Diagnostik Awal</h2>
              <p className="text-[11px] text-slate-400">
                Peserta: {currentUser.fullName} ({currentUser.username})
              </p>
            </div>
          </div>

          <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] flex items-center justify-between">
            <div>
              <div className="text-[10px] text-slate-400">Skor Baseline Kompetensi Awal:</div>
              <div className="text-2xl font-black text-amber-400 mt-0.5 font-mono">
                {preTest ? (
                  <>
                    {preTest.score} <span className="text-sm font-normal text-slate-400">/ 100</span>
                  </>
                ) : (
                  <span className="text-base font-bold text-amber-300">Belum dikerjakan</span>
                )}
              </div>
            </div>
            <span className="text-[11px] text-slate-500 font-mono">
              {preTest
                ? new Date(preTest.completedAt).toLocaleDateString('id-ID', {
                    day: '2-digit',
                    month: 'short',
                    year: 'numeric',
                  })
                : 'Wajib'}
            </span>
          </div>

          {preTest ? (
            <div className="space-y-3 text-xs pt-1">
              <div className="p-3.5 rounded-xl bg-sky-950/20 border border-sky-500/20 text-[11px] text-slate-300 space-y-1">
                <span className="text-[10px] text-sky-400 font-bold uppercase tracking-wider block">
                  Status Nilai Awal T1 (Terkunci · 1 Kali):
                </span>
                <p className="leading-relaxed">
                  Nilai Pre-Test sebesar <strong className="text-white">{preTest.score}/100</strong> telah tersimpan permanen sebagai titik awal (baseline) perhitungan kenaikan kompetensi T1 di dasbor lembaga (L14) dan tidak dapat dikerjakan ulang oleh peserta.
                </p>
              </div>
            </div>
          ) : (
            <div className="space-y-3 text-xs">
              <div className="p-3.5 rounded-xl bg-amber-950/20 border border-amber-500/30 text-[11px] text-amber-200 leading-relaxed">
                Anda belum mengerjakan Pre-Test. Selesaikan 20 soal di lembar uji sebelah kanan untuk membuka misi pertama{' '}
                <strong>{firstMissionCode}</strong>.
              </div>
              {!isExamActive && (
                <button
                  onClick={() => startExam('pre')}
                  className="w-full py-2.5 px-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs flex items-center justify-center gap-1.5 cursor-pointer"
                >
                  <Play className="w-3.5 h-3.5" />
                  <span>Mulai Pre-Test Sekarang</span>
                </button>
              )}
            </div>
          )}
        </div>

        {/* CENTER COLUMN (5 cols): Interactive 20-Question Exam OR Exam Summary */}
        <div className="lg:col-span-5 bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
          <div className="flex items-center justify-between pb-2 border-b border-[#1e293b] gap-2">
            <div>
              <h2 className="text-sm font-bold text-white">
                {activeTab === 'pre'
                  ? 'Lembar Uji Pre-Test (20 Soal)'
                  : 'Lembar Uji Post-Test (20 Soal)'}
              </h2>
              <p className="text-[11px] text-slate-400">
                20 Soal Pilihan Ganda · Batas Waktu 30 Menit · Terjawab {answeredCount}/20
              </p>
            </div>
            <div className="px-2.5 py-1 rounded-lg bg-sky-950/50 border border-sky-500/40 text-sky-400 text-xs font-mono font-bold flex items-center gap-1 shrink-0">
              <Clock className="w-3.5 h-3.5" />
              <span>{isExamActive ? `${formatTimer(secondsLeft)} Tersisa` : '30:00'}</span>
            </div>
          </div>

          {isExamActive ? (
            <>
              {/* Active Question Card */}
              <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-3">
                <div className="flex items-center justify-between text-[10px] font-bold text-sky-400 uppercase tracking-wider">
                  <span>
                    SOAL NO. {activeQuestionIdx + 1} DARI {PRE_POST_TEST_QUESTIONS.length} ·{' '}
                    {currentQuestion.category}
                  </span>
                </div>
                <p className="text-xs font-semibold text-white leading-relaxed">
                  {currentQuestion.question}
                </p>

                <div className="space-y-2 pt-1 text-xs">
                  {currentQuestion.options.map((opt, oIdx) => {
                    const isSelected = selectedAnswers[activeQuestionIdx] === oIdx;
                    return (
                      <button
                        key={oIdx}
                        type="button"
                        onClick={() =>
                          setSelectedAnswers((prev) => ({
                            ...prev,
                            [activeQuestionIdx]: oIdx,
                          }))
                        }
                        className={`w-full text-left p-2.5 rounded-xl border text-[11px] leading-snug transition-all flex items-center justify-between cursor-pointer ${
                          isSelected
                            ? 'bg-sky-950/50 border-sky-500 text-sky-200 font-semibold'
                            : 'border-[#1e293b] bg-[#1e293b]/30 hover:bg-[#1e293b] text-slate-300'
                        }`}
                      >
                        <span>{opt}</span>
                        {isSelected && <Check className="w-3.5 h-3.5 text-sky-400 shrink-0 ml-2" />}
                      </button>
                    );
                  })}
                </div>

                {/* Prev / Next Navigation */}
                <div className="flex items-center justify-between pt-2">
                  <button
                    type="button"
                    disabled={activeQuestionIdx === 0}
                    onClick={() => setActiveQuestionIdx((i) => Math.max(0, i - 1))}
                    className="px-3 py-1.5 rounded-lg bg-[#1e293b] hover:bg-[#334155] disabled:opacity-40 text-xs font-semibold text-slate-200 cursor-pointer"
                  >
                    ← Sebelumnya
                  </button>
                  <button
                    type="button"
                    disabled={activeQuestionIdx === PRE_POST_TEST_QUESTIONS.length - 1}
                    onClick={() =>
                      setActiveQuestionIdx((i) =>
                        Math.min(PRE_POST_TEST_QUESTIONS.length - 1, i + 1)
                      )
                    }
                    className="px-3 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 disabled:opacity-40 text-xs font-semibold text-white cursor-pointer"
                  >
                    Berikutnya →
                  </button>
                </div>
              </div>

              {/* 20-Question Navigator */}
              <div className="space-y-1.5 pt-1">
                <div className="text-[10px] text-slate-400 uppercase tracking-wider font-bold">
                  Navigator 20 Nomor Soal:
                </div>
                <div className="grid grid-cols-10 gap-1.5">
                  {PRE_POST_TEST_QUESTIONS.map((_, idx) => {
                    const isCurrent = idx === activeQuestionIdx;
                    const isAnswered = selectedAnswers[idx] !== undefined;
                    return (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => setActiveQuestionIdx(idx)}
                        className={`h-7 rounded-lg text-[11px] font-mono font-bold transition-all cursor-pointer ${
                          isCurrent
                            ? 'bg-sky-500 text-white ring-2 ring-sky-400/50'
                            : isAnswered
                            ? 'bg-emerald-600/30 text-emerald-400 border border-emerald-500/40'
                            : 'bg-[#1e293b] text-slate-400 border border-[#334155]'
                        }`}
                      >
                        {idx + 1}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Submit Button */}
              <div className="pt-2 border-t border-[#1e293b] space-y-2">
                <button
                  type="button"
                  onClick={handleSubmitExam}
                  className="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-md cursor-pointer"
                >
                  <ClipboardCheck className="w-4 h-4" />
                  <span>
                    Kumpulkan Jawaban {activeTab === 'pre' ? 'Pre-Test' : 'Post-Test'} ({answeredCount}/20 Terjawab)
                  </span>
                </button>
              </div>
            </>
          ) : (
            <div className="p-5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-4 text-xs">
              {activeTab === 'pre' && preTest ? (
                <>
                  <div className="flex items-center gap-2 text-emerald-400 font-bold text-sm">
                    <CheckCircle2 className="w-5 h-5" />
                    <span>Pre-Test Sudah Diselesaikan</span>
                  </div>
                  <p className="text-slate-300 leading-relaxed">
                    Anda telah menyelesaikan Pre-Test Diagnostik dengan skor{' '}
                    <strong className="text-white">{preTest.score} / 100</strong>. Nilai awal (T1) hanya dikerjakan satu kali dan terkunci; reset hanya dapat dilakukan melalui Reset Data Demo atau oleh Admin Lembaga.
                  </p>
                  {onStartFirstMission && passedCount === 0 && (
                    <div className="flex flex-wrap gap-2">
                      <button
                        onClick={() => onStartFirstMission(firstMissionCode)}
                        className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold cursor-pointer"
                      >
                        Mulai Misi {firstMissionCode} →
                      </button>
                    </div>
                  )}
                </>
              ) : activeTab === 'post' && !canTakePostTest ? (
                <>
                  <div className="flex items-center gap-2 text-amber-400 font-bold text-sm">
                    <Lock className="w-5 h-5" />
                    <span>Post-Test Kelulusan Masih Terkunci</span>
                  </div>
                  <p className="text-slate-300 leading-relaxed">
                    Sesuai aturan FR-09, Post-Test hanya terbuka setelah seluruh misi wajib pada jalur{' '}
                    <strong>{trackLabel}</strong> ({trackMissions.length} misi) lulus dan Misi Kelulusan{' '}
                    <strong>{gradMissionCode}</strong> mencapai skor ≥ {gradThreshold}.
                  </p>
                  <div className="p-3 rounded-lg bg-[#0f172a] border border-[#1e293b] space-y-1 text-[11px]">
                    <div className={preTest ? 'text-emerald-400' : 'text-slate-400'}>
                      {preTest ? '✓' : '○'} Pre-Test Awal: {preTest ? `Selesai (${preTest.score})` : 'Belum selesai'}
                    </div>
                    <div className={allMissionsPassed ? 'text-emerald-400' : 'text-slate-400'}>
                      {allMissionsPassed ? '✓' : '○'} Misi Jalur {trackLabel}: {passedCount} / {trackMissions.length} Lulus
                    </div>
                    <div className={gradPassed ? 'text-emerald-400' : 'text-slate-400'}>
                      {gradPassed ? '✓' : '○'} Misi Kelulusan {gradMissionCode} (≥ {gradThreshold}):{' '}
                      {gradResult ? `Skor ${gradResult.totalScore}` : 'Belum dikerjakan'}
                    </div>
                  </div>
                </>
              ) : (
                <>
                  <div className="flex items-center gap-2 text-emerald-400 font-bold text-sm">
                    <CheckCircle2 className="w-5 h-5" />
                    <span>
                      {postTest ? `Post-Test Selesai · Skor ${postTest.score} / 100` : 'Post-Test Terbuka'}
                    </span>
                  </div>
                  <p className="text-slate-300 leading-relaxed">
                    {postTest
                      ? 'Perbandingan nilai Pre-Test vs Post-Test Anda tercatat di panel hasil sebelah kanan.'
                      : 'Semua syarat terpenuhi! Klik tombol di bawah untuk memulai ujian Post-Test (20 soal, 30 menit, KKM ≥ 70).'}
                  </p>
                  <button
                    onClick={() => startExam('post')}
                    className="px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold cursor-pointer"
                  >
                    {postTest ? 'Kerjakan Ulang Post-Test' : 'Mulai Post-Test Sekarang →'}
                  </button>
                </>
              )}
            </div>
          )}
        </div>

        {/* RIGHT COLUMN (3 cols): Post-Test Results & Comparison Pre vs Post */}
        <div className="lg:col-span-3 bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
          <div className="flex items-center justify-between pb-2 border-b border-[#1e293b]">
            <div>
              <span
                className={`text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider ${
                  postTest
                    ? 'bg-emerald-500/20 text-emerald-400'
                    : canTakePostTest
                    ? 'bg-purple-500/20 text-purple-300'
                    : 'bg-slate-800 text-slate-400'
                }`}
              >
                Pasca Pelatihan
              </span>
              <h2 className="text-sm font-bold text-white mt-1.5">Post-Test &amp; Perbandingan T1</h2>
              <p className="text-[11px] text-slate-400">
                Peserta: {currentUser.fullName}
              </p>
            </div>
          </div>

          <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] flex items-center justify-between gap-2">
            <div>
              <div className="text-[10px] text-slate-400">Capaian Post-Test Akhir:</div>
              <div className="text-2xl font-black text-emerald-400 mt-0.5 font-mono">
                {postTest ? (
                  <>
                    {postTest.score} <span className="text-sm font-normal text-slate-400">/ 100</span>
                  </>
                ) : (
                  <span className="text-sm font-bold text-slate-400">
                    {canTakePostTest ? 'Siap Ujian' : 'Terkunci'}
                  </span>
                )}
              </div>
            </div>
            {postTest && (
              <span
                className={`text-[10px] font-bold px-2 py-0.5 rounded-md border ${
                  postTest.score >= 70
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'
                    : 'bg-rose-500/20 text-rose-300 border-rose-500/30'
                }`}
              >
                {postTest.score >= 70 ? 'Lulus (≥70)' : 'Belum Lulus'}
              </span>
            )}
          </div>

          {/* Metric T1 Result Card */}
          <div className="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/30 space-y-2 text-xs">
            <span className="text-[10px] text-emerald-400 font-bold uppercase tracking-wider block">
              Perbandingan Pre-Test vs Post-Test (T1):
            </span>
            <div className="flex items-center justify-between text-[11px] font-mono text-slate-300">
              <span>
                Pre-Test: <strong className="text-white">{preTest ? preTest.score : '–'}</strong>
              </span>
              <span>
                Post-Test: <strong className="text-emerald-400">{postTest ? postTest.score : '–'}</strong>
              </span>
            </div>
            {t1Diff !== null && t1Pct !== null ? (
              <>
                <div className="text-xs font-bold text-emerald-300">
                  Kenaikan: {t1Diff >= 0 ? `+${t1Diff}` : t1Diff} Poin ({Number(t1Pct) >= 0 ? `+${t1Pct}` : t1Pct}%)
                </div>
                <div className="py-1 px-2 rounded-lg bg-emerald-500/20 text-emerald-300 text-[10px] font-bold text-center border border-emerald-500/30">
                  {Number(t1Pct) >= 25
                    ? `✓ MELEBIHI TARGET PRD T1 (+${t1Pct}% > 25%)`
                    : `Target PRD T1: ≥ 25%`}
                </div>
              </>
            ) : (
              <div className="text-[11px] text-slate-400">
                Perbandingan T1 akan muncul setelah Pre-Test dan Post-Test diselesaikan.
              </div>
            )}
          </div>

          {/* 4 Checklist Criteria */}
          <div className="space-y-1.5 text-[11px] pt-1">
            <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
              Status Verifikasi Syarat Piagam:
            </div>
            <div className={`${allMissionsPassed ? 'text-emerald-400' : 'text-slate-400'} flex items-center gap-1.5`}>
              <span>{allMissionsPassed ? '✓' : '○'}</span>
              <span>
                {trackMissions.length} Misi Jalur {trackLabel}: {passedCount}/{trackMissions.length}{' '}
                {allMissionsPassed ? 'Selesai' : 'Lulus'}
              </span>
            </div>
            <div className={`${gradPassed ? 'text-emerald-400' : 'text-slate-400'} flex items-center gap-1.5`}>
              <span>{gradPassed ? '✓' : '○'}</span>
              <span>
                Misi Kelulusan {gradMissionCode}:{' '}
                {gradResult ? `Skor ${gradResult.totalScore} (KKM ≥ ${gradThreshold})` : 'Belum selesai'}
              </span>
            </div>
            <div
              className={`${
                postTest && postTest.score >= 70 ? 'text-emerald-400' : 'text-slate-400'
              } flex items-center gap-1.5`}
            >
              <span>{postTest && postTest.score >= 70 ? '✓' : '○'}</span>
              <span>
                Post-Test Akhir: {postTest ? `${postTest.score} / 100` : 'Belum dikerjakan'} (KKM ≥ 70)
              </span>
            </div>
            <div className={`${validCert ? 'text-emerald-400' : 'text-slate-400'} flex items-center gap-1.5`}>
              <span>{validCert ? '✓' : '○'}</span>
              <span>
                {validCert
                  ? `Piagam ${validCert.certificateNumber}: TERBIT (${validCert.operatorLevel})`
                  : 'Piagam: Belum Terbit'}
              </span>
            </div>
          </div>

          {validCert && (
            <button
              onClick={onViewCertificate}
              className="w-full py-2.5 px-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-1.5 shadow-md shadow-sky-950/50 cursor-pointer"
            >
              <FileCheck2 className="w-3.5 h-3.5" />
              <span>Lihat Piagam Saya (L8) →</span>
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

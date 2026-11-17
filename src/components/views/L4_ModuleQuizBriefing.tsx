/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useMemo, useState } from 'react';
import { Mission } from '../../types';
import { useApp } from '../../context/AppContext';
import { shuffleQuizQuestions } from '../../utils/gamification';
import {
  ArrowLeft,
  Check,
  CheckCircle2,
  ClipboardCheck,
  Info,
  Lock,
} from 'lucide-react';

interface ModuleQuizProps {
  mission: Mission;
  onStartSimulation: () => void;
  onBack: () => void;
}

export const L4_ModuleQuizBriefing: React.FC<ModuleQuizProps> = ({
  mission,
  onStartSimulation,
  onBack,
}) => {
  const { currentUser, getBestMissionResult, showTechnicalRefs } = useApp();
  const existingResult = currentUser
    ? getBestMissionResult(currentUser.id, mission.code)
    : undefined;
  const alreadyPassedMission = Boolean(existingResult && existingResult.isPassed);

  const shuffledQuiz = useMemo(
    () => shuffleQuizQuestions(mission.quiz),
    [mission.code, currentUser?.id]
  );

  const buildPassedAnswers = (): Record<number, string> => {
    const map: Record<number, string> = {};
    shuffledQuiz.forEach((q, idx) => {
      map[idx] = q.correctOptionId;
    });
    return map;
  };

  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, string>>(() =>
    alreadyPassedMission ? buildPassedAnswers() : {}
  );
  const [isQuizSubmitted, setIsQuizSubmitted] = useState<boolean>(alreadyPassedMission);
  const [quizScore, setQuizScore] = useState<number>(alreadyPassedMission ? 100 : 0);

  useEffect(() => {
    if (alreadyPassedMission) {
      setSelectedAnswers(buildPassedAnswers());
      setIsQuizSubmitted(true);
      setQuizScore(100);
    } else {
      setSelectedAnswers({});
      setIsQuizSubmitted(false);
      setQuizScore(0);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mission.code, currentUser?.id, shuffledQuiz]);

  const handleSelectOption = (qIdx: number, optId: string) => {
    setSelectedAnswers((prev) => ({ ...prev, [qIdx]: optId }));
    if (isQuizSubmitted) {
      setIsQuizSubmitted(false);
    }
  };

  const handleEvaluateQuiz = () => {
    let correct = 0;
    shuffledQuiz.forEach((q, idx) => {
      if (selectedAnswers[idx] === q.correctOptionId) {
        correct += 1;
      }
    });
    const score = Math.round((correct / Math.max(1, shuffledQuiz.length)) * 100);
    setQuizScore(score);
    setIsQuizSubmitted(true);
  };

  const correctCount = shuffledQuiz.filter(
    (q, idx) => selectedAnswers[idx] === q.correctOptionId
  ).length;
  const isGatePassed = isQuizSubmitted && quizScore >= 60;
  const allAnswered = Object.keys(selectedAnswers).length === shuffledQuiz.length;

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Top Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-[#1e293b]">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
            Modul Materi &amp; Kuis Pra-Misi
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Misi {mission.code}: {mission.name} ({mission.levelName})
            {showTechnicalRefs ? ' · PRD §7, §9' : ''}
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

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* LEFT COLUMN: Materi Teori & SOP Penanganan */}
        <div className="lg:col-span-7 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">
              Materi Teori &amp; SOP: {mission.name}
            </h2>
            <p className="text-xs text-slate-400">
              Standar Pengolahan Fisik-Kimia &amp; Distribusi Air Minum (Permenkes No. 2/2023 &amp; SNI 6774:2008)
            </p>
          </div>

          {/* Skenario Box */}
          <div className="p-4 rounded-xl bg-sky-950/30 border border-sky-500/30 text-xs space-y-1.5">
            <span className="text-[10px] text-sky-400 font-bold uppercase tracking-wider block">
              Ringkasan Skenario Misi {mission.code}
              {showTechnicalRefs ? ' (PRD §7)' : ''}:
            </span>
            <p className="text-slate-200 leading-relaxed text-[11px]">
              {mission.briefing.situation}
            </p>
            <p className="text-sky-300 leading-relaxed text-[11px] font-semibold">
              Tujuan: {mission.briefing.objective}
            </p>
          </div>

          {/* 3 SOP Poin & Ambang Batas Kritis */}
          <div>
            <div className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">
              Poin SOP &amp; Ambang Batas Operasional Kritis (Permenkes No. 2/2023):
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Batas Kekeruhan Air Olahan</div>
                <div className="text-base font-extrabold text-rose-400 mt-0.5">&lt; 3,0 NTU</div>
                <div className="text-[9px] text-slate-500 mt-1">≥ 3 NTU: Alarm Tinggi</div>
              </div>

              <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Rentang Aman pH &amp; Klorin</div>
                <div className="text-base font-extrabold text-emerald-400 mt-0.5">6,5–8,5 | 0,2–0,5</div>
                <div className="text-[9px] text-slate-500 mt-1">Koreksi pH &amp; Sisa Klor (mg/L)</div>
              </div>

              <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                <div className="text-[10px] text-slate-400">Ambang Lulus Misi {mission.code}</div>
                <div className="text-base font-extrabold text-amber-400 mt-0.5">
                  Skor ≥ {mission.passScore}
                </div>
                <div className="text-[9px] text-slate-500 mt-1">
                  Batas Waktu: {(() => {
                    const sec = mission.durationLimitSec || 300;
                    const mins = Math.floor(sec / 60);
                    const rem = sec % 60;
                    const mmss = `${String(mins).padStart(2, '0')}:${String(rem).padStart(2, '0')}`;
                    return rem === 0 ? `${mins} Menit (${mmss})` : `${mins} Menit ${rem} Detik (${mmss})`;
                  })()}
                </div>
              </div>
            </div>
          </div>

          {/* SOP Resmi */}
          {mission.code === 'IPA-06' ? (
            <div className="space-y-2">
              <div className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Langkah Standar Operasional Prosedur (SOP Penanganan Lonjakan Kekeruhan):
              </div>
              <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-[11px] text-slate-300 leading-relaxed font-mono">
                <p>1. <span className="text-sky-300 font-bold">Akui Alarm (ACK):</span> Segera tekan tombol Akui begitu alarm "Kekeruhan Air Baku Tinggi" muncul di HMI.</p>
                <p>2. <span className="text-sky-300 font-bold">Buka Panel Koagulasi:</span> Klik titik kontrol Flash Mixer Koagulasi di diagram mimic HMI.</p>
                <p>3. <span className="text-sky-300 font-bold">Naikkan Dosis Koagulan:</span> Sesuaikan setpoint dosis PAC dari 20 mg/L ke 48 mg/L sesuai kurva jar-test.</p>
                <p>4. <span className="text-sky-300 font-bold">Koreksi pH Air:</span> Pastikan dosis penyesuai pH aktif agar pH bertahan stabil di angka 7,20.</p>
                <p>5. <span className="text-sky-300 font-bold">Turunkan Debit Intake (Opsional):</span> Jika flok lambat mengendap, kurangi debit dari 100 L/s ke 75 L/s.</p>
                <p>6. <span className="text-sky-300 font-bold">Pantau Bak Sedimentasi &amp; Filtrasi:</span> Awasi kekeruhan keluar sedimentasi dan kenaikan headloss filter.</p>
                <p>7. <span className="text-sky-300 font-bold">Verifikasi Pemulihan:</span> Alarm akan auto-clear saat kekeruhan air olahan &lt;2,7 NTU stabil 10 detik.</p>
              </div>
            </div>
          ) : (
            <div className="space-y-2">
              <div className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Fokus Pelatihan &amp; Arahan Instruktur Misi {mission.code}:
              </div>
              <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-[11px] text-slate-300 leading-relaxed">
                <p><strong className="text-sky-300">Fokus Kompetensi:</strong> {mission.trainingFocus}</p>
                <p className="italic text-slate-400">{mission.briefing.mentorQuote}</p>
              </div>
            </div>
          )}

          <div className="p-3 rounded-xl bg-[#1e293b]/50 border border-[#334155] text-[11px] text-slate-400 flex items-center gap-2">
            <Info className="w-4 h-4 text-sky-400 shrink-0" />
            <span>
              Catatan: Membuka narasi titik kontrol (&quot;i&quot;) kapan saja <strong>TIDAK mengurangi skor</strong>
              {showTechnicalRefs ? ' (PRD §9)' : ''}.
            </span>
          </div>
        </div>

        {/* RIGHT COLUMN: Kuis Pra-Misi (5 Soal Kunci) */}
        <div className="lg:col-span-5 bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 space-y-5 shadow-lg">
          <div>
            <h2 className="text-base font-bold text-white">
              Kuis Pra-Misi ({mission.quiz.length} Soal Kunci)
            </h2>
            <p className="text-xs text-slate-400">
              Syarat Gerbang: Nilai Kuis ≥ 60 membuka Simulator · Nilai kuis memberi bonus +80 XP
            </p>
          </div>

          {/* Status Kuis Gerbang Box */}
          <div
            className={`p-3.5 rounded-xl border text-xs flex items-center justify-between ${
              isGatePassed
                ? 'bg-emerald-950/30 border-emerald-500/40 text-emerald-300'
                : isQuizSubmitted
                ? 'bg-rose-950/30 border-rose-500/40 text-rose-300'
                : 'bg-amber-950/20 border-amber-500/40 text-amber-300'
            }`}
          >
            <div>
              <div className="font-bold flex items-center gap-1.5 text-xs">
                {isGatePassed ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                ) : (
                  <Lock className="w-4 h-4 text-amber-400" />
                )}
                <span>
                  {isGatePassed
                    ? `STATUS KUIS: LULUS GERBANG (NILAI: ${quizScore} / 100)`
                    : isQuizSubmitted
                    ? `BELUM LULUS GERBANG (NILAI: ${quizScore} / 100)`
                    : `JAWAB ${mission.quiz.length} SOAL UNTUK MEMBUKA SIMULATOR`}
                </span>
              </div>
              <div className="text-[10px] text-slate-400 mt-0.5">
                {isQuizSubmitted
                  ? `${correctCount} dari ${mission.quiz.length} Soal Benar`
                  : `Terjawab ${Object.keys(selectedAnswers).length} dari ${mission.quiz.length} soal`}
              </div>
            </div>
            <span
              className={`text-xs font-mono font-bold px-2.5 py-1 rounded-lg border ${
                isGatePassed
                  ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'
                  : 'bg-slate-800 text-slate-300 border-slate-700'
              }`}
            >
              SYARAT ≥ 60
            </span>
          </div>

          {/* Quiz Questions List */}
          <div className="space-y-4 max-h-[460px] overflow-y-auto pr-1">
            {shuffledQuiz.map((q, qIdx) => {
              const selectedOptId = selectedAnswers[qIdx];
              return (
                <div
                  key={q.id}
                  className="p-3.5 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-2 text-xs"
                >
                  <div className="font-bold text-white text-[11px] leading-snug">
                    SOAL {qIdx + 1} DARI {shuffledQuiz.length} · {q.question}
                  </div>
                  <div className="space-y-1.5 pt-1">
                    {q.options.map((opt, optIdx) => {
                      const isChosen = selectedOptId === opt.id;
                      const isCorrectAnswer = opt.id === q.correctOptionId;
                      const optionLabel = ['A', 'B', 'C', 'D'][optIdx] || String(optIdx + 1);
                      return (
                        <button
                          key={opt.id}
                          type="button"
                          onClick={() => handleSelectOption(qIdx, opt.id)}
                          className={`w-full text-left p-2 rounded-lg border text-[11px] transition-all flex items-center justify-between cursor-pointer ${
                            isQuizSubmitted && isChosen && isCorrectAnswer
                              ? 'bg-emerald-950/40 border-emerald-500 text-emerald-300 font-semibold'
                              : isQuizSubmitted && isChosen && !isCorrectAnswer
                              ? 'bg-rose-950/40 border-rose-500 text-rose-300 font-semibold'
                              : isQuizSubmitted && isCorrectAnswer
                              ? 'border-emerald-500/40 text-emerald-400'
                              : isChosen
                              ? 'bg-sky-950/50 border-sky-500 text-sky-200 font-semibold'
                              : 'border-[#1e293b] bg-[#1e293b]/30 hover:bg-[#1e293b] text-slate-300'
                          }`}
                        >
                          <span>{optionLabel}. {opt.text}</span>
                          {isQuizSubmitted && isChosen && isCorrectAnswer && (
                            <Check className="w-3.5 h-3.5 text-emerald-400 shrink-0 ml-1" />
                          )}
                        </button>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Action Buttons */}
          <div className="space-y-2 pt-2 border-t border-[#1e293b]">
            {!isGatePassed && (
              <button
                type="button"
                onClick={handleEvaluateQuiz}
                disabled={!allAnswered}
                className={`w-full py-2.5 px-4 rounded-xl font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 ${
                  allAnswered
                    ? 'bg-amber-500 hover:bg-amber-400 text-slate-950 cursor-pointer shadow-sm'
                    : 'bg-slate-800 text-slate-500 border border-slate-700 cursor-not-allowed'
                }`}
              >
                <ClipboardCheck className="w-4 h-4" />
                <span>
                  {allAnswered
                    ? 'Kirim & Nilai Kuis Pra-Misi'
                    : `Jawab Semua Soal (${Object.keys(selectedAnswers).length}/${mission.quiz.length})`}
                </span>
              </button>
            )}

            <button
              onClick={onStartSimulation}
              disabled={!isGatePassed}
              className={`w-full py-3 px-4 rounded-xl font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-md ${
                isGatePassed
                  ? 'bg-sky-600 hover:bg-sky-500 text-white shadow-sky-950/50 cursor-pointer'
                  : 'bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700'
              }`}
            >
              <span>Mulai Simulator SCADA ({mission.code}) →</span>
            </button>
            <p className="text-[10px] text-center text-slate-500">
              {isGatePassed
                ? 'Gerbang kuis telah terpenuhi. Sesi simulator siap dibuka.'
                : 'Selesaikan kuis pra-misi dengan nilai ≥ 60 untuk membuka simulator.'}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

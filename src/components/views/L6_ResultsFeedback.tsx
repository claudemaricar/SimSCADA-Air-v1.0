/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useEffect, useMemo } from 'react';
import { Mission, MissionResult } from '../../types';
import { useApp } from '../../context/AppContext';
import confetti from 'canvas-confetti';
import {
  Award,
  History,
  Home,
  Sparkles,
  Zap,
} from 'lucide-react';
import { scadaAudio } from '../../utils/audio';
import { formatSimTime } from '../../engine/simulationEngine';
import {
  computeMissionXP,
  computeStarsFromScore,
  formatNumberID,
  getMissionDifficultyMultiplier,
} from '../../utils/gamification';

interface ResultsFeedbackProps {
  mission: Mission;
  result: MissionResult;
  onRetry: () => void;
  onNextMission: () => void;
  onBackToHome: () => void;
  onViewBadges?: () => void;
}

export const L6_ResultsFeedback: React.FC<ResultsFeedbackProps> = ({
  mission,
  result,
  onRetry,
  onNextMission,
  onBackToHome,
  onViewBadges,
}) => {
  const {
    currentUser,
    activeTrack,
    getMissionsForTrack,
    getUserOperatorLevel,
    setCurrentView,
    setReplayUserId,
    userBadges,
    showTechnicalRefs,
  } = useApp();
  const participantFirstName = currentUser?.fullName?.split(/\s+/)[0] || 'Operator';

  useEffect(() => {
    if (result.isPassed) {
      scadaAudio.playSuccessFanfare();
      try {
        confetti({
          particleCount: 70,
          spread: 60,
          origin: { y: 0.6 },
        });
      } catch {}
    }
  }, [result.isPassed]);

  const operatorLevel = getUserOperatorLevel(result.userId);
  const myBadgeCount = (userBadges[result.userId] || []).length;

  const displayScore = result.totalScore;
  const passScore = mission.passScore || 70;
  const isPassed = result.isPassed && displayScore >= passScore;
  const displayStars = computeStarsFromScore(displayScore, passScore);
  const multiplier = getMissionDifficultyMultiplier(mission);
  const displayXP = computeMissionXP(mission, displayScore, isPassed);
  const scoreTindakan = result.scoreTindakan;
  const scoreWaktu = result.scoreWaktuRespons;
  const scoreStabilitas = result.scoreStabilitas;
  const scoreAlarm = result.scoreAlarm;

  const trackMissions = getMissionsForTrack(result.track || currentUser?.track || activeTrack);
  const currentIdx = trackMissions.findIndex((m) => m.code === mission.code);
  const nextMission = currentIdx >= 0 && currentIdx < trackMissions.length - 1 ? trackMissions[currentIdx + 1] : null;

  const isTimedOutExam =
    mission.level === 5 && !isPassed && result.durationSec >= (mission.durationLimitSec || 600);

  // Merge alarm events and operator action logs chronologically
  const timelineEvents = useMemo(() => {
    const items: Array<{ timeSec: number; text: string; tone: string }> = [];

    result.alarmLogs.forEach((a) => {
      items.push({
        timeSec: a.timestampSec,
        text: `Alarm ${a.priority.toUpperCase()} (${a.controlPointName}): ${a.message} [${
          a.status === 'clear' ? `Clear (${a.clearMethod || 'auto'})` : a.status
        }]`,
        tone: a.priority === 'kritis' ? 'text-rose-400' : a.priority === 'tinggi' ? 'text-amber-400' : 'text-sky-300',
      });
    });

    result.actionLogs.forEach((l) => {
      items.push({
        timeSec: l.timestampSec,
        text: `[${l.controlPointId}] ${l.action}${l.value !== undefined ? ` (${l.value})` : ''}`,
        tone: l.isCorrect === false ? 'text-rose-400 font-bold' : 'text-emerald-400',
      });
    });

    items.sort((a, b) => a.timeSec - b.timeSec);
    return items;
  }, [result.alarmLogs, result.actionLogs]);

  const correctActionCount = result.actionLogs.filter((a) => a.isCorrect !== false).length;
  const clearedAlarmsCount = result.alarmLogs.filter((a) => a.status === 'clear').length;

  return (
    <div className="max-w-[1720px] mx-auto px-4 sm:px-6 py-6 font-sans text-slate-100 space-y-6">
      {/* Title */}
      <div className="pb-2 border-b border-[#1e293b]">
        <h1 className="text-xl sm:text-2xl font-bold text-white tracking-tight">
          Hasil Evaluasi Simulasi &amp; Umpan Balik Skor
        </h1>
        <p className="text-xs text-slate-400 mt-0.5">
          Misi {mission.code}: {mission.name}{showTechnicalRefs ? ' · PRD §8' : ''}
        </p>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">

        {/* LEFT COLUMN */}
        <div className="lg:col-span-8 space-y-6">

          {/* Main Score Hero Card */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-6 shadow-lg space-y-5">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 rounded-xl bg-[#0b1120] border border-[#1e293b]">
              <div>
                <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-bold">
                  SKOR KELULUSAN AKHIR SIMULASI{showTechnicalRefs ? ' (PRD §8)' : ''}:
                </span>
                <div className="flex items-center gap-3 mt-1">
                  <span className="text-4xl font-black text-white font-mono">
                    {displayScore} <span className="text-sm font-normal text-slate-400">/ 100</span>
                  </span>
                  <span
                    className={`px-3 py-1 rounded-xl font-bold text-xs border ${
                      isPassed
                        ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'
                        : 'bg-rose-500/20 text-rose-300 border-rose-500/30'
                    }`}
                  >
                    {isPassed
                      ? `LULUS (${displayStars}★ BINTANG)`
                      : isTimedOutExam
                      ? `TIDAK LULUS (WAKTU UJIAN HABIS · KKM ≥ ${passScore})`
                      : `BELUM LULUS (KKM ≥ ${passScore})`}
                  </span>
                </div>
                <div className="text-[11px] text-slate-400 mt-1">
                  Aturan Bintang: &lt;{passScore} Belum Lulus · {passScore}–84 (1★) ·{' '}
                  <strong className="text-amber-400">85–94 (2★)</strong> · ≥95 (3★)
                </div>
              </div>

              <div className="p-3 rounded-xl bg-purple-950/30 border border-purple-500/40 text-center shrink-0">
                <span className="text-[10px] text-purple-300 font-bold block uppercase tracking-wider">
                  XP DIPEROLEH ({formatNumberID(multiplier, 1)}x):
                </span>
                <span className="text-xl font-black text-amber-400 font-mono">
                  +{displayXP} XP
                </span>
              </div>
            </div>

            {/* Rincian 4 Komponen Penilaian Otomatis (PRD §8) */}
            <div className="space-y-2">
              <div className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Rincian 4 Komponen Penilaian Otomatis{showTechnicalRefs ? ' (PRD §8)' : ''}:
              </div>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <div className="text-[10px] text-slate-400">Ketepatan Tindakan (40%)</div>
                  <div className="text-xl font-black text-white mt-0.5 font-mono">
                    {scoreTindakan} <span className="text-xs font-normal text-slate-500">/ 40</span>
                  </div>
                  <div className="text-[9px] text-emerald-400 mt-1">
                    {result.actionLogs.length > 0
                      ? `${correctActionCount}/${result.actionLogs.length} aksi sesuai SOP`
                      : 'Tidak ada pelanggaran SOP'}
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <div className="text-[10px] text-slate-400">Waktu Respons (25%)</div>
                  <div className="text-xl font-black text-white mt-0.5 font-mono">
                    {scoreWaktu} <span className="text-xs font-normal text-slate-500">/ 25</span>
                  </div>
                  <div className="text-[9px] text-emerald-400 mt-1">
                    Durasi {formatSimTime(result.durationSec)} / {formatSimTime(mission.durationLimitSec || 300)}
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <div className="text-[10px] text-slate-400">Stabilitas Mutu (20%)</div>
                  <div className="text-xl font-black text-white mt-0.5 font-mono">
                    {scoreStabilitas} <span className="text-xs font-normal text-slate-500">/ 20</span>
                  </div>
                  <div className="text-[9px] text-sky-400 mt-1">
                    {Math.round((scoreStabilitas / 20) * 100)}% durasi di rentang aman
                  </div>
                </div>

                <div className="p-3 rounded-xl bg-[#0b1120] border border-[#1e293b]">
                  <div className="text-[10px] text-slate-400">Penanganan Alarm (15%)</div>
                  <div className="text-xl font-black text-white mt-0.5 font-mono">
                    {scoreAlarm} <span className="text-xs font-normal text-slate-500">/ 15</span>
                  </div>
                  <div className="text-[9px] text-cyan-400 mt-1">
                    {result.alarmLogs.length > 0
                      ? `${clearedAlarmsCount}/${result.alarmLogs.length} alarm clear`
                      : '0 alarm aktif saat selesai'}
                  </div>
                </div>
              </div>
            </div>

            {/* Log Kejadian Alarm (Snapshot Nilai Saat Kejadian) */}
            <div className="space-y-2">
              <div className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Log Kejadian Alarm &amp; Snapshot Nilai Saat Kejadian{showTechnicalRefs ? ' (PRD §10)' : ''}:
              </div>
              <div className="overflow-x-auto rounded-xl border border-[#1e293b] bg-[#0b1120]">
                <table className="w-full text-left text-[11px] text-slate-300">
                  <thead className="bg-[#0f172a] text-slate-400 text-[10px] uppercase tracking-wider border-b border-[#1e293b]">
                    <tr>
                      <th className="py-2 px-3">Waktu Kejadian</th>
                      <th className="py-2 px-3">Titik Kontrol &amp; Prioritas</th>
                      <th className="py-2 px-3">Pesan &amp; Nilai Saat Kejadian</th>
                      <th className="py-2 px-3">Waktu ACK</th>
                      <th className="py-2 px-3">Tindakan</th>
                      <th className="py-2 px-3">Waktu Clear</th>
                      <th className="py-2 px-3">Cara Clear</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#1e293b]">
                    {result.alarmLogs.length === 0 ? (
                      <tr>
                        <td colSpan={7} className="py-4 px-3 text-center text-slate-500">
                          Tidak ada kejadian alarm pada sesi ini.
                        </td>
                      </tr>
                    ) : (
                      result.alarmLogs.map((a) => (
                        <tr key={a.id} className="hover:bg-[#1e293b]/40">
                          <td className="py-2 px-3 font-mono text-slate-400 whitespace-nowrap">
                            {a.timestamp}
                          </td>
                          <td className="py-2 px-3">
                            <div className="font-semibold text-white">{a.controlPointName}</div>
                            <span
                              className={`text-[9px] font-bold uppercase ${
                                a.priority === 'kritis'
                                  ? 'text-rose-400'
                                  : a.priority === 'tinggi'
                                  ? 'text-amber-400'
                                  : 'text-sky-400'
                              }`}
                            >
                              {a.priority}
                            </span>
                          </td>
                          <td className="py-2 px-3">
                            <div className="text-slate-200">{a.message}</div>
                            {a.triggerSnapshotValue && (
                              <div className="text-[10px] font-mono text-sky-400">
                                Snapshot: {a.triggerSnapshotValue}
                              </div>
                            )}
                          </td>
                          <td className="py-2 px-3 font-mono text-sky-300 whitespace-nowrap">
                            {a.ackTimestamp || 'Belum ACK'}
                          </td>
                          <td className="py-2 px-3 text-slate-300">
                            {a.actionSummary || 'Belum ada tindakan koreksi tercatat'}
                          </td>
                          <td className="py-2 px-3 font-mono text-emerald-400 whitespace-nowrap">
                            {a.clearedTimestamp || (a.status === 'clear' ? 'Selesai' : '–')}
                          </td>
                          <td className="py-2 px-3 whitespace-nowrap">
                            {a.status === 'clear' ? (
                              <span className="px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[10px] font-semibold">
                                {a.clearMethod === 'manual' ? 'Manual' : 'Otomatis (10 dtk)'}
                              </span>
                            ) : (
                              <span className="px-2 py-0.5 rounded-md bg-rose-500/20 text-rose-300 border border-rose-500/30 text-[10px] font-semibold">
                                Belum Clear
                              </span>
                            )}
                          </td>
                        </tr>
                      ))
                    )}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Log Urutan Tindakan */}
            <div className="space-y-2">
              <div className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                Log Urutan Tindakan &amp; Alarm Sesi {mission.code}:
              </div>
              <div className="p-4 rounded-xl bg-[#0b1120] border border-[#1e293b] space-y-1.5 text-[11px] font-mono leading-relaxed text-slate-300 max-h-60 overflow-y-auto">
                {timelineEvents.length === 0 ? (
                  <div className="text-slate-400">
                    ⏱ {formatSimTime(result.durationSec)} · Sesi selesai tanpa tindakan tambahan tercatat.
                  </div>
                ) : (
                  timelineEvents.map((ev, idx) => (
                    <div key={idx} className={ev.tone}>
                      ⏱ {formatSimTime(ev.timeSec)} · {ev.text}
                    </div>
                  ))
                )}
                <div className="text-slate-400 pt-1 border-t border-[#1e293b]">
                  ⏱ {formatSimTime(result.durationSec)} · Simulasi selesai. Skor {scoreTindakan} + {scoreWaktu} + {scoreStabilitas} + {scoreAlarm}
                  {result.scoreDeductions > 0 ? ` − ${result.scoreDeductions} penalti` : ''} = {displayScore}
                </div>
              </div>
            </div>

            {/* Debriefing Evaluasi Mentor */}
            <div className="p-4 rounded-xl bg-sky-950/20 border border-sky-500/30 text-xs space-y-2">
              <div className="font-bold text-sky-400 flex items-center gap-1.5 uppercase tracking-wider text-[11px]">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Debriefing Evaluasi Mentor (Operator Senior):</span>
              </div>
              <p className="text-slate-200 text-xs leading-relaxed italic">
                "{isTimedOutExam
                  ? `Waktu ujian kelulusan (${formatSimTime(mission.durationLimitSec || 600)}) telah habis sebelum seluruh parameter selesai dipulihkan. Sesuai aturan ujian${showTechnicalRefs ? ' PRD §8' : ''}, misi ujian dinyatakan tidak lulus.`
                  : isPassed
                  ? `Kerja bagus, ${participantFirstName}! ${mission.debriefing.success}`
                  : `${participantFirstName}, ${mission.debriefing.failure}`}"
              </p>
              {nextMission && (
                <div className="text-[11px] text-sky-300 font-semibold pt-1">
                  Langkah berikutnya: {isPassed ? `Lanjutkan ke Misi ${nextMission.code} (${nextMission.name}).` : `Ulangi Misi ${mission.code} untuk mencapai KKM ≥ ${passScore}.`}
                </div>
              )}
            </div>
          </div>
        </div>

        {/* RIGHT COLUMN */}
        <div className="lg:col-span-4 space-y-6">

          {/* Badge Status Card */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-4 shadow-lg">
            <div className="text-[10px] font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1">
              <Award className="w-3.5 h-3.5" />
              <span>Pencapaian Lencana{showTechnicalRefs ? ' (L7)' : ''}</span>
            </div>

            <div className="p-4 rounded-xl bg-purple-950/30 border border-purple-500/40 flex items-center gap-3.5">
              <div className="w-12 h-12 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center font-bold text-lg shrink-0">
                <Zap className="w-6 h-6" />
              </div>
              <div>
                <div className="text-xs font-bold text-white">
                  {isPassed ? `Misi ${mission.code} Lulus (${displayStars}★)` : `Misi ${mission.code} Perlu Pengulangan`}
                </div>
                <div className="text-[11px] text-slate-300 mt-0.5">
                  Durasi sesi: {formatSimTime(result.durationSec)} · Penalti: −{result.scoreDeductions} Poin
                </div>
                <div className="text-[10px] text-sky-400 font-mono mt-0.5">
                  Petunjuk terpakai: {result.hintsUsedCount} kali
                </div>
              </div>
            </div>

            <div className="text-[11px] text-slate-400">
              Total Lencana Anda: <strong className="text-white">{myBadgeCount} dari 8 Lencana{showTechnicalRefs ? ' PRD' : ''} Terbuka</strong>.{' '}
              <button
                type="button"
                onClick={() => (onViewBadges ? onViewBadges() : setCurrentView('badges'))}
                className="text-sky-400 hover:text-sky-300 underline font-semibold cursor-pointer"
              >
                Lihat{showTechnicalRefs ? ' di L7' : ' Galeri Lencana'} →
              </button>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="bg-[#0f172a] rounded-2xl border border-[#24324d] p-5 space-y-3 shadow-lg">
            <div className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">
              Langkah Berikutnya:
            </div>
            <p className="text-[11px] text-slate-400">
              Progres misi {mission.code} telah tersimpan otomatis.
            </p>

            <button
              type="button"
              onClick={onRetry}
              className="w-full py-2.5 px-3 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 hover:text-white font-bold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <span>Ulangi Simulasi Misi {mission.code}</span>
            </button>

            <button
              type="button"
              onClick={() => {
                setReplayUserId(result.userId);
                setCurrentView('replay');
              }}
              className="w-full py-2.5 px-3 rounded-xl bg-[#1e293b] hover:bg-[#334155] border border-[#334155] text-slate-200 hover:text-white font-bold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <History className="w-4 h-4 text-sky-400" />
              <span>Putar Ulang Sesi Simulasi{showTechnicalRefs ? ' (L11 Replay)' : ''}</span>
            </button>

            {nextMission && (
              <button
                type="button"
                onClick={onNextMission}
                className="w-full py-2.5 px-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-all flex items-center justify-center gap-2 shadow-md shadow-sky-950/50 cursor-pointer"
              >
                <span>Lanjut ke Misi Berikut: {nextMission.code} ({nextMission.name}) →</span>
              </button>
            )}

            <button
              type="button"
              onClick={onBackToHome}
              className="w-full py-2.5 px-3 rounded-xl bg-[#0b1120] hover:bg-[#1e293b] border border-[#1e293b] text-slate-400 hover:text-slate-200 font-semibold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              <Home className="w-4 h-4" />
              <span>Kembali ke Beranda Peserta{showTechnicalRefs ? ' (L2)' : ''}</span>
            </button>

            {/* Automatic System Notes */}
            <div className="pt-3 border-t border-[#1e293b] text-[10px] text-slate-400 space-y-1">
              <div className="font-bold text-slate-300 text-[11px]">Catatan Evaluasi Otomatis Sistem:</div>
              <div>
                • Status Misi: {isPassed ? `Lulus ${displayStars}★` : 'Belum Lulus'} (Skor {displayScore})
              </div>
              <div>
                • Pengali XP: {formatNumberID(multiplier, 1)}x = +{displayXP} XP Misi
              </div>
              <div>
                • Level Saat Ini: {operatorLevel.level} ({operatorLevel.currentXP.toLocaleString('id-ID')} XP)
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

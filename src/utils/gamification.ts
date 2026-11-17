/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { Mission, MissionResult, OperatorLevelName } from '../types';

/**
 * Pengali XP resmi per kode misi (PRD SimSCADA-Air v1.1 §7 & §8):
 * - Mudah (1,0x): IPA-01, IPA-02, DST-01, DST-02
 * - Sedang (1,5x): IPA-03, IPA-04, IPA-05, DST-03, DST-04
 * - Sulit (2,0x): IPA-06, IPA-07, IPA-08, DST-05, DST-06
 * - Sangat Sulit (2,5x): TRP-01
 * - Ujian / Misi Kelulusan (3,0x): IPA-09, DST-07, TRP-02
 */
const MISSION_MULTIPLIER_MAP: Record<string, number> = {
  'IPA-01': 1.0,
  'IPA-02': 1.0,
  'IPA-03': 1.5,
  'IPA-04': 1.5,
  'IPA-05': 1.5,
  'IPA-06': 2.0,
  'IPA-07': 2.0,
  'IPA-08': 2.0,
  'IPA-09': 3.0,
  'DST-01': 1.0,
  'DST-02': 1.0,
  'DST-03': 1.5,
  'DST-04': 1.5,
  'DST-05': 2.0,
  'DST-06': 2.0,
  'DST-07': 3.0,
  'TRP-01': 2.5,
  'TRP-02': 3.0,
};

export function getMissionDifficultyMultiplier(missionOrCode: string | Mission): number {
  const code = typeof missionOrCode === 'string' ? missionOrCode : missionOrCode.code;
  if (code in MISSION_MULTIPLIER_MAP) {
    return MISSION_MULTIPLIER_MAP[code];
  }
  if (typeof missionOrCode !== 'string') {
    const label = missionOrCode.levelName.toLowerCase();
    if (label.includes('ujian') || label.includes('kelulusan') || missionOrCode.level === 5) return 3.0;
    if (label.includes('sangat sulit') || missionOrCode.level === 4) return 2.5;
    if (label.includes('sulit') || missionOrCode.level === 3) return 2.0;
    if (label.includes('sedang')) return 1.5;
    if (label.includes('mudah') || missionOrCode.level === 1) return 1.0;
    if (missionOrCode.level === 2) return 1.5;
  }
  return 1.0;
}

/**
 * Bintang dihitung otomatis dari skor (PRD §8):
 * - < passScore (70 umum, 80 ujian kelulusan) = 0★ (belum lulus)
 * - 70–84 = 1★ (khusus ujian kelulusan: 80–84 = 1★)
 * - 85–94 = 2★
 * - >= 95 = 3★
 */
export function computeStarsFromScore(score: number, passScore = 70): number {
  if (score < passScore) return 0;
  if (score >= 95) return 3;
  if (score >= 85) return 2;
  return 1;
}

/**
 * XP misi = round(skor × pengali tingkat misi) jika lulus.
 */
export function computeMissionXP(
  missionOrCode: string | Mission,
  score: number,
  isPassed: boolean
): number {
  if (!isPassed) return 0;
  const multiplier = getMissionDifficultyMultiplier(missionOrCode);
  return Math.round(score * multiplier);
}

/**
 * Mengambil hasil terbaik yang lulus untuk setiap kode misi,
 * dengan stars & xpEarned yang dihitung ulang dari skor.
 */
export function computeBestPassedResults(
  results: MissionResult[],
  missionsList: Mission[]
): MissionResult[] {
  const missionMap = new Map(missionsList.map((m) => [m.code, m]));
  const bestByCode = new Map<string, MissionResult>();

  results.forEach((res) => {
    const mission = missionMap.get(res.missionCode);
    const passScore = mission?.passScore ?? 70;
    const isPassed = res.totalScore >= passScore;
    if (!isPassed) return;

    const normalized: MissionResult = {
      ...res,
      isPassed: true,
      stars: computeStarsFromScore(res.totalScore, passScore),
      xpEarned: computeMissionXP(mission ?? res.missionCode, res.totalScore, true),
    };

    const existing = bestByCode.get(res.missionCode);
    if (!existing || normalized.totalScore > existing.totalScore) {
      bestByCode.set(res.missionCode, normalized);
    }
  });

  return Array.from(bestByCode.values());
}

/**
 * Menghitung total bintang, XP misi, XP kuis, dan total XP peserta secara konsisten.
 */
export function computeUserTotalStarsAndXP(
  results: MissionResult[],
  missionsList: Mission[],
  quizScoresByCode?: Record<string, number>
): {
  passedCount: number;
  totalStars: number;
  missionXP: number;
  quizXP: number;
  totalXP: number;
} {
  const bestPassed = computeBestPassedResults(results, missionsList);
  let totalStars = 0;
  let missionXP = 0;
  let quizXP = 0;

  bestPassed.forEach((res) => {
    totalStars += res.stars;
    missionXP += res.xpEarned;
    quizXP += quizScoresByCode?.[res.missionCode] ?? 80;
  });

  return {
    passedCount: bestPassed.length,
    totalStars,
    missionXP,
    quizXP,
    totalXP: missionXP + quizXP,
  };
}

export function getOperatorLevelFromXP(xp: number): {
  level: OperatorLevelName;
  minXP: number;
  nextXP: number;
  progress: number;
  currentXP: number;
} {
  if (xp >= 3500) {
    return { level: 'Operator Ahli', minXP: 3500, nextXP: 5000, progress: 100, currentXP: xp };
  }
  if (xp >= 2500) {
    return {
      level: 'Operator Utama',
      minXP: 2500,
      nextXP: 3500,
      progress: Math.round(((xp - 2500) / 1000) * 100),
      currentXP: xp,
    };
  }
  if (xp >= 1200) {
    return {
      level: 'Operator Madya',
      minXP: 1200,
      nextXP: 2500,
      progress: Math.round(((xp - 1200) / 1300) * 100),
      currentXP: xp,
    };
  }
  if (xp >= 400) {
    return {
      level: 'Operator Muda',
      minXP: 400,
      nextXP: 1200,
      progress: Math.round(((xp - 400) / 800) * 100),
      currentXP: xp,
    };
  }
  return {
    level: 'Operator Magang',
    minXP: 0,
    nextXP: 400,
    progress: Math.round((xp / 400) * 100),
    currentXP: xp,
  };
}

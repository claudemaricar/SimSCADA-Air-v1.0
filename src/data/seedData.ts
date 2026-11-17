/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import {
  Badge,
  Certificate,
  ControlPointDef,
  Mission,
  PrePostTestResult,
  QuizQuestion,
  Tenant,
  TrainingGroup,
  User,
  MissionResult,
} from '../types';
import { computeMissionXP, computeStarsFromScore } from '../utils/gamification';

// ====================================================================
// A. LEMBAGA (TENANTS) SESUAI PRD §5 & BAGIAN 5 DOKUMEN HTML
// ====================================================================
export const INITIAL_TENANTS: Tenant[] = [
  {
    id: 'nusantara',
    code: 'NUS',
    name: 'Balai Diklat Air Minum Nusantara',
    shortName: 'Balai Nusantara',
    address: 'Jl. Tirta Darma No. 45, Kompleks Pengolahan Air, Jakarta Timur',
    contact: '(021) 8892-1200 / info@diklatnusantara.id',
    type: 'balai_pelatihan',
    license: {
      packageTracks: ['ipa', 'distribusi', 'terpadu'],
      seatQuota: 50,
      seatsUsed: 46, // 46 terpakai (92% -> Peringatan Kuota >= 90%)
      startDate: '2026-01-01',
      endDate: '2026-10-31', // Sisa lisensi 245 hari
      isActive: true,
    },
    signers: {
      leaderName: 'Dr. Ir. Bambang Sutrisno, M.Eng.',
      leaderTitle: 'Kepala Balai Diklat Air Minum Nusantara',
      instructorName: 'Budi Santoso, S.T.',
      instructorTitle: 'Instruktur Utama SPAM',
    },
    config: {
      passThresholdScore: 70,
      graduationThresholdScore: 80,
      leaderboardEnabled: true,
      localSopNotes: {
        intake: 'SOP-NUS-01: Pergantian pompa duty/standby wajib dicatat di logsheet harian shift.',
        koagulasi: 'Di instalasi latih IPA Balai Nusantara, injeksi koagulan memakai dosing pump otomatis dengan kalibrasi larutan PAC 10%. Batas minimum tangki harian adalah 20%.',
        filtrasi: 'SOP-NUS-04: Headloss > 2,0 mH2O atau waktu operasi 24 jam memicu backwash bertahap.',
        desinfeksi: 'SOP-NUS-05: Sisa klor di titik reservoir wajib dipertahankan 0,30–0,40 mg/L.',
      },
    },
  },
  {
    id: 'tirta',
    code: 'TRM',
    name: 'Pusat Pelatihan Tirta Mandiri',
    shortName: 'Tirta Mandiri',
    address: 'Jl. Rinjani No. 12, Kota Bandung, Jawa Barat',
    contact: '(022) 7201-9988 / diklat@tirtamandiri.co.id',
    type: 'swasta',
    license: {
      packageTracks: ['ipa'], // Hanya paket IPA
      seatQuota: 50,
      seatsUsed: 22,
      startDate: '2026-03-01',
      endDate: '2026-12-08', // Sisa lisensi 28 hari (<= 30 hari -> Peringatan berakhir)
      isActive: true,
    },
    signers: {
      leaderName: 'Ir. Hendra Kusuma, M.T.',
      leaderTitle: 'Direktur Pusat Pelatihan Tirta Mandiri',
      instructorName: 'Agus Salim, M.T.',
      instructorTitle: 'Instruktur Utama Operasi IPA Tirta Mandiri',
    },
    config: {
      passThresholdScore: 70,
      graduationThresholdScore: 80,
      leaderboardEnabled: true,
      localSopNotes: {
        intake: 'SOP-TRM-01: Verifikasi debit inflow minimum 75 L/s saat pompa beroperasi.',
      },
    },
  },
];

// ====================================================================
// B. KELOMPOK BELAJAR (GROUPS)
// ====================================================================
export const INITIAL_GROUPS: TrainingGroup[] = [
  {
    id: 'grp-nusantara-1',
    tenantId: 'nusantara',
    name: 'Angkatan 1 (24 Peserta)',
    instructorId: 'user-instruktur-nusantara',
    track: 'terpadu',
    createdAt: '2026-08-01',
  },
  {
    id: 'grp-nusantara-2',
    tenantId: 'nusantara',
    name: 'Angkatan 2 (22 Peserta)',
    instructorId: 'user-instruktur-nusantara',
    track: 'ipa',
    createdAt: '2026-09-15',
  },
  {
    id: 'grp-tirta-1',
    tenantId: 'tirta',
    name: 'Angkatan 1 Tirta Mandiri',
    instructorId: 'user-instruktur-tirta',
    track: 'ipa',
    createdAt: '2026-10-01',
  },
];

// ====================================================================
// C. 10 AKUN DEMO RESMI PRD §5 (SANDI: Demo#2026) + PESERTA CONTOH
// ====================================================================
// Total Nusantara: 4 akun demo peserta (baru, ipa, distribusi, lulus) + 42 peserta contoh = 46 kursi terpakai
export const INITIAL_USERS: User[] = [
  // 1. Superadmin
  {
    id: 'user-superadmin',
    username: 'superadmin',
    fullName: 'Super Administrator',
    email: 'superadmin@simscada-air.id',
    role: 'superadmin',
    tenantId: 'platform',
    createdAt: '2026-01-01',
    lastLoginAt: '2026-10-28T07:30:00Z',
  },
  // 2. Admin Nusantara
  {
    id: 'user-admin-nusantara',
    username: 'admin.nusantara',
    fullName: 'Rina Oktaviani',
    email: 'rina.oktaviani@diklatnusantara.id',
    role: 'admin_lembaga',
    tenantId: 'nusantara',
    createdAt: '2026-01-15',
    lastLoginAt: '2026-10-28T08:15:00Z',
  },
  // 3. Pimpinan Nusantara
  {
    id: 'user-pimpinan-nusantara',
    username: 'pimpinan.nusantara',
    fullName: 'Dr. Ir. Bambang Sutrisno, M.Eng.',
    email: 'bambang.sutrisno@diklatnusantara.id',
    role: 'pimpinan_lembaga',
    tenantId: 'nusantara',
    createdAt: '2026-01-15',
    lastLoginAt: '2026-10-28T09:00:00Z',
  },
  // 4. Instruktur Nusantara
  {
    id: 'user-instruktur-nusantara',
    username: 'instruktur.nusantara',
    fullName: 'Budi Santoso, S.T.',
    email: 'budi.santoso@diklatnusantara.id',
    role: 'instruktur',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    createdAt: '2026-01-20',
    lastLoginAt: '2026-10-28T10:05:00Z',
  },
  // 5. Peserta Baru
  {
    id: 'user-peserta-baru',
    username: 'peserta.baru',
    fullName: 'Budi Baru',
    email: 'budi.baru@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'terpadu',
    createdAt: '2026-10-25',
    lastLoginAt: '2026-10-28T11:00:00Z',
  },
  // 6. Peserta IPA (Dimas Wahyu Pratama)
  {
    id: 'user-peserta-ipa',
    username: 'peserta.ipa',
    fullName: 'Dimas Wahyu Pratama',
    email: 'dimas.pratama@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'ipa',
    createdAt: '2026-09-01',
    lastLoginAt: '2026-10-28T08:30:00Z',
  },
  // 7. Peserta Distribusi (Siti Rahmawati)
  {
    id: 'user-peserta-distribusi',
    username: 'peserta.distribusi',
    fullName: 'Siti Rahmawati',
    email: 'siti.rahmawati@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'distribusi',
    createdAt: '2026-09-05',
    lastLoginAt: '2026-10-26T14:20:00Z',
  },
  // 8. Peserta Lulus (Andi Kurniawan)
  {
    id: 'user-peserta-lulus',
    username: 'peserta.lulus',
    fullName: 'Andi Kurniawan',
    email: 'andi.kurniawan@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'terpadu',
    createdAt: '2026-08-01',
    lastLoginAt: '2026-10-28T10:15:00Z',
  },
  // 9. Admin Tirta Mandiri
  {
    id: 'user-admin-tirta',
    username: 'admin.tirta',
    fullName: 'Hj. Dewi Anggraini',
    email: 'dewi.anggraini@tirtamandiri.co.id',
    role: 'admin_lembaga',
    tenantId: 'tirta',
    createdAt: '2026-03-01',
    lastLoginAt: '2026-10-28T08:30:00Z',
  },
  // Pimpinan Tirta Mandiri (contoh lembaga Tirta)
  {
    id: 'user-pimpinan-tirta',
    username: 'pimpinan.tirta',
    fullName: 'Ir. Hendra Kusuma, M.T.',
    email: 'hendra.kusuma@tirtamandiri.co.id',
    role: 'pimpinan_lembaga',
    tenantId: 'tirta',
    createdAt: '2026-03-01',
    lastLoginAt: '2026-10-28T08:45:00Z',
  },
  // Instruktur Tirta Mandiri (contoh lembaga Tirta)
  {
    id: 'user-instruktur-tirta',
    username: 'instruktur.tirta',
    fullName: 'Agus Salim, M.T.',
    email: 'agus.salim@tirtamandiri.co.id',
    role: 'instruktur',
    tenantId: 'tirta',
    groupId: 'grp-tirta-1',
    createdAt: '2026-03-05',
    lastLoginAt: '2026-10-28T09:15:00Z',
  },
  // 10. Peserta Tirta Mandiri
  {
    id: 'user-peserta-tirta',
    username: 'peserta.tirta',
    fullName: 'Siti Aminah',
    email: 'siti.aminah@peserta.tirtamandiri.co.id',
    role: 'peserta',
    tenantId: 'tirta',
    groupId: 'grp-tirta-1',
    track: 'ipa',
    createdAt: '2026-10-18',
    lastLoginAt: '2026-10-28T09:00:00Z',
  },

  // --- Peserta Contoh Tambahan Balai Nusantara (bukan akun demo) ---
  // Rian Hidayat (Menunggu Persetujuan Instruktur L8b, SSA/NUS/2026/0002)
  {
    id: 'user-rian-hidayat',
    username: 'rian.hidayat',
    fullName: 'Rian Hidayat',
    email: 'rian.hidayat@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'ipa',
    createdAt: '2026-08-10',
    lastLoginAt: '2026-10-28T09:45:00Z',
  },
  // Eko Prasetyo (Tertinggal, gagal IPA-07 3x)
  {
    id: 'user-eko-prasetyo',
    username: 'eko.prasetyo',
    fullName: 'Eko Prasetyo',
    email: 'eko.prasetyo@peserta.diklatnusantara.id',
    role: 'peserta',
    tenantId: 'nusantara',
    groupId: 'grp-nusantara-1',
    track: 'ipa',
    createdAt: '2026-08-15',
    lastLoginAt: '2026-10-25T11:20:00Z',
  },
];

// Generate 40 additional mock participants for Nusantara to reach exactly 46 users (24 in Grp 1, 22 in Grp 2)
// 42 active (login within 14 days)
(function populateNusantaraParticipants() {
  // Grp 1 already has: baru, ipa, distribusi, lulus, rian, eko (6 users)
  // Grp 1 needs 18 more to make 24
  for (let i = 1; i <= 18; i++) {
    const isInactive = i === 18; // 1 inactive in grp 1
    INITIAL_USERS.push({
      id: `user-nus-grp1-${i}`,
      username: `peserta.g1.${i}`,
      fullName: `Peserta Angkatan 1 - ${String.fromCharCode(64 + i)}`,
      email: `peserta.g1.${i}@diklatnusantara.id`,
      role: 'peserta',
      tenantId: 'nusantara',
      groupId: 'grp-nusantara-1',
      track: i % 2 === 0 ? 'ipa' : 'terpadu',
      createdAt: '2026-08-01',
      lastLoginAt: isInactive ? '2026-09-10T00:00:00Z' : '2026-10-24T10:00:00Z',
    });
  }

  // Grp 2 needs 22 users (Angkatan 2)
  for (let i = 1; i <= 22; i++) {
    const isInactive = i >= 20; // 3 inactive in grp 2 -> Total inactive = 4, Total active = 42!
    INITIAL_USERS.push({
      id: `user-nus-grp2-${i}`,
      username: `peserta.g2.${i}`,
      fullName: `Peserta Angkatan 2 - Nomor ${i}`,
      email: `peserta.g2.${i}@diklatnusantara.id`,
      role: 'peserta',
      tenantId: 'nusantara',
      groupId: 'grp-nusantara-2',
      track: i % 3 === 0 ? 'distribusi' : 'ipa',
      createdAt: '2026-09-15',
      lastLoginAt: isInactive ? '2026-09-20T00:00:00Z' : '2026-10-26T15:00:00Z',
    });
  }

  // Tirta Mandiri: 22 users total in grp-tirta-1 (18 active, 4 inactive)
  for (let i = 1; i <= 21; i++) {
    const isInactive = i >= 18;
    INITIAL_USERS.push({
      id: `user-trm-${i}`,
      username: `peserta.trm.${i}`,
      fullName: `Peserta Tirta Mandiri ${i}`,
      email: `peserta.trm.${i}@tirtamandiri.co.id`,
      role: 'peserta',
      tenantId: 'tirta',
      groupId: 'grp-tirta-1',
      track: 'ipa',
      createdAt: '2026-10-01',
      lastLoginAt: isInactive ? '2026-09-15T00:00:00Z' : '2026-10-27T08:00:00Z',
    });
  }
})();

// ====================================================================
// D. 8 LENCANA RESMI PRD §8
// ====================================================================
export const BADGES_LIST: Badge[] = [
  {
    id: 'b-penjelajah',
    name: 'Penjelajah Titik Kontrol',
    description: 'Membuka narasi edukasi semua titik kontrol di satu jalur simulasi.',
    iconName: 'Compass',
    requirement: 'Buka narasi semua titik kontrol IPA / Distribusi.',
  },
  {
    id: 'b-respons-kilat',
    name: 'Respons Kilat',
    description: 'Tindakan benar pertama dilakukan < 50% waktu target pada skenario gangguan.',
    iconName: 'Zap',
    requirement: 'Atasi gangguan dalam waktu < 30 detik (50% dari target 60 detik di IPA-06).',
  },
  {
    id: 'b-tanpa-alarm-terlewat',
    name: 'Tanpa Alarm Terlewat',
    description: 'Menyelesaikan misi gangguan dengan semua alarm diakui dan clear tanpa kesalahan.',
    iconName: 'ShieldCheck',
    requirement: '100% penanganan alarm berhasil tanpa rejected clear.',
  },
  {
    id: 'b-penjaga-mutu',
    name: 'Penjaga Mutu Air',
    description: 'Kekeruhan dan sisa klor di rentang normal sepanjang misi IPA.',
    iconName: 'Droplets',
    requirement: 'Kekeruhan dan sisa klor di rentang normal sepanjang misi IPA.',
  },
  {
    id: 'b-penjaga-tekanan',
    name: 'Penjaga Tekanan',
    description: 'Tekanan semua zona di rentang layanan sepanjang misi distribusi.',
    iconName: 'Gauge',
    requirement: 'Tekanan semua zona di rentang layanan sepanjang misi distribusi.',
  },
  {
    id: 'b-tiga-bintang',
    name: 'Tiga Bintang IPA / Distribusi',
    description: 'Meraih skor ≥95 (3★) pada semua misi jalur IPA atau Distribusi.',
    iconName: 'Star',
    requirement: 'Meraih skor ≥95 (3★) pada semua misi jalur IPA atau Distribusi.',
  },
  {
    id: 'b-hulu-ke-hilir',
    name: 'Hulu ke Hilir',
    description: 'Berhasil mengatasi gangguan berantai terpadu dari IPA sampai distribusi (TRP-01).',
    iconName: 'GitFork',
    requirement: 'Lulus misi TRP-01 dengan minimal 1 bintang.',
  },
  {
    id: 'b-tanpa-petunjuk',
    name: 'Lulus Tanpa Petunjuk',
    description: 'Menyelesaikan seluruh jalur hingga lulus ujian kelulusan tanpa pernah memakai tombol bantuan petunjuk (-5 poin) di semua percobaan misi.',
    iconName: 'Award',
    requirement: 'Lulus semua misi, Misi Kelulusan, dan Post-Test dengan 0 petunjuk terpakai di seluruh percobaan misi.',
  },
];

// ====================================================================
// E. TITIK KONTROL DENGAN 6 BAGIAN NARASI RESMI (PRD §9)
// ====================================================================
export const CONTROL_POINTS: ControlPointDef[] = [
  {
    id: 'intake',
    name: 'Intake & Pompa Air Baku',
    category: 'ipa',
    monitoredParams: ['Debit Air Baku (L/s)', 'Kekeruhan Air Baku (NTU)', 'Status Pompa 1 & 2', 'pH Air Baku'],
    controllableParams: ['Start / Stop Pompa 1 & 2', 'Pilih Duty/Standby', 'Atur Debit (L/s)', 'Reset Trip Pompa'],
    normalRanges: {
      debit: { min: 70, max: 120, unit: 'L/s', desc: 'Debit intake optimal pengolahan (100 L/s nominal)' },
      kekeruhan: { min: 15, max: 50, unit: 'NTU', desc: 'Kekeruhan normal air sungai' },
    },
    narrative: {
      apaIni: 'Unit Intake menyadap air baku dari badan air alami (sungai/waduk) menggunakan saringan kasar (bar screen) dan pompa air baku menuju instalasi pengolahan.',
      yangDipantau: 'Debit aliran air baku (L/s), kekeruhan air baku (NTU), status operasi pompa (Run/Stop/Trip), dan level sumur intake.',
      yangBisaDikendalikan: 'Start/stop Pompa 1 dan Pompa 2, pemilihan pompa utama (duty) dan cadangan (standby), pengaturan debit intake, serta reset alarm trip pompa.',
      dampakKeHilir: 'Bila debit intake drop, seluruh bak sedimentasi dan reservoir akan kekurangan pasokan. Bila kekeruhan air baku melonjak tajam tanpa penyesuaian koagulan, air olahan akan keruh.',
      gangguanUmumDanSop: 'Pompa trip akibat beban lebih atau sampah: Segera alihkan ke pompa cadangan, periksa panel, tekan tombol Reset, lalu clear alarm.',
      pelajariLebihLanjut: 'Modul IPA Bab 1: Hidrolika Intake dan Karakteristik Air Baku Sungai Indonesia.',
    },
  },
  {
    id: 'koagulasi',
    name: 'Flash Mixer Koagulasi',
    category: 'ipa',
    monitoredParams: ['Dosis Koagulan PAC (mg/L)', 'Dosis Penyesuai pH Kapur (mg/L)', 'pH Air Koagulasi', 'Kecepatan Flash Mixer (RPM)'],
    controllableParams: ['Setpoint Dosis Koagulan PAC (mg/L)', 'Dosis Penyesuai pH (mg/L)', 'Saklar On/Off Mixer (120 RPM)'],
    normalRanges: {
      dosis: { min: 20, max: 50, unit: 'mg/L', desc: 'Dosis PAC (20–30 mg/L normal, 45–55 mg/L banjir)' },
      ph: { min: 6.5, max: 8.5, unit: 'pH', desc: 'Baku mutu Permenkes No. 2/2023 (Target: 7,20)' },
    },
    narrative: {
      apaIni: 'Unit pengaduk berkecepatan tinggi (Flash Mixer, G > 750 s⁻¹) yang meratakan koagulan PAC ke seluruh aliran air baku dalam waktu < 60 detik untuk mendestabilisasi koloid.',
      yangDipantau: 'Dosis koagulan PAC aktual (mg/L), dosis penyesuai pH (mg/L), pH hasil koagulasi (6,5–8,5), dan putaran motor mixer (100–150 RPM).',
      yangBisaDikendalikan: 'Setpoint dosis koagulan PAC, setpoint dosis kapur penyesuai pH, dan saklar On/Off motor flash mixer.',
      dampakKeHilir: 'Underdosing: Flok tidak terbentuk sempurna, kekeruhan lolos melewati bak sedimentasi dan membebani filter. Overdosing: Pemborosan kimia, pH anjlok tajam, dan lumpur berlebih meluap ke filter.',
      gangguanUmumDanSop: 'Lonjakan Kekeruhan Baku: Naikkan dosis PAC (misal 20 ke 48 mg/L) sesuai kurva jar-test; Pompa Dosing Macet: Pindahkan ke pompa cadangan lalu lakukan flushing; pH Drop: Tambahkan kapur agar pH tetap 6,5–8,5.',
      pelajariLebihLanjut: 'Modul Teori IPA-03 (Koagulasi) & Standar Permenkes No. 2/2023 Bab II.',
    },
  },
  {
    id: 'flokulasi',
    name: 'Flokulator (3 Kompartemen)',
    category: 'ipa',
    monitoredParams: ['Kecepatan Stage 1 (RPM)', 'Kecepatan Stage 2 (RPM)', 'Kecepatan Stage 3 (RPM)', 'Kondisi Pembentukan Flok'],
    controllableParams: ['On/Off Pengaduk Lambat', 'Kecepatan Bertahap'],
    normalRanges: {
      stage1: { min: 35, max: 50, unit: 'RPM', desc: 'Stage 1: Pengadukan cepat-sedang (45 RPM)' },
      stage2: { min: 25, max: 35, unit: 'RPM', desc: 'Stage 2: Pengadukan sedang (30 RPM)' },
      stage3: { min: 10, max: 20, unit: 'RPM', desc: 'Stage 3: Pengadukan lambat (15 RPM)' },
    },
    narrative: {
      apaIni: 'Flokulator 3 kompartemen menggabungkan partikel mikro terdestabilisasi menjadi gumpalan flok makro yang padat dan mudah mengendap secara bertahap (gradien G menurun).',
      yangDipantau: 'Kecepatan putar pengaduk lambat tiap kompartemen dan indeks visual pembentukan flok.',
      yangBisaDikendalikan: 'Saklar On/Off dan regulasi kecepatan pengaduk per stage.',
      dampakKeHilir: 'Pengadukan terlalu lambat membuat flok mengendap prematur di saluran; terlalu kencang menyebabkan flok pecah (floc shear) sehingga lolos ke filter.',
      gangguanUmumDanSop: 'Motor pengaduk macet: Periksa panel proteksi overload, jalankan motor backup kompartemen.',
      pelajariLebihLanjut: 'Modul IPA Bab 3: Desain Kompartemen Flokulasi dan Gradien Kecepatan.',
    },
  },
  {
    id: 'sedimentasi',
    name: 'Sedimentasi (Plate Settler)',
    category: 'ipa',
    monitoredParams: ['Kekeruhan Keluar Bak (NTU)', 'Selimut Lumpur (Meter)', 'Tren Kekeruhan'],
    controllableParams: ['Valve Blowdown Lumpur (Buang)'],
    normalRanges: {
      kekeruhanKeluar: { min: 2.0, max: 15.0, unit: 'NTU', desc: 'Air jernih sebelum masuk filter (nominal 12,4 NTU)' },
      selimutLumpur: { min: 0.5, max: 2.0, unit: 'Meter', desc: 'Tinggi akumulasi lumpur di hopper' },
    },
    narrative: {
      apaIni: 'Bak sedimentasi dengan plate settler mengendapkan flok secara gravitasi dan memisahkan air bersih di permukaan dari endapan lumpur di dasar.',
      yangDipantau: 'Kekeruhan air olahan keluar sedimentasi dan ketebalan selimut lumpur di hopper.',
      yangBisaDikendalikan: 'Membuka valve blowdown lumpur untuk membuang endapan ke bak penampung.',
      dampakKeHilir: 'Bila lumpur menumpuk melebihi 2,0 m, terjadi sludge carryover yang langsung menyumbat media filter dalam beberapa menit.',
      gangguanUmumDanSop: 'Selimut lumpur tinggi: Lakukan blowdown rutin setiap shift selama 1–2 menit hingga cairan buangan encer kembali.',
      pelajariLebihLanjut: 'Modul IPA Bab 4: Efisiensi Pengendapan Bak Lamella.',
    },
  },
  {
    id: 'filtrasi',
    name: 'Filtrasi (Dual Sand Filter)',
    category: 'ipa',
    monitoredParams: ['Kekeruhan Air Olahan Masuk Reservoir (NTU)', 'Headloss Filter (Meter)', 'Status Filter 1 & 2'],
    controllableParams: ['Pencucian Balik (Backwash Filter)'],
    normalRanges: {
      kekeruhanOlahan: { min: 0.5, max: 2.8, unit: 'NTU', desc: 'Wajib < 3,0 NTU (Permenkes 2/2023)' },
      headloss: { min: 0.5, max: 1.8, unit: 'Meter', desc: 'Kehilangan tekanan media pasir' },
    },
    narrative: {
      apaIni: 'Unit Filtrasi menggunakan media ganda (antrasit dan pasir silika) untuk menyaring sisa partikel halus tak terendapkan.',
      yangDipantau: 'Kekeruhan air olahan (wajib < 3,0 NTU; ≥ 3,0 NTU memicu alarm TINGGI) dan headloss kehilangan tekanan filter.',
      yangBisaDikendalikan: 'Mengaktifkan siklus pencucian balik (backwash) untuk memulihkan kapasitas filtrasi.',
      dampakKeHilir: 'Kekeruhan air olahan ≥ 3,0 NTU melanggar baku mutu Permenkes dan dapat menyebarkan bakteri ke reservoir kota.',
      gangguanUmumDanSop: 'Kekeruhan air olahan melonjak ≥ 3,0 NTU: Akui alarm segera, evaluasi dosis PAC di koagulasi. Bila headloss > 2,0 m, lakukan backwash bergantian.',
      pelajariLebihLanjut: 'Modul IPA Bab 5: Pengoperasian dan Pembersihan Filter Pasir Cepat.',
    },
  },
  {
    id: 'reservoir',
    name: 'Reservoir Air Bersih & Klorinasi',
    category: 'ipa',
    monitoredParams: ['Level Air Reservoir (Meter / %)', 'Sisa Klorin Ujung (mg/L)', 'Katup Masuk/Keluar'],
    controllableParams: ['Setpoint Dosis Klorin (mg/L)', 'Katup Masuk / Keluar'],
    normalRanges: {
      level: { min: 2.0, max: 4.8, unit: 'Meter', desc: 'Level aman tangki (4,2 m = 84%)' },
      sisaKlor: { min: 0.2, max: 0.5, unit: 'mg/L', desc: 'Permenkes: 0,2–0,5 mg/L (Target: 0,38)' },
    },
    narrative: {
      apaIni: 'Tangki penyimpanan air olahan bersih yang dilengkapi injeksi klorin untuk membunuh patogen dan menjaga residu desinfektan di jaringan pipa.',
      yangDipantau: 'Ketinggian air reservoir (meter dan %), sisa klor bebas outlet (harus 0,2–0,5 mg/L).',
      yangBisaDikendalikan: 'Setpoint dosing klorin (1,20 mg/L) dan valve buka/tutup isolasi.',
      dampakKeHilir: 'Sisa klor < 0,2 mg/L memicu alarm KRITIS karena risiko kontaminasi bakteri di jaringan. Level < 1,0 m membahayakan pompa distribusi karena kavitasi.',
      gangguanUmumDanSop: 'Sisa klor drop < 0,2 mg/L: Segera naikkan dosing klor ke 1,5–1,8 mg/L hingga terdeteksi residu stabil 0,38 mg/L.',
      pelajariLebihLanjut: 'Modul IPA Bab 6: Kimia Klorinasi dan Regulasi Permenkes No. 2/2023.',
    },
  },
  {
    id: 'pompa_distribusi',
    name: 'Pompa Distribusi',
    category: 'distribusi',
    monitoredParams: ['Tekanan Keluar (bar)', 'Total Debit Pompa (L/s)', 'Status Pompa 1 & 2'],
    controllableParams: ['Start / Stop Pompa 1 & 2', 'Jumlah Pompa Jalan', 'Reset Trip Pompa'],
    normalRanges: {
      tekanan: { min: 3.5, max: 4.5, unit: 'bar', desc: 'Tekanan buang stasiun pompa (nominal 4,1 bar)' },
      debit: { min: 39, max: 56, unit: 'L/s', desc: 'Total aliran normal ke jaringan pipa distribusi (L/s)' },
    },
    narrative: {
      apaIni: 'Stasiun Pompa Distribusi memompa air minum dari reservoir ke jaringan pipa perpipaan kota dengan tekanan memadai.',
      yangDipantau: 'Tekanan pipa buang stasiun pompa (bar), total debit aliran (L/s), dan status proteksi motor listrik.',
      yangBisaDikendalikan: 'Start/Stop pompa P-101 dan P-102, memilih jumlah pompa yang jalan, dan reset alarm trip.',
      dampakKeHilir: 'Pompa distribusi trip menyebabkan tekanan seluruh kota drop seketika, pasokan terhenti dan risiko kontaminasi dari air tanah masuk ke pipa.',
      gangguanUmumDanSop: 'Pompa trip: Alarm berbunyi KRITIS! Segera start pompa cadangan, periksa panel proteksi, tekan tombol Reset Pompa, lalu clear alarm.',
      pelajariLebihLanjut: 'Modul Distribusi Bab 2: Kurva Karakteristik Pompa Sentrifugal dan Paralel.',
    },
  },
  {
    id: 'valve_prv',
    name: 'Katup Pengurang Tekanan (PRV) & Isolasi',
    category: 'distribusi',
    monitoredParams: ['Status Valve Zona 1 & 2', 'Setpoint PRV (bar)', 'Status Valve Isolasi Bocor'],
    controllableParams: ['Buka/Tutup Valve Zona 1', 'Buka/Tutup Valve Zona 2', 'Valve Isolasi Kebocoran', 'Setpoint PRV (bar)'],
    normalRanges: {
      prv: { min: 2.0, max: 2.8, unit: 'bar', desc: 'Setpoint reduksi tekanan zona (nominal 2,5 bar; rentang 2,0–2,8 bar)' },
    },
    narrative: {
      apaIni: 'Pressure Reducing Valve (PRV) dan Katup Sekat Zona mengontrol tekanan hidrolika dan mencegah lonjakan water hammer yang merusak meteran pelanggan.',
      yangDipantau: 'Posisi katup zona, setpoint PRV dalam satuan bar, dan status katup isolasi ruas pipa.',
      yangBisaDikendalikan: 'Mengatur setpoint bukaan PRV dalam bar dan menutup valve isolasi saat terjadi kebocoran pipa.',
      dampakKeHilir: 'Kebocoran pipa tidak diisolasi menyebabkan kehilangan air masif dan tekanan zona drop di bawah 2,0 bar.',
      gangguanUmumDanSop: 'Pipa pecah/bocor: Tutup katup isolasi ruas pipa terkait (Valve Isolasi Bocor) dalam waktu target 60 detik untuk melokalisir kebocoran.',
      pelajariLebihLanjut: 'Modul Distribusi Bab 3: Manajemen Tekanan Zona (DMA) dan Operasional PRV.',
    },
  },
  {
    id: 'titik_pantau_jaringan',
    name: 'Titik Pantau Jaringan (Zona 1 & 2)',
    category: 'distribusi',
    monitoredParams: ['Tekanan Zona 1 (bar)', 'Tekanan Zona 2 (bar)', 'Debit Zona (L/s)', 'Sisa Klor Ujung (mg/L)'],
    controllableParams: ['Pemantauan Telemetri Lapangan'],
    normalRanges: {
      tekananZona1: { min: 2.0, max: 2.8, unit: 'bar', desc: 'Tekanan layanan zona 1 (nominal 2,4 bar; standar 2,0–2,8 bar)' },
      tekananZona2: { min: 2.0, max: 2.8, unit: 'bar', desc: 'Tekanan layanan zona 2 (nominal 2,2 bar; standar 2,0–2,8 bar)' },
      sisaKlorUjung: { min: 0.2, max: 0.5, unit: 'mg/L', desc: 'Residu klorin ujung pipa (standar 0,20–0,50 mg/L)' },
    },
    narrative: {
      apaIni: 'Titik Pantau Jaringan telemetri IoT memantau tekanan hidrolika dan kualitas air di titik sambungan terjauh pelanggan.',
      yangDipantau: 'Tekanan pipa dinamis (bar), laju aliran zona (L/s), dan sisa klorin bebas ujung pipa.',
      yangBisaDikendalikan: 'Unit sensor pantau (read-only) untuk diagnostik ruang kontrol.',
      dampakKeHilir: 'Bila tekanan < 2,0 bar, pelayanan pelanggan terganggu dan berisiko intrusi air tanah. Bila sisa klor < 0,20 mg/L, air berisiko tercemar bakteri.',
      gangguanUmumDanSop: 'Tekanan drop diiringi debit melonjak: Indikasi kebocoran pipa distribusi. Lakukan isolasi katup zona segera.',
      pelajariLebihLanjut: 'Modul Distribusi Bab 4: Analisis Pola Kebocoran dan Residual Klorin.',
    },
  },
];

// ====================================================================
// F. KATALOG MISI RESMI PRD §7 (IPA-01..09, DST-01..07, TRP-01..02)
// ====================================================================
export const MISSIONS_LIST: Mission[] = [
  // --- JALUR IPA (9 MISI) ---
  {
    code: 'IPA-01',
    name: 'Kenali Ruang Kendali IPA',
    level: 1,
    levelName: 'Tingkat 1: Pengenalan (Mudah · 1,0x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Membuka narasi semua titik kontrol IPA, membaca nilai proses dan batas aman.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Selamat datang di Ruang Kendali Instalasi Pengolahan Air (IPA). Hari ini Anda memulai shift orientasi pertama.',
      objective: 'Buka narasi edukasi titik kontrol Intake, Koagulasi, Flokulasi, Sedimentasi, Filtrasi, Desinfeksi, dan Reservoir.',
      mentorQuote: '"Pahami setiap unit pengolahan dan batas operasinya sebelum kamu menyentuh saklar kendali." — Pak Slamet',
    },
    debriefing: {
      success: 'Bagus sekali! Anda telah membaca dan menginspeksi seluruh unit pengolahan air bersih.',
      failure: 'Pastikan Anda mengeklik ikon informasi di setiap titik kontrol dan membaca parameter normalnya.',
    },
    disturbances: [],
    hints: ['Klik ikon "i" pada diagram SCADA untuk membuka narasi titik kontrol.'],
    quiz: [
      {
        id: 'q1',
        question: 'Berapa batas maksimal kekeruhan air olahan menurut Permenkes No. 2 Tahun 2023?',
        options: ['10,0 NTU', '5,0 NTU', '3,0 NTU', '1,5 NTU'],
        correctIndex: 2,
        explanation: 'Menurut Permenkes No. 2 Tahun 2023, standar baku mutu kekeruhan air minum adalah kurang dari 3,0 NTU.',
      },
      {
        id: 'q2',
        question: 'Apa fungsi utama penambahan koagulan (PAC) pada unit pengolahan air?',
        options: ['Menetralkan sisa klorin bebas di dalam bak sedimentasi', 'Mendestabilisasi muatan koloid agar menggumpal menjadi flok', 'Menurunkan kesadahan total kalsium dan magnesium secara langsung', 'Menaikkan tekanan pompa hisap pada saluran pipa intake'],
        correctIndex: 1,
        explanation: 'Koagulan mendestabilisasi partikel koloid bermuatan negatif agar membentuk mikroflok.',
      },
      {
        id: 'q3',
        question: 'Rentang sisa klor bebas yang aman di air olahan reservoir adalah...',
        options: ['0,05–0,15 mg/L', '0,20–0,50 mg/L', '0,80–1,20 mg/L', '1,50–2,50 mg/L'],
        correctIndex: 1,
        explanation: 'Standar sisa klor bebas yang aman dan efektif adalah 0,20–0,50 mg/L.',
      },
      {
        id: 'q4',
        question: 'Kapan operator harus menjalankan siklus backwash pada filter pasir cepat?',
        options: ['Setiap satu jam sekali tanpa memperhatikan data pembacaan panel sensor', 'Saat headloss melebihi 2,0 m atau kekeruhan efluen naik', 'Ketika kapasitas tangki reservoir air bersih mencapai setengah penuh', 'Hanya bila seluruh pompa intake dihentikan beroperasi secara total'],
        correctIndex: 1,
        explanation: 'Backwash wajib dijalankan saat media filter jenuh kotoran ditandai headloss tinggi (> 2,0 m) atau terobosan kekeruhan.',
      },
      {
        id: 'q5',
        question: 'Bila alarm pompa trip muncul dengan status terkunci (latched), urutan penanganan sesuai SOP adalah...',
        options: ['Langsung menekan tombol Clear lalu menyalakan kembali pompa yang trip', 'Menghentikan seluruh unit flokulasi dan filtrasi secara bersamaan di IPA', 'Jalankan pompa cadangan, periksa penyebab, tekan Reset, baru Clear', 'Hanya mengakui alarm lalu membiarkan pompa tetap dalam kondisi mati'],
        correctIndex: 2,
        explanation: 'SOP pompa trip: alihkan segera ke pompa cadangan, periksa kelistrikan, tekan Reset, baru Clear alarm.',
      },
    ],
  },
  {
    code: 'IPA-02',
    name: 'Menyalakan Intake & Aliran Baku',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Mudah · 1,0x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Menghidupkan pompa intake air baku dan mencapai debit target stabil.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Instalasi baru selesai masa perawatan. Nyalakan pompa intake untuk memulai produksi air baku.',
      objective: 'Hidupkan Pompa Intake 1, pastikan flash mixer aktif, dan jaga debit stabil di 75–100 L/s.',
      mentorQuote: '"Nyalakan pompa intake dengan tenang. Pastikan pengaduk cepat aktif agar siap menerima injeksi koagulan." — Pak Slamet',
    },
    debriefing: {
      success: 'Mantap! Pompa intake beroperasi lancar dan debit aliran air baku tercapai stabil sesuai kapasitas.',
      failure: 'Debit air baku belum stabil atau pompa intake tidak dihidupkan dengan benar.',
    },
    disturbances: [],
    hints: ['Pilih titik Intake pada diagram SCADA, lalu klik tombol "Start Pompa 1".'],
    quiz: [
      {
        id: 'q1',
        question: 'Komponen yang berfungsi menyaring sampah kasar di bibir saluran intake adalah...',
        options: ['Venturi flow meter intake', 'Bar screen saringan sampah', 'Plate settler bak pengendap', 'Orifice dosing plat kimia'],
        correctIndex: 1,
        explanation: 'Bar screen menahan sampah kasar sebelum masuk ke pipa hisap pompa intake.',
      },
      {
        id: 'q2',
        question: 'Mengapa pompa intake dilengkapi unit cadangan (standby)?',
        options: ['Untuk menggantikan fungsi katup PRV pada jaringan pipa distribusi kota', 'Menjamin kontinuitas pasokan air baku bila satu pompa dirawat', 'Untuk menaikkan pH air baku sebelum masuk unit koagulasi', 'Agar waktu detensi bak sedimentasi berkurang menjadi setengahnya saja'],
        correctIndex: 1,
        explanation: 'Prinsip redundansi (duty/standby) menjamin keandalan suplai air baku tanpa putus.',
      },
      {
        id: 'q3',
        question: 'SOP pengoperasian pompa sentrifugal melarang menjalankan pompa dalam keadaan...',
        options: ['Kering tanpa air atau saat katup hisap tertutup penuh', 'Tersambung penuh ke panel proteksi relai beban lebih termal', 'Katup hisap terbuka penuh dan ruang impeler terisi air', 'Tekanan hisap dan debit aliran berada pada titik desain'],
        correctIndex: 0,
        explanation: 'Dry running akan merusak mechanical seal pompa seketika akibat panas berlebih.',
      },
      {
        id: 'q4',
        question: 'Apa dampak jika debit intake melebihi kapasitas desain pengolahan?',
        options: ['Efisiensi pengendapan lumpur meningkat tajam di dalam bak clarifier', 'Waktu detensi sedimentasi berkurang sehingga flok terbawa lolos ke filter', 'Kadar sisa klorin bebas di tangki reservoir otomatis menjadi nol', 'Headloss media filter turun drastis karena kecepatan aliran sangat tinggi'],
        correctIndex: 1,
        explanation: 'Kelebihan debit mempercepat aliran dan membuat flok terbawa ke saringan filter.',
      },
      {
        id: 'q5',
        question: 'Debit normal desain intake pada instalasi SimSCADA-Air ini adalah...',
        options: ['25–40 L/s', '75–100 L/s', '180–220 L/s', '450–600 L/s'],
        correctIndex: 1,
        explanation: 'Debit operasi normal desain adalah 75–100 L/s.',
      },
    ],
  },
  {
    code: 'IPA-03',
    name: 'Dosis Koagulan Kondisi Normal',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Sedang · 1,5x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Mengatur dosis koagulan PAC dan pengadukan sampai kekeruhan air olahan < 3,0 NTU.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Air baku sungai memiliki kekeruhan 25,0 NTU. Anda bertugas mengoptimalkan dosis koagulan PAC dan menjaga pH tetap 6,8–7,5.',
      objective: 'Atur setpoint dosis koagulan ke 25–30 mg/L dan pastikan pengaduk lambat beroperasi.',
      mentorQuote: '"Dosis koagulan yang pas adalah kunci kebersihan air dan efisiensi bahan kimia." — Pak Slamet',
    },
    debriefing: {
      success: 'Luar biasa! Kekeruhan air olahan stabil di angka 1,2 NTU, memenuhi baku mutu Permenkes.',
      failure: 'Dosis koagulan belum optimal sehingga kekeruhan belum memenuhi syarat.',
    },
    disturbances: [],
    hints: ['Pilih unit Koagulasi, atur setpoint dosis koagulan ke 28 mg/L.'],
    quiz: [
      {
        id: 'q1',
        question: 'Metode laboratorium baku untuk menentukan dosis koagulan optimum adalah...',
        options: ['Uji titrasi alkalinitas asidimetri', 'Jar test koagulasi-flokulasi laboratorium', 'Uji spektrofotometri residu klorin', 'Uji bakteriologis koloni Coliform'],
        correctIndex: 1,
        explanation: 'Jar test mensimulasikan pembubuhan koagulan di laboratorium untuk menentukan dosis optimum.',
      },
      {
        id: 'q2',
        question: 'Jika dosis koagulan diberikan berlebihan tanpa koreksi kapur, nilai pH air akan...',
        options: ['Naik menjadi basa kuat (> 9,0)', 'Turun menjadi asam (< 6,5)', 'Tetap stabil di angka netral 7,0', 'Berfluktuasi mengikuti tekanan pompa distribusi'],
        correctIndex: 1,
        explanation: 'Koagulan mengonsumsi alkalinitas air sehingga menurunkan nilai pH.',
      },
      {
        id: 'q3',
        question: 'Dosis koagulan PAC tipikal untuk kekeruhan air baku normal 25,0 NTU adalah...',
        options: ['3–8 mg/L', '20–30 mg/L', '55–75 mg/L', '120–150 mg/L'],
        correctIndex: 1,
        explanation: 'Untuk air baku normal 20–30 NTU, dosis PAC tipikal berkisar 20–30 mg/L.',
      },
      {
        id: 'q4',
        question: 'Waktu pengadukan cepat pada koagulasi berlangsung selama...',
        options: ['30–60 detik', '10–15 menit', '45–60 menit', '2–3 jam'],
        correctIndex: 0,
        explanation: 'Flash mixing adalah reaksi dispersi kilat selama 30–60 detik.',
      },
      {
        id: 'q5',
        question: 'Standar rentang pH air minum yang dipersyaratkan Permenkes No. 2/2023 adalah...',
        options: ['4,5–6,0', '6,5–8,5', '8,6–9,8', '5,0–7,0'],
        correctIndex: 1,
        explanation: 'Baku mutu pH air minum adalah 6,5–8,5.',
      },
    ],
  },
  {
    code: 'IPA-04',
    name: 'Jaga Filter, Lakukan Backwash',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Sedang · 1,5x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Membaca kenaikan headloss filter dan menjalankan backwash bergantian.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Filter Pasir 1 telah beroperasi 36 jam. Indikator headloss naik mendekati 1,85 m.',
      objective: 'Jalankan prosedur pencucian balik (Backwash) pada Filter 1 sambil memastikan Filter 2 tetap beroperasi.',
      mentorQuote: '"Jangan pernah mencuci dua filter sekaligus agar aliran produksi air tidak terputus." — Pak Slamet',
    },
    debriefing: {
      success: 'Pencucian filter berjalan sempurna. Headloss kembali normal dan kejernihan air terjaga.',
      failure: 'Headloss filter melebihi batas atau kedua filter dimatikan bersamaan.',
    },
    disturbances: [],
    hints: ['Pilih unit Filtrasi di SCADA panel, lalu klik tombol "Backwash Filter".'],
    quiz: [
      {
        id: 'q1',
        question: 'Tanda fisik utama media filter pasir cepat sudah jenuh adalah...',
        options: ['Nilai pH air olahan naik tinggi melebihi batas 8,5', 'Kenaikan headloss melewati batas aman dan laju filtrasi turun', 'Sisa klorin bebas di reservoir naik melebihi 1,0 mg/L', 'Debit pompa intake air baku meningkat melebihi 120 L/s'],
        correctIndex: 1,
        explanation: 'Tersumbatnya pori media pasir oleh kotoran menyebabkan kehilangan tekan (headloss) naik.',
      },
      {
        id: 'q2',
        question: 'Media filter ganda (dual media) umumnya terdiri atas...',
        options: ['Pasir silika dan butiran antrasit', 'Karbon aktif dan batu kapur', 'Zeolit sintetis dan resin kation', 'Pasir kuarsa dan membran ultrafiltrasi'],
        correctIndex: 0,
        explanation: 'Antrasit (lapisan atas) dan pasir silika (lapisan bawah) membentuk filter kedalaman.',
      },
      {
        id: 'q3',
        question: 'Mengapa backwash tidak boleh dilakukan serentak pada semua bak filter?',
        options: ['Karena kadar sisa klorin di reservoir akan melampaui 0,5 mg/L', 'Menghindari terhentinya pasokan air olahan ke reservoir secara total', 'Karena kecepatan pengaduk cepat koagulasi akan langsung turun otomatis', 'Agar selimut lumpur di bak sedimentasi tidak ikut mengendap'],
        correctIndex: 1,
        explanation: 'Sistem pencucian bergantian (staggered backwash) menjamin kontinuitas suplai ke reservoir.',
      },
      {
        id: 'q4',
        question: 'Tujuan ekspansi media saat siklus backwash dijalankan adalah...',
        options: ['Memadatkan lapisan pasir silika agar pori media semakin rapat', 'Menguraikan butiran media 20–30% agar kotoran terjebak dapat terlepas', 'Menguras seluruh cadangan air bersih di dalam tangki reservoir', 'Menetralkan sisa koagulan PAC yang tertinggal di bak flokulasi'],
        correctIndex: 1,
        explanation: 'Ekspansi media membebaskan partikel lumpur yang menempel pada butiran antrasit dan pasir.',
      },
      {
        id: 'q5',
        question: 'Air bilasan awal hasil backwash sebaiknya dialirkan ke...',
        options: ['Langsung menuju ke dalam tangki reservoir air minum bersih', 'Saluran drainase menuju bak pengolah lumpur atau sludge lagoon', 'Pipa distribusi Zona 1 untuk membantu menaikkan tekanan layanan', 'Sisi hisap pompa intake agar diolah ulang tanpa pengendapan'],
        correctIndex: 1,
        explanation: 'Air bekas cucian filter mengandung konsentrasi padatan tinggi sehingga harus dibuang ke unit pengolah lumpur.',
      },
    ],
  },
  {
    code: 'IPA-05',
    name: 'Klorinasi Tepat & Residu Aman',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Sedang · 1,5x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Mengatur dosis klor hingga sisa klor bebas berada di rentang 0,2–0,5 mg/L sesuai Permenkes.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Air olahan siap masuk ke reservoir penampungan. Pastikan sisa klorin bebas terukur stabil di 0,3–0,4 mg/L.',
      objective: 'Atur setpoint dosing klorin pada rentang 1,2–1,5 mg/L hingga sisa klor bebas terukur stabil.',
      mentorQuote: '"Klorin adalah benteng terakhir melawan patogen. Dosis kurang berbahaya bagi warga, dosis lebih menimbulkan bau kaporit menyengat." — Pak Slamet',
    },
    debriefing: {
      success: 'Bagus! Sisa klor stabil di 0,38 mg/L, memenuhi ketentuan Permenkes No. 2/2023 secara presisi.',
      failure: 'Sisa klor bebas berada di luar batas 0,2–0,5 mg/L.',
    },
    disturbances: [],
    hints: ['Pilih unit Desinfeksi di diagram HMI, atur setpoint dosis klor ke 1,3 mg/L.'],
    quiz: [
      {
        id: 'q1',
        question: 'Dua bentuk senyawa klorin aktif yang berperan sebagai desinfektan utama dalam air adalah...',
        options: ['Natrium klorida dan kalsium karbonat', 'Kalsium hidroksida dan aluminium sulfat', 'Asam hipoklorit dan ion hipoklorit', 'Kloramin anorganik dan polialuminium klorida'],
        correctIndex: 2,
        explanation: 'HOCl dan OCl⁻ merupakan komponen sisa klor bebas aktif dalam desinfeksi air minum.',
      },
      {
        id: 'q2',
        question: 'Sisa klor bebas di titik terjauh jaringan distribusi disarankan minimal tetap sebesar...',
        options: ['0,20 mg/L', '0,05 mg/L', '1,20 mg/L', '2,50 mg/L'],
        correctIndex: 0,
        explanation: 'Minimal 0,20 mg/L sisa klor bebas mencegah rekontaminasi bakteri di sepanjang pipa.',
      },
      {
        id: 'q3',
        question: 'Waktu kontak minimum yang disyaratkan untuk desinfeksi klorin di reservoir adalah...',
        options: ['Kontak 1–2 menit', 'Kontak 5–10 menit', 'Kontak 12–18 jam', 'Minimal 30 menit'],
        correctIndex: 3,
        explanation: 'Waktu kontak minimal 30 menit diperlukan agar proses inaktivasi mikroorganisme efektif.',
      },
      {
        id: 'q4',
        question: 'Jika pH air terlalu basa (> 8,5), efektivitas desinfeksi klorin akan...',
        options: ['Meningkat tajam karena reaksi oksidasi klor berlangsung lebih cepat', 'Menurun akibat perubahan HOCl menjadi ion OCl⁻ yang lebih lemah', 'Tetap stabil selama debit intake dijaga pada angka 100 L/s', 'Meningkat dua kali lipat seiring turunnya tingkat kekeruhan air baku'],
        correctIndex: 1,
        explanation: 'Pada pH basa (> 8,5), klorin bergeser menjadi OCl⁻ yang jauh kurang efektif dibanding HOCl.',
      },
      {
        id: 'q5',
        question: 'Baku mutu rentang sisa klor bebas pada air reservoir menurut Permenkes No. 2/2023 adalah...',
        options: ['0,05–0,15 mg/L', '0,60–1,20 mg/L', '0,20–0,50 mg/L', '1,50–2,00 mg/L'],
        correctIndex: 2,
        explanation: 'Rentang baku mutu sisa klor bebas adalah 0,20–0,50 mg/L.',
      },
    ],
  },
  {
    code: 'IPA-06',
    name: 'Gangguan: Lonjakan Kekeruhan Air Baku',
    level: 3,
    levelName: 'Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Menaikkan dosis koagulan PAC dan menyesuaikan pH saat terjadi banjir lumpur di hulu.',
    durationLimitSec: 510, // 8 menit 30 detik
    passScore: 70,
    briefing: {
      situation: 'Hujan lebat di hulu sungai menyebabkan banjir bandang. Kekeruhan air baku melonjak tiba-tiba dari 20,0 NTU hingga 185,0 NTU!',
      objective: 'Akui alarm, naikkan dosis koagulan PAC ke 48 mg/L, atur dosis kapur ke 8,5 mg/L (pH 7,20), dan turunkan debit intake ke 75 L/s agar kekeruhan air olahan kembali normal.',
      mentorQuote: '"Alarm akan berbunyi kencang! Segera akui alarm, naikkan dosis koagulan, dan tunggu 10 detik stabil hingga alarm auto-clear." — Pak Slamet',
    },
    debriefing: {
      success: 'Kerja luar biasa! Tindakan koreksi Anda menjaga mutu air olahan pulih di bawah ambang 3,0 NTU dan memenuhi syarat Lencana Respons Kilat.',
      failure: 'Kekeruhan air olahan melampaui ambang batas 3,0 NTU atau penanganan alarm tidak sesuai urutan SOP.',
    },
    disturbances: [
      {
        id: 'dist-turbidity-spike',
        name: 'Lonjakan Kekeruhan Air Baku (185,0 NTU)',
        triggerTimeSec: 75, // 01:15
        type: 'kekeruhan_lonjakan',
        description: 'Kekeruhan air baku naik tajam ke 185,0 NTU memicu alarm sedang, disusul alarm tinggi pada air olahan.',
        expectedActions: [
          'Akui alarm kekeruhan air baku pada 01:25',
          'Akui alarm air olahan pada 01:50',
          'Naikkan dosis PAC dari 20 ke 48 mg/L pada 02:10 (respons 25 detik)',
          'Koreksi pH dengan kapur 8,5 mg/L pada 02:25',
          'Turunkan debit intake ke 75 L/s pada 02:40',
        ],
      },
    ],
    hints: [
      'Segera tekan tombol ACK pada banner alarm begitu muncul.',
      'Buka panel Koagulasi, naikkan setpoint dosis PAC ke 48 mg/L.',
      'Sistem akan otomatis menghapus alarm (Auto-Clear) setelah kekeruhan air olahan ≤ 2,7 NTU selama 10 detik berturut-turut.',
    ],
    quiz: [
      {
        id: 'q1',
        question: 'Ketika kekeruhan air baku melonjak dari 20,0 ke 185,0 NTU, tindakan pertama operator adalah...',
        options: ['Menutup seluruh katup keluar reservoir agar air bersih tetap tersimpan', 'Akui alarm dan naikkan dosis PAC sesuai jar test', 'Menghentikan motor flash mixer segera untuk mencegah pecahnya mikroflok air', 'Membuka valve blowdown lumpur secara kontinu tanpa penyesuaian dosis kimia'],
        correctIndex: 1,
        explanation: 'SOP tanggap darurat: acknowledge alarm, lalu segera sesuaikan dosis koagulan PAC dan pH.',
      },
      {
        id: 'q2',
        question: 'Berapa target waktu respons skenario pada misi IPA-06 untuk meraih lencana Respons Kilat?',
        options: ['120 detik dengan tindakan benar pertama < 60 detik', '60 detik (tindakan benar pertama < 30 detik)', '180 detik dengan tindakan benar pertama < 90 detik', '30 detik dengan tindakan benar pertama < 15 detik'],
        correctIndex: 1,
        explanation: 'Target skenario adalah 60 detik, syarat lencana adalah tindakan benar pertama < 50% target (yaitu < 30 detik).',
      },
      {
        id: 'q3',
        question: 'Pada SimSCADA-Air, bagaimana alarm lonjakan kekeruhan air olahan akan clear?',
        options: ['Menekan tombol Manual Clear meskipun kekeruhan air masih di atas 3,0 NTU', 'Otomatis clear setelah kekeruhan air olahan ≤ 2,7 NTU selama 10 detik', 'Otomatis clear tepat lima detik setelah tombol ACK ditekan oleh operator', 'Hanya dapat clear setelah seluruh pompa intake air baku dimatikan sementara'],
        correctIndex: 1,
        explanation: 'Sistem SCADA modern menerapkan auto-clear dengan deadband ≤ 2,7 NTU dan timer stabilisasi 10 detik.',
      },
      {
        id: 'q4',
        question: 'Apa akibatnya jika tombol Manual Clear ditekan saat kekeruhan air olahan masih 3,4 NTU?',
        options: ['Alarm langsung terhapus dan dihitung sistem sebagai kejadian auto-clear otomatis', 'Ditolak dengan pesan "Penyebab belum ditangani" dan mengurangi skor alarm', 'Dosis koagulan PAC otomatis dinaikkan ke 50 mg/L oleh pengendali SCADA', 'Status prioritas alarm langsung diturunkan dari Tinggi menjadi level Info'],
        correctIndex: 1,
        explanation: 'Manual clear pada kondisi proses abnormal ditolak dan dicatat sebagai kesalahan penanganan alarm.',
      },
      {
        id: 'q5',
        question: 'Mengapa menurunkan debit intake dari 100 L/s ke 75 L/s membantu saat banjir lumpur ekstrem?',
        options: ['Menambah waktu tinggal hidrolis di bak sedimentasi agar flok mengendap', 'Menurunkan dosis kebutuhan klorin di reservoir bersih hingga 50 persen', 'Menaikkan kecepatan putar pengaduk lambat flokulator secara otomatis di SCADA', 'Mengurangi headloss filter pasir cepat tanpa perlu menjalankan proses backwash'],
        correctIndex: 0,
        explanation: 'Menurunkan debit memperpanjang hydraulic retention time bak pengendap sehingga pengendapan flok lebih optimal.',
      },
    ],
  },
  {
    code: 'IPA-07',
    name: 'Gangguan: Pompa Intake Trip',
    level: 3,
    levelName: 'Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Menghadapi trip pompa intake, mengalihkan ke pompa standby, dan mereset proteksi.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Pompa Intake 1 mengalami trip tiba-tiba akibat beban lebih. Aliran air baku berhenti!',
      objective: 'Akui alarm, alihkan operasional ke Pompa Intake 2 (Standby), periksa kelistrikan, tekan tombol Reset Pompa, lalu clear alarm.',
      mentorQuote: '"Pompa trip memiliki alarm berstatus terkunci (latched). Kamu tidak bisa menghapus alarm sebelum menyalakan pompa cadangan dan menekan tombol Reset Pompa!" — Pak Slamet',
    },
    debriefing: {
      success: 'Respon tepat! Pompa cadangan segera aktif dan sistem proteksi berhasil direset tanpa memicu gangguan ke unit hilir.',
      failure: 'Anda lupa menekan tombol Reset Pompa atau pasokan air baku terhenti terlalu lama.',
    },
    disturbances: [
      {
        id: 'dist-intake-trip',
        name: 'Pompa Intake 1 Trip',
        triggerTimeSec: 20,
        type: 'pompa_trip',
        description: 'Pompa Intake 1 mengalami trip overload kelistrikan.',
        expectedActions: ['Akui alarm kritis', 'Start Pompa Intake 2', 'Tekan Reset Pompa Intake', 'Clear alarm trip'],
      },
    ],
    hints: ['Pilih unit Intake, nyalakan Pompa 2.', 'Tekan tombol "Reset Pompa" di panel Intake sebelum menekan Clear alarm.'],
    quiz: [
      {
        id: 'q1',
        question: 'Apa arti status alarm terkunci (latched alarm) pada kasus pompa trip?',
        options: ['Alarm hanya dapat hilang apabila seluruh simulasi diulang lagi dari awal', 'Alarm baru bisa di-clear setelah tombol Reset proteksi pompa ditekan', 'Alarm otomatis terhapus dalam sepuluh detik setelah pompa cadangan mulai menyala', 'Alarm akan berpindah menjadi prioritas Info sesudah tombol ACK ditekan operator'],
        correctIndex: 1,
        explanation: 'Latched alarm membutuhkan intervensi reset proteksi eksplisit agar kondisi gangguan kelistrikan/mekanis benar-benar terverifikasi.',
      },
      {
        id: 'q2',
        question: 'Langkah pertama saat pompa intake utama mendadak trip adalah...',
        options: ['Akui alarm lalu segera nyalakan pompa cadangan (standby)', 'Menghentikan pompa distribusi agar level air reservoir tidak berubah', 'Langsung menekan Clear alarm sebelum memeriksa panel proteksi pompa', 'Menurunkan setpoint dosis koagulan PAC hingga menjadi nol mg/L'],
        correctIndex: 0,
        explanation: 'Menghidupkan unit cadangan menjaga kontinuitas aliran air baku sambil melakukan pemeriksaan proteksi.',
      },
      {
        id: 'q3',
        question: 'Urutan SOP penanganan pompa trip di SimSCADA-Air adalah...',
        options: ['Clear Alarm, lalu tekan Reset Pompa, lalu jalankan pompa cadangan', 'Jalankan pompa cadangan, periksa proteksi, tekan Reset Pompa, lalu Clear', 'Reset Pompa, tekan Clear Alarm, lalu matikan pengaduk cepat koagulasi', 'Akui Alarm, turunkan debit ke 0 L/s, lalu tekan tombol Clear'],
        correctIndex: 1,
        explanation: 'SOP resmi: alihkan beban ke pompa cadangan, periksa proteksi, tekan Reset, baru lakukan Manual Clear.',
      },
      {
        id: 'q4',
        question: 'Apa yang terjadi jika operator menekan Clear pada alarm pompa trip sebelum tombol Reset ditekan?',
        options: ['Alarm langsung terhapus sempurna dan nilai Penanganan Alarm tetap dihitung penuh', 'Clear ditolak bertuliskan "Penyebab belum ditangani" dan mengurangi skor alarm', 'Operator mendapat penalti -15 poin tindakan tidak aman dan sesi dihentikan', 'Pompa cadangan yang baru dinyalakan otomatis dimatikan kembali oleh relai proteksi'],
        correctIndex: 1,
        explanation: 'Menekan Clear sebelum penyebab ditangani ditolak sistem dengan pesan "Penyebab belum ditangani" dan memengaruhi komponen Penanganan Alarm (15%), bukan penalti tindakan tidak aman.',
      },
      {
        id: 'q5',
        question: 'Apa fungsi tombol Reset Pompa pada panel SCADA?',
        options: ['Menghapus seluruh riwayat log tindakan operator selama sesi simulasi berlangsung', 'Mereset relai proteksi overload motor setelah kondisi trip terverifikasi', 'Membuka katup blowdown lumpur pada dasar bak sedimentasi secara otomatis', 'Mengubah setpoint pompa cadangan menjadi dua kali lipat kapasitas nominal'],
        correctIndex: 1,
        explanation: 'Reset melepaskan penguncian (latch) pada kontak relai proteksi kelistrikan motor.',
      },
    ],
  },
  {
    code: 'IPA-08',
    name: 'Gangguan: Dosis Klor Tidak Sesuai',
    level: 3,
    levelName: 'Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP)',
    track: ['ipa', 'terpadu'],
    trainingFocus: 'Mengatasi kegagalan pompa injeksi klorin dan memulihkan sisa klor bebas sebelum air masuk ke jaringan pipa.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Sensor telemetri mendeteksi sisa klor bebas anjlok hingga 0,08 mg/L (jauh di bawah batas 0,20 mg/L). Bahaya bakteri coliform!',
      objective: 'Akui alarm klorin kritis, periksa pompa dosing klor, naikkan setpoint dosing klorin ke 1,6 mg/L, dan pantau kenaikan sisa klorin bebas.',
      mentorQuote: '"Sisa klorin adalah indikator keselamatan air minum. Jangan biarkan air tanpa klorin lolos ke pipa pelanggan!" — Pak Slamet',
    },
    debriefing: {
      success: 'Desinfeksi berhasil dipulihkan! Sisa klorin kembali ke 0,35 mg/L, menjamin sterilitas pasokan air.',
      failure: 'Sisa klorin gagal dipulihkan ke rentang aman 0,2–0,5 mg/L.',
    },
    disturbances: [
      {
        id: 'dist-chlorine-drop',
        name: 'Sisa Klorin Anjlok',
        triggerTimeSec: 25,
        type: 'klor_salah',
        description: 'Dosing klorin drop memicu alarm kritis sisa klor bebas rendah.',
        expectedActions: ['Akui alarm klor kritis', 'Naikkan setpoint klorin ke 1,6 mg/L', 'Tunggu sisa klor stabil 0,35 mg/L'],
      },
    ],
    hints: ['Pilih unit Desinfeksi/Reservoir, geser setpoint dosis klor ke 1,6 mg/L.'],
    quiz: [
      {
        id: 'q1',
        question: 'Berapa batas minimum sisa klor bebas menurut Permenkes No. 2/2023?',
        options: ['0,05 mg/L', '0,20 mg/L', '0,80 mg/L', '1,50 mg/L'],
        correctIndex: 1,
        explanation: 'Batas minimal sisa klor bebas adalah 0,20 mg/L.',
      },
      {
        id: 'q2',
        question: 'Prioritas alarm untuk kondisi sisa klorin < 0,20 mg/L adalah...',
        options: ['Info', 'Sedang', 'Tinggi', 'Kritis'],
        correctIndex: 3,
        explanation: 'Berdasarkan standar manajemen alarm proses, sisa klor < 0,20 mg/L berkategori KRITIS.',
      },
      {
        id: 'q3',
        question: 'Apa bahaya utama jika sisa klorin bebas di reservoir habis (0,0 mg/L)?',
        options: ['Kekeruhan air olahan langsung melonjak tinggi melewati 10,0 NTU', 'Bakteri patogen berisiko berkembang biak di sepanjang pipa distribusi', 'Katup PRV pada jaringan distribusi otomatis menutup aliran penuh', 'Headloss saringan pasir cepat langsung meningkat drastis hingga jenuh'],
        correctIndex: 1,
        explanation: 'Ketiadaan residu klorin membuat air kehilangan perlindungan terhadap pertumbuhan mikroorganisme patogen.',
      },
      {
        id: 'q4',
        question: 'Berapa batas maksimal sisa klorin yang diizinkan agar tidak menimbulkan bau menyengat?',
        options: ['0,50 mg/L', '1,50 mg/L', '2,50 mg/L', '5,00 mg/L'],
        correctIndex: 0,
        explanation: 'Batas atas yang aman pada air olahan adalah 0,50 mg/L.',
      },
      {
        id: 'q5',
        question: 'Setelah menaikkan dosis klorin, reaksi pemulihan sisa klor bebas memerlukan...',
        options: ['Waktu kontak hidrolis hingga kadar residu stabil di rentang aman', 'Penutupan seluruh katup pompa intake air baku selama 15 menit', 'Pengaktifan siklus backwash bergantian pada kedua unit filter pasir cepat', 'Penurunan nilai pH air olahan ke bawah ambang batas 5,5'],
        correctIndex: 0,
        explanation: 'Reaksi kimia desinfeksi dan homogenisasi di reservoir memerlukan waktu kontak hidrolis.',
      },
    ],
  },
  {
    code: 'IPA-09',
    name: 'Misi Kelulusan Operator IPA',
    level: 5,
    levelName: 'Tingkat 5: Misi Kelulusan Ujian (Ujian · 3,0x XP)',
    track: ['ipa'],
    trainingFocus: 'Ujian komprehensif mengendalikan seluruh unit IPA dalam kondisi gangguan tak terduga tanpa tombol petunjuk.',
    durationLimitSec: 600,
    passScore: 80, // KKM Misi Kelulusan adalah 80!
    briefing: {
      situation: 'Ini adalah Ujian Kelulusan Praktik Jalur Operator IPA. Seluruh sistem akan diuji dengan skenario darurat majemuk.',
      objective: 'Atasi semua alarm, pertahankan mutu air < 3,0 NTU, jaga sisa klor 0,2–0,5 mg/L. Skor minimal kelulusan adalah 80!',
      mentorQuote: '"Kamu sendirian di ruang kontrol sekarang. Buktikan kompetensimu dan raih Piagam Kelulusan!" — Pak Slamet',
    },
    debriefing: {
      success: 'SELAMAT! Anda telah lulus Ujian Praktik Operator IPA dengan nilai di atas KKM 80. Berhak atas pengajuan Piagam Kelulusan!',
      failure: 'Skor Anda belum mencapai ambang kelulusan KKM 80. Evaluasi kesalahan Anda dan ulangi ujian.',
    },
    disturbances: [
      {
        id: 'dist-exam-ipa',
        name: 'Ujian Komprehensif IPA (Lonjakan Kekeruhan)',
        triggerTimeSec: 30,
        type: 'kekeruhan_lonjakan',
        description: 'Lonjakan kekeruhan air baku 185,0 NTU memicu alarm air olahan tinggi.',
        expectedActions: ['Atasi alarm sesuai SOP', 'Naikkan PAC dan jaga mutu air stabil'],
      },
      {
        id: 'dist-exam-ipa-cl',
        name: 'Ujian Komprehensif IPA (Fluktuasi Klorin)',
        triggerTimeSec: 90,
        type: 'klor_salah',
        description: 'Fluktuasi pompa dosing klor menyebabkan sisa klor turun di bawah 0,20 mg/L.',
        expectedActions: ['Periksa pompa dosing klor', 'Naikkan setpoint dosis klor'],
      },
    ],
    hints: [],
    quiz: [
      {
        id: 'q1',
        question: 'Ambang skor minimal (KKM) kelulusan untuk Misi Kelulusan Ujian adalah...',
        options: ['65 poin', '70 poin', '75 poin', '80 poin'],
        correctIndex: 3,
        explanation: 'Misi Kelulusan mewajibkan skor minimal 80 poin.',
      },
      {
        id: 'q2',
        question: 'Pengali XP untuk Misi Kelulusan Tingkat 5 adalah...',
        options: ['3,0x (Ujian)', '1,0x (Mudah)', '1,5x (Sedang)', '2,5x (Berantai)'],
        correctIndex: 0,
        explanation: 'Tingkat 5 memberikan pengali XP tertinggi sebesar 3,0x.',
      },
      {
        id: 'q3',
        question: 'Apakah tombol Bantuan Petunjuk (-5 poin) diperbolehkan pada Misi Kelulusan?',
        options: ['Diperbolehkan maksimal satu kali saja dengan penalti pengurangan -5 poin', 'Dinonaktifkan pada misi ujian kelulusan demi menjaga objektivitas asesmen', 'Diperbolehkan bebas setelah waktu simulasi berjalan melewati lima menit', 'Aktif secara otomatis setiap kali ada alarm kritis yang muncul'],
        correctIndex: 1,
        explanation: 'Pada misi ujian kelulusan, tombol petunjuk dinonaktifkan agar kemandirian peserta teruji.',
      },
      {
        id: 'q4',
        question: 'Parameter mutu utama air minum yang wajib memenuhi standar Permenkes No. 2/2023 adalah...',
        options: ['Kekeruhan < 5,0 NTU, pH 5,5–9,0, Sisa klor 0,05–1,0 mg/L', 'Kekeruhan < 10,0 NTU, pH 6,0–8,0, Sisa klor > 1,5 mg/L', 'Kekeruhan < 3,0 NTU, pH 6,5–8,5, Sisa klor 0,20–0,50 mg/L', 'Kekeruhan < 1,0 NTU, pH tepat 7,00, Sisa klor 1,0–2,0 mg/L'],
        correctIndex: 2,
        explanation: 'Tiga parameter kunci fisika-kimia baku mutu air minum instalasi adalah kekeruhan < 3,0 NTU, pH 6,5–8,5, dan sisa klor 0,20–0,50 mg/L.',
      },
      {
        id: 'q5',
        question: 'Setelah lulus Misi Kelulusan dan Post-Test, piagam akan terbit setelah...',
        options: ['Peserta mengunduh langsung tanpa verifikasi ketika lulus ujian Pre-Test', 'Mendapat verifikasi instruktur dan pengesahan oleh pimpinan lembaga diklat', 'Peserta menyelesaikan minimal tiga misi pengenalan dengan nilai ≥ 70', 'Admin lembaga mereset nilai Pre-Test menjadi nilai baseline yang baru'],
        correctIndex: 1,
        explanation: 'Kebijakan verifikasi mensyaratkan persetujuan instruktur sebelum piagam resmi terbit.',
      },
    ],
  },

  // --- JALUR DISTRIBUSI (7 MISI) ---
  {
    code: 'DST-01',
    name: 'Kenali Jaringan Distribusi',
    level: 1,
    levelName: 'Tingkat 1: Pengenalan (Mudah · 1,0x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Membuka narasi telemetri pipa, pompa distribusi, PRV, dan titik pantau zona.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Shift orientasi Jaringan Distribusi. Pelajari pembagian zona pipa dan stasiun pompa pendorong kota.',
      objective: 'Buka narasi titik kontrol Pompa Distribusi, Valve PRV, dan Titik Pantau Jaringan.',
      mentorQuote: '"Jaringan pipa adalah labirin di bawah tanah kota. Pahami tekanan dan debit sebelum mengoperasikan pompa distribusi." — Pak Slamet',
    },
    debriefing: {
      success: 'Bagus! Anda memahami skema pembagian zona distribusi dan batasan tekanan pipa.',
      failure: 'Buka narasi semua titik kontrol distribusi untuk menyelesaikan misi ini.',
    },
    disturbances: [],
    hints: ['Klik titik kontrol Pompa Distribusi, PRV, dan Titik Pantau Jaringan.'],
    quiz: [
      {
        id: 'q1',
        question: 'Tujuan utama pembagian area pelayanan menjadi District Metered Area (DMA) adalah...',
        options: ['Memudahkan pemantauan kebocoran air (NRW) dan manajemen tekanan zona', 'Menaikkan tekanan pipa utama distribusi hingga melampaui batas desain', 'Menghilangkan kebutuhan injeksi klorinasi sekunder di tangki reservoir bersih', 'Menggabungkan seluruh aliran air baku langsung menuju pipa pelanggan'],
        correctIndex: 0,
        explanation: 'DMA membagi jaringan menjadi zona terukur untuk pengendalian kehilangan air dan tekanan.',
      },
      {
        id: 'q2',
        question: 'Fungsi utama Pressure Reducing Valve (PRV) di jaringan distribusi adalah...',
        options: ['Menaikkan tekanan pipa buang pompa distribusi hingga batas maksimum', 'Menyaring sedimen halus sebelum air masuk ke meteran pelanggan', 'Mereduksi serta menstabilkan tekanan hilir agar pipa tidak pecah', 'Menghitung total debit pemakaian air warga pada jam puncak'],
        correctIndex: 2,
        explanation: 'PRV menjaga tekanan hilir tetap stabil pada rentang aman.',
      },
      {
        id: 'q3',
        question: 'Rentang tekanan layanan yang ideal pada jaringan pipa distribusi pelanggan adalah...',
        options: ['0,5–1,2 bar', '2,0–2,8 bar', '4,5–6,0 bar', '8,0–10,0 bar'],
        correctIndex: 1,
        explanation: 'Tekanan layanan 2,0–2,8 bar memadai untuk mengalirkan air hingga lantai atas tanpa merusak pipa.',
      },
      {
        id: 'q4',
        question: 'Tekanan di bawah 1,0 bar pada jaringan pipa dapat menyebabkan...',
        options: ['Peningkatan efisiensi daya pompa sentrifugal distribusi secara otomatis', 'Akumulasi sisa klorin bebas berlebih di ujung jaringan pipa', 'Penurunan kekeruhan air olahan di unit saringan pasir cepat', 'Aliran terhenti ke pelanggan dan risiko intrusi air tanah'],
        correctIndex: 3,
        explanation: 'Tekanan negatif atau terlalu rendah berisiko menghisap air tanah kotor ke dalam pipa.',
      },
      {
        id: 'q5',
        question: 'Kehilangan air yang disebabkan pipa bocor fisik tergolong dalam...',
        options: ['Kehilangan air non-fisik akibat kesalahan baca meter', 'Pemakaian resmi air yang tidak bermeter pelanggan', 'Kehilangan air fisik akibat kebocoran teknis jaringan', 'Kehilangan tekanan aliran akibat gesekan katup PRV'],
        correctIndex: 2,
        explanation: 'Kebocoran pipa dan tangki termasuk Real Loss (kehilangan air fisik).',
      },
    ],
  },
  {
    code: 'DST-02',
    name: 'Pompa Distribusi & Level Reservoir',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Mudah · 1,0x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Menghidupkan pompa distribusi dan menjaga keseimbangan level reservoir.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Pagi hari menjelang jam sibuk warga. Nyalakan pompa distribusi P-101 dan pantau tekanan pipa keluar.',
      objective: 'Hidupkan Pompa Distribusi 1, jaga tekanan buang 3,8–4,2 bar, pastikan level reservoir > 50%.',
      mentorQuote: '"Pastikan katup buang terbuka sebelum menyalakan pompa distribusi agar tidak terjadi shut-off head." — Pak Slamet',
    },
    debriefing: {
      success: 'Stasiun pompa distribusi beroperasi optimal menyuplai kebutuhan air warga.',
      failure: 'Tekanan buang pompa belum tercapai atau level reservoir drop.',
    },
    disturbances: [],
    hints: ['Pilih stasiun Pompa Distribusi, klik "Start Pompa 1".'],
    quiz: [
      {
        id: 'q1',
        question: 'Level reservoir di bawah 20% berbahaya bagi pompa distribusi karena...',
        options: ['Kadar sisa klorin langsung melonjak tinggi di atas 2,0 mg/L', 'Dapat memicu kavitasi dan pompa beroperasi kering (dry running)', 'Katup PRV pada zona pelanggan otomatis terkunci tertutup penuh', 'Kekeruhan air olahan di dalam bak sedimentasi langsung meningkat'],
        correctIndex: 1,
        explanation: 'Kavitasi merusak impeler pompa akibat tekanan hisap (NPSH) yang terlalu rendah.',
      },
      {
        id: 'q2',
        question: 'Tekanan normal discharge pompa distribusi pada instalasi ini adalah...',
        options: ['1,0–1,8 bar', '3,8–4,2 bar', '6,5–8,0 bar', '0,5–0,9 bar'],
        correctIndex: 1,
        explanation: 'Tekanan buang stasiun pompa distribusi normal berkisar 3,8–4,2 bar.',
      },
      {
        id: 'q3',
        question: 'Ketika kebutuhan pelanggan menurun saat tengah malam, tindakan operator stasiun pompa adalah...',
        options: ['Menjalankan seluruh unit pompa cadangan distribusi secara paralel', 'Mengurangi jumlah pompa jalan atau menurunkan frekuensi VFD', 'Menutup katup keluar reservoir secara total sepanjang malam', 'Menaikkan setpoint katup PRV hingga di atas 3,5 bar'],
        correctIndex: 1,
        explanation: 'Menyesuaikan kapasitas pompa dengan kurva fluktuasi harian pelanggan menekan pemborosan daya dan kebocoran.',
      },
      {
        id: 'q4',
        question: 'Gejala water hammer pada sistem perpipaan biasanya dipicu oleh...',
        options: ['Penutupan katup mendadak atau pompa berhenti tanpa check valve', 'Penambahan dosis koagulan PAC berlebih di bak pengaduk cepat', 'Pengaturan sisa klorin bebas stabil pada angka 0,35 mg/L', 'Pembukaan valve blowdown dasar bak sedimentasi selama satu menit'],
        correctIndex: 0,
        explanation: 'Perubahan momentum aliran mendadak menciptakan gelombang kejut tekanan destruktif.',
      },
      {
        id: 'q5',
        question: 'Alat pengaman yang dipasang untuk meredam gelombang pukulan air (water hammer) adalah...',
        options: ['Tangki surge peredam gelombang kejut', 'Saringan bar screen saluran intake', 'Pelat pengendap lamella unit sedimentasi', 'Pompa dosing injeksi bahan kimia'],
        correctIndex: 0,
        explanation: 'Air chamber atau surge tank menyerap dan meredam lonjakan tekanan transien di pipa.',
      },
    ],
  },
  {
    code: 'DST-03',
    name: 'Atur Tekanan Jam Puncak',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Sedang · 1,5x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Mengatur 2 pompa distribusi jalan saat jam puncak pagi hari agar tekanan zona stabil.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Pukul 06.30 pagi: pemakaian air melonjak tajam (jam puncak aktivitas mandi dan memasak).',
      objective: 'Jalankan 2 pompa distribusi paralel dan setel PRV agar tekanan Zona 1 tetap 2,2–2,5 bar.',
      mentorQuote: '"Saat jam puncak, debit aliran berlipat ganda. Tambah pompa yang jalan dan awasi jangan sampai tekanan drop!" — Pak Slamet',
    },
    debriefing: {
      success: 'Pasokan air jam puncak sukses terpenuhi dengan tekanan merata di seluruh sambungan pelanggan.',
      failure: 'Tekanan zona pelanggan drop di bawah batas layanan minimum.',
    },
    disturbances: [],
    hints: ['Pilih stasiun Pompa Distribusi, aktifkan Pompa 1 dan Pompa 2 secara paralel.'],
    quiz: [
      {
        id: 'q1',
        question: 'Kapan jam puncak pemakaian air bersih umumnya terjadi di kawasan perkotaan?',
        options: ['Tengah malam sekitar pukul 01.00–03.00 dini hari', 'Pagi (06.00–08.00) dan sore hari (17.00–19.00)', 'Hanya pada siang hari pukul 12.00–14.00 WIB', 'Merata konstan tanpa fluktuasi sepanjang 24 jam'],
        correctIndex: 1,
        explanation: 'Kurva pemakaian diurnal menunjukkan dua puncak utama: pagi dan sore hari.',
      },
      {
        id: 'q2',
        question: 'Bila dua pompa yang sama dioperasikan secara paralel, yang meningkat signifikan adalah...',
        options: ['Tekanan buang naik dua kali lipat tanpa perubahan debit', 'Kekeruhan air baku di saluran intake meningkat drastis', 'Debit aliran (L/s) bertambah pada head kerja hampir sama', 'Kadar sisa klorin bebas di ujung pipa distribusi naik'],
        correctIndex: 2,
        explanation: 'Operasi paralel menggabungkan kapasitas debit aliran (L/s) pada head kerja sistem.',
      },
      {
        id: 'q3',
        question: 'Dampak tekanan berlebih pada jaringan saat jam non-puncak (malam hari) adalah...',
        options: ['Memperpanjang umur pakai seluruh sambungan pipa rumah pelanggan', 'Meningkatnya risiko pipa pecah dan kebocoran fisik (NRW)', 'Mengurangi nilai headloss di unit filtrasi pasir cepat IPA', 'Menjaga sisa klorin tetap 0,5 mg/L tanpa pembubuhan dosis'],
        correctIndex: 1,
        explanation: 'Tekanan malam hari yang terlalu tinggi memperbesar laju kehilangan air fisik dan risiko pecah pipa.',
      },
      {
        id: 'q4',
        question: 'Untuk mengendalikan tekanan berlebih pada malam hari, operator dapat...',
        options: ['Menutup seluruh katup intake air baku', 'Menurunkan setpoint PRV atau mematikan pompa tambahan', 'Menambah dosis koagulan PAC di flokulator', 'Membuka valve isolasi kebocoran secara penuh'],
        correctIndex: 1,
        explanation: 'Manajemen tekanan malam hari (Night Flow Management) menurunkan laju kebocoran.',
      },
      {
        id: 'q5',
        question: 'Faktor jam puncak (Peak Hour Factor) biasanya berkisar antara...',
        options: ['1,0–1,1 kali debit rata-rata harian', '1,5–2,5 kali debit rata-rata harian', '4,0–5,5 kali debit rata-rata harian', '8,0–10,0 kali debit rata-rata harian'],
        correctIndex: 1,
        explanation: 'Fluktuasi jam puncak umumnya berkisar 1,5 hingga 2,5 kali kebutuhan rata-rata.',
      },
    ],
  },
  {
    code: 'DST-04',
    name: 'Sisa Klor di Ujung Jaringan',
    level: 2,
    levelName: 'Tingkat 2: Operasi Normal (Sedang · 1,5x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Memastikan residu klorin di sambungan terjauh (dead-end) tidak habis.',
    durationLimitSec: 300,
    passScore: 70,
    briefing: {
      situation: 'Laporan telemetri: Sisa klorin di ujung Zona 2 mendekati 0,12 mg/L. Risiko rekontaminasi!',
      objective: 'Naikkan sedikit injeksi klorin di reservoir hingga residu di ujung jaringan terukur minimal 0,20 mg/L.',
      mentorQuote: '"Jarak tempuh pipa yang panjang menghabiskan klorin. Pastikan sampai di kran rumah terakhir klorin tetap tersisa!" — Pak Slamet',
    },
    debriefing: {
      success: 'Residu klorin di seluruh pelosok jaringan aman terlindungi sesuai standar Permenkes.',
      failure: 'Sisa klorin di ujung jaringan masih berada di bawah 0,20 mg/L.',
    },
    disturbances: [],
    hints: ['Pilih unit Desinfeksi/Reservoir, sesuaikan dosing klor ke 1,6 mg/L.'],
    quiz: [
      {
        id: 'q1',
        question: 'Penyebab utama hilangnya residu klorin sepanjang perjalanan pipa distribusi adalah...',
        options: ['Reaksi klorin dengan biofilm pipa, organik, dan waktu tinggal lama', 'Penurunan tekanan layanan katup PRV di bawah angka 2,5 bar', 'Kecepatan putaran motor pompa sentrifugal distribusi yang terlalu stabil', 'Kekeruhan air olahan keluar filter di bawah batas 1,0 NTU'],
        correctIndex: 0,
        explanation: 'Biofilm dinding pipa dan waktu detensi yang panjang mengonsumsi residu klorin (chlorine decay).',
      },
      {
        id: 'q2',
        question: 'Berapa batas minimum sisa klorin di titik keran terjauh pelanggan?',
        options: ['0,05 mg/L', '0,20 mg/L', '0,80 mg/L', '1,50 mg/L'],
        correctIndex: 1,
        explanation: 'Permenkes mewajibkan minimal 0,20 mg/L sisa klor bebas di titik keran pelanggan.',
      },
      {
        id: 'q3',
        question: 'Tindakan yang dapat dilakukan di titik pipa buntu (dead-end) dengan air stagnant adalah...',
        options: ['Flushing air secara rutin melalui hidran pembuangan ujung', 'Menutup katup isolasi utama seluruh zona selama 24 jam', 'Menurunkan setpoint katup pengurang tekanan PRV menjadi 0,5 bar', 'Menambah dosis koagulan PAC berlebih di dalam bak sedimentasi'],
        correctIndex: 0,
        explanation: 'Flushing berkala menguras air stagnant agar air segar berklorin masuk ke ujung pipa.',
      },
      {
        id: 'q4',
        question: 'Stasiun injeksi klorin sekunder (re-chlorination) biasanya dibangun jika...',
        options: ['Kadar kekeruhan air baku di sungai berada di bawah 20 NTU', 'Jaringan pipa terlalu luas sehingga injeksi di reservoir tidak mencukupi', 'Tekanan buang stasiun pompa distribusi utama melebihi batas 4,0 bar', 'Headloss unit saringan pasir cepat masih di bawah 1,0 meter'],
        correctIndex: 1,
        explanation: 'Booster chlorination menjaga kadar residu tetap ≥ 0,20 mg/L pada jaringan distribusi yang panjang.',
      },
      {
        id: 'q5',
        question: 'Bila sisa klorin 0,0 mg/L terdeteksi di suatu zona, bahaya kesehatan yang mengancam adalah...',
        options: ['Kenaikan nilai pH air olahan hingga melampaui batas 9,5', 'Perkembangbiakan bakteri patogen seperti E. coli penyebab penyakit diare', 'Pengendapan lumpur berlebih di dalam unit bak plate settler', 'Penurunan tekanan hisap pompa distribusi akibat gejala kavitasi air'],
        correctIndex: 1,
        explanation: 'Air tanpa klorin pelindung rentan terhadap pertumbuhan bakteri patogen penyebab waterborne disease.',
      },
    ],
  },
  {
    code: 'DST-05',
    name: 'Gangguan: Kebocoran Pipa Distribusi',
    level: 3,
    levelName: 'Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Mendeteksi pipa transmisi pecah dari anomali debit-tekanan dan mengisolasi katup ruas bocor.',
    durationLimitSec: 180,
    passScore: 70,
    briefing: {
      situation: 'Alarm Tinggi: Pipa transmisi diameter 300 mm di Zona 1 pecah akibat pekerjaan galian! Debit melonjak drastis, tekanan drop.',
      objective: 'Akui alarm, cari titik kebocoran, dan segera tutup Katup Isolasi Pipa Bocor dalam waktu target 60 detik.',
      mentorQuote: '"Lihat polanya: debit melonjak tapi tekanan jatuh itu pasti pipa pecah! Segera tutup katup isolasi ruas terkait!" — Pak Slamet',
    },
    debriefing: {
      success: 'Pipa bocor berhasil diisolasi dalam tempo kilat! Kehilangan air terminimalisir dan tekanan zona pulih.',
      failure: 'Tekanan jaringan drop terlalu lama atau katup isolasi tidak ditutup dengan benar.',
    },
    disturbances: [
      {
        id: 'dist-pipe-burst',
        name: 'Pipa Pecah Zona 1',
        triggerTimeSec: 15,
        type: 'pipa_bocor',
        description: 'Kebocoran besar pipa memicu lonjakan debit dan drop tekanan.',
        expectedActions: ['Akui alarm pipa pecah', 'Tutup Valve Isolasi Bocor dalam 60 dtk', 'Tunggu tekanan pulih stabil 10 dtk'],
      },
    ],
    hints: ['Pilih unit Valve PRV & Isolasi di SCADA panel.', 'Klik tombol "Tutup Valve Isolasi Bocor".'],
    quiz: [
      {
        id: 'q1',
        question: 'Pola data telemetri yang menandakan terjadinya pipa transmisi pecah secara mendadak adalah...',
        options: ['Tekanan zona naik tajam dan debit aliran turun ke nol', 'Kekeruhan air olahan di filter naik bersamaan dengan nilai pH', 'Debit aliran melonjak drastis disertai tekanan zona jatuh serentak', 'Sisa klorin bebas meningkat tinggi di ujung pipa distribusi'],
        correctIndex: 2,
        explanation: 'Pipa pecah menghilangkan tahanan hidrolik sehingga debit keluar melonjak sementara tekanan zona jatuh.',
      },
      {
        id: 'q2',
        question: 'Tindakan tanggap darurat pertama operator saat pipa pecah terkonfirmasi adalah...',
        options: ['Menutup katup isolasi ruas bocor untuk melokalisir area terdampak', 'Menaikkan setpoint PRV hingga 3,5 bar agar tekanan zona naik', 'Menyalakan pompa cadangan secara paralel tanpa menutup titik kebocoran', 'Menurunkan dosis injeksi klorin di reservoir hingga 0,2 mg/L'],
        correctIndex: 0,
        explanation: 'Isolasi sectional menghentikan kehilangan air di segmen bocor tanpa memadamkan seluruh jaringan.',
      },
      {
        id: 'q3',
        question: 'Berapa target waktu skenario penutupan katup isolasi pipa pecah untuk meraih lencana?',
        options: ['120 detik', '180 detik', '300 detik', '60 detik'],
        correctIndex: 3,
        explanation: 'Target waktu skenario darurat penutupan isolasi adalah 60 detik.',
      },
      {
        id: 'q4',
        question: 'Dampak buruk jika kebocoran besar dibiarkan berlangsung berjam-jam adalah...',
        options: ['Kadar sisa klorin bebas di ujung pipa meningkat sangat drastis', 'Reservoir cepat terkuras dan tekanan layanan ke pelanggan anjlok', 'Tekanan pipa distribusi pelanggan otomatis stabil pada angka 2,5 bar', 'Headloss pada unit filtrasi pasir cepat menurun dengan tajam'],
        correctIndex: 1,
        explanation: 'Kehilangan air masif mengosongkan cadangan reservoir, menjatuhkan tekanan kota, dan merusak infrastruktur.',
      },
      {
        id: 'q5',
        question: 'Setelah katup isolasi ditutup dan tekanan kembali normal, alarm akan...',
        options: ['Langsung terhapus seketika pada detik pertama tanpa verifikasi stabilitas', 'Berubah menjadi status terkunci (latched) yang memerlukan reset kelistrikan', 'Auto-clear otomatis setelah tekanan stabil normal selama 10 detik', 'Memicu alarm susulan pada unit flash mixer koagulasi'],
        correctIndex: 2,
        explanation: 'Sistem SCADA menerapkan auto-clear setelah parameter tekanan kembali normal dan stabil selama 10 detik.',
      },
    ],
  },
  {
    code: 'DST-06',
    name: 'Gangguan: Tekanan Jaringan Drop',
    level: 3,
    levelName: 'Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP)',
    track: ['distribusi', 'terpadu'],
    trainingFocus: 'Mengatasi penurunan tekanan zona akibat katup PRV macet menutup.',
    durationLimitSec: 240,
    passScore: 70,
    briefing: {
      situation: 'Alarm Tekanan Rendah: Katup PRV macet separuh menutup. Tekanan Zona 1 drop di bawah 2,0 bar!',
      objective: 'Akui alarm, buka panel PRV, naikkan setpoint PRV kembali ke 2,5 bar, dan verifikasi tekanan layanan pulih.',
      mentorQuote: '"Periksa setpoint katup pengurang tekanan. Pulihkan bukaan pegas PRV agar tekanan pelanggan kembali normal!" — Pak Slamet',
    },
    debriefing: {
      success: 'Tekanan layanan pulih sempurna. Pelanggan kembali menerima aliran air bertekanan stabil.',
      failure: 'Tekanan zona pelanggan masih di bawah batas layanan minimum.',
    },
    disturbances: [
      {
        id: 'dist-prv-fail',
        name: 'Tekanan Drop PRV',
        triggerTimeSec: 20,
        type: 'tekanan_drop',
        description: 'PRV malfunction menurunkan tekanan zona di bawah standar.',
        expectedActions: ['Akui alarm tekanan rendah', 'Setel PRV ke 2,5 bar', 'Tunggu tekanan pulih'],
      },
    ],
    hints: ['Buka panel Valve PRV, geser setpoint PRV ke 2,5 bar.'],
    quiz: [
      {
        id: 'q1',
        question: 'Penyebab mekanis utama katup PRV macet menutup adalah...',
        options: ['Kotoran atau kerak pasir menyumbat pilot valve PRV', 'Kadar sisa klorin bebas berada pada angka 0,35 mg/L', 'Kekeruhan air olahan berada di bawah 1,5 NTU', 'Waktu kontak di reservoir lebih dari 30 menit'],
        correctIndex: 0,
        explanation: 'Pilot filter PRV yang tersumbat endapan membuat diafragma gagal membuka sesuai setpoint.',
      },
      {
        id: 'q2',
        question: 'Rentang tekanan layanan standar jaringan distribusi yang aman di pelanggan adalah...',
        options: ['0,5–1,2 bar', '4,0–6,0 bar', '2,0–2,8 bar', '0,8–1,5 bar'],
        correctIndex: 2,
        explanation: 'Standar tekanan layanan jaringan distribusi SimSCADA-Air adalah 2,0–2,8 bar.',
      },
      {
        id: 'q3',
        question: 'Jika tekanan drop berlarut-larut pada jam aktivitas warga, dampaknya bagi layanan PDAM adalah...',
        options: ['Keluhan pelanggan, risiko intrusi air tanah, dan pelanggaran SPM', 'Efisiensi pengadukan di bak koagulasi langsung meningkat sangat drastis', 'Penurunan kebutuhan dosis koagulan PAC pada instalasi pengolahan hulu', 'Peningkatan kapasitas tampung bersih di dalam tangki reservoir distribusi'],
        correctIndex: 0,
        explanation: 'Penurunan tekanan memicu gangguan aliran pelanggan, risiko intrusi, dan melanggar standar SPM.',
      },
      {
        id: 'q4',
        question: 'Pada panel kendali SCADA, besaran bukaan PRV dikendalikan dalam satuan...',
        options: ['Liter per detik (L/s)', 'Bar (tekanan layanan hilir)', 'NTU (tingkat kekeruhan air)', 'Miligram per liter (mg/L)'],
        correctIndex: 1,
        explanation: 'Pada panel kendali SCADA, setpoint PRV diatur dalam satuan tekanan bar.',
      },
      {
        id: 'q5',
        question: 'Untuk membersihkan kotoran yang menyumbat pilot valve PRV, teknisi melakukan...',
        options: ['Menaikkan dosis kapur di bak koagulasi menjadi 15 mg/L', 'Menutup katup masuk reservoir selama jam puncak pagi hari', 'Menjalankan siklus pencucian balik pada unit bak sedimentasi clarifier', 'Flushing strainer pilot PRV secara berkala sesuai jadwal pemeliharaan'],
        correctIndex: 3,
        explanation: 'Pemeliharaan preventif PRV mencakup pembilasan (flushing) strainer pilot line.',
      },
    ],
  },
  {
    code: 'DST-07',
    name: 'Misi Kelulusan Operator Distribusi',
    level: 5,
    levelName: 'Tingkat 5: Misi Kelulusan Ujian (Ujian · 3,0x XP)',
    track: ['distribusi'],
    trainingFocus: 'Ujian komprehensif penanganan hidrolika perpipaan, stasiun pompa, kebocoran pipa, dan manajemen tekanan.',
    durationLimitSec: 600,
    passScore: 80,
    briefing: {
      situation: 'Ujian Kelulusan Praktik Jalur Distribusi: Pipa bocor bertepatan dengan lonjakan jam puncak!',
      objective: 'Kendalikan stasiun pompa paralel, isolasi kebocoran ruas pipa, dan pertahankan tekanan pelanggan di atas 2,0 bar tanpa petunjuk.',
      mentorQuote: '"Ketenangan dan kecepatan pengambilan keputusan adalah tanda operator distribusi sejati. Sukses untuk ujianmu!" — Pak Slamet',
    },
    debriefing: {
      success: 'SELAMAT! Anda lulus Ujian Praktik Operator Distribusi dengan skor di atas KKM 80!',
      failure: 'Skor Anda belum mencapai ambang kelulusan KKM 80.',
    },
    disturbances: [
      {
        id: 'dist-exam-dst',
        name: 'Ujian Praktik Distribusi (Kebocoran Pipa)',
        triggerTimeSec: 25,
        type: 'pipa_bocor',
        description: 'Kebocoran pipa pada jam sibuk menyebabkan debit melonjak dan tekanan drop.',
        expectedActions: ['Tutup valve isolasi ruas bocor'],
      },
      {
        id: 'dist-exam-dst-drop',
        name: 'Ujian Praktik Distribusi (Tekanan Jam Puncak Drop)',
        triggerTimeSec: 75,
        type: 'tekanan_drop',
        description: 'Penurunan tekanan layanan jaringan pada beban puncak.',
        expectedActions: ['Tambah pompa distribusi P-102 atau naikkan setpoint PRV'],
      },
    ],
    hints: [],
    quiz: [
      {
        id: 'q1',
        question: 'KKM nilai kelulusan untuk Misi Kelulusan Distribusi (DST-07) adalah...',
        options: ['65 poin', '70 poin', '80 poin', '90 poin'],
        correctIndex: 2,
        explanation: 'Seluruh Misi Kelulusan mewajibkan skor minimal 80 poin.',
      },
      {
        id: 'q2',
        question: 'Penalti skor untuk setiap pemakaian tombol petunjuk pada misi latihan adalah...',
        options: ['-5 poin', '-2 poin', '-10 poin', '-15 poin'],
        correctIndex: 0,
        explanation: 'Penggunaan petunjuk mengurangi 5 poin per pemakaian.',
      },
      {
        id: 'q3',
        question: 'Penalti skor untuk tindakan tidak aman (misalnya menghentikan seluruh pompa pasokan mendadak) adalah...',
        options: ['-5 poin per kejadian', '-15 poin per kejadian', '-30 poin per kejadian', '-4 poin komponen alarm'],
        correctIndex: 1,
        explanation: 'Tindakan tidak aman (seperti menghentikan seluruh pompa distribusi mendadak) dikenakan penalti -15 poin.',
      },
      {
        id: 'q4',
        question: 'Keberhasilan misi kelulusan diukur dari 4 komponen penilaian otomatis yaitu...',
        options: [
          'Dosis Kimia (40%), Debit Air Baku (25%), Level Reservoir (20%), Durasi Sesi (15%)',
          'Jumlah Alarm (40%), Jumlah Klik (25%), Sisa Klor (20%), Headloss (15%)',
          'Ketepatan Tindakan (40%), Waktu Respons (25%), Stabilitas Mutu (20%), Penanganan Alarm (15%)',
          'Nilai Pre-Test (40%), Kuis Pra-Misi (25%), Waktu Login (20%), Banyaknya Petunjuk (15%)',
        ],
        correctIndex: 2,
        explanation: 'Formula 4 komponen penilaian otomatis di SimSCADA-Air: Tindakan 40%, Waktu Respons 25%, Stabilitas 20%, Penanganan Alarm 15%.',
      },
      {
        id: 'q5',
        question: 'Predikat "Lulus dengan Pujian" diberikan jika rata-rata skor terbaik mencapai...',
        options: ['≥ 75 (Bintang 1)', '≥ 80 (KKM Kelulusan)', '≥ 85 (Bintang 2)', '≥ 95 (Bintang 3)'],
        correctIndex: 3,
        explanation: 'Predikat Lulus dengan Pujian mensyaratkan skor rata-rata ≥ 95.',
      },
    ],
  },

  // --- JALUR KHUSUS TERPADU (2 MISI) ---
  {
    code: 'TRP-01',
    name: 'Hulu ke Hilir: Gangguan Berantai',
    level: 4,
    levelName: 'Tingkat 4: Gangguan Berantai (Sangat Sulit · 2,5x XP)',
    track: ['terpadu'],
    trainingFocus: 'Menangani gangguan berantai simultan: banjir lumpur di intake, penurunan level reservoir, dan pipa pecah di kota.',
    durationLimitSec: 480,
    passScore: 70,
    briefing: {
      situation: 'Kondisi krisis total: Badai tropis memicu lonjakan lumpur ekstrem di intake IPA, bersamaan dengan pipa distribusi kota pecah tergerus banjir!',
      objective: 'Kendalikan dosis koagulan di IPA dan segera isolasi katup pipa bocor di jaringan distribusi sebelum reservoir habis.',
      mentorQuote: '"Inilah ujian terpadu sesungguhnya. Jangan panik, tangani sumber air baku dulu lalu secepatnya isolasi kebocoran pipa kota!" — Pak Slamet',
    },
    debriefing: {
      success: 'LUAR BIASA! Anda berhasil menuntaskan skenario gangguan berantai hulu ke hilir dan meraih lencana "Hulu ke Hilir"!',
      failure: 'Sistem kolaps karena salah satu unit pengolahan atau distribusi gagal dikendalikan tepat waktu.',
    },
    disturbances: [
      {
        id: 'dist-cascading',
        name: 'Gangguan Berantai Hulu ke Hilir',
        triggerTimeSec: 20,
        type: 'hulu_hilir',
        description: 'Lonjakan kekeruhan air baku simultan dengan pipa bocor di distribusi.',
        expectedActions: ['Tangani koagulasi', 'Isolasi kebocoran pipa', 'Jaga pasokan reservoir'],
      },
    ],
    hints: ['Tangani lonjakan kekeruhan di unit Koagulasi terlebih dahulu.', 'Beralih ke unit PRV & Isolasi untuk menutup katup pipa bocor.'],
    quiz: [
      {
        id: 'q1',
        question: 'Pada Jalur Terpadu, berapa total jumlah misi yang wajib diselesaikan untuk kelulusan?',
        options: ['9 misi (seluruh paket misi jalur IPA)', '7 misi (seluruh paket misi jalur Distribusi)', '16 misi (IPA-01..08, DST-01..06, TRP-01, dan TRP-02)', '18 misi (termasuk ujian IPA-09 dan DST-07)'],
        correctIndex: 2,
        explanation: 'Jalur Terpadu mencakup 16 misi terpadu: 8 IPA + 6 Distribusi + 2 Terpadu (TRP-01 & TRP-02).',
      },
      {
        id: 'q2',
        question: 'Pengali XP untuk skenario Tingkat 4 Gangguan Berantai adalah...',
        options: ['2,5x (Berantai)', '1,5x (Sedang)', '2,0x (Sulit)', '3,0x (Ujian)'],
        correctIndex: 0,
        explanation: 'Tingkat 4 memiliki pengali XP sebesar 2,5x.',
      },
      {
        id: 'q3',
        question: 'Apakah peserta harus menyelesaikan Jalur IPA terlebih dahulu sebelum memilih Jalur Terpadu?',
        options: ['Wajib lulus seluruh sembilan misi Jalur IPA terlebih dahulu', 'Tidak ada prasyarat; peserta bebas memilih langsung Jalur Terpadu', 'Wajib lulus Jalur Distribusi dan Post-Test Distribusi terlebih dahulu', 'Hanya dapat dibuka setelah mendapat surat persetujuan dari instruktur'],
        correctIndex: 1,
        explanation: 'Peserta bebas memilih langsung Jalur Terpadu sejak awal pelatihan bila paket lembaga mendukung.',
      },
      {
        id: 'q4',
        question: 'Bila peserta yang telah lulus IPA-01 s.d. IPA-07 pindah ke Jalur Terpadu, status misinya adalah...',
        options: ['Seluruh progres misi sebelumnya direset menjadi status belum dikerjakan', 'Misi IPA-01 s.d. IPA-07 tetap dihitung lulus tanpa mengulang', 'Peserta dikenai pengurangan skor sepuluh persen saat berpindah jalur', 'Skor misi tetap tersimpan tetapi nilai XP tidak dihitung'],
        correctIndex: 1,
        explanation: 'Misi yang sudah lulus di jalur sebelumnya langsung diakui otomatis pada Jalur Terpadu.',
      },
      {
        id: 'q5',
        question: 'Lencana khusus yang didapat setelah menyelesaikan TRP-01 adalah...',
        options: ['Penjaga Mutu Air', 'Hulu ke Hilir', 'Peraih Tiga Bintang', 'Aksi Respons Kilat'],
        correctIndex: 1,
        explanation: 'Lencana "Hulu ke Hilir" diberikan khusus setelah menyelesaikan misi TRP-01.',
      },
    ],
  },
  {
    code: 'TRP-02',
    name: 'Misi Kelulusan Terpadu Hulu-Hilir',
    level: 5,
    levelName: 'Tingkat 5: Misi Kelulusan Ujian (Ujian · 3,0x XP)',
    track: ['terpadu'],
    trainingFocus: 'Ujian akhir komprehensif mencakup seluruh siklus penyediaan air minum dari air baku hingga kran pelanggan.',
    durationLimitSec: 600,
    passScore: 80,
    briefing: {
      situation: 'Puncak evaluasi: Ujian Praktik Kompetensi Mandiri Operator SPAM Terpadu (IPA & Distribusi).',
      objective: 'Pertahankan kontinuitas, kualitas, kuantitas, dan keterjangkauan air di seluruh sistem SCADA. KKM skor minimal 80!',
      mentorQuote: '"Selamat berjuang. Anda membuktikan bahwa operator air minum Indonesia adalah penjaga kesehatan bangsa!" — Pak Slamet',
    },
    debriefing: {
      success: 'SEMPURNA! Anda lulus Ujian Terpadu Hulu-Hilir dengan prestasi tinggi dan memenuhi syarat kelulusan jalur terpadu!',
      failure: 'Skor Anda di bawah 80. Pelajari kembali materi dan ulangi simulasi.',
    },
    disturbances: [
      {
        id: 'dist-exam-trp',
        name: 'Evaluasi Final Terpadu (Hulu-Hilir)',
        triggerTimeSec: 30,
        type: 'hulu_hilir',
        description: 'Ujian simulasi komprehensif hulu-hilir (lonjakan kekeruhan + kebocoran pipa).',
        expectedActions: ['Kelola proses IPA', 'Isolasi kebocoran distribusi'],
      },
      {
        id: 'dist-exam-trp-cl',
        name: 'Evaluasi Final Terpadu (Klorinasi)',
        triggerTimeSec: 90,
        type: 'klor_salah',
        description: 'Penurunan sisa klor bebas di reservoir saat beban puncak.',
        expectedActions: ['Periksa pompa dosing klor', 'Naikkan setpoint dosis klor'],
      },
    ],
    hints: [],
    quiz: [
      {
        id: 'q1',
        question: 'Berapa skor kelulusan minimal (KKM) untuk TRP-02?',
        options: ['65 poin', '70 poin', '80 poin', '90 poin'],
        correctIndex: 2,
        explanation: 'KKM ujian kelulusan adalah 80 poin.',
      },
      {
        id: 'q2',
        question: 'Predikat tertinggi pada Piagam Kelulusan adalah...',
        options: ['Lulus Standar (skor 70–84 poin)', 'Lulus dengan Baik (85–94 poin)', 'Lulus dengan Pujian (≥ 95)', 'Operator Teladan (skor 100 poin)'],
        correctIndex: 2,
        explanation: 'Predikat tertinggi pada Piagam Kelulusan adalah Lulus dengan Pujian (rata-rata skor ≥ 95).',
      },
      {
        id: 'q3',
        question: 'Level operator tertinggi yang dapat dicapai (≥ 3.500 XP) adalah...',
        options: ['Operator Magang', 'Operator Muda', 'Operator Madya', 'Operator Ahli'],
        correctIndex: 3,
        explanation: 'Level tertinggi pada sistem gamifikasi adalah Operator Ahli (≥ 3.500 XP).',
      },
      {
        id: 'q4',
        question: 'Format nomor piagam resmi yang diterbitkan oleh SimSCADA-Air adalah...',
        options: ['SSA/<kode_lembaga>/<tahun>/<nomor_urut>', 'CERT/<kode_jalur>/<bulan>/<nomor_urut>', 'SIM-<id_peserta>-<tahun>', 'PIAGAM/<kode_misi>/<nomor_urut>'],
        correctIndex: 0,
        explanation: 'Format resmi penomoran piagam adalah SSA/<kode_lembaga>/<tahun>/<nomor_urut>.',
      },
      {
        id: 'q5',
        question: 'Catatan hukum wajib yang harus tertulis pada setiap piagam simulator adalah...',
        options: ['Piagam berlaku resmi sebagai pengganti surat pengangkatan pegawai tetap', 'Piagam ini setara dengan sertifikat kompetensi resmi BNSP bidang SPAM', 'Piagam berlaku secara internasional tanpa perlu verifikasi instansi terkait', 'Piagam menyatakan penyelesaian pelatihan simulator dan bukan sertifikat kompetensi resmi'],
        correctIndex: 3,
        explanation: 'Klausul wajib tercantum untuk membedakan pelatihan berbasis simulator dengan sertifikasi kompetensi resmi BNSP.',
      },
    ],
  },
];

// ====================================================================
// G. DATA HISTORIS PRE-SEED
// ====================================================================

// Pre/Post-Test Results
export const INITIAL_TEST_RESULTS: PrePostTestResult[] = [
  // Dimas Wahyu Pratama (peserta.ipa): pre-test 56
  {
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    type: 'pre',
    score: 56,
    completedAt: '2026-09-01T08:00:00Z',
  },
  // Andi Kurniawan (peserta.lulus): pre-test 54, post-test 88 (kenaikan +63%)
  {
    userId: 'user-peserta-lulus',
    tenantId: 'nusantara',
    type: 'pre',
    score: 54,
    completedAt: '2026-08-01T08:00:00Z',
  },
  {
    userId: 'user-peserta-lulus',
    tenantId: 'nusantara',
    type: 'post',
    score: 88,
    completedAt: '2026-10-28T09:30:00Z',
  },
  // Siti Rahmawati (peserta.distribusi): pre-test 58
  {
    userId: 'user-peserta-distribusi',
    tenantId: 'nusantara',
    type: 'pre',
    score: 58,
    completedAt: '2026-09-05T08:30:00Z',
  },
  // Rian Hidayat (peserta contoh): pre-test 54, post-test 82
  {
    userId: 'user-rian-hidayat',
    tenantId: 'nusantara',
    type: 'pre',
    score: 54,
    completedAt: '2026-08-10T08:00:00Z',
  },
  {
    userId: 'user-rian-hidayat',
    tenantId: 'nusantara',
    type: 'post',
    score: 82,
    completedAt: '2026-10-28T10:00:00Z',
  },
  // Eko Prasetyo (tertinggal, gagal IPA-07 3x): pre-test 52
  {
    userId: 'user-eko-prasetyo',
    tenantId: 'nusantara',
    type: 'pre',
    score: 52,
    completedAt: '2026-08-15T08:00:00Z',
  },
];

// Generate Nusantara alumni & active participant test results (Pre avg ≈ 56.0, Post avg ≈ 72.0 -> T1 ≈ +28.6%)
const NUSANTARA_ALUMNI_IDS: string[] = [
  ...Array.from({ length: 17 }, (_, idx) => `user-nus-grp1-${idx + 1}`),
  ...Array.from({ length: 14 }, (_, idx) => `user-nus-grp2-${idx + 1}`),
];

(function populateTestResults() {
  // 31 certified alumni: pre & post (post 70..73 so avg with Andi 88 & Rian 82 = ~72.0)
  NUSANTARA_ALUMNI_IDS.forEach((uid, idx) => {
    INITIAL_TEST_RESULTS.push({
      userId: uid,
      tenantId: 'nusantara',
      type: 'pre',
      score: 52 + (idx % 9),
      completedAt: '2026-08-05T08:00:00Z',
    });
    INITIAL_TEST_RESULTS.push({
      userId: uid,
      tenantId: 'nusantara',
      type: 'post',
      score: 70 + (idx % 3), // 70, 71, 72 -> 31 alumni + Andi(88) + Rian(82) => avg ~71.8..72.0
      completedAt: '2026-10-20T08:00:00Z',
    });
  });

  // 5 active non-graduated grp2 trainees: pre-test only
  for (let j = 15; j <= 19; j++) {
    INITIAL_TEST_RESULTS.push({
      userId: `user-nus-grp2-${j}`,
      tenantId: 'nusantara',
      type: 'pre',
      score: 53 + (j % 6),
      completedAt: '2026-09-16T08:00:00Z',
    });
  }

  // Tirta Mandiri (TRM): 18 active participants Pre-Test avg = 55,0; 12 graduates Post-Test avg = 74,0 -> T1 = +34,5%
  INITIAL_TEST_RESULTS.push({
    userId: 'user-peserta-tirta',
    tenantId: 'tirta',
    type: 'pre',
    score: 56,
    completedAt: '2026-10-18T08:00:00Z',
  });
  for (let i = 1; i <= 17; i++) {
    const preScore = i === 1 ? 54 : 55; // (56 + 54 + 16*55) / 18 = 990 / 18 = 55.0
    INITIAL_TEST_RESULTS.push({
      userId: `user-trm-${i}`,
      tenantId: 'tirta',
      type: 'pre',
      score: preScore,
      completedAt: '2026-10-02T08:00:00Z',
    });
    if (i <= 12) {
      const postScore = i % 2 === 0 ? 76 : 72; // 6*76 + 6*72 = 888 / 12 = 74.0
      INITIAL_TEST_RESULTS.push({
        userId: `user-trm-${i}`,
        tenantId: 'tirta',
        type: 'post',
        score: postScore,
        completedAt: '2026-10-24T09:00:00Z',
      });
    }
  }
})();

// Pre-seeded results for Nusantara alumni & grp2 active participants so L9/L8/L14 match 100%
export const NUSANTARA_ALUMNI_MISSION_RESULTS: Record<string, MissionResult[]> = (() => {
  const map: Record<string, MissionResult[]> = {};
  const ipaAll = ['IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06', 'IPA-07', 'IPA-08', 'IPA-09'];
  const dstAll = ['DST-01', 'DST-02', 'DST-03', 'DST-04', 'DST-05', 'DST-06', 'DST-07'];
  const trpAll = [
    'IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06', 'IPA-07', 'IPA-08',
    'DST-01', 'DST-02', 'DST-03', 'DST-04', 'DST-05', 'DST-06',
    'TRP-01', 'TRP-02',
  ];

  NUSANTARA_ALUMNI_IDS.forEach((uid, alumniIdx) => {
    const userObj = INITIAL_USERS.find((u) => u.id === uid);
    const track = userObj?.track || 'ipa';
    const codes = track === 'ipa' ? ipaAll : track === 'distribusi' ? dstAll : trpAll;
    const baseScore = 84 + (alumniIdx % 12); // 84..95

    map[uid] = codes.map((code, idx) => {
      const isGrad = code === 'IPA-09' || code === 'DST-07' || code === 'TRP-02';
      const passScore = isGrad ? 80 : 70;
      const score = Math.min(98, Math.max(passScore + 2, baseScore + ((idx + alumniIdx) % 4) - 1));
      const day = String(10 + (idx % 18)).padStart(2, '0');
      return {
        id: `res-${uid}-${code}`,
        userId: uid,
        tenantId: 'nusantara',
        missionCode: code,
        track,
        completedAt: `2026-10-${day}T11:00:00Z`,
        durationSec: 225,
        scoreTindakan: Math.round(score * 0.4),
        scoreWaktuRespons: Math.round(score * 0.25),
        scoreStabilitas: Math.round(score * 0.2),
        scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
        scoreDeductions: idx === 0 && alumniIdx % 2 === 1 ? 5 : 0,
        totalScore: score,
        stars: computeStarsFromScore(score, passScore),
        xpEarned: computeMissionXP(code, score, true),
        hintsUsedCount: idx === 0 && alumniIdx % 2 === 1 ? 1 : 0,
        isPassed: true,
        actionLogs: [],
        alarmLogs: [],
        trendHistory: [],
      };
    });
  });

  // Active in-progress grp2 trainees (user-nus-grp2-15..19)
  for (let j = 15; j <= 19; j++) {
    const uid = `user-nus-grp2-${j}`;
    const userObj = INITIAL_USERS.find((u) => u.id === uid);
    const track = userObj?.track || 'ipa';
    const pool = track === 'distribusi' ? dstAll : ipaAll;
    const partialCodes = pool.slice(0, 4 + (j % 3));
    map[uid] = partialCodes.map((code, idx) => {
      const score = 76 + ((j + idx) % 12);
      return {
        id: `res-${uid}-${code}`,
        userId: uid,
        tenantId: 'nusantara',
        missionCode: code,
        track,
        completedAt: `2026-10-${String(18 + idx).padStart(2, '0')}T14:00:00Z`,
        durationSec: 250,
        scoreTindakan: Math.round(score * 0.4),
        scoreWaktuRespons: Math.round(score * 0.25),
        scoreStabilitas: Math.round(score * 0.2),
        scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
        scoreDeductions: 0,
        totalScore: score,
        stars: computeStarsFromScore(score, 70),
        xpEarned: computeMissionXP(code, score, true),
        hintsUsedCount: 0,
        isPassed: true,
        actionLogs: [],
        alarmLogs: [],
        trendHistory: [],
      };
    });
  }

  return map;
})();

// Initial Certificates
export const INITIAL_CERTIFICATES: Certificate[] = [
  // 1. Andi Kurniawan - Piagam Terbit SSA/NUS/2026/0001
  {
    id: 'cert-andi-0001',
    certificateNumber: 'SSA/NUS/2026/0001',
    userId: 'user-peserta-lulus',
    userName: 'Andi Kurniawan',
    tenantId: 'nusantara',
    tenantName: 'Balai Diklat Air Minum Nusantara',
    track: 'terpadu',
    trackName: 'Jalur Operator Air Minum Terpadu',
    predicate: 'Lulus dengan Pujian',
    averageScore: 96,
    starsCount: 48,
    operatorLevel: 'Operator Ahli',
    issueDate: '28 Oktober 2026',
    status: 'valid',
    instructorApproved: true,
    leaderSigned: true,
    qrVerificationUrl: 'https://simscada.id/verifikasi/SSA-NUS-2026-0001',
  },
  // 2. Rian Hidayat - Pending approval SSA/NUS/2026/0002
  {
    id: 'cert-rian-0002',
    certificateNumber: 'SSA/NUS/2026/0002',
    userId: 'user-rian-hidayat',
    userName: 'Rian Hidayat',
    tenantId: 'nusantara',
    tenantName: 'Balai Diklat Air Minum Nusantara',
    track: 'ipa',
    trackName: 'Jalur Operator IPA (9 Misi)',
    predicate: 'Lulus',
    averageScore: 80,
    starsCount: 9,
    operatorLevel: 'Operator Madya',
    issueDate: '28 Oktober 2026',
    status: 'valid',
    instructorApproved: false, // Menunggu persetujuan instruktur sebelum terbit
    leaderSigned: false,
    qrVerificationUrl: 'https://simscada.id/verifikasi/SSA-NUS-2026-0002',
  },
  // 3. Revoked certificate example for verification demonstration
  {
    id: 'cert-revoked-0007',
    certificateNumber: 'SSA/NUS/2026/0007',
    userId: 'user-unknown',
    userName: 'Peserta Data Salah',
    tenantId: 'nusantara',
    tenantName: 'Balai Diklat Air Minum Nusantara',
    track: 'ipa',
    trackName: 'Jalur Operator IPA',
    predicate: 'Lulus',
    averageScore: 78,
    starsCount: 14,
    operatorLevel: 'Operator Muda',
    issueDate: '2 November 2026',
    status: 'revoked',
    revokedReason: 'Piagam terbit atas nama peserta yang salah (data diperbaiki, piagam baru diterbitkan).',
    revokedAt: '2026-11-02T10:00:00Z',
    instructorApproved: true,
    leaderSigned: true,
    qrVerificationUrl: 'https://simscada.id/verifikasi/SSA-NUS-2026-0007',
  },
];

// Add 31 valid certificates mapped to real Nusantara alumni (total valid = 32 including Andi)
(function populateNusantaraCertificates() {
  let serial = 3;
  NUSANTARA_ALUMNI_IDS.forEach((uid) => {
    if (serial === 7) serial += 1; // 0007 is reserved for the revoked demo cert
    const userObj = INITIAL_USERS.find((u) => u.id === uid);
    const results = NUSANTARA_ALUMNI_MISSION_RESULTS[uid] || [];
    const avgScore = results.length > 0 ? Math.round(results.reduce((s, r) => s + r.totalScore, 0) / results.length) : 86;
    const totalStars = results.reduce((s, r) => s + r.stars, 0);
    const track = userObj?.track || 'ipa';
    const certNo = `SSA/NUS/2026/${String(serial).padStart(4, '0')}`;

    INITIAL_CERTIFICATES.push({
      id: `cert-nus-${serial}`,
      certificateNumber: certNo,
      userId: uid,
      userName: userObj?.fullName || uid,
      tenantId: 'nusantara',
      tenantName: 'Balai Diklat Air Minum Nusantara',
      track,
      trackName:
        track === 'ipa'
          ? 'Jalur Operator IPA'
          : track === 'distribusi'
          ? 'Jalur Operator Distribusi'
          : 'Jalur Operator Air Minum Terpadu',
      predicate: avgScore >= 95 ? 'Lulus dengan Pujian' : avgScore >= 85 ? 'Lulus dengan Baik' : 'Lulus',
      averageScore: avgScore,
      starsCount: totalStars,
      operatorLevel: track === 'terpadu' ? 'Operator Ahli' : 'Operator Madya',
      issueDate: '15 Oktober 2026',
      status: 'valid',
      instructorApproved: true,
      leaderSigned: true,
      qrVerificationUrl: `https://simscada.id/verifikasi/SSA-NUS-2026-${String(serial).padStart(4, '0')}`,
    });
    serial += 1;
  });

  // 12 certificates for Tirta Mandiri (TRM)
  for (let i = 1; i <= 12; i++) {
    const certNo = `SSA/TRM/2026/${String(i).padStart(4, '0')}`;
    INITIAL_CERTIFICATES.push({
      id: `cert-trm-${i}`,
      certificateNumber: certNo,
      userId: `user-trm-${i}`,
      userName: `Peserta Tirta Mandiri ${i}`,
      tenantId: 'tirta',
      tenantName: 'Pusat Pelatihan Tirta Mandiri',
      track: 'ipa',
      trackName: 'Jalur Operator IPA (9 Misi)',
      predicate: i % 3 === 0 ? 'Lulus dengan Pujian' : 'Lulus dengan Baik',
      averageScore: 86 + (i % 6),
      starsCount: 18 + (i % 5),
      operatorLevel: 'Operator Madya',
      issueDate: '24 Oktober 2026',
      status: 'valid',
      instructorApproved: true,
      leaderSigned: true,
      qrVerificationUrl: `https://simscada.id/verifikasi/SSA-TRM-2026-${String(i).padStart(4, '0')}`,
    });
  }
})();

// ====================================================================
// H. SKOR AWAL DIMAS WAHYU PRATAMA (1.465 XP EXACT PRD §5)
// ====================================================================
export const DIMAS_MISSION_RESULTS: MissionResult[] = [
  // IPA-01: 96 (3★) -> Mudah (×1.0) = 96 XP
  {
    id: 'res-dimas-ipa01',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-01',
    track: 'ipa',
    completedAt: '2026-09-02T10:00:00Z',
    durationSec: 150,
    scoreTindakan: 40,
    scoreWaktuRespons: 25,
    scoreStabilitas: 20,
    scoreAlarm: 15,
    scoreDeductions: 4, // 96
    totalScore: 96,
    stars: 3,
    xpEarned: 96,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  // IPA-02: 92 (2★) -> Mudah (×1.0) = 92 XP
  {
    id: 'res-dimas-ipa02',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-02',
    track: 'ipa',
    completedAt: '2026-09-05T11:00:00Z',
    durationSec: 180,
    scoreTindakan: 38,
    scoreWaktuRespons: 24,
    scoreStabilitas: 18,
    scoreAlarm: 12,
    scoreDeductions: 0,
    totalScore: 92,
    stars: 2,
    xpEarned: 92,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  // IPA-03: 88 (2★) -> Sedang (×1.5) = 132 XP
  {
    id: 'res-dimas-ipa03',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-03',
    track: 'ipa',
    completedAt: '2026-09-12T14:00:00Z',
    durationSec: 210,
    scoreTindakan: 36,
    scoreWaktuRespons: 23,
    scoreStabilitas: 17,
    scoreAlarm: 12,
    scoreDeductions: 0,
    totalScore: 88,
    stars: 2,
    xpEarned: 132,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  // IPA-04: 85 (2★) -> Sedang (×1.5) = 128 XP (round 85 * 1.5 = 127.5 -> 128)
  {
    id: 'res-dimas-ipa04',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-04',
    track: 'ipa',
    completedAt: '2026-09-18T09:30:00Z',
    durationSec: 240,
    scoreTindakan: 35,
    scoreWaktuRespons: 22,
    scoreStabilitas: 16,
    scoreAlarm: 12,
    scoreDeductions: 0,
    totalScore: 85,
    stars: 2,
    xpEarned: 128,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  // IPA-05: 86 (2★) -> Sedang (×1.5) = 129 XP (86 * 1.5 = 129)
  {
    id: 'res-dimas-ipa05',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-05',
    track: 'ipa',
    completedAt: '2026-09-25T15:00:00Z',
    durationSec: 220,
    scoreTindakan: 36,
    scoreWaktuRespons: 22,
    scoreStabilitas: 16,
    scoreAlarm: 12,
    scoreDeductions: 0,
    totalScore: 86,
    stars: 2,
    xpEarned: 129,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  // IPA-06: 88 (2★) -> Sulit (×2.0) = 176 XP
  // Sesi contoh resmi: 01:15 alarm sedang, 01:25 ACK, 01:45 alarm tinggi, 01:50 ACK, 02:10 PAC 48 (respons 25s), 02:25 kapur 8.5, 02:40 debit 75, 06:10 2.4 NTU, 06:20 auto-clear, 08:30 selesai. Skor 38 + 22 + 15 + 13 = 88
  {
    id: 'res-dimas-ipa06',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-06',
    track: 'ipa',
    completedAt: '2026-10-15T08:30:00Z',
    durationSec: 510, // 08:30
    scoreTindakan: 38, // 38/40 (95% SOP Skenario Benar)
    scoreWaktuRespons: 22, // 22/25 (Respons 25s < 50% target 60s)
    scoreStabilitas: 15, // 15/20 (75% Durasi di Rentang Baku)
    scoreAlarm: 13, // 13/15 (Semua Diakui & Auto-Clear)
    scoreDeductions: 0,
    totalScore: 88,
    stars: 2,
    xpEarned: 176,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [
      { timestampSec: 75, controlPointId: 'intake', action: 'Alarm SEDANG muncul: kekeruhan air baku melonjak 20 → 185 NTU', value: 185, isCorrect: true },
      { timestampSec: 85, controlPointId: 'intake', action: 'ACK alarm air baku dalam 10 detik', value: 'ACK', isCorrect: true },
      { timestampSec: 105, controlPointId: 'filtrasi', action: 'Alarm TINGGI muncul: kekeruhan air olahan 3,4 NTU (≥ 3,0 NTU)', value: 3.4, isCorrect: true },
      { timestampSec: 110, controlPointId: 'filtrasi', action: 'ACK alarm air olahan dalam 5 detik', value: 'ACK', isCorrect: true },
      { timestampSec: 130, controlPointId: 'koagulasi', action: 'Dosis PAC 20 → 48 mg/L (tindakan benar pertama: 25 detik setelah alarm Tinggi)', value: 48, isCorrect: true },
      { timestampSec: 145, controlPointId: 'koagulasi', action: 'Dosis kapur 8,5 mg/L, pH dijaga 7,20', value: 8.5, isCorrect: true },
      { timestampSec: 160, controlPointId: 'intake', action: 'Debit intake 100 → 75 L/s', value: 75, isCorrect: true },
      { timestampSec: 370, controlPointId: 'filtrasi', action: 'Kekeruhan air olahan 2,4 NTU (≤ 2,7 NTU)', value: 2.4, isCorrect: true },
      { timestampSec: 380, controlPointId: 'filtrasi', action: 'Alarm Tinggi clear otomatis setelah stabil 10 detik', value: 'CLEAR', isCorrect: true },
      { timestampSec: 510, controlPointId: 'simulasi', action: 'Simulasi selesai. Skor 38 + 22 + 15 + 13 = 88', value: 88, isCorrect: true },
    ],
    alarmLogs: [
      {
        id: 'alm-sedang-01',
        timestamp: '01:15',
        timestampSec: 75,
        priority: 'sedang',
        controlPointId: 'intake',
        controlPointName: 'Intake Air Baku',
        message: 'Kekeruhan air baku tinggi (185,0 NTU, ambang normal ≤ 50 NTU)',
        triggerSnapshotValue: '185,0 NTU',
        ackAtSec: 85,
        ackTimestamp: '01:25',
        actionSummary: 'Dosis PAC 20 → 48 mg/L; kapur 8,5 mg/L; debit intake 75 L/s',
        clearedAtSec: 400,
        clearedTimestamp: '06:40',
        status: 'clear',
        clearMethod: 'auto',
        clearNote: 'Pulih otomatis: kekeruhan air baku kembali normal (≤ 50 NTU)',
      },
      {
        id: 'alm-tinggi-02',
        timestamp: '01:45',
        timestampSec: 105,
        priority: 'tinggi',
        controlPointId: 'filtrasi',
        controlPointName: 'Filtrasi (Air Olahan)',
        message: 'Kekeruhan air olahan ≥ 3,0 NTU (Terukur saat kejadian: 3,40 NTU)',
        triggerSnapshotValue: '3,40 NTU',
        ackAtSec: 110,
        ackTimestamp: '01:50',
        actionSummary: 'Dosis PAC 20 → 48 mg/L; kapur 8,5 mg/L; debit intake 75 L/s',
        clearedAtSec: 380,
        clearedTimestamp: '06:20',
        status: 'clear',
        clearMethod: 'auto',
        clearNote: 'Pulih otomatis: kekeruhan air olahan ≤ 2,7 NTU stabil 10 detik (saat clear: 2,40 NTU)',
      },
    ],
    trendHistory: [
      { timeSec: 0, turbidity: 20, settledTurbidity: 3.5, freeChlorine: 0.35, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
      { timeSec: 75, turbidity: 185, settledTurbidity: 3.5, freeChlorine: 0.35, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
      { timeSec: 105, turbidity: 185, settledTurbidity: 12.0, freeChlorine: 0.35, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
      { timeSec: 130, turbidity: 185, settledTurbidity: 10.5, freeChlorine: 0.35, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
      { timeSec: 370, turbidity: 185, settledTurbidity: 4.0, freeChlorine: 0.35, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
      { timeSec: 510, turbidity: 185, settledTurbidity: 2.4, freeChlorine: 0.38, reservoirLevel: 4.2, zonePressure: 2.4, zoneFlow: 100 },
    ],
  },
  // IPA-07: 76 (1★) -> Sulit (×2.0) = 152 XP
  {
    id: 'res-dimas-ipa07',
    userId: 'user-peserta-ipa',
    tenantId: 'nusantara',
    missionCode: 'IPA-07',
    track: 'ipa',
    completedAt: '2026-10-22T10:00:00Z',
    durationSec: 280,
    scoreTindakan: 30,
    scoreWaktuRespons: 18,
    scoreStabilitas: 15,
    scoreAlarm: 13,
    scoreDeductions: 0,
    totalScore: 76,
    stars: 1,
    xpEarned: 152,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
];
// Total misi Dimas = 96 + 92 + 132 + 128 + 129 + 176 + 152 = 905 XP
// Tambah 7 kuis bernilai 80 (7 * 80 = 560 XP)
// Total XP Dimas = 905 + 560 = 1.465 XP! Level = Operator Madya (1.200 - 2.499 XP). Sisa 1.035 ke Utama (2.500 XP)!

// Pre-seeded results for Andi Kurniawan (16 missions, all score 96 -> 48★, 2.592 mission XP + 1.280 quiz XP = 3.872 XP, Operator Ahli)
export const ANDI_MISSION_RESULTS: MissionResult[] = [
  'IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06', 'IPA-07', 'IPA-08',
  'DST-01', 'DST-02', 'DST-03', 'DST-04', 'DST-05', 'DST-06',
  'TRP-01', 'TRP-02'
].map((code, idx) => {
  const score = 96;
  const passScore = code === 'TRP-02' ? 80 : 70;
  const stars = computeStarsFromScore(score, passScore);
  const xpEarned = computeMissionXP(code, score, true);
  const day = String(11 + idx).padStart(2, '0');
  return {
    id: `res-andi-${code}`,
    userId: 'user-peserta-lulus',
    tenantId: 'nusantara',
    missionCode: code,
    track: 'terpadu' as const,
    completedAt: `2026-10-${day}T16:00:00Z`,
    durationSec: 200,
    scoreTindakan: 38,
    scoreWaktuRespons: 24,
    scoreStabilitas: 19,
    scoreAlarm: 15,
    scoreDeductions: 0,
    totalScore: score,
    stars,
    xpEarned,
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  };
});

// Pre-seeded results for Siti Rahmawati (DST-01..05 lulus: 97, 85, 86, 86, 85 -> 11★, 610 mission XP + 400 quiz XP = 1.010 XP, Operator Muda)
const SITI_SCORES: Array<{ code: string; score: number; completedAt: string }> = [
  { code: 'DST-01', score: 97, completedAt: '2026-10-16T10:00:00Z' },
  { code: 'DST-02', score: 85, completedAt: '2026-10-18T11:00:00Z' },
  { code: 'DST-03', score: 86, completedAt: '2026-10-20T12:00:00Z' },
  { code: 'DST-04', score: 86, completedAt: '2026-10-22T13:00:00Z' },
  { code: 'DST-05', score: 85, completedAt: '2026-10-24T14:00:00Z' },
];

export const SITI_MISSION_RESULTS: MissionResult[] = SITI_SCORES.map(({ code, score, completedAt }) => ({
  id: `res-siti-${code}`,
  userId: 'user-peserta-distribusi',
  tenantId: 'nusantara',
  missionCode: code,
  track: 'distribusi' as const,
  completedAt,
  durationSec: 220,
  scoreTindakan: Math.round(score * 0.4),
  scoreWaktuRespons: Math.round(score * 0.25),
  scoreStabilitas: Math.round(score * 0.2),
  scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
  scoreDeductions: 0,
  totalScore: score,
  stars: computeStarsFromScore(score, 70),
  xpEarned: computeMissionXP(code, score, true),
  hintsUsedCount: 0,
  isPassed: true,
  actionLogs: [],
  alarmLogs: [],
  trendHistory: [],
}));

// Pre-seeded results for Rian Hidayat (9/9 IPA passed, IPA-09 score 82, waiting for approval)
export const RIAN_MISSION_RESULTS: MissionResult[] = [
  'IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06', 'IPA-07', 'IPA-08', 'IPA-09'
].map((code, idx) => {
  const is9 = code === 'IPA-09';
  const score = is9 ? 82 : 80;
  const passScore = is9 ? 80 : 70;
  const day = String(19 + idx).padStart(2, '0');
  return {
    id: `res-rian-${code}`,
    userId: 'user-rian-hidayat',
    tenantId: 'nusantara',
    missionCode: code,
    track: 'ipa' as const,
    completedAt: `2026-10-${day}T10:00:00Z`,
    durationSec: 260,
    scoreTindakan: 32,
    scoreWaktuRespons: 20,
    scoreStabilitas: 16,
    scoreAlarm: is9 ? 14 : 12,
    scoreDeductions: 0,
    totalScore: score,
    stars: computeStarsFromScore(score, passScore),
    xpEarned: computeMissionXP(code, score, true),
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  };
});

// Pre-seeded results for Eko Prasetyo (gagal IPA-07 3x berturut-turut -> lagging alert in L9)
export const EKO_MISSION_RESULTS: MissionResult[] = [
  'IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06'
].map((code, idx) => {
  const score = 75;
  return {
    id: `res-eko-${code}`,
    userId: 'user-eko-prasetyo',
    tenantId: 'nusantara',
    missionCode: code,
    track: 'ipa' as const,
    completedAt: `2026-10-${String(10 + idx).padStart(2, '0')}T10:00:00Z`,
    durationSec: 280,
    scoreTindakan: 30,
    scoreWaktuRespons: 18,
    scoreStabilitas: 15,
    scoreAlarm: 12,
    scoreDeductions: 0,
    totalScore: score,
    stars: computeStarsFromScore(score, 70),
    xpEarned: computeMissionXP(code, score, true),
    hintsUsedCount: 0,
    isPassed: true,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  };
}).concat([
  // 3 failed attempts on IPA-07
  {
    id: 'res-eko-ipa07-1',
    userId: 'user-eko-prasetyo',
    tenantId: 'nusantara',
    missionCode: 'IPA-07',
    track: 'ipa' as const,
    completedAt: '2026-10-22T09:00:00Z',
    durationSec: 300,
    scoreTindakan: 22,
    scoreWaktuRespons: 12,
    scoreStabilitas: 14,
    scoreAlarm: 10,
    scoreDeductions: 0,
    totalScore: 58,
    stars: 0,
    xpEarned: 0,
    hintsUsedCount: 0,
    isPassed: false,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  {
    id: 'res-eko-ipa07-2',
    userId: 'user-eko-prasetyo',
    tenantId: 'nusantara',
    missionCode: 'IPA-07',
    track: 'ipa' as const,
    completedAt: '2026-10-23T11:00:00Z',
    durationSec: 300,
    scoreTindakan: 24,
    scoreWaktuRespons: 13,
    scoreStabilitas: 13,
    scoreAlarm: 10,
    scoreDeductions: 0,
    totalScore: 60,
    stars: 0,
    xpEarned: 0,
    hintsUsedCount: 0,
    isPassed: false,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
  {
    id: 'res-eko-ipa07-3',
    userId: 'user-eko-prasetyo',
    tenantId: 'nusantara',
    missionCode: 'IPA-07',
    track: 'ipa' as const,
    completedAt: '2026-10-25T14:00:00Z',
    durationSec: 300,
    scoreTindakan: 22,
    scoreWaktuRespons: 12,
    scoreStabilitas: 14,
    scoreAlarm: 10,
    scoreDeductions: 0,
    totalScore: 58,
    stars: 0,
    xpEarned: 0,
    hintsUsedCount: 0,
    isPassed: false,
    actionLogs: [],
    alarmLogs: [],
    trendHistory: [],
  },
]);

// Pre-seeded results for Siti Aminah (peserta.tirta · Jalur IPA Tirta Mandiri)
// IPA-01: 90 (2★) = 90 + 80 = 170 XP; IPA-02: 86 (2★) = 86 + 80 = 166 XP; IPA-03: 82 (1★) = 123 + 80 = 203 XP -> 539 XP (Operator Muda), 5★
const SITI_AMINAH_SCORES: Array<{ code: string; score: number; completedAt: string }> = [
  { code: 'IPA-01', score: 90, completedAt: '2026-10-20T09:30:00Z' },
  { code: 'IPA-02', score: 86, completedAt: '2026-10-23T11:15:00Z' },
  { code: 'IPA-03', score: 82, completedAt: '2026-10-26T14:20:00Z' },
];

export const SITI_AMINAH_MISSION_RESULTS: MissionResult[] = SITI_AMINAH_SCORES.map(({ code, score, completedAt }) => ({
  id: `res-siti-aminah-${code}`,
  userId: 'user-peserta-tirta',
  tenantId: 'tirta',
  missionCode: code,
  track: 'ipa' as const,
  completedAt,
  durationSec: 210,
  scoreTindakan: Math.round(score * 0.4),
  scoreWaktuRespons: Math.round(score * 0.25),
  scoreStabilitas: Math.round(score * 0.2),
  scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
  scoreDeductions: 0,
  totalScore: score,
  stars: computeStarsFromScore(score, 70),
  xpEarned: computeMissionXP(code, score, true),
  hintsUsedCount: 0,
  isPassed: true,
  actionLogs:
    code === 'IPA-03'
      ? [
          { timestampSec: 20, controlPointId: 'koagulasi', action: 'Mengatur dosis koagulan PAC awal ke 26 mg/L', value: 26, isCorrect: true },
          { timestampSec: 65, controlPointId: 'flokulasi', action: 'Menyesuaikan pengadukan lambat flokulator 28 RPM', value: 28, isCorrect: true },
          { timestampSec: 140, controlPointId: 'filtrasi', action: 'Kekeruhan air olahan stabil di 1,4 NTU (< 3,0 NTU)', value: 1.4, isCorrect: true },
          { timestampSec: 210, controlPointId: 'simulasi', action: 'Simulasi IPA-03 selesai. Skor total 82', value: 82, isCorrect: true },
        ]
      : [],
  alarmLogs: [],
  trendHistory:
    code === 'IPA-03'
      ? [
          { timeSec: 0, turbidity: 25, settledTurbidity: 4.1, freeChlorine: 0.34, reservoirLevel: 4.1, zonePressure: 2.3, zoneFlow: 95 },
          { timeSec: 90, turbidity: 25, settledTurbidity: 2.6, freeChlorine: 0.35, reservoirLevel: 4.1, zonePressure: 2.3, zoneFlow: 95 },
          { timeSec: 210, turbidity: 25, settledTurbidity: 1.4, freeChlorine: 0.36, reservoirLevel: 4.2, zonePressure: 2.3, zoneFlow: 95 },
        ]
      : [],
}));

// Pre-seeded results for Tirta Mandiri alumni (user-trm-1..12) and active trainees (user-trm-13..17)
export const TIRTA_ALUMNI_MISSION_RESULTS: Record<string, MissionResult[]> = (() => {
  const map: Record<string, MissionResult[]> = {};
  const ipaAll = ['IPA-01', 'IPA-02', 'IPA-03', 'IPA-04', 'IPA-05', 'IPA-06', 'IPA-07', 'IPA-08', 'IPA-09'];

  for (let i = 1; i <= 12; i++) {
    const uid = `user-trm-${i}`;
    const baseScore = 86 + (i % 6);
    map[uid] = ipaAll.map((code, idx) => {
      const score = Math.min(98, baseScore + (idx % 2 === 0 ? 1 : -1));
      const passScore = code === 'IPA-09' ? 80 : 70;
      return {
        id: `res-trm-${i}-${code}`,
        userId: uid,
        tenantId: 'tirta',
        missionCode: code,
        track: 'ipa' as const,
        completedAt: `2026-10-${String(12 + idx).padStart(2, '0')}T10:00:00Z`,
        durationSec: 230,
        scoreTindakan: Math.round(score * 0.4),
        scoreWaktuRespons: Math.round(score * 0.25),
        scoreStabilitas: Math.round(score * 0.2),
        scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
        scoreDeductions: 0,
        totalScore: score,
        stars: computeStarsFromScore(score, passScore),
        xpEarned: computeMissionXP(code, score, true),
        hintsUsedCount: 0,
        isPassed: true,
        actionLogs: [],
        alarmLogs: [],
        trendHistory: [],
      };
    });
  }

  for (let i = 13; i <= 17; i++) {
    const uid = `user-trm-${i}`;
    const partialCodes = ipaAll.slice(0, 5 + (i % 2));
    map[uid] = partialCodes.map((code, idx) => {
      const score = 78 + ((i + idx) % 7);
      return {
        id: `res-trm-${i}-${code}`,
        userId: uid,
        tenantId: 'tirta',
        missionCode: code,
        track: 'ipa' as const,
        completedAt: `2026-10-${String(18 + idx).padStart(2, '0')}T13:00:00Z`,
        durationSec: 250,
        scoreTindakan: Math.round(score * 0.4),
        scoreWaktuRespons: Math.round(score * 0.25),
        scoreStabilitas: Math.round(score * 0.2),
        scoreAlarm: Math.max(0, score - Math.round(score * 0.4) - Math.round(score * 0.25) - Math.round(score * 0.2)),
        scoreDeductions: 0,
        totalScore: score,
        stars: computeStarsFromScore(score, 70),
        xpEarned: computeMissionXP(code, score, true),
        hintsUsedCount: 0,
        isPassed: true,
        actionLogs: [],
        alarmLogs: [],
        trendHistory: [],
      };
    });
  }

  return map;
})();

// ====================================================================
// I. DUA SET SOAL PARALEL PRE-TEST (SET A) & POST-TEST (SET B)
//    Kisi-kisi identik: 4 soal x 5 kompetensi = 20 soal per set
// ====================================================================
export interface PrePostQuestion extends QuizQuestion {
  category:
    | 'Operasi normal IPA'
    | 'Mutu air'
    | 'Respons gangguan'
    | 'Penanganan alarm'
    | 'Hidrolika distribusi';
}

export const PRE_TEST_QUESTIONS_SET_A: PrePostQuestion[] = [
  // --- 1. Operasi normal IPA (4 soal) ---
  {
    id: 'pre-1',
    category: 'Operasi normal IPA',
    question: 'Urutan tahapan pengolahan konvensional pada Instalasi Pengolahan Air (IPA) yang benar adalah...',
    options: [
      'Filtrasi → Koagulasi → Flokulasi → Sedimentasi → Desinfeksi → Reservoir',
      'Intake → Koagulasi → Flokulasi → Sedimentasi → Filtrasi → Desinfeksi',
      'Intake → Desinfeksi → Sedimentasi → Flokulasi → Filtrasi → Reservoir',
      'Koagulasi → Intake → Sedimentasi → Flokulasi → Filtrasi → Reservoir',
    ],
    correctIndex: 1,
    explanation: 'Aliran pengolahan IPA standar dimulai dari Intake, Koagulasi, Flokulasi, Sedimentasi, Filtrasi, hingga Desinfeksi sebelum masuk reservoir.',
  },
  {
    id: 'pre-2',
    category: 'Operasi normal IPA',
    question: 'Jika kecepatan putaran (RPM) pengaduk lambat di bak flokulasi terlalu tinggi, dampak yang terjadi adalah...',
    options: [
      'Flok terbentuk pecah kembali sehingga sulit mengendap di bak sedimentasi',
      'Kadar sisa klorin bebas meningkat sangat drastis di sepanjang jaringan distribusi',
      'Tekanan keluar pompa air baku di intake naik melampaui kapasitas nominal',
      'Nilai headloss pada unit saringan pasir cepat turun menjadi nol meter',
    ],
    correctIndex: 0,
    explanation: 'Gradien kecepatan berlebih di flokulator menimbulkan gaya geser tinggi yang memecah makroflok.',
  },
  {
    id: 'pre-3',
    category: 'Operasi normal IPA',
    question: 'Indikator utama bahwa unit Saringan Pasir Cepat perlu segera dilakukan pencucian balik (backwash) adalah...',
    options: [
      'Nilai pH air olahan terukur stabil di angka netral 7,20',
      'Kapasitas tampung level reservoir air bersih terisi penuh 90 persen',
      'Headloss filter mencapai ≥ 2,0 mH2O atau kekeruhan efluen naik',
      'Laju debit pompa air baku tetap stabil di angka 85 L/s',
    ],
    correctIndex: 2,
    explanation: 'Kenaikan headloss (> 2,0 mH2O) menunjukkan pori media pasir tersumbat kotoran dan memerlukan backwash.',
  },
  {
    id: 'pre-4',
    category: 'Operasi normal IPA',
    question: 'Prosedur aman pergantian pompa intake duty ke pompa cadangan (standby) secara paralel adalah...',
    options: [
      'Matikan pompa duty selama sepuluh menit lalu nyalakan pompa cadangan secara perlahan',
      'Tutup seluruh katup buang pipa utama sebelum mulai menghidupkan unit pompa cadangan',
      'Biarkan pompa bermasalah tetap menyala sambil memutus aliran air baku dari sungai',
      'Buka katup hisap, nyalakan pompa standby hingga stabil, lalu matikan pompa duty',
    ],
    correctIndex: 3,
    explanation: 'Menyalakan pompa standby terlebih dahulu mencegah terputusnya debit aliran secara mendadak sebelum pompa duty dimatikan.',
  },

  // --- 2. Mutu air (4 soal) ---
  {
    id: 'pre-5',
    category: 'Mutu air',
    question: 'Berdasarkan standar baku mutu air minum Permenkes No. 2 Tahun 2023, batas maksimum kekeruhan air olahan adalah...',
    options: [
      '< 10,0 NTU',
      '< 5,0 NTU',
      '< 3,0 NTU',
      '< 15,0 NTU',
    ],
    correctIndex: 2,
    explanation: 'Permenkes No. 2/2023 menetapkan batas maksimum kekeruhan air minum adalah kurang dari 3,0 NTU.',
  },
  {
    id: 'pre-6',
    category: 'Mutu air',
    question: 'Rentang kadar sisa klorin bebas yang aman dan efektif pada outlet reservoir IPA adalah...',
    options: [
      '0,01–0,05 mg/L',
      '0,20–0,50 mg/L',
      '1,50–2,50 mg/L',
      '5,00–8,00 mg/L',
    ],
    correctIndex: 1,
    explanation: 'Sisa klorin 0,20–0,50 mg/L melindungi air dari rekontaminasi bakteri di pipa tanpa menimbulkan bau menyengat berlebih.',
  },
  {
    id: 'pre-7',
    category: 'Mutu air',
    question: 'Rentang pH air minum yang dipersyaratkan agar koagulasi PAC optimal dan air aman dikonsumsi pelanggan adalah...',
    options: [
      '6,5–8,5',
      '4,5–5,5',
      '9,0–10,5',
      '3,0–6,0',
    ],
    correctIndex: 0,
    explanation: 'Rentang pH aman air minum sesuai baku mutu adalah 6,5–8,5 sekaligus rentang kerja efektif koagulan PAC.',
  },
  {
    id: 'pre-8',
    category: 'Mutu air',
    question: 'Pada ujung jaringan distribusi terjauh, sisa klorin bebas terukur 0,08 mg/L. Langkah koreksi yang tepat adalah...',
    options: [
      'Menutup seluruh katup zona pelanggan distribusi agar air tidak terus mengalir',
      'Menurunkan nilai pH air olahan di unit filter menjadi angka 5,0',
      'Melakukan pengurasan lumpur blowdown secara total pada dasar bak sedimentasi',
      'Naikkan dosis klorin sambil menjaga residu reservoir ≤ 0,50 mg/L',
    ],
    correctIndex: 3,
    explanation: 'Penurunan residu di ujung pipa menandakan peluruhan klor; injeksi klorin perlu dinaikkan secara terkendali dalam batas aman.',
  },

  // --- 3. Respons gangguan (4 soal) ---
  {
    id: 'pre-9',
    category: 'Respons gangguan',
    question: 'Saat kekeruhan air baku naik tiba-tiba dari 20 NTU menjadi 185 NTU akibat banjir hulu, tindakan awal terpenting adalah...',
    options: [
      'Akui alarm, naikkan dosis PAC, koreksi pH, dan sesuaikan debit intake',
      'Segera menghentikan seluruh unit pompa intake agar air baku tidak masuk',
      'Membuka penuh katup penguras lumpur hingga isi bak sedimentasi benar-benar kering',
      'Mematikan motor pengaduk cepat flash mixer agar pemakaian listrik lebih hemat',
    ],
    correctIndex: 0,
    explanation: 'Lonjakan kekeruhan membutuhkan penambahan koagulan sesuai kebutuhan flokulasi, penjagaan pH, dan waktu detensi pengendapan yang cukup.',
  },
  {
    id: 'pre-10',
    category: 'Respons gangguan',
    question: 'Mengapa penambahan dosis koagulan PAC dalam jumlah besar sering diikuti oleh penurunan pH air?',
    options: [
      'PAC mengandung gas oksigen terlarut tinggi yang menaikkan suhu air baku',
      'PAC mengendapkan seluruh mineral natrium terlarut di dalam tangki reservoir bersih',
      'Dosis PAC tinggi selalu membuat suhu air meningkat tajam di flokulator',
      'Hidrolisis koagulan mengonsumsi alkalinitas air sehingga perlu penyesuai pH kapur',
    ],
    correctIndex: 3,
    explanation: 'Hidrolisis koagulan melepaskan ion H+ yang menurunkan alkalinitas; penyesuai pH menjaga pH tetap di rentang 6,5–8,5.',
  },
  {
    id: 'pre-11',
    category: 'Respons gangguan',
    question: 'Ketika terjadi gangguan berantai Hulu-Hilir (banjir lumpur di IPA sekaligus pipa pecah di distribusi), urutan prioritas yang tepat adalah...',
    options: [
      'Mematikan seluruh pompa distribusi utama agar jaringan pipa kota kosong total',
      'Mengisolasi ruas bocor guna menjaga reservoir sekaligus menaikkan dosis PAC IPA',
      'Membiarkan kebocoran pipa hingga proses di IPA selesai dua jam lagi',
      'Membuka penuh katup PRV ke tekanan maksimum agar aliran air deras',
    ],
    correctIndex: 1,
    explanation: 'Isolasi kebocoran menyelamatkan cadangan air bersih di reservoir sementara pengaturan PAC menjaga mutu air olahan IPA.',
  },
  {
    id: 'pre-12',
    category: 'Respons gangguan',
    question: 'Bila sisa klorin bebas di unit desinfeksi anjlok di bawah 0,20 mg/L akibat gangguan pompa dosing, langkah pemulihan adalah...',
    options: [
      'Mengurangi laju debit pompa air baku dari sungai menjadi nol L/s',
      'Menjalankan prosedur backwash serentak pada kedua unit filter pasir cepat sekaligus',
      'Akui alarm kritis, cek pompa dosing, lalu naikkan setpoint 1,5–1,8 mg/L',
      'Menambahkan larutan kapur ke bak koagulasi hingga pH naik mencapai 9,5',
    ],
    correctIndex: 2,
    explanation: 'Penyesuaian setpoint dosing klor memulihkan sisa klor bebas kembali ke rentang aman 0,20–0,50 mg/L.',
  },

  // --- 4. Penanganan alarm (4 soal) ---
  {
    id: 'pre-13',
    category: 'Penanganan alarm',
    question: 'Perbedaan fungsi antara status "Diakui (ACK)" dan "Clear" pada daftar alarm ruang kendali SCADA adalah...',
    options: [
      'ACK langsung memperbaiki kerusakan pompa secara otomatis tanpa intervensi operator',
      'Clear harus ditekan sebelum ACK agar sirine peringatan berhenti berbunyi',
      'Tidak ada perbedaan fungsi antara ACK dan Clear pada SCADA',
      'ACK mengonfirmasi penerimaan operator, sedangkan Clear menandakan parameter kembali aman',
    ],
    correctIndex: 3,
    explanation: 'ACK mengonfirmasi kesadaran operator; Clear hanya terjadi setelah akar gangguan selesai ditangani.',
  },
  {
    id: 'pre-14',
    category: 'Penanganan alarm',
    question: 'Apa yang terjadi jika operator menekan tombol "Clear" manual saat kekeruhan air olahan masih 3,40 NTU (belum ditangani)?',
    options: [
      'Alarm langsung terhapus dan operator mendapat skor Penanganan Alarm penuh',
      'Kapasitas pompa distribusi dinaikkan otomatis untuk menguras isi air reservoir',
      'Clear ditolak berpesan "Penyebab belum ditangani" dan mengurangi skor alarm',
      'Prioritas alarm diturunkan sementara dari Tinggi menjadi Info selama 10 detik',
    ],
    correctIndex: 2,
    explanation: 'Clear bersyarat mencegah penghapusan alarm palsu ketika kondisi proses masih berada di luar batas aman.',
  },
  {
    id: 'pre-15',
    category: 'Penanganan alarm',
    question: 'Langkah wajib sebelum alarm "Pompa Trip" yang bersifat terkunci (latched) dapat di-clear secara manual adalah...',
    options: [
      'Menunggu sepuluh detik hingga alarm hilang otomatis setelah air olahan stabil',
      'Hidupkan pompa cadangan, periksa panel proteksi, dan tekan tombol Reset Pompa',
      'Menurunkan setpoint dosis injeksi klorin di reservoir hingga angka 0,20 mg/L',
      'Membuka katup penguras clarifier selama lima menit untuk menurunkan tekanan hisap',
    ],
    correctIndex: 1,
    explanation: 'Alarm latched membutuhkan Reset Trip eksplisit setelah aliran diamankan dengan pompa cadangan.',
  },
  {
    id: 'pre-16',
    category: 'Penanganan alarm',
    question: 'Urutan prioritas penanganan apabila muncul alarm KRITIS (merah), TINGGI (oranye), dan SEDANG (kuning) secara bersamaan adalah...',
    options: [
      'Tangani KRITIS lebih awal, diikuti TINGGI, kemudian SEDANG',
      'Tangani SEDANG terlebih dahulu karena penanganannya lebih cepat selesai',
      'Tangani TINGGI terlebih dahulu agar proses filtrasi tetap berjalan',
      'Akui alarm SEDANG lalu tunggu alarm KRITIS melakukan auto-clear',
    ],
    correctIndex: 0,
    explanation: 'Prioritas Kritis mengancam keselamatan mutu air atau kontinuitas pasokan total sehingga wajib ditangani paling awal.',
  },

  // --- 5. Hidrolika distribusi (4 soal) ---
  {
    id: 'pre-17',
    category: 'Hidrolika distribusi',
    question: 'Rentang tekanan layanan standar yang perlu dipertahankan pada zona jaringan distribusi pelanggan adalah...',
    options: [
      '0,2–0,5 bar',
      '2,0–2,8 bar',
      '8,0–10,0 bar',
      '0,0–0,1 bar',
    ],
    correctIndex: 1,
    explanation: 'Tekanan 2,0–2,8 bar menjamin air mengalir memadai hingga lantai atas sekaligus mencegah intrusi air tanah dan pecah pipa.',
  },
  {
    id: 'pre-18',
    category: 'Hidrolika distribusi',
    question: 'Tanda khas pada monitor SCADA apabila terjadi kebocoran besar pipa pecah di Zona 1 adalah...',
    options: [
      'Debit zona melonjak disertai penurunan tekanan zona dan level reservoir',
      'Debit aliran turun ke nol sementara tekanan pipa naik ke 8 bar',
      'Tingkat kekeruhan air baku di saluran intake turun di bawah 5 NTU',
      'Nilai pH air olahan di unit filter naik mencapai angka 9,5',
    ],
    correctIndex: 0,
    explanation: 'Pipa pecah menghilangkan tahanan hidrolik pipa sehingga debit keluar melonjak sementara tekanan zona anjlok.',
  },
  {
    id: 'pre-19',
    category: 'Hidrolika distribusi',
    question: 'Fungsi utama katup pengurang tekanan (PRV / Pressure Reducing Valve) pada zona jaringan berkontur rendah adalah...',
    options: [
      'Menaikkan nilai kekeruhan air olahan sebelum masuk ke pipa sambungan rumah',
      'Menghentikan pasokan air bersih ke seluruh wilayah kota secara permanen',
      'Mengukur kadar residu sisa klorin bebas secara otomatis di hilir',
      'Menurunkan serta menstabilkan tekanan hilir guna mencegah pecah pipa dan kebocoran',
    ],
    correctIndex: 3,
    explanation: 'PRV menahan tekanan berlebih di hilir pada setpoint aman sehingga menekan risiko pipa pecah.',
  },
  {
    id: 'pre-20',
    category: 'Hidrolika distribusi',
    question: 'Pada jam puncak pagi (06.00–08.00), bagaimana operator menjaga debit dan tekanan distribusi agar tidak drop di bawah 2,0 bar?',
    options: [
      'Menutup katup keluar tangki reservoir agar cadangan air bersih tetap penuh',
      'Menghentikan sementara operasional seluruh unit saringan pasir cepat di IPA',
      'Jalankan pompa paralel dan atur setpoint PRV sambil memantau reservoir',
      'Menutup seluruh katup distribusi zona komersial kota tanpa pemberitahuan warga',
    ],
    correctIndex: 2,
    explanation: 'Operasi paralel menambah kapasitas debit aliran (L/s) dan pengaturan PRV menjaga tekanan layanan 2,0–2,8 bar.',
  },
];

export const POST_TEST_QUESTIONS_SET_B: PrePostQuestion[] = [
  // --- 1. Operasi normal IPA (4 soal — berbeda isi, setara kisi-kisi) ---
  {
    id: 'post-1',
    category: 'Operasi normal IPA',
    question: 'Fungsi utama pencampuran berkecepatan tinggi (flash mixer) segera setelah titik pembubuhan koagulan PAC adalah...',
    options: [
      'Mengendapkan seluruh padatan tersuspensi secara langsung di dalam bak koagulasi',
      'Menguapkan sisa klorin bebas sebelum aliran masuk ke bak sedimentasi',
      'Meratakan koagulan dalam hitungan detik agar muatan koloid cepat terdestabilisasi',
      'Menurunkan nilai headloss saringan pasir cepat tanpa perlu proses backwash',
    ],
    correctIndex: 2,
    explanation: 'Reaksi destabilisasi koloid berlangsung sangat cepat sehingga memerlukan pengadukan berenergi tinggi yang merata.',
  },
  {
    id: 'post-2',
    category: 'Operasi normal IPA',
    question: 'Mengapa pada unit saringan pasir ganda (dual sand filter) pencucian balik (backwash) tidak boleh dilakukan serentak pada semua bak filter?',
    options: [
      'Agar warna air baku di sungai langsung berubah menjadi jernih seketika',
      'Supaya laju konsumsi bahan kimia kapur meningkat dua kali lebih banyak',
      'Karena tekanan pada bar screen di saluran intake akan meningkat drastis',
      'Menjaga kontinuitas aliran air olahan ke reservoir tanpa menghentikan produksi',
    ],
    correctIndex: 3,
    explanation: 'Backwash bergantian (staggered) memastikan minimal satu unit filter tetap menyaring air ke reservoir.',
  },
  {
    id: 'post-3',
    category: 'Operasi normal IPA',
    question: 'Tujuan membuka katup penguras lumpur (blowdown) secara berkala pada bak sedimentasi adalah...',
    options: [
      'Mencegah penumpukan selimut lumpur agar flok tidak lolos ke filter',
      'Menaikkan dosis koagulan PAC secara otomatis ketika terjadi hujan deras',
      'Menambah tekanan keluar pada stasiun pompa distribusi utama ke kota',
      'Meningkatkan kecepatan putaran motor pengaduk cepat menjadi dua kali lipat',
    ],
    correctIndex: 0,
    explanation: 'Penumpukan selimut lumpur (> 2 meter) memicu carryover yang menyumbat media pasir filter.',
  },
  {
    id: 'post-4',
    category: 'Operasi normal IPA',
    question: 'Debit desain operasi normal pada aliran air baku instalasi SimSCADA-Air berada pada kisaran...',
    options: [
      '10–25 L/s',
      '75–100 L/s',
      '250–350 L/s',
      '500–750 L/s',
    ],
    correctIndex: 1,
    explanation: 'Rentang debit operasi normal air baku instalasi berada pada 75–100 L/s agar waktu detensi bak pengolahan terjaga.',
  },

  // --- 2. Mutu air (4 soal — berbeda isi, setara kisi-kisi) ---
  {
    id: 'post-5',
    category: 'Mutu air',
    question: 'Jika hasil pembacaan sensor kekeruhan air olahan keluar filter menunjukkan 3,3 NTU, status kelayakan air terhadap baku mutu Permenkes No. 2/2023 adalah...',
    options: [
      'Melebihi ambang (< 3,0 NTU), tidak layak dialirkan sebelum diturunkan',
      'Masih aman selama kadar sisa klorin bebas melebihi angka 1,5 mg/L',
      'Memenuhi baku mutu selama nilai pH air dijaga pada angka 9,2',
      'Dianggap normal apabila debit intake air baku ditingkatkan di atas 120 L/s',
    ],
    correctIndex: 0,
    explanation: 'Kekeruhan ≥ 3,0 NTU melanggar batas baku mutu dan memicu alarm Tinggi di sistem SCADA.',
  },
  {
    id: 'post-6',
    category: 'Mutu air',
    question: 'Dampak langsung apabila pH air olahan berada di atas 8,5 terhadap efektivitas klorinasi adalah...',
    options: [
      'Daya bunuh klorin meningkat sepuluh kali lipat terhadap pertumbuhan mikroba patogen',
      'Kekeruhan air baku di sungai langsung turun menjadi angka 1,0 NTU',
      'Efektivitas desinfeksi turun karena HOCl berubah menjadi ion OCl- yang lemah',
      'Nilai headloss di saringan pasir langsung turun menuju kondisi media bersih',
    ],
    correctIndex: 2,
    explanation: 'Pada pH basa (> 8,5), kesetimbangan klor bergeser ke ion hipoklorit (OCl-) yang daya desinfeksinya jauh lebih rendah.',
  },
  {
    id: 'post-7',
    category: 'Mutu air',
    question: 'Risiko utama bagi pelanggan jika kadar sisa klorin di reservoir terlalu tinggi (> 1,5 mg/L) atau terlalu rendah (< 0,20 mg/L) berturut-turut adalah...',
    options: [
      'Kenaikan kekeruhan air olahan filter dan lonjakan tekanan zona di atas 4,0 bar',
      'Pompa intake mengalami trip proteksi listrik dan headloss media pasir menjadi nol',
      'Penurunan pH air baku sungai serta pengendapan flok di dalam pipa distribusi',
      'Bau kaporit menyengat bila berlebih, serta pertumbuhan patogen bila < 0,20 mg/L',
    ],
    correctIndex: 3,
    explanation: 'Rentang 0,20–0,50 mg/L menyeimbangkan sterilitas mikrobiologis tanpa mengganggu kenyamanan rasa/bau air.',
  },
  {
    id: 'post-8',
    category: 'Mutu air',
    question: 'Metode pengujian laboratorium yang dijadikan acuan menentukan dosis optimum koagulan PAC saat karakteristik air baku berubah adalah...',
    options: [
      'Uji ketahanan tekanan hidrostatis pipa',
      'Jar test koagulasi-flokulasi skala laboratorium',
      'Kalibrasi katup pengurang tekanan PRV',
      'Pengukuran debit memakai venturi meter',
    ],
    correctIndex: 1,
    explanation: 'Jar test mensimulasikan dosis koagulan dan kecepatan pengadukan pada sampel air baku untuk menemukan dosis teroptimal.',
  },

  // --- 3. Respons gangguan (4 soal — berbeda isi, setara kisi-kisi) ---
  {
    id: 'post-9',
    category: 'Respons gangguan',
    question: 'Saat banjir lumpur menyebabkan kekeruhan air baku mencapai 185,0 NTU, mengapa menurunkan debit intake dari 100 L/s ke 75 L/s membantu pemulihan?',
    options: [
      'Menghentikan kebutuhan proses klorinasi di dalam tangki reservoir sepenuhnya',
      'Memperpanjang waktu tinggal di sedimentasi agar flok mengendap optimal',
      'Menaikkan tekanan keluar pompa distribusi kota ke 6,0 bar',
      'Langsung menghilangkan keperluan penambahan dosis bahan kimia koagulan PAC',
    ],
    correctIndex: 1,
    explanation: 'Mengurangi laju aliran memperbesar waktu detensi pengendapan sehingga beban partikel menuju filter berkurang.',
  },
  {
    id: 'post-10',
    category: 'Respons gangguan',
    question: 'Langkah penanganan paling efektif ketika pipa distribusi Zona 1 pecah terkonfirmasi pada monitor SCADA adalah...',
    options: [
      'Menutup katup isolasi ruas bocor untuk memulihkan tekanan zona',
      'Menyalakan seluruh pompa intake air baku dengan kapasitas aliran maksimal',
      'Menurunkan dosis koagulan PAC pada bak koagulasi hingga 5 mg/L',
      'Membiarkan katup zona terbuka penuh selama 30 menit sebelum bertindak',
    ],
    correctIndex: 0,
    explanation: 'Penutupan katup isolasi memutus kebocoran fisik seketika sehingga tekanan layanan segera pulih dan level reservoir terselamatkan.',
  },
  {
    id: 'post-11',
    category: 'Respons gangguan',
    question: 'Jika katup PRV mengalami gangguan macet separuh menutup sehingga tekanan Zona 1 jatuh di bawah 2,0 bar, tindakan koreksi di panel SCADA adalah...',
    options: [
      'Menutup katup masuk tangki reservoir agar air tidak terus mengalir',
      'Menjalankan siklus backwash serentak pada filter pasir di unit IPA',
      'Mematikan pompa distribusi utama P-101 tanpa menyalakan pompa cadangan',
      'Akui alarm lalu kembalikan setpoint PRV ke angka 2,5 bar',
    ],
    correctIndex: 3,
    explanation: 'Memulihkan setpoint PRV ke 2,5 bar mengembalikan bukaan hidrolis agar tekanan layanan kembali ke rentang aman 2,0–2,8 bar.',
  },
  {
    id: 'post-12',
    category: 'Respons gangguan',
    question: 'Bahaya kerusakan mekanis apabila operator menyalakan pompa sentrifugal saat level air reservoir sangat rendah (< 15%) atau katup hisap tertutup adalah...',
    options: [
      'Kekeruhan air olahan turun drastis di bawah 0,5 NTU',
      'Sisa klorin di ujung pipa meningkat drastis ke 2,0 mg/L',
      'Terjadi kavitasi dan dry running yang merusak impeler pompa',
      'Nilai pH air baku otomatis kembali ke angka netral 7,0',
    ],
    correctIndex: 2,
    explanation: 'Kekurangan air di sisi hisap menimbulkan gelembung uap (kavitasi) dan panas berlebih pada seal pompa.',
  },

  // --- 4. Penanganan alarm (4 soal — berbeda isi, setara kisi-kisi) ---
  {
    id: 'post-13',
    category: 'Penanganan alarm',
    question: 'Agar alarm gangguan proses seperti kekeruhan air olahan, sisa klor rendah, atau tekanan drop mengalami Auto-Clear, syarat yang harus terpenuhi adalah...',
    options: [
      'Operator menekan tombol ACK berulang kali sebanyak lima kali berturut-turut',
      'Nilai parameter menyentuh rentang aman selama tepat satu detik saja',
      'Parameter kembali ke rentang normal dan bertahan stabil 10 detik',
      'Seluruh unit pompa di instalasi dimatikan sementara selama dua detik',
    ],
    correctIndex: 2,
    explanation: 'Waktu tunda stabilisasi 10 detik mencegah alarm berkedip (chattering) saat nilai baru pulih sesaat.',
  },
  {
    id: 'post-14',
    category: 'Penanganan alarm',
    question: 'Nilai deadband pemulihan otomatis (auto-clear) untuk alarm kekeruhan air olahan Tinggi (ambang ≥ 3,0 NTU) adalah...',
    options: [
      '≤ 4,5 NTU bertahan stabil selama 3 detik',
      '≤ 2,7 NTU dan bertahan stabil 10 detik',
      '≤ 10,0 NTU bertahan stabil selama 60 detik',
      'Harus mencapai tepat 0,0 NTU sebelum dapat clear',
    ],
    correctIndex: 1,
    explanation: 'Deadband ≤ 2,7 NTU selama 10 detik memastikan air olahan benar-benar stabil di bawah ambang 3,0 NTU sebelum alarm clear.',
  },
  {
    id: 'post-15',
    category: 'Penanganan alarm',
    question: 'Mengapa alarm Pompa Trip dikategorikan sebagai alarm terkunci (latched) dengan prioritas KRITIS?',
    options: [
      'Agar operator mengalihkan beban ke cadangan dan menekan tombol Reset',
      'Karena sensor kekeruhan membutuhkan waktu 30 menit untuk kalibrasi ulang',
      'Supaya operator dapat langsung menekan Clear tanpa menyalakan pompa cadangan',
      'Karena pompa cadangan membutuhkan persetujuan pimpinan lembaga sebelum mulai dinyalakan',
    ],
    correctIndex: 0,
    explanation: 'Alarm latched mencegah peralatan yang mengalami gangguan kelistrikan/mekanis dianggap pulih tanpa tindakan reset eksplisit.',
  },
  {
    id: 'post-16',
    category: 'Penanganan alarm',
    question: 'Status alarm "Pulih, Belum Clear" pada daftar alarm menandakan kondisi berikut:',
    options: [
      'Operator sudah melakukan Clear namun gangguan lapangan masih berlangsung parah',
      'Alarm baru saja muncul pertama kali dan belum dilihat operator',
      'Nilai kekeruhan air olahan kembali naik melewati batas 5,0 NTU',
      'Penyebab atau reset sudah selesai, namun menunggu Clear manual operator',
    ],
    correctIndex: 3,
    explanation: 'Status Pulih, Belum Clear umumnya muncul pada alarm terkunci setelah tombol Reset ditekan sebelum Clear manual dilakukan.',
  },

  // --- 5. Hidrolika distribusi (4 soal — berbeda isi, setara kisi-kisi) ---
  {
    id: 'post-17',
    category: 'Hidrolika distribusi',
    question: 'Apa akibat utama jika tekanan jaringan pipa distribusi turun jauh di bawah 1,0–2,0 bar dalam waktu lama?',
    options: [
      'Debit pompa distribusi utama otomatis bertambah menjadi tiga kali lipat',
      'Kekeruhan di dalam bak flokulator menurun tajam secara seketika',
      'Umur katup pengurang tekanan PRV bertambah dua kali lebih panjang',
      'Pelanggan terganggu dan berisiko terjadi intrusi air tanah ke pipa',
    ],
    correctIndex: 3,
    explanation: 'Tekanan layanan rendah (≥ 2,0 bar idealnya) mencegah aliran balik/intrusi patogen dari sekitar pipa bawah tanah.',
  },
  {
    id: 'post-18',
    category: 'Hidrolika distribusi',
    question: 'Ketika operator mengaktifkan dua pompa distribusi identik secara paralel di stasiun pompa, perubahan hidrolika utama yang dihasilkan adalah...',
    options: [
      'Kadar sisa klorin di reservoir berubah menjadi 0,0 mg/L',
      'Kekeruhan air baku di saluran intake turun drastis',
      'Kapasitas debit aliran (L/s) bertambah untuk memenuhi jam puncak',
      'Tekanan pipa buang stasiun pompa turun menjadi 0,5 bar',
    ],
    correctIndex: 2,
    explanation: 'Operasi paralel dua pompa menggabungkan kapasitas aliran (L/s) guna memenuhi lonjakan permintaan pelanggan.',
  },
  {
    id: 'post-19',
    category: 'Hidrolika distribusi',
    question: 'Mengapa tekanan jaringan distribusi tidak boleh dibiarkan terlalu tinggi (misal > 2,8–3,5 bar) pada jam malam berkebutuhan rendah?',
    options: [
      'Membuat meteran air pelanggan berhenti berputar di malam hari',
      'Meningkatkan laju kebocoran fisik dan risiko sambungan pipa pecah',
      'Mengurangi waktu tinggal air bersih di titik pipa buntu',
      'Menurunkan konsumsi daya listrik pada stasiun pompa distribusi utama',
    ],
    correctIndex: 1,
    explanation: 'Tekanan berlebih memperbesar debit kebocoran di titik lemah jaringan; pengendalian PRV menekan angka NRW.',
  },
  {
    id: 'post-20',
    category: 'Hidrolika distribusi',
    question: 'Gejala lonjakan gelombang tekanan sesaat (water hammer) pada pipa distribusi umumnya dipicu oleh...',
    options: [
      'Penutupan katup pipa mendadak atau berhentinya pompa tiba-tiba',
      'Peningkatan dosis kapur sebesar 2 mg/L di bak koagulasi',
      'Pembacaan telemetri sisa klorin ujung pipa sebesar 0,30 mg/L',
      'Pembukaan katup penguras lumpur bak sedimentasi selama satu menit',
    ],
    correctIndex: 0,
    explanation: 'Perubahan momentum fluida secara tiba-tiba menimbulkan gelombang kejut tekanan tinggi di sepanjang pipa.',
  },
];

// Backward-compatible alias pointing to Set A
export const PRE_POST_TEST_QUESTIONS: PrePostQuestion[] = PRE_TEST_QUESTIONS_SET_A;


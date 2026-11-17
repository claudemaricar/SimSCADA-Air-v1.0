#!/usr/bin/env python3
"""
SimSCADA-Air Documentation Generator
Generates:
1. DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.md
2. DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html
3. public/DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html
"""

BASE_URL = "https://ais-pre-vzs4fmaac6yadtqm4sbtwf-792857744769.asia-northeast1.run.app"

# 19 Mockup screens dictionary
SCREENS = [
    ("L1", "mockup_l1_login.svg", "Portal Autentikasi Multi-Tenant", "Semua Peran", "Auto-detect peran & lembaga dari 10 akun demo PRD §5. Dilarang pemilih peran manual, hapus kata 'Sertifikasi' dari tagline. Sandi: Demo#2026."),
    ("L2", "mockup_l2_trainee_dashboard.svg", "Beranda Peserta & Roadmap Misi", "Peserta Operator", "Peta 5 tingkat kesulitan misi jalur aktif. Level operator (Muda 820 XP), aturan bintang PRD §8, AI Advisor, dan status piagam."),
    ("L3", "mockup_l3_track_select.svg", "Pemilihan Jalur Pembelajaran", "Peserta Operator", "3 Kartu Jalur PRD §7: IPA (9 misi), Distribusi (7 misi), Terpadu (17 misi). Tanpa prasyarat untuk Terpadu; pengakuan otomatis misi lulus."),
    ("L4", "mockup_l4_module_quiz.svg", "Modul Materi & Kuis Pra-Misi", "Peserta Operator", "Sesi contoh konsisten IPA-06 'Lonjakan Kekeruhan'. Briefing mentor Pak Slamet, batas Permenkes 2/2023, kuis 5 soal (KKM ≥60%)."),
    ("L4a", "mockup_l4a_pre_post_test.svg", "Pre-Test & Post-Test Evaluasi", "Peserta Operator", "Pengukuran Metrik T1: Kenaikan Kompetensi ≥25%. Komparasi Pre-test baseline (56) vs Post-test kelulusan (84, +50%)."),
    ("L5", "mockup_l5_scada_workspace.svg", "Workspace Simulator SCADA HMI", "Peserta Operator", "Mimic HMI 1 Hz. Unit distribusi nonaktif pada jalur IPA. Sistem alarm ISA-18.2 (bentuk simbol, 4 status, auto-clear). Kontrol lengkap PRD §9."),
    ("L5a", "mockup_l5a_control_narrative.svg", "Pop-up Narasi Titik Kontrol (Koagulasi)", "Peserta Operator", "Modal 'i' 6 bagian lengkap PRD §9 (Definisi, Parameter, Kontrol, Dampak, SOP, Referensi) + Catatan SOP Lokal Balai Nusantara & tooltip."),
    ("L6", "mockup_l6_results_scoring.svg", "Hasil Evaluasi Skor 4 Komponen", "Peserta Operator", "Skor 88/100 (2★, +176 XP). 4 Komponen: Ketepatan 38, Respons 22, Stabilitas 15, Alarm 13. Lencana 'Respons Kilat', debriefing Pak Slamet."),
    ("L7", "mockup_l7_badges_leaderboard.svg", "Galeri Lencana & Papan Peringkat", "Peserta Operator", "8 Lencana resmi PRD §8. Papan peringkat terisolasi dengan tab Kelompok/Lembaga & Mingguan/Sepanjang Waktu."),
    ("L8", "mockup_l8_certificate.svg", "PIAGAM KELULUSAN RESMI TERBIT", "Peserta Operator", "Format cetak A4 Landscape. Judul 'PIAGAM KELULUSAN' (bukan Sertifikat). Nomor SSA/NUS/2026/0001, Predikat Lulus dengan Baik, TTD Pimpinan & Instruktur, QR publik."),
    ("L8b", "mockup_l8b_certificate_pending.svg", "Status Piagam: Menunggu Persetujuan", "Peserta Operator", "Layar L8 versi kedua: Status pending verifikasi instruktur (Pak Budi). Tombol unduh nonaktif dengan tanda air peringatan."),
    ("L9", "mockup_l9_instructor_dashboard.svg", "Dasbor Pengawasan Kelas Instruktur", "Instruktur SPAM", "Matriks Peserta × Misi resmi (IPA-01..TRP-02). Deteksi peserta tertinggal (3x gagal). Aksi: Tugaskan, Buka Kunci, Beri Catatan, Setujui Piagam."),
    ("L10", "mockup_l10_manage_scenarios.svg", "Kelola Skenario Gangguan Kustom", "Instruktur SPAM", "Authoring tool skenario (FR-23) dengan isian tingkat kesulitan (1 Mudah s/d 5 Ujian), parameter deviasi, kunci SOP, dan penugasan kelas."),
    ("L11", "mockup_l11_session_replay.svg", "Putar Ulang Sesi & Audit Log (Replay)", "Instruktur SPAM", "Timeline scrubber interaktif. Sesi konsisten IPA-06 Dimas (08:30, skor 88). Sinkronisasi kurva sensor 1 Hz & evaluasi pedagogis Pak Budi."),
    ("L12", "mockup_l12_manage_users.svg", "Kelola Pengguna, Kelompok & Sisa Kursi", "Admin Lembaga", "Manajemen 7 akun resmi Balai Nusantara PRD §5. Monitoring kuota 46/50 kursi (⚠️ Peringatan Kuota ≥90%) dan kelompok Angkatan 1 & 2."),
    ("L13", "mockup_l13_tenant_settings.svg", "Pengaturan Lembaga & SOP Lokal", "Admin Lembaga", "Ambang kelulusan KKM, warna aksen piagam (Navy), saklar 'Persetujuan Instruktur Wajib', catatan SOP lokal koagulasi. Ambang alarm baku terkunci."),
    ("L14", "mockup_l14_tenant_evaluation.svg", "Dasbor Evaluasi Lembaga (Pimpinan)", "Pimpinan Lembaga", "4 Metrik Kunci T1–T4 PRD §3 (T1 +28.6%, T2 83.3%, T3 58 Hari, T4 75%). Kartu pemakaian lisensi, analisis 5 misi tersulit, dan ekspor PDF/Excel."),
    ("L15", "mockup_l15_superadmin.svg", "Konsol Super Admin Multi-Tenant", "Super Admin", "Monitoring multi-tenant: Balai Nusantara (NUS) & Tirta Mandiri (TRM). Peringatan dini: Kuota ≥90% & Lisensi berakhir ≤30 hari."),
    ("L16", "mockup_l16_public_verification.svg", "Portal Verifikasi Piagam Publik", "Publik / Rekruter", "Portal terbuka tanpa login. Nomor SSA/NUS/2026/0001. Hanya tampil 5 data inti: Nama, Lembaga, Jalur, Tanggal, Predikat & Status Sah. Tanpa NIP/Nilai/PDF.")
]

def generate_markdown():
    md = f"""# DOKUMEN CETAK BIRU & MOCK-UP LENGKAP SISTEM SimSCADA-Air v1.0
*(Arsitektur Desain Konseptual Sesuai PRD SimSCADA-Air v1.0)*

> **Pemberitahuan Dokumen:**  
> Dokumen ini memuat spesifikasi cetak biru (*blueprint*), diagram alur multi-role swimlane berformat standard **Draw.io (`.drawio`)**, dan berkas mock-up visual grafis berskala penuh (1600 × 1000 px) yang merepresentasikan desain konseptual **SimSCADA-Air v1.0** sesuai dengan seluruh ketentuan dalam *Product Requirements Document* (PRD).
>
> Seluruh 19 berkas mock-up grafis vektor definisi tinggi (*High-Definition Scalable Vector Graphics*) disimpan di direktori publik server aplikasi dan siap dibuka di peramban, diunduh langsung, maupun diimpor ke aplikasi desain (Figma, Illustrator, Inkscape).

---

## 📥 DAFTAR BERKAS MOCK-UP LENGKAP 19 LAYAR (L1 S/D L16, L4a, L5a, L8b)

| No | Kode | Nama Layar Prototipe PRD | Peran Pengguna | Tautan Unduh Langsung Berkas SVG | Ringkasan Fitur & Penyesuaian PRD |
| :---: | :---: | :--- | :--- | :--- | :--- |
"""
    for idx, (code, fname, name, role, desc) in enumerate(SCREENS, 1):
        url = f"{BASE_URL}/{fname}"
        md += f"| {idx} | **{code}** | {name} | {role} | [Buka `{fname}`]({url}) | {desc} |\n"

    md += f"""
---

## 🗺️ 1. DIAGRAM ALUR KERJA SISTEM BERFORMAT DRAW.IO & MULTI-ROLE SWIMLANE

### 📦 Berkas Diagram Draw.io Resmi:
* **Nama Berkas:** `alur_kerja_simscada.drawio` (Format Standar XML diagrams.net / draw.io)
* **Tautan Unduh Langsung:** [📥 **Unduh `alur_kerja_simscada.drawio`**]({BASE_URL}/alur_kerja_simscada.drawio)
* **Cara Membuka / Mengedit:**
  1. Buka [app.diagrams.net](https://app.diagrams.net) di peramban web (gratis, tanpa registrasi).
  2. Klik menu **File** > **Open From** > **Device...** lalu pilih berkas `alur_kerja_simscada.drawio`.
  3. Alternatif di VS Code / Cursor: Pasang ekstensi *"Draw.io Integration"* (karya Henning Dieterichs), lalu klik berkas `.drawio` untuk membuka editor visual interaktif secara langsung.

### 👥 Struktur 5 Jalur Peran (Swimlane Architecture):
1. **Swimlane 1: Super Admin Platform (`L15`)**
   * *Warna:* Indigo Tua (`#1e1b4b` / `#4338ca`)
   * *Tugas & Ruang Lingkup:* Registrasi lembaga tenant (Balai Diklat Air Minum Nusantara & Pusat Pelatihan Tirta Mandiri), alokasi paket jalur dan kuota kursi lisensi (50 kursi/tenant), pemeliharaan ambang batas alarm baku terpusat (Permenkes No. 2/2023), serta monitoring peringatan kuota ≥90% dan lisensi berakhir ≤30 hari.
2. **Swimlane 2: Administrator Lembaga / Tenant (`L1, L12, L13`)**
   * *Warna:* Hijau Zamrud (`#064e3b` / `#059669`)
   * *Tugas & Ruang Lingkup:* Konfigurasi profil lembaga, penetapan ambang kelulusan KKM (KKM biasa 70, kelulusan 80, post-test 70), pemilihan warna aksen piagam (Navy Blue), pengaktifan saklar *"Persetujuan Instruktur Wajib"*, penulisan catatan SOP lokal per titik kontrol (tampil di L5a), serta pengelolaan kuota 50 kursi dan kelompok angkatan.
3. **Swimlane 3: Instruktur / Pengajar SPAM (`L9, L10, L11`)**
   * *Warna:* Kuning Amber (`#451a03` / `#d97706`)
   * *Tugas & Ruang Lingkup:* Dasbor pengawasan kelas live (roster siswa × matriks misi IPA-01..TRP-02), deteksi otomatis peserta tertinggal (3x gagal berturut-turut pada misi yang sama), perancangan skenario gangguan kustom dengan isian tingkat kesulitan (FR-23), intervensi buka kunci misi manual bagi peserta remedial, audit investigasi rekaman sesi detik-per-detik (Replay L11), serta verifikasi & penandatanganan piagam kelulusan.
   * *Catatan Penting PRD:* **Instruktur BUKAN peserta tes**. Skenario yang dibuat instruktur di L10 disalurkan ke katalog kurikulum kelas (L3), bukan mengharuskan instruktur ikut remedial.
4. **Swimlane 4: Peserta Operator Air Minum (`L4a, L2 s/d L8, L8b`)**
   * *Warna:* Biru Laut (`#082f49` / `#0284c7`)
   * *Tugas & Ruang Lingkup:* Pre-Test diagnostik awal (L4a: baseline T1), Beranda roadmap 5 tingkat (L2: level Operator Magang ➔ Muda ➔ Madya ➔ Utama ➔ Ahli), pemilihan 3 jalur belajar (L3: IPA 9 misi, Distribusi 7 misi, Terpadu 17 misi tanpa prasyarat), modul materi & kuis pra-misi 5 soal KKM ≥60% (L4: sesi contoh IPA-06), workspace simulator SCADA HMI 1 Hz (L5), pop-up narasi titik kontrol 'i' 6 bagian (L5a), evaluasi skor 4 komponen (L6: skor 88, 2★, +176 XP, Lencana 'Respons Kilat', debriefing mentor Pak Slamet), pembukaan 8 lencana PRD & papan peringkat terisolasi (L7), Post-Test akhir KKM ≥70 (L4a: Metrik T1 naik +50%), pengajuan piagam pending (L8b), hingga penerbitan resmi Piagam Kelulusan A4 (L8).
5. **Swimlane 5: Pimpinan Lembaga & Verifikasi Publik (`L14, L16`)**
   * *Warna:* Ungu Deep (`#3b0764` / `#9333ea`)
   * *Tugas & Ruang Lingkup:* **Pimpinan (L14):** Dasbor evaluasi eksekutif berbasis 4 Metrik Kunci PRD §3 (T1 Kenaikan Kompetensi +28.6%, T2 Penguasaan 5 Gangguan Utama 83.3%, T3 Waktu Lulus 58 Hari, T4 Tingkat Kelulusan 75%), kartu pemakaian lisensi (46/50 kursi, sisa 245 hari, 412 jam simulasi), 5 misi paling sulit, dan ekspor laporan berkop PDF/Excel.<br>**Publik (L16):** Portal terbuka tanpa login untuk rekruter/regulator dengan validasi 5 data pokok (Nama, Lembaga, Jalur, Tanggal, Predikat) dan status keabsahan SAH/VALID tanpa menampilkan detail nilai, NIP, atau tombol unduh PDF.

---

### 🗺️ Peta Alur Teks Lengkap (ASCII Multi-Role Journey Map):

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   [ L15: KONSOL SUPER ADMIN PLATFORM (PROVISIONING GLOBAL) ]                                     │
│                                   • Daftarkan Tenant: Balai Diklat Air Minum Nusantara & Pusat Tirta Mandiri                     │
│                                   • Alokasi 50 Kursi/Tenant · Tetapkan Ambang Alarm Baku Terpusat (Permenkes 2/2023)             │
│                                   • Pantau Peringatan Kuota ≥90% (Nusantara 46/50) & Lisensi ≤30 Hari (Tirta 28 Hari)             │
└─────────────────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────┘
                                                              │
                                                              ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    [ TATA KELOLA ADMINISTRATOR LEMBAGA / TENANT ADMIN ]                                          │
│        ├─ [ L13: Pengaturan Lembaga ] ───> Ambang KKM (70/80), Warna Aksen Navy, Saklar Approval 'ON', SOP Lokal Koagulasi        │
│        └─ [ L12: Kelola Akun & Kursi ] ──> Alokasi Kursi (46/50 Terpakai, Sisa 4), Kelompok Angkatan 1 & 2, Roster Akun PRD §5   │
└─────────────────────────────────────────────────────────────┬────────────────────────────────────────────────────────────────────┘
                                                              │
                                                              ▼
                                                 [ L1: Login Multi-Tenant ]
                                       Auto-Detect Akun Demo PRD §5 (Sandi: Demo#2026)
                                                              │
                ┌─────────────────────────────────────────────┴─────────────────────────────────────────────┐
                │                                                                                           │
                ▼ (Peran: Instruktur SPAM)                                                                  ▼ (Peran: Peserta Operator)
┌───────────────────────────────────────────────────────────────┐                         ┌───────────────────────────────────────────────────────────────┐
│               [ JALUR INSTRUKTUR PENGAJAR ]                   │                         │             [ JALUR BELAJAR OPERATOR AIR MINUM ]              │
│                                                               │                         │                                                               │
│ 1. [ L9: Dasbor Pengawasan Kelas Instruktur ]                 │                         │ 1. [ L4a: Pre-Test Diagnostik Awal ]                          │
│    • Pantau Matriks Peserta × Misi (IPA-01 s/d TRP-02)        │                         │    Baseline Kompetensi Awal: Skor 56/100 (Metrik T1)          │
│    • Pantau Bintang, Skor Terakhir & Hari Sejak Aktif         │                         │                      │                                        │
│    • Deteksi Otomatis Peserta Tertinggal (3x Gagal IPA-07)    │                         │                      ▼                                        │
│    • Tombol: Tugaskan Skenario, Buka Kunci, Beri Catatan      │                         │ 2. [ L2: Beranda Peserta & Roadmap Misi ]                     │
│                      │                                        │                         │    • Level: Operator Muda (820 XP / 1.200 XP ke Madya)        │
│                      ▼                                        │                         │    • Roadmap 5 Tingkat: Pengenalan, Normal, Gangguan, Ujian   │
│ 2. [ L10: Kelola Skenario Gangguan Kustom (FR-23) ]           │                         │    • AI Advisor: Saran latihan ulang IPA-07                   │
│    • Rancang Skenario Abnormalitas Hidrolika & Kimia          │                         │                      │                                        │
│    • Pilihan Tingkat Kesulitan PRD: 1 Mudah s/d 5 Ujian       │                         │                      ▼                                        │
│    • Tugaskan ke Kelompok Kelas (Angkatan 1 Nusantara)        │════════════════════════>│ 3. [ L3: Pemilihan Jalur Pembelajaran ]                       │
│                      │              (Skenario Masuk Katalog)  │                         │    • 3 Kartu: IPA (9), Distribusi (7), Terpadu (17 Misi)      │
│                      ▼                                        │                         │    • Tanpa prasyarat Terpadu · Pengakuan progres otomatis     │
│ 3. [ L11: Investigasi Audit & Putar Ulang (Replay) ]          │                         │                      │                                        │
│    • Interactive Scrubber Bar (00:00 s/d 08:30)               │                         │                      ▼                                        │
│    • Audit Kronologis Alarm ISA-18.2 & Respon ACK             │                         │ 4. [ L4: Modul Materi & Kuis 5 Soal Pra-Misi ]                │
│    • Sinkronisasi Kurva Kekeruhan vs Dosis Koagulan 1 Hz      │                         │    • Sesi Contoh: IPA-06 Lonjakan Kekeruhan (T3 Sulit)        │
│    • Tulis Catatan Pedagogis Pak Budi & Validasi Sesi         │                         │    • Briefing Mentor Pak Slamet & Batas Permenkes 2/2023      │
│                      │                                        │                         │    • Kuis 5 Soal Pra-Misi (KKM ≥ 60 Membuka Simulator)        │
│                      │                                        │                         │                      │                                        │
│                      │                                        │                         │                      ▼                                        │
│                      │                                        │                         │ 5. [ L5: Workspace Simulator SCADA HMI Dinamis 1 Hz ]         │
│                      │                                        │                         │    • Mimic IPA Aktif · Unit Distribusi Nonaktif (Dimmed)      │
│                      │                                        │                         │    • Titik Pantau: Tekanan bar, Debit L/s, Sisa Klor mg/L     │
│                      │                                        │                         │    • Alarm ISA-18.2 (Bentuk Simbol, 4 Status, Auto-Clear)     │
│                      │                                        │                         │    • Tombol Clear Nonaktif jika penyebab belum selesai        │
│                      │                                        │                         │    • Buka Ikon 'i': [ L5a Pop-up Narasi Titik Kontrol ]       │
│                      │                                        │                         │                      │                                        │
│                      │                                        │                         │                      ▼                                        │
│                      │                                        │                         │ 6. [ L6: Hasil Evaluasi Skor 4 Komponen ]                     │
│                      │                                        │                         │    • Formula Bobot: Ketepatan 38/40 + Respons 22/25 +         │
│                      │                                        │                         │      Stabilitas 15/20 + Alarm 13/15 = Skor 88 / 100           │
│                      │                                        │                         │    • Bintang: 2★ (85-94) · XP: 88 × 2,0x = +176 XP            │
│                      │                                        │                         │    • Lencana Baru Terbuka: 'Respons Kilat'                    │
│                      │                                        │                         │    • Debriefing Tokoh Mentor: Operator Senior (Pak Slamet)    │
│                      │                                        │                         │                      │                                        │
│                      │                                        │                         │       ┌──────────────┴──────────────┐                         │
│                      │                                        │                         │       ▼ (Skor < KKM 70/80)          ▼ (Skor ≥ KKM)            │
│                      │                                        │                         │ [Remedial Mandiri]           [Lulus Misi Jalur]               │
│                      │                                        │                         │       │                             │                         │
│                      │                                        │                         │       │ (Intervensi Unlock)         ▼                         │
│                      ├────────────────────────────────────────│────────────────────────>│ [L9: Buka Kunci]             7. [ L7: Lencana & Rank ]        │
│                      │                                        │                         │                                 • 8 Lencana Resmi PRD §8      │
│                      │                                        │                         │                                 • Papan Peringkat Terisolasi  │
│                      │                                        │                         │                                             │                 │
│                      │ (Data Telemetri Log Mengalir ke Replay)│                         │                                             ▼                 │
│                      │<───────────────────────────────────────│─────────────────────────│ 8. [ L4a: Post-Test Evaluasi Akhir Jalur ]                    │
│                      │                                        │                         │    Skor 84/100 (Kenaikan Metrik T1: +50% > 25%)               │
│                      │                                        │                         │                      │                                        │
│                      ▼                                        │                         │                      ▼                                        │
│ 4. [ L9: Verifikasi & Tanda Tangan Piagam ]                   │                         │ 9. [ L8b: Piagam Menunggu Persetujuan ]                       │
│    • Verifikasi 4 Syarat Kelulusan PRD §13                    │                         │    Tombol Unduh Nonaktif Sampai Diverifikasi Instruktur       │
│    • Bubuhkan TTD Digital Instruktur (Pak Budi)               │                         │                      │                                        │
│                      │                                        │                         │                      ▼                                        │
│                      └────────────────────────────────────────│────────────────────────>│ 10. [ L8: PIAGAM KELULUSAN RESMI TERBIT ]                     │
│                                       (Pengesahan Piagam Selesai)                       │     • Format Cetak A4 Landscape Bersih (Bukan Sertifikat)     │
│                                                                                         │     • Nomor: SSA/NUS/2026/0001 · Predikat: Lulus dengan Baik  │
│                                                                                         │     • Disahkan Pimpinan (Dr. Bambang) & Instruktur (Pak Budi) │
│                                                                                         │     • QR Code Verifikasi Publik · Catatan Kaki Wajib PRD §13  │
└───────────────────────────────────────────────────────────────┘                         └──────────────────────┬────────────────────────────────────────┘
                                                                                                                 │
                                 ┌───────────────────────────────────────────────────────────────────────────────┴────────────────────────────────────────┐
                                 │                                                                                                                        │
                                 ▼                                                                                                                        ▼
┌───────────────────────────────────────────────────────────────┐                         ┌───────────────────────────────────────────────────────────────┐
│           [ L14: DASBOR EVALUASI LEMBAGA (PIMPINAN) ]         │                         │            [ L16: PORTAL VERIFIKASI PIAGAM PUBLIK ]           │
│ • Metrik T1: Kenaikan Kompetensi (+28,6% > Target 25%)        │                         │ • Portal Terbuka Tanpa Login untuk Rekruter & Regulator       │
│ • Metrik T2: 83,3% Lulus 5 Gangguan Utama (> Target 80%)      │                         │ • Input Nomor Registrasi: SSA/NUS/2026/0001                   │
│ • Metrik T3: Waktu Menuju Lulus 58 Hari (±2 Bulan)            │                         │ • Tampilkan 5 Data Pokok: Nama, Lembaga, Jalur, Tanggal, Predikat│
│ • Metrik T4: Tingkat Kelulusan 75% (> Target 70%)             │                         │ • Status Keabsahan: SAH / VALID (Bebas Pencabutan)            │
│ • Kartu Lisensi: 46/50 Kursi (92%), Sisa 245 Hari, 412 Jam    │                         │ • Tanpa NIP, Tanpa Detail Nilai, Tanpa Tombol Unduh PDF       │
│ • Analisis 5 Misi Paling Sulit & Kesalahan Tersering          │                         │ • Catatan Kaki Wajib PRD §13 Tampil Jelas Tidak Tertutup      │
│ • Ekspor Laporan Berkop Resmi PDF & Excel (.xlsx)             │                         └──────────────────────────────┬────────────────────────────────┘
└───────────────────────────────────────────────────────────────┘                                                        │
                                                                                                                         ▼
                                                                                                          [ Operator Siap Bertugas Nyata ]
```

---

## 📐 2. ANATOMI WIREFRAME & DETAIL MOCK-UP PER LAYAR (19 LAYAR LENGKAP)

Seluruh 19 berkas mock-up visual grafis SVG (1600 × 1000 px) telah dikoreksi total dan siap ditinjau:
"""
    for code, fname, name, role, desc in SCREENS:
        url = f"{BASE_URL}/{fname}"
        md += f"""
### Layar {code}: {name}
* **Nama Berkas SVG:** [`{fname}`]({url})
* **Peran Pengguna:** {role}
* **Tinjauan Kepatuhan PRD v1.0:**
  {desc}
"""
    return md

def generate_html(md_content):
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dokumen Blueprint & Mock-up SimSCADA-Air v1.0</title>
  <style>
    :root {{
      --bg: #0b1120;
      --card: #1e293b;
      --border: #334155;
      --primary: #0284c7;
      --accent: #38bdf8;
      --success: #10b981;
      --amber: #f59e0b;
      --text: #f8fafc;
      --muted: #94a3b8;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      margin: 0;
      padding: 30px;
    }}
    .container {{
      max-width: 1400px;
      margin: 0 auto;
    }}
    h1, h2, h3, h4 {{
      color: #ffffff;
      margin-top: 1.5em;
    }}
    h1 {{
      font-size: 2.2rem;
      border-bottom: 2px solid var(--primary);
      padding-bottom: 12px;
      color: var(--accent);
    }}
    h2 {{
      font-size: 1.6rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
      color: var(--text);
    }}
    a {{
      color: var(--accent);
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      background: var(--card);
      border-radius: 8px;
      overflow: hidden;
    }}
    th, td {{
      padding: 12px 16px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    th {{
      background: #0f172a;
      color: var(--accent);
      font-weight: 700;
    }}
    tr:nth-child(even) {{
      background: rgba(15, 23, 42, 0.4);
    }}
    pre {{
      background: #070c18;
      padding: 20px;
      border-radius: 8px;
      border: 1px solid var(--border);
      overflow-x: auto;
      font-family: monospace;
      font-size: 12px;
      line-height: 1.35;
      color: #cbd5e1;
    }}
    blockquote {{
      background: rgba(2, 132, 199, 0.1);
      border-left: 4px solid var(--primary);
      padding: 12px 20px;
      margin: 20px 0;
      color: #cbd5e1;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: bold;
      background: #0284c7;
      color: #fff;
    }}
    .btn {{
      display: inline-block;
      padding: 8px 16px;
      background: var(--primary);
      color: white;
      border-radius: 6px;
      font-weight: 600;
      text-decoration: none;
      margin: 4px 0;
    }}
    .btn:hover {{
      background: #0369a1;
      text-decoration: none;
    }}
    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>📘 Dokumen Blueprint &amp; Mock-up Lengkap SimSCADA-Air v1.0</h1>
    <blockquote>
      <strong>Pemberitahuan Resmi:</strong> Dokumen ini merangkum cetak biru arsitektur, diagram swimlane Draw.io multi-peran, dan seluruh 19 berkas mock-up grafis berskala penuh (1600 × 1000 px SVG) yang 100% patuh pada Dokumen Kebutuhan Produk (PRD SimSCADA-Air v1.0).
    </blockquote>

    <h2>📥 Daftar Berkas Mock-up Lengkap 19 Layar (L1 s/d L16, L4a, L5a, L8b)</h2>
    <table>
      <thead>
        <tr>
          <th>No</th>
          <th>Kode</th>
          <th>Nama Layar Prototipe PRD</th>
          <th>Peran Pengguna</th>
          <th>Tautan Buka / Unduh SVG</th>
          <th>Spesifikasi Kepatuhan PRD</th>
        </tr>
      </thead>
      <tbody>
"""
    for idx, (code, fname, name, role, desc) in enumerate(SCREENS, 1):
        url = f"{BASE_URL}/{fname}"
        html += f"""        <tr>
          <td>{idx}</td>
          <td><strong>{code}</strong></td>
          <td>{name}</td>
          <td><span class="badge">{role}</span></td>
          <td><a class="btn" href="{url}" target="_blank">Buka {fname}</a></td>
          <td><small>{desc}</small></td>
        </tr>\n"""

    html += f"""      </tbody>
    </table>

    <h2>🗺️ Diagram Alur Kerja Sistem Berformat Draw.io (Multi-Role Swimlane)</h2>
    <div class="card">
      <p><strong>Berkas Resmi Draw.io:</strong> <a class="btn" href="{BASE_URL}/alur_kerja_simscada.drawio" download>📥 Unduh alur_kerja_simscada.drawio</a></p>
      <p>Berkas diagram XML standar diagrams.net ini memisahkan secara tegas 5 peran pengguna:</p>
      <ul>
        <li><strong>Super Admin Platform (L15):</strong> Provisioning multi-tenant, alokasi lisensi kuota kursi, ambang alarm baku terpusat.</li>
        <li><strong>Admin Lembaga (L1, L12, L13):</strong> Konfigurasi KKM kelulusan, warna aksen piagam, saklar persetujuan instruktur, catatan SOP lokal.</li>
        <li><strong>Instruktur SPAM (L9, L10, L11):</strong> Dasbor pengawasan kelas live, authoring skenario kustom (FR-23), replay investigasi audit, approval piagam.</li>
        <li><strong>Peserta Operator (L4a, L2-L8, L8b):</strong> Pre-test, beranda roadmap 5 tingkat, 3 pilihan jalur, kuis pra-misi, simulator SCADA HMI 1 Hz, pop-up narasi 'i', 4 komponen skor, 8 lencana, post-test, hingga piagam resmi.</li>
        <li><strong>Pimpinan &amp; Publik (L14, L16):</strong> Dasbor eksekutif evaluasi T1-T4, ROI diklat, dan portal verifikasi nomor registrasi publik tanpa login.</li>
      </ul>
    </div>

    <h2>🗺️ Diagram Alur Teks (ASCII Journey Map)</h2>
    <pre>{generate_markdown().split('```')[1]}</pre>

    <h2>📐 Rincian 19 Layar Prototipe</h2>
"""
    for code, fname, name, role, desc in SCREENS:
        url = f"{BASE_URL}/{fname}"
        html += f"""    <div class="card">
      <h3>Layar {code}: {name}</h3>
      <p><strong>Berkas SVG:</strong> <a href="{url}" target="_blank">{fname}</a> | <strong>Peran:</strong> {role}</p>
      <p>{desc}</p>
      <iframe src="{fname}" width="100%" height="450" style="border:1px solid #334155; border-radius:6px; background:#0b1120;"></iframe>
    </div>\n"""

    html += """  </div>
</body>
</html>"""
    return html

md = generate_markdown()
html = generate_html(md)

with open("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.md", "w") as f:
    f.write(md)

with open("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html", "w") as f:
    f.write(html)

with open("public/DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html", "w") as f:
    f.write(html)

print("Documentation generated successfully: .md and .html in root and /public.")

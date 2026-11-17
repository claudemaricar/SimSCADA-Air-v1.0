#!/usr/bin/env python3
"""
SimSCADA-Air Documentation Updater
Generates:
1. DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.md
2. DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html
3. public/DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html
"""
import os

SCREENS = [
    ("L1", "mockup_l1_login.svg", "Portal Autentikasi Multi-Tenant", "Semua Peran", 
     "Auto-detect peran dan lembaga dari 10 akun demo PRD §5 tanpa pemilih peran manual. Pilihan lembaga resmi 'Balai Diklat Air Minum Nusantara' dan 'Pusat Pelatihan Tirta Mandiri'. 5 Peran lengkap termasuk Pimpinan Lembaga. Sandi: Demo#2026."),
    
    ("L2", "mockup_l2_trainee_dashboard.svg", "Beranda Peserta & Roadmap Misi", "Peserta Operator", 
     "Dasbor Dimas Wahyu Pratama (peserta.ipa): 7 dari 9 misi IPA lulus, 14 bintang (3,2,2,2,2,2,1,-,-), 820 XP, jenjang Operator Muda (sisa 380 XP ke Madya). Peta 5 tingkat kesulitan misi khusus jalur IPA (IPA-01..IPA-09), grafik tren skor, 3 lencana terbuka, peringkat #2, dan status piagam belum memenuhi."),
    
    ("L3", "mockup_l3_track_select.svg", "Pemilihan Jalur Pembelajaran", "Peserta Operator", 
     "3 Kartu Jalur PRD §7: Pengolahan IPA (9 misi), Distribusi (7 misi), dan Terpadu (17 misi). Tanpa prasyarat untuk jalur Terpadu; pengakuan otomatis misi yang telah lulus saat berpindah jalur. Catatan isolasi paket lisensi tenant."),
    
    ("L4", "mockup_l4_module_quiz.svg", "Modul Materi & Kuis Pra-Misi", "Peserta Operator", 
     "Sesi contoh konsisten IPA-06 'Lonjakan Kekeruhan Air Baku'. Pengenalan SOP koagulasi darurat, batas Permenkes No. 2/2023 (<1,5 NTU), target batas waktu respons alarm skenario 60 detik, kuis 5 butir soal pemahaman (KKM ≥60%). Kartu poin SOP rapi tanpa penumpukan teks."),
    
    ("L4a", "mockup_l4a_pre_post_test.svg", "Pre-Test & Post-Test Evaluasi", "Peserta Operator", 
     "Instrumen pengukuran Target KPI T1 (Kenaikan Kompetensi ≥25%). Sisi Pre-Test menampilkan baseline awal Dimas Wahyu Pratama (Skor 56/100). Sisi Post-Test menampilkan evaluasi kelulusan Andi Kurniawan (Skor 88/100, kenaikan +32 poin / +57,1%, melampaui target T1 25%)."),
    
    ("L5", "mockup_l5_scada_workspace.svg", "Workspace Simulator SCADA HMI", "Peserta Operator", 
     "Mimic HMI interaktif frekuensi 1 Hz. Menit 02:00 saat alarm kekeruhan tinggi diakui (ACK) dan penanganan dosis 48 mg/L berlangsung. Banner alarm menampilkan status Diakui (ACK), tombol Clear dinonaktifkan dengan pesan peringatan 'Penyebab belum selesai: 3,4 NTU ≥ 3,0 NTU'. Kontrol lengkap PRD §9, PRV disembunyikan untuk misi IPA, unit distribusi diredupkan."),
    
    ("L5a", "mockup_l5a_control_narrative.svg", "Pop-up Narasi Titik Kontrol (Koagulasi)", "Peserta Operator", 
     "Modal informasi 'i' 6 bagian lengkap PRD §9: Definisi proses hidrolika/kimia, Parameter dipantau (satuan & rentang normal), Variabel kendali, Dampak ke hilir, Gangguan umum & SOP singkat, serta Referensi belajar. Dilengkapi kotak catatan SOP lokal Balai Nusantara dan tata letak teks berjenjang rapi bebas terpotong."),
    
    ("L6", "mockup_l6_results_scoring.svg", "Hasil Evaluasi Skor 4 Komponen", "Peserta Operator", 
     "Evaluasi terinci sesi Dimas Wahyu Pratama pada misi IPA-06: Skor 88/100, Bintang 2 (85–94), XP +176 (88 × 2,0x). Rincian 4 kartu komponen PRD §8 (Mutu 23/25, Waktu Respons 25/25 [25 dtk < 50% × 60s target], Efisiensi Kimia 22/25, Prosedur Alarm 18/25). Perolehan lencana 'Respons Kilat' dan debriefing mentor Pak Slamet."),
    
    ("L7", "mockup_l7_badges_leaderboard.svg", "Galeri Lencana & Papan Peringkat", "Peserta Operator", 
     "8 Lencana resmi PRD §8 (Penjelajah Titik Kontrol, Respons Kilat, Tanpa Alarm Terlewat, Penjaga Mutu Air, Penjaga Tekanan, Tiga Bintang IPA, Hulu ke Hilir, Lulus Tanpa Petunjuk) dengan syarat persis PRD. Papan peringkat terisolasi Balai Nusantara (FR-21) dengan filter Kelompok / Seluruh Lembaga dan Mingguan / Sepanjang Waktu. Posisi Dimas #2 (820 XP) di bawah Andi Kurniawan #1 (3.820 XP)."),
    
    ("L8", "mockup_l8_certificate.svg", "Piagam Kelulusan Operator (Terbit)", "Peserta Operator", 
     "Piagam Kelulusan sah Andi Kurniawan (peserta.lulus). Nomor Register: SSA/NUS/2026/0001 (SUDAH TERBIT 15 Maret 2026). Jalur Terpadu 17 Misi, Skor Post-Test 96/100, Bintang 3 (Sangat Baik), 3.820 XP, Operator Ahli. Ditandatangani Instruktur Penilai Budi Santoso, S.T. dan Kepala Balai Diklat Ir. H. Bambang Sutrisno, M.Eng. Dilengkapi QR verifikasi."),
    
    ("L8b", "mockup_l8b_certificate_pending.svg", "Status Piagam: Menunggu Persetujuan", "Peserta Operator", 
     "Varian layar L8 versi kedua: Pratinjau draf piagam Rian Hidayat (peserta contoh - Angkatan 1) dengan nomor register dicadangkan SSA/NUS/2026/0002. Tanda air 'DRAFT - MENUNGGU ACC', tombol unduh nonaktif, dan status menunggu validasi sesi replay oleh instruktur."),
    
    ("L9", "mockup_l9_instructor_dashboard.svg", "Dasbor Pengawasan Kelas Instruktur", "Instruktur SPAM", 
     "Dasbor instruktur Budi Santoso, S.T. memantau 42 peserta aktif dalam 2 kelompok binaan (Angkatan 1 & 2). Matriks progres resmi IPA-01 s/d IPA-09 / DST. Data konsisten: Andi (Piagam Terbit, Ahli), Dimas (14★, 820 XP), Siti (12★), Rian (Menunggu ACC), Budi Baru (Magang). Tombol aksi: Tinjau Sesi Replay, Setujui Piagam, Ekspor Portofolio Nilai CSV."),
    
    ("L10", "mockup_l10_manage_scenarios.svg", "Kelola Skenario Gangguan Kustom", "Instruktur SPAM", 
     "Authoring Tool skenario gangguan (FR-23). Form perancangan skenario lengkap dengan dropdown tingkat kesulitan dan pengali XP PRD §7 (1,0x s/d 3,0x), batas toleransi respons alarm (target 60 detik), dan katalog misi bawaan IPA-01..IPA-09, DST-01..DST-07, TRP-01, TRP-02."),
    
    ("L11", "mockup_l11_session_replay.svg", "Putar Ulang Sesi & Audit Log (Replay)", "Instruktur SPAM", 
     "Replay audit sesi IPA-06 Dimas Wahyu Pratama. Log kronologis identik L6: Gangguan 01:00, Alarm 01:10, ACK 01:25 (respons 25 detik < 50% × 60s), Dosis 48 mg/L 01:45, Mixer 100 RPM 02:30, Auto-clear 06:20 (1,2 NTU), Selesai 08:30 (Skor 88). Scrubber interaktif dengan label penanda berjenjang rapi tanpa tabrakan."),
    
    ("L12", "mockup_l12_manage_users.svg", "Kelola Pengguna, Kelompok & Lisensi", "Admin Lembaga", 
     "Manajemen 46 akun terdaftar (kuota 50 kursi lisensi Balai Nusantara, 42 peserta aktif login 14 hari). Menampilkan 7 akun demo PRD §5 dan ringkasan 39 peserta contoh lainnya. Tombol Tambah Pengguna, Impor CSV (FR-20), aksi Ubah/Reset/Nonaktifkan per baris, dan manajemen kelompok belajar Angkatan 1 & 2."),
    
    ("L13", "mockup_l13_tenant_settings.svg", "Pengaturan Lembaga & Standar Evaluasi", "Admin Lembaga", 
     "Konfigurasi standar evaluasi: 3 kartu ambang kelulusan KKM rapi (Latihan ≥70, Kelulusan ≥80, Bintang Tiga ≥95), bobot 4 komponen (30%, 25%, 25%, 20%). Fitur unggah logo lembaga, saklar papan peringkat peserta (FR-21), serta penatausahaan nama dan jabatan instruktur dan kepala balai penanda tangan piagam."),
    
    ("L14", "mockup_l14_tenant_evaluation.svg", "Dasbor Evaluasi & Utilisasi Lembaga", "Pimpinan Lembaga", 
     "Dasbor eksekutif Ir. H. Bambang Sutrisno, M.Eng. memantau target pencapaian PRD §3: T1 Peningkatan Pre-to-Post (+50,5% > target 25%), T2 Penyelesaian Misi (83,3% > target 70%), T3 Waktu Tanggap Darurat (28,4 dtk < target 45s), T4 Tingkat Kelulusan (76,2% > target 60%). Utilisasi lisensi 42 peserta aktif / 46 terdaftar / 50 kuota (92% okupansi)."),
    
    ("L15", "mockup_l15_superadmin.svg", "Konsol Super Admin Multi-Tenant", "Super Admin", 
     "Konsol pengawasan pusat platform SimSCADA-Air. Menampilkan 2 lembaga: Balai Diklat Air Minum Nusantara (NUS, 50 kursi, paket lengkap: IPA + Distribusi + Terpadu 3 Jalur) dan Pusat Pelatihan Tirta Mandiri (TRM, 50 kursi, paket: IPA + Distribusi 2 Jalur). Manajemen kuota, isolasi database, dan audit trail pusat."),
    
    ("L16", "mockup_l16_public_verification.svg", "Portal Publik Verifikasi Piagam", "Publik / Rekruter", 
     "Portal terbuka tanpa otentikasi login untuk memeriksa keaslian piagam. Menampilkan data sah nomor SSA/NUS/2026/0001 atas nama Andi Kurniawan (Jalur Terpadu, Skor 96, Predikat Sangat Baik, Operator Ahli 3.820 XP, Terbit 15 Maret 2026 oleh Balai Diklat Air Minum Nusantara). Segel otentikasi digital QR dan formulir pencarian nomor piagam lainnya.")
]

def generate_markdown():
    md = """# DOKUMEN CETAK BIRU & MOCK-UP LENGKAP SISTEM SimSCADA-Air v1.0
*(Arsitektur Desain Konseptual Sesuai Dokumen Kebutuhan Produk PRD SimSCADA-Air v1.0)*

> **Status Dokumen:**  
> Dokumen ini memuat spesifikasi cetak biru (*blueprint*), diagram alur kerja multi-role swimlane berformat standard **Draw.io (`alur_kerja_simscada.drawio`)**, dan 19 berkas mock-up grafis SVG berskala penuh (1920 × 1080 px) yang merepresentasikan desain konseptual **SimSCADA-Air v1.0** sesuai dengan ketentuan dalam *Product Requirements Document* (PRD).

---

## 1. Ringkasan Eksekutif & Struktur Mock-up

Sistem **SimSCADA-Air v1.0** dirancang sebagai platform simulasi SCADA mandiri untuk pelatihan operator Sistem Penyediaan Air Minum (SPAM). Seluruh alur pembelajaran dan operasional disajikan dalam 19 antarmuka visual (L1–L16, termasuk L4a, L5a, dan L8b) yang mencakup 5 peran pengguna: **Super Administrator, Admin Lembaga, Pimpinan Lembaga, Instruktur Pengajar, dan Peserta Operator**, serta akses **Publik**.

### 1.1 Matriks Keselarasan Data Contoh Antar-Layar
Data contoh diselaraskan secara konsisten di seluruh layar:
* **Lembaga Demo:** "Balai Diklat Air Minum Nusantara" (kode `NUS`, kuota 50 kursi) dan "Pusat Pelatihan Tirta Mandiri" (kode `TRM`, kuota 50 kursi).
* **Akun Demo PRD §5 (Sandi: `Demo#2026`):**
  1. `superadmin` — Super Administrator Platform
  2. `admin.nusantara` — Admin Lembaga Balai Diklat Air Minum Nusantara
  3. `pimpinan.nusantara` — Ir. H. Bambang Sutrisno, M.Eng. (Pimpinan Lembaga)
  4. `instruktur.nusantara` — Budi Santoso, S.T. (Instruktur Pengajar)
  5. `peserta.baru` — Budi Baru (Peserta Magang, baru menyelesaikan pre-test 52/100)
  6. `peserta.ipa` — Dimas Wahyu Pratama (Peserta Muda, 820 XP, 14★, 7/9 misi IPA lulus)
  7. `peserta.distribusi` — Siti Rahmawati (Peserta Muda, 750 XP, 12★, 5/7 misi Distribusi)
  8. `peserta.lulus` — Andi Kurniawan (Operator Ahli, 3.820 XP, 48★, Jalur Terpadu 17 misi, Piagam `SSA/NUS/2026/0001` SUDAH TERBIT)
  9. `admin.tirta` — Admin Lembaga Pusat Pelatihan Tirta Mandiri
  10. `peserta.tirta` — Peserta Pelatihan Tirta Mandiri
* **Sesi Contoh Konsisten (L4, L5, L6, L11):** Skenario IPA-06 "Gangguan: Lonjakan Kekeruhan Air Baku" yang dijalankan oleh Dimas Wahyu Pratama:
  - Lonjakan kekeruhan air baku: 15 NTU → 45 NTU pada menit 01:00.
  - Alarm Kekeruhan Tinggi (3,4 NTU ≥ 3,0 NTU) aktif pada menit 01:10.
  - ACK alarm diterima pada menit 01:25 (respons 25 detik < batas 50% × 60s target = lencana Respons Kilat diraih).
  - Intervensi operator: Dosis koagulan dinaikkan dari 25 mg/L ke 48 mg/L pada 01:45, flash mixer disetel ke 100 RPM pada 02:30.
  - Auto-clear alarm: Tercapai otomatis pada menit 06:20 saat kekeruhan stabil pada 1,2 NTU (<1,5 NTU).
  - Selesai pada 08:30 dengan Skor 88/100, Bintang 2 (85–94), XP +176 (88 × 2,0x pengali Sulit).

---

## 2. Katalog 19 Layar Mock-up SimSCADA-Air

| Kode | Nama Layar & Berkas SVG | Peran Pengguna | Ringkasan Fungsi Utama |
| :--- | :--- | :--- | :--- |
"""
    for code, fname, name, role, desc in SCREENS:
        md += f"| **{code}** | `{fname}`<br>*{name}* | {role} | {desc} |\n"

    md += """
---

## 3. Diagram Alur Kerja Multi-Peran (Swimlane Draw.io)

Alur kerja operasional SimSCADA-Air dipetakan secara detail dalam berkas standar **`public/alur_kerja_simscada.drawio`**, yang memisahkan tanggung jawab berdasarkan 6 swimlane jalur kerja:
1. **Jalur Super Admin:** Provisioning tenant, alokasi paket jalur lisensi (IPA/Distribus/Terpadu), dan monitoring kesehatan platform.
2. **Jalur Admin Lembaga:** Pengaturan KKM & bobot evaluasi, unggah logo resmi, saklar privasi papan peringkat (FR-21), impor pengguna (CSV), dan pembentukan kelompok belajar.
3. **Jalur Pimpinan Lembaga:** Tinjauan metrik keberhasilan institusi (Target KPI T1–T4 PRD §3), utilisasi kursi lisensi (42 peserta aktif / 46 terdaftar / 50 kuota), dan tanda tangan digital piagam kelulusan.
4. **Jalur Instruktur SPAM:** Perancangan skenario gangguan kustom (Authoring Tool FR-23), pemantauan matriks kompetensi kelas (L9), audit rekaman sesi replay (L11), dan validasi pengajuan piagam peserta (L8b).
5. **Jalur Peserta Operator:** Pre-Test diagnostik (L4a), pemilihan jalur materi (L3), penanganan gangguan HMI SCADA 1 Hz (L5), eksplorasi narasi titik kontrol 6 bagian (L5a), evaluasi skor 4 komponen (L6), pengumpulan 8 lencana & papan peringkat (L7), hingga penerbitan piagam kelulusan resmi (L8).
6. **Jalur Publik / Rekruter:** Verifikasi instan keaslian nomor piagam melalui portal publik (L16) dan pemindaian kode QR tanpa login.

---

## 4. Spesifikasi Perhitungan Gamifikasi & Kelulusan (PRD §8)

* **Aturan Bintang:**
  - Skor < 70 = Belum Lulus (Remedial tanpa batas).
  - Skor 70–84 = 1 Bintang (★☆☆).
  - Skor 85–94 = 2 Bintang (★★☆).
  - Skor ≥ 95 = 3 Bintang (★★★, Predikat Sangat Baik).
  - *Misi Kelulusan Ujian (IPA-09 & TRP-02):* Lulus bila skor ≥ 80.
* **Pengali XP Berdasarkan Tingkat Kesulitan Skenario (PRD §7):**
  - Tingkat 1: Pengenalan / Mudah = 1,0x XP.
  - Tingkat 2: Operasi Normal / Sedang = 1,5x XP.
  - Tingkat 3: Gangguan Tunggal / Sulit = 2,0x XP (contoh: IPA-06 Skor 88 × 2,0 = 176 XP).
  - Tingkat 4: Gangguan Berantai / Sangat Sulit = 2,5x XP.
  - Tingkat 5: Misi Kelulusan / Ujian = 3,0x XP.
* **Tangga Jenjang Jabatan Operator:**
  - **Operator Magang:** 0 – 399 XP
  - **Operator Muda:** 400 – 1.199 XP (Contoh: Dimas Wahyu Pratama, 820 XP)
  - **Operator Madya:** 1.200 – 2.499 XP
  - **Operator Utama:** 2.500 – 3.499 XP
  - **Operator Ahli:** ≥ 3.500 XP (Contoh: Andi Kurniawan, 3.820 XP)
* **8 Lencana Resmi PRD §8:**
  1. *Penjelajah Titik Kontrol:* Buka narasi dan pelajari seluruh titik kontrol IPA dan Distribusi.
  2. *Respons Kilat:* Merespons alarm pertama <50% dari batas waktu target skenario (IPA-06: target 60s, respons 25s < 30s).
  3. *Tanpa Alarm Terlewat:* Menyelesaikan sesi tanpa ada alarm yang terlewat atau tidak diakui.
  4. *Penjaga Mutu Air:* Mempertahankan kekeruhan air olahan <1,5 NTU sepanjang sesi evaluasi.
  5. *Penjaga Tekanan:* Menjaga fluktuasi tekanan zona distribusi dalam toleransi ±0,2 bar.
  6. *Tiga Bintang IPA / Distribusi:* Meraih bintang 3 (skor ≥95) pada seluruh misi jalur aktif.
  7. *Hulu ke Hilir:* Lulus seluruh misi jalur Terpadu dari IPA-01 hingga TRP-02.
  8. *Lulus Tanpa Petunjuk:* Lulus Misi Kelulusan Ujian tanpa menggunakan tombol petunjuk (−5 poin).

---
*Dokumen ini merupakan spesifikasi rujukan resmi desain antarmuka dan logika sistem SimSCADA-Air v1.0.*
"""
    return md

def generate_html():
    cards_html = ""
    for code, fname, name, role, desc in SCREENS:
        cards_html += f"""
      <div class="screen-card" id="{code.lower()}">
        <div class="screen-header">
          <div class="badge-code">{code}</div>
          <div class="screen-title-group">
            <h3>{name}</h3>
            <span class="role-tag">{role}</span>
          </div>
          <div class="file-action">
            <a href="{fname}" target="_blank" class="btn-download">Buka Berkas SVG ↗</a>
          </div>
        </div>
        <p class="screen-desc">{desc}</p>
        <div class="preview-box">
          <img src="{fname}" alt="{name}" loading="lazy" />
        </div>
      </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dokumen Cetak Biru & Mock-up Lengkap SimSCADA-Air v1.0</title>
  <style>
    :root {{
      --bg: #0b1120;
      --card-bg: #0f172a;
      --card-border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #0284c7;
      --accent-hover: #0369a1;
      --gold: #f59e0b;
      --green: #10b981;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 32px 24px;
    }}
    .container {{
      max-width: 1400px;
      margin: 0 auto;
    }}
    header {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 36px 32px;
      margin-bottom: 32px;
    }}
    h1 {{
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 8px;
    }}
    .subtitle {{
      color: #38bdf8;
      font-size: 15px;
      font-weight: 600;
      margin-bottom: 16px;
    }}
    .notice-box {{
      background: #0b1120;
      border-left: 4px solid var(--accent);
      padding: 16px 20px;
      border-radius: 6px;
      color: var(--text-muted);
      font-size: 13.5px;
      margin-top: 16px;
    }}
    .notice-box strong {{
      color: #ffffff;
    }}
    .nav-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 24px;
    }}
    .nav-btn {{
      background: #1e293b;
      border: 1px solid var(--card-border);
      color: var(--text);
      text-decoration: none;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
      background: var(--accent);
      border-color: var(--accent);
      color: #ffffff;
    }}
    .section-title {{
      font-size: 20px;
      font-weight: 700;
      margin: 40px 0 20px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .screen-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 32px;
    }}
    .screen-header {{
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }}
    .badge-code {{
      background: var(--accent);
      color: #ffffff;
      font-size: 14px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 6px;
    }}
    .screen-title-group h3 {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
    }}
    .role-tag {{
      display: inline-block;
      background: #1e293b;
      border: 1px solid #475569;
      color: #94a3b8;
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      margin-top: 4px;
    }}
    .file-action {{
      margin-left: auto;
    }}
    .btn-download {{
      background: #1e293b;
      border: 1px solid #38bdf8;
      color: #38bdf8;
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      transition: all 0.2s ease;
    }}
    .btn-download:hover {{
      background: #0284c7;
      color: #ffffff;
    }}
    .screen-desc {{
      color: var(--text-muted);
      font-size: 13.5px;
      margin-bottom: 18px;
      line-height: 1.6;
    }}
    .preview-box {{
      width: 100%;
      background: #080e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 12px;
    }}
    .preview-box img {{
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      background: var(--card-bg);
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--card-border);
    }}
    th, td {{
      padding: 12px 16px;
      text-align: left;
      font-size: 13px;
    }}
    th {{
      background: #1e293b;
      color: #38bdf8;
      font-weight: 700;
      border-bottom: 1px solid var(--card-border);
    }}
    td {{
      border-bottom: 1px solid #1e293b;
      color: var(--text-muted);
    }}
    td strong {{
      color: #ffffff;
    }}
    tr:last-child td {{
      border-bottom: none;
    }}
    footer {{
      margin-top: 60px;
      text-align: center;
      color: #64748b;
      font-size: 12px;
      padding-top: 24px;
      border-top: 1px solid var(--card-border);
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>📘 Dokumen Cetak Biru &amp; Mock-up Lengkap SimSCADA-Air v1.0</h1>
      <div class="subtitle">Platform Pembelajaran Mandiri SCADA SPAM Berbasis Simulasi Hidrolika &amp; Kimia Air</div>
      <div class="notice-box">
        <strong>Pemberitahuan Dokumen:</strong> Dokumen ini menyajikan arsitektur desain konseptual, diagram swimlane Draw.io multi-peran, dan seluruh 19 berkas mock-up grafis SVG berskala penuh (1920 × 1080 px) yang telah diverifikasi dan diselaraskan secara matematis sesuai dengan ketentuan <em>Product Requirements Document</em> (PRD SimSCADA-Air v1.0).
      </div>
      <div class="nav-links">
        <a href="#ringkasan" class="nav-btn">Ringkasan Sistem</a>
        <a href="#katalog" class="nav-btn">Katalog 19 Mock-up</a>
        <a href="#drawio" class="nav-btn">Diagram Alur Draw.io</a>
        <a href="#gamifikasi" class="nav-btn">Aturan Skor &amp; Gamifikasi</a>
        <a href="alur_kerja_simscada.drawio" target="_blank" class="nav-btn" style="border-color:#f59e0b; color:#fbbf24;">Unduh alur_kerja_simscada.drawio ↗</a>
      </div>
    </header>

    <section id="ringkasan">
      <div class="section-title">
        <span>1. Ringkasan Eksekutif &amp; Keselarasan Data Contoh</span>
      </div>
      <p style="color:var(--text-muted); font-size:14px; margin-bottom:16px;">
        Seluruh antarmuka mock-up dan diagram alur menggunakan satu ekosistem data contoh yang saling terhubung secara konsisten di seluruh layar:
      </p>
      <table>
        <thead>
          <tr>
            <th>Entitas Data</th>
            <th>Nilai Contoh Resmi PRD SimSCADA-Air</th>
            <th>Layar Terkait</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lembaga Pelatihan</strong></td>
            <td>Balai Diklat Air Minum Nusantara (kode: <code>NUS</code>) &amp; Pusat Pelatihan Tirta Mandiri (kode: <code>TRM</code>). Lisensi: 50 kursi per lembaga.</td>
            <td>L1, L7, L8, L9, L12, L13, L14, L15, L16</td>
          </tr>
          <tr>
            <td><strong>Akun Demo PRD §5</strong></td>
            <td>10 Akun Demo: <code>superadmin</code>, <code>admin.nusantara</code>, <code>pimpinan.nusantara</code>, <code>instruktur.nusantara</code>, <code>peserta.baru</code>, <code>peserta.ipa</code>, <code>peserta.distribusi</code>, <code>peserta.lulus</code>, <code>admin.tirta</code>, <code>peserta.tirta</code> (Sandi: <code>Demo#2026</code>).</td>
            <td>L1, L7, L9, L12, L15</td>
          </tr>
          <tr>
            <td><strong>Peserta Aktif &amp; Lisensi</strong></td>
            <td>42 Peserta aktif (login 14 hari terakhir) dari 46 akun terdaftar dalam 2 kelompok (Angkatan 1 &amp; 2). Kuota: 50 kursi lisensi (92% terpakai).</td>
            <td>L9, L12, L14, L15</td>
          </tr>
          <tr>
            <td><strong>Sesi Contoh Konsisten</strong></td>
            <td>Misi IPA-06 "Gangguan: Lonjakan Kekeruhan Air Baku" oleh Dimas Wahyu Pratama: 01:00 gangguan 45 NTU, 01:10 alarm 3,4 NTU, 01:25 ACK (25 dtk &lt; 50% × 60s target), 01:45 dosis 48 mg/L, 02:30 mixer 100 RPM, 06:20 auto-clear (1,2 NTU), 08:30 selesai. Skor 88/100, 2★, +176 XP.</td>
            <td>L4, L5, L6, L11</td>
          </tr>
          <tr>
            <td><strong>Piagam Terbit</strong></td>
            <td>Nomor Register: <code>SSA/NUS/2026/0001</code> atas nama Andi Kurniawan (peserta.lulus, Jalur Terpadu 17 Misi, Skor 96, 3★, 3.820 XP, Operator Ahli). Diterbitkan 15 Maret 2026.</td>
            <td>L4a, L7, L8, L9, L12, L16</td>
          </tr>
          <tr>
            <td><strong>Piagam Pending Approval</strong></td>
            <td>Nomor Register Dicadangkan: <code>SSA/NUS/2026/0002</code> atas nama Rian Hidayat (peserta contoh - Angkatan 1, Jalur IPA 9 Misi, Skor Post-Test 82, Menunggu ACC).</td>
            <td>L8b, L9</td>
          </tr>
        </tbody>
      </table>
    </section>

    <section id="katalog">
      <div class="section-title">
        <span>2. Galeri Mock-up 19 Layar (L1 s/d L16, L4a, L5a, L8b)</span>
      </div>
      {cards_html}
    </section>

    <section id="drawio">
      <div class="section-title">
        <span>3. Diagram Alur Kerja Berbasis Peran (Swimlane Draw.io)</span>
      </div>
      <p style="color:var(--text-muted); font-size:14px; margin-bottom:16px;">
        Berkas diagram alur kerja <strong><code>alur_kerja_simscada.drawio</code></strong> tersimpan di direktori publik dan dapat diimpor langsung ke aplikasi diagrams.net / draw.io. Alur kerja dipisahkan menjadi 6 swimlane jalur kerja yang jelas:
      </p>
      <div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:20px; margin-bottom:24px;">
        <ul style="color:var(--text-muted); font-size:13.5px; line-height:1.8; margin-left:20px;">
          <li><strong style="color:#ffffff;">Super Administrator:</strong> Onboarding lembaga pelatihan baru, konfigurasi kuota lisensi (50 kursi), penentuan paket jalur aktif (IPA / Distribusi / Terpadu).</li>
          <li><strong style="color:#ffffff;">Admin Lembaga:</strong> Penyiapan ambang kelulusan KKM &amp; bobot komponen evaluasi, unggah logo resmi, saklar papan peringkat peserta (FR-21), pembuatan akun &amp; impor CSV, pembentukan kelompok belajar.</li>
          <li><strong style="color:#ffffff;">Pimpinan Lembaga:</strong> Pemantauan dasbor evaluasi eksekutif (Target KPI T1–T4 PRD §3), utilisasi kursi lisensi (42 peserta aktif login 14 hari), pengesahan tanda tangan piagam kelulusan.</li>
          <li><strong style="color:#ffffff;">Instruktur Pengajar:</strong> Penugasan skenario gangguan kustom (Authoring Tool FR-23), pemantauan matriks kelas dan deteksi peserta tertinggal (L9), audit rekaman sesi replay (L11), validasi &amp; persetujuan draf piagam (L8b).</li>
          <li><strong style="color:#ffffff;">Peserta Operator:</strong> Pre-Test mandiri (L4a), pemilihan jalur materi (L3), intervensi HMI SCADA 1 Hz (L5), eksplorasi narasi titik kontrol 6 bagian (L5a), evaluasi skor 4 komponen (L6), pengumpulan 8 lencana &amp; papan peringkat (L7), hingga perolehan piagam kelulusan (L8).</li>
          <li><strong style="color:#ffffff;">Publik / Rekruter:</strong> Otentikasi keabsahan nomor piagam melalui portal publik (L16) dan verifikasi QR instan tanpa login.</li>
        </ul>
      </div>
    </section>

    <section id="gamifikasi">
      <div class="section-title">
        <span>4. Logika Penilaian, Bintang, XP, dan Level Operator (PRD §8)</span>
      </div>
      <table>
        <thead>
          <tr>
            <th>Komponen</th>
            <th>Kriteria &amp; Nilai PRD SimSCADA-Air</th>
            <th>Penerapan pada Mock-up</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sistem Bintang</strong></td>
            <td>Skor &lt;70: Belum Lulus · 70–84: 1★ · 85–94: 2★ · ≥95: 3★ (Sangat Baik). Misi Kelulusan Ujian lulus bila skor ≥80.</td>
            <td>L2, L6, L7, L8, L9, L13</td>
          </tr>
          <tr>
            <td><strong>Pengali XP</strong></td>
            <td>Tingkat 1 Mudah: 1,0x · Tingkat 2 Sedang: 1,5x · Tingkat 3 Sulit: 2,0x · Tingkat 4 S.Sulit: 2,5x · Tingkat 5 Ujian: 3,0x.</td>
            <td>L2, L6, L7, L10, L11</td>
          </tr>
          <tr>
            <td><strong>Jenjang Jabatan</strong></td>
            <td>Magang: 0 XP · Muda: 400 XP · Madya: 1.200 XP · Utama: 2.500 XP · Ahli: 3.500 XP.</td>
            <td>L2, L7, L8, L9, L12, L14</td>
          </tr>
          <tr>
            <td><strong>8 Lencana Resmi</strong></td>
            <td>Penjelajah Titik Kontrol, Respons Kilat, Tanpa Alarm Terlewat, Penjaga Mutu Air, Penjaga Tekanan, Tiga Bintang IPA/Distribusi, Hulu ke Hilir, Lulus Tanpa Petunjuk.</td>
            <td>L6, L7, L11</td>
          </tr>
        </tbody>
      </table>
    </section>

    <footer>
      Dokumen Cetak Biru &amp; Mock-up SimSCADA-Air v1.0 · Berkas rujukan resmi desain arsitektur konseptual sebelum implementasi teknis.
    </footer>
  </div>
</body>
</html>"""
    return html

def main():
    md_content = generate_markdown()
    html_content = generate_html()

    # Write root Markdown
    with open("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.md written.")

    # Write root HTML
    with open("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html written.")

    # Write public/ HTML
    pub_html_path = os.path.join("public", "DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html")
    with open(pub_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("public/DOKUMEN_MOCKUP_DAN_ALUR_SimSCADA-Air.html written.")

if __name__ == "__main__":
    main()

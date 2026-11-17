#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 4: L7, L8, L8b, L9
"""
import os
import sys

OUTPUT_DIR = "public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

def generate_l7():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    # Title block with generous vertical spacing to prevent header collision
    title = page_title_block("Galeri Lencana &amp; Papan Peringkat Kompetensi", "8 Lencana Resmi PRD SimSCADA-Air §8 · Papan Peringkat Terisolasi Antar-Lembaga", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: 8 Official Badges PRD §8 (Width: 960) -->
  <g transform="translate(32, 190)">
    <rect width="960" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 24)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">8 Lencana Prestasi Operator (PRD SimSCADA-Air v1.0 §8)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Koleksi pencapaian kompetensi operasional · 3 Lencana Terbuka, 5 Terkunci</text>

      <line x1="0" y1="55" x2="896" y2="55" stroke="#334155" stroke-width="1" />

      <!-- 8 Badges Grid: 2 columns x 4 rows (Width 435 each, Height 145 each) -->
      
      <!-- ROW 1 -->
      <!-- 1. Penjelajah Titik Kontrol (UNLOCKED) -->
      <g transform="translate(0, 70)">
        <rect width="435" height="135" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="32" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="64" fill="#ffffff" font-size="24" text-anchor="middle">🔍</text>
        
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>

        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Penjelajah Titik Kontrol</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="11">Membuka narasi semua titik kontrol</text>
        <text x="96" y="88" fill="#cbd5e1" font-size="11">di satu jalur pembelajaran.</text>
        <text x="96" y="112" fill="#34d399" font-size="10.5" font-weight="600">Capaian: 7/7 Titik Kontrol IPA Dibuka</text>
      </g>

      <!-- 2. Respons Kilat (UNLOCKED - Earned in IPA-06) -->
      <g transform="translate(460, 70)">
        <rect width="435" height="135" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="32" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="64" fill="#ffffff" font-size="24" text-anchor="middle">⚡</text>
        
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>

        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Respons Kilat</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="11">Tindakan benar pertama &lt; 50% waktu target</text>
        <text x="96" y="88" fill="#cbd5e1" font-size="11">pada misi skenario gangguan.</text>
        <text x="96" y="112" fill="#34d399" font-size="10.5" font-weight="600">Diraih di: IPA-06 (Respons 25s &lt; 45s target)</text>
      </g>

      <!-- ROW 2 -->
      <!-- 3. Tanpa Alarm Terlewat (UNLOCKED) -->
      <g transform="translate(0, 220)">
        <rect width="435" height="135" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="32" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="64" fill="#ffffff" font-size="24" text-anchor="middle">🔔</text>
        
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>

        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Tanpa Alarm Terlewat</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="11">Menyelesaikan misi gangguan dengan</text>
        <text x="96" y="88" fill="#cbd5e1" font-size="11">semua alarm diakui dan clear.</text>
        <text x="96" y="112" fill="#34d399" font-size="10.5" font-weight="600">Capaian: 100% Alarm Diakui &amp; Clear di IPA-06</text>
      </g>

      <!-- 4. Penjaga Mutu Air (LOCKED) -->
      <g transform="translate(460, 220)">
        <rect width="435" height="135" rx="10" fill="#090d16" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="32" fill="#1e293b" />
        <text x="50" y="64" fill="#64748b" font-size="24" text-anchor="middle">🔒</text>
        
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#1e293b" />
        <text x="367" y="29" fill="#64748b" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>

        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Penjaga Mutu Air</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="11">Kekeruhan dan sisa klor selalu di rentang</text>
        <text x="96" y="88" fill="#64748b" font-size="11">normal sepanjang seluruh misi jalur IPA.</text>
        <text x="96" y="112" fill="#f59e0b" font-size="10.5">Sisa: Selesaikan IPA-08 &amp; IPA-09</text>
      </g>

      <!-- ROW 3 -->
      <!-- 5. Penjaga Tekanan (LOCKED) -->
      <g transform="translate(0, 370)">
        <rect width="435" height="135" rx="10" fill="#090d16" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="32" fill="#1e293b" />
        <text x="50" y="64" fill="#64748b" font-size="24" text-anchor="middle">🔒</text>

        <rect x="320" y="14" width="95" height="22" rx="4" fill="#1e293b" />
        <text x="367" y="29" fill="#64748b" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>

        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Penjaga Tekanan</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="11">Tekanan semua zona di rentang layanan</text>
        <text x="96" y="88" fill="#64748b" font-size="11">sepanjang misi jaringan distribusi.</text>
        <text x="96" y="112" fill="#64748b" font-size="10.5">Khusus Jalur Distribusi / Terpadu</text>
      </g>

      <!-- 6. Tiga Bintang IPA / Distribusi (LOCKED) -->
      <g transform="translate(460, 370)">
        <rect width="435" height="135" rx="10" fill="#090d16" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="32" fill="#1e293b" />
        <text x="50" y="64" fill="#64748b" font-size="24" text-anchor="middle">🔒</text>

        <rect x="320" y="14" width="95" height="22" rx="4" fill="#1e293b" />
        <text x="367" y="29" fill="#64748b" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>

        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Tiga Bintang IPA / Distribusi</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="11">Semua misi di jalur tersebut diselesaikan</text>
        <text x="96" y="88" fill="#64748b" font-size="11">dengan nilai sempurna 3 Bintang (≥95).</text>
        <text x="96" y="112" fill="#f59e0b" font-size="10.5">Progres Saat Ini: 1/9 Misi 3 Bintang</text>
      </g>

      <!-- ROW 4 -->
      <!-- 7. Hulu ke Hilir (LOCKED) -->
      <g transform="translate(0, 520)">
        <rect width="435" height="135" rx="10" fill="#090d16" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="32" fill="#1e293b" />
        <text x="50" y="64" fill="#64748b" font-size="24" text-anchor="middle">🔒</text>

        <rect x="320" y="14" width="95" height="22" rx="4" fill="#1e293b" />
        <text x="367" y="29" fill="#64748b" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>

        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Hulu ke Hilir</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="11">Lulus misi berantai TRP-01 pada</text>
        <text x="96" y="88" fill="#64748b" font-size="11">Jalur Air Minum Terpadu.</text>
        <text x="96" y="112" fill="#818cf8" font-size="10.5">Tingkat 4 Sangat Sulit (Khusus Terpadu)</text>
      </g>

      <!-- 8. Lulus Tanpa Petunjuk (LOCKED) -->
      <g transform="translate(460, 520)">
        <rect width="435" height="135" rx="10" fill="#090d16" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="32" fill="#1e293b" />
        <text x="50" y="64" fill="#64748b" font-size="24" text-anchor="middle">🔒</text>

        <rect x="320" y="14" width="95" height="22" rx="4" fill="#1e293b" />
        <text x="367" y="29" fill="#64748b" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>

        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Lulus Tanpa Petunjuk</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="11">Menyelesaikan seluruh jalur pelatihan tanpa</text>
        <text x="96" y="88" fill="#64748b" font-size="11">menggunakan tombol bantuan sama sekali.</text>
        <text x="96" y="112" fill="#34d399" font-size="10.5">Status: 0 Petunjuk Digunakan (Tepat Sasaran)</text>
      </g>
    </g>
  </g>

  <!-- Right Column: Leaderboard with Dual Tabs PRD §8 (Width: 540) -->
  <g transform="translate(1028, 190)">
    <rect width="540" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 24)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Papan Peringkat Kompetensi (PRD §8)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Terisolasi dalam Balai Diklat Air Minum Nusantara</text>

      <!-- TAB ROW 1: Kelompok vs Lembaga -->
      <g transform="translate(0, 56)">
        <rect width="235" height="34" rx="6" fill="#0284c7" />
        <text x="117" y="22" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">TAB: KELOMPOK (ANGKATAN 1)</text>

        <rect x="245" width="235" height="34" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="362" y="22" fill="#94a3b8" font-size="11.5" font-weight="600" text-anchor="middle">LEMBAGA (SELURUH NUSANTARA)</text>
      </g>

      <!-- TAB ROW 2: Mingguan vs Sepanjang Waktu -->
      <g transform="translate(0, 98)">
        <rect width="235" height="30" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="117" y="20" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle">Mingguan</text>

        <rect x="245" width="235" height="30" rx="6" fill="#065f46" stroke="#059669" />
        <text x="362" y="20" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Sepanjang Waktu (All-Time) ✓</text>
      </g>

      <line x1="0" y1="140" x2="484" y2="140" stroke="#334155" stroke-width="1" />

      <!-- Leaderboard Ranking Rows -->
      <!-- Rank 1: Peserta Lulus -->
      <g transform="translate(0, 155)">
        <rect width="484" height="60" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
        <text x="24" y="36" fill="#f59e0b" font-size="18" font-weight="800">1</text>
        <circle cx="64" cy="30" r="18" fill="#1e1b4b" />
        <text x="64" y="36" fill="#c7d2fe" font-size="12" font-weight="700" text-anchor="middle">PL</text>

        <text x="94" y="26" fill="#ffffff" font-size="13" font-weight="700">peserta.lulus</text>
        <text x="94" y="44" fill="#a7f3d0" font-size="11">Operator Ahli · Piagam Terbit</text>

        <text x="460" y="28" fill="#f59e0b" font-size="15" font-weight="800" text-anchor="end">3.820 XP</text>
        <text x="460" y="44" fill="#94a3b8" font-size="10.5" text-anchor="end">17 Misi Lulus (48★)</text>
      </g>

      <!-- Rank 2: Dimas (Current User Highlighted) -->
      <g transform="translate(0, 225)">
        <rect width="484" height="64" rx="8" fill="#0c2538" stroke="#38bdf8" stroke-width="2" />
        <text x="24" y="38" fill="#38bdf8" font-size="18" font-weight="800">2</text>
        <circle cx="64" cy="32" r="18" fill="#0369a1" />
        <text x="64" y="38" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">DW</text>

        <text x="94" y="27" fill="#ffffff" font-size="13" font-weight="700">Dimas Wahyu Pratama (Anda)</text>
        <text x="94" y="46" fill="#38bdf8" font-size="11" font-weight="600">Operator Muda · Jalur IPA</text>

        <text x="460" y="29" fill="#38bdf8" font-size="15" font-weight="800" text-anchor="end">820 XP</text>
        <text x="460" y="46" fill="#f59e0b" font-size="10.5" text-anchor="end">7 Misi Lulus (14★)</text>
      </g>

      <!-- Rank 3: Peserta Distribusi -->
      <g transform="translate(0, 300)">
        <rect width="484" height="60" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="24" y="36" fill="#cbd5e1" font-size="18" font-weight="800">3</text>
        <circle cx="64" cy="30" r="18" fill="#1e293b" />
        <text x="64" y="36" fill="#94a3b8" font-size="12" font-weight="700" text-anchor="middle">PD</text>

        <text x="94" y="26" fill="#ffffff" font-size="13" font-weight="700">peserta.distribusi</text>
        <text x="94" y="44" fill="#94a3b8" font-size="11">Operator Muda · Jalur Distribusi</text>

        <text x="460" y="28" fill="#cbd5e1" font-size="15" font-weight="700" text-anchor="end">680 XP</text>
        <text x="460" y="44" fill="#94a3b8" font-size="10.5" text-anchor="end">5 Misi Lulus (11★)</text>
      </g>

      <!-- Rank 4: Peserta Baru -->
      <g transform="translate(0, 370)">
        <rect width="484" height="60" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="24" y="36" fill="#64748b" font-size="18" font-weight="800">4</text>
        <circle cx="64" cy="30" r="18" fill="#1e293b" />
        <text x="64" y="36" fill="#64748b" font-size="12" font-weight="700" text-anchor="middle">PB</text>

        <text x="94" y="26" fill="#94a3b8" font-size="13" font-weight="600">peserta.baru</text>
        <text x="94" y="44" fill="#64748b" font-size="11">Operator Magang · Pre-Test</text>

        <text x="460" y="28" fill="#94a3b8" font-size="15" font-weight="700" text-anchor="end">80 XP</text>
        <text x="460" y="44" fill="#64748b" font-size="10.5" text-anchor="end">1 Misi Lulus (2★)</text>
      </g>

      <!-- Privacy & Tenant Isolation Note PRD §8 -->
      <g transform="translate(0, 460)">
        <rect width="484" height="110" rx="8" fill="#0c4a6e" opacity="0.3" stroke="#0284c7" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">🔒 KEAMANAN &amp; ISOLASI DATA (PRD §8):</text>
        <text x="16" y="44" fill="#cbd5e1" font-size="11">Peserta hanya dapat melihat peringkat dalam lembaganya</text>
        <text x="16" y="62" fill="#cbd5e1" font-size="11">sendiri (Balai Nusantara). Admin Lembaga dapat</text>
        <text x="16" y="80" fill="#cbd5e1" font-size="11">mengaktifkan/menonaktifkan papan peringkat ini kapan saja.</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L7: GALERI LENCANA & PAPAN PERINGKAT (SimSCADA-Air v1.0)")

def generate_l8():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Madya · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Piagam Kelulusan Resmi Terbit", "Format Baku Cetak A4 Landscape · Sesuai Ketentuan Ketat PRD SimSCADA-Air §13", 120)

    content = f"""{hdr}
{title}

  <!-- Left: Official Certificate A4 Landscape Clean Design (PRD §13, Width: 1040, Height: 750) -->
  <g transform="translate(32, 190)" filter="url(#dropShadow)">
    <!-- Certificate Paper Outer Glow & Border -->
    <rect width="1040" height="750" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    
    <!-- Elegant Guilloche / Double Border Inside -->
    <rect x="20" y="20" width="1000" height="710" rx="8" fill="#f8fafc" stroke="#0f172a" stroke-width="2" />
    <rect x="28" y="28" width="984" height="694" fill="none" stroke="#d97706" stroke-width="1.5" stroke-dasharray="8,4" />

    <!-- Certificate Content Block -->
    <g transform="translate(60, 60)">
      
      <!-- Top Header: Logo + Lembaga (PRD §13) -->
      <g transform="translate(0, 0)">
        <rect width="52" height="52" rx="12" fill="#0284c7" />
        <path d="M 26 12 C 26 12, 16 26, 16 34 A 10 10 0 0 0 36 34 C 36 26, 26 12, 26 12 Z" fill="#ffffff" />
        
        <text x="70" y="26" fill="#0f172a" font-size="22" font-weight="800" letter-spacing="0.5">BALAI DIKLAT AIR MINUM NUSANTARA</text>
        <text x="70" y="46" fill="#64748b" font-size="12" font-weight="600" letter-spacing="1">LEMBAGA PELATIHAN OPERATOR SISTEM PENYEDIAAN AIR MINUM</text>

        <!-- Unique Certificate Number PRD §13 (SSA/<kode>/<tahun>/<nomor>) -->
        <rect x="680" y="10" width="240" height="32" rx="6" fill="#0f172a" />
        <text x="800" y="31" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="0.5">SSA/NUS/2026/0001</text>
      </g>

      <line x1="0" y1="75" x2="920" y2="75" stroke="#0f172a" stroke-width="2" />

      <!-- Official Title (PRD §13: WAJIB "PIAGAM KELULUSAN", BUKAN SERTIFIKAT) -->
      <text x="460" y="125" fill="#0f172a" font-size="30" font-weight="800" text-anchor="middle" letter-spacing="2">PIAGAM KELULUSAN</text>
      <text x="460" y="150" fill="#0284c7" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="1.5">JALUR OPERATOR AIR MINUM TERPADU</text>

      <!-- Recipient Declaration -->
      <text x="460" y="195" fill="#475569" font-size="14" font-weight="500" text-anchor="middle">Diberikan dengan bangga kepada:</text>
      <text x="460" y="240" fill="#0f172a" font-size="28" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIMAS WAHYU PRATAMA</text>
      <text x="460" y="265" fill="#64748b" font-size="13" text-anchor="middle">Angkatan 1 · Balai Diklat Air Minum Nusantara</text>

      <!-- Statement of Achievement -->
      <g transform="translate(110, 285)">
        <text x="350" y="22" fill="#334155" font-size="13.5" text-anchor="middle" line-height="1.5">Telah menyelesaikan seluruh rangkaian pelatihan berbasis simulator SCADA</text>
        <text x="350" y="44" fill="#334155" font-size="13.5" text-anchor="middle">mulai dari Instalasi Pengolahan Air (IPA) hingga Jaringan Distribusi,</text>
        <text x="350" y="66" fill="#334155" font-size="13.5" text-anchor="middle">memenuhi seluruh kriteria kompetensi penanganan gangguan dan dinyatakan:</text>
      </g>

      <!-- Predicate Banner (PRD §13: Lulus / Lulus dengan Baik / Lulus dengan Pujian) -->
      <g transform="translate(310, 385)">
        <rect width="300" height="42" rx="8" fill="#d97706" />
        <text x="150" y="27" fill="#ffffff" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="1">PREDIKAT: LULUS DENGAN BAIK</text>
      </g>

      <!-- Summary Badges inside Piagam (Level, Stars, Date) -->
      <g transform="translate(160, 445)">
        <text x="80" y="16" fill="#64748b" font-size="11" text-anchor="middle">TANGGAL LULUS:</text>
        <text x="80" y="34" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">28 Oktober 2026</text>

        <text x="300" y="16" fill="#64748b" font-size="11" text-anchor="middle">LEVEL KOMPETENSI:</text>
        <text x="300" y="34" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Operator Madya</text>

        <text x="520" y="16" fill="#64748b" font-size="11" text-anchor="middle">CAPAIAN BINTANG:</text>
        <text x="520" y="34" fill="#d97706" font-size="13" font-weight="700" text-anchor="middle">42 Bintang (17 Misi)</text>
      </g>

      <!-- Signatures PRD §13: Pimpinan Lembaga & Instruktur Penilai -->
      <g transform="translate(50, 500)">
        <!-- Left Sign: Instruktur Penilai -->
        <g transform="translate(40, 0)">
          <text x="110" y="16" fill="#64748b" font-size="12" text-anchor="middle">Instruktur Penilai,</text>
          <!-- Signature Graphic -->
          <path d="M 60 48 Q 90 28, 120 52 T 160 38" fill="none" stroke="#0284c7" stroke-width="2.5" />
          <line x1="20" y1="65" x2="200" y2="65" stroke="#94a3b8" />
          <text x="110" y="82" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Budi Santoso, S.T.</text>
          <text x="110" y="98" fill="#64748b" font-size="11" text-anchor="middle">Instruktur Utama SPAM</text>
        </g>

        <!-- Center: QR Code & Verification Link -->
        <g transform="translate(390, 0)">
          <rect width="80" height="80" fill="#0f172a" rx="6" />
          <!-- Mock QR matrix pattern -->
          <rect x="8" y="8" width="24" height="24" fill="#ffffff" />
          <rect x="14" y="14" width="12" height="12" fill="#0f172a" />
          <rect x="48" y="8" width="24" height="24" fill="#ffffff" />
          <rect x="54" y="14" width="12" height="12" fill="#0f172a" />
          <rect x="8" y="48" width="24" height="24" fill="#ffffff" />
          <rect x="14" y="54" width="12" height="12" fill="#0f172a" />
          <text x="40" y="96" fill="#64748b" font-size="8.5" text-anchor="middle">Scan Validasi L16</text>
        </g>

        <!-- Right Sign: Pimpinan Lembaga -->
        <g transform="translate(600, 0)">
          <text x="110" y="16" fill="#64748b" font-size="12" text-anchor="middle">Pimpinan Lembaga,</text>
          <path d="M 50 45 Q 100 20, 130 50 T 170 42" fill="none" stroke="#d97706" stroke-width="2.5" />
          <line x1="20" y1="65" x2="200" y2="65" stroke="#94a3b8" />
          <text x="110" y="82" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Dr. Ir. Bambang Sutrisno, M.Eng.</text>
          <text x="110" y="98" fill="#64748b" font-size="11" text-anchor="middle">Kepala Balai Diklat</text>
        </g>
      </g>

      <!-- Bottom Mandatory Disclaimer & Simulator Note PRD §13 -->
      <g transform="translate(0, 615)">
        <line x1="0" y1="0" x2="920" y2="0" stroke="#cbd5e1" stroke-width="1" />
        <text x="460" y="18" fill="#64748b" font-size="10.5" font-weight="600" text-anchor="middle">"Piagam ini menyatakan penyelesaian pelatihan berbasis simulator dan bukan sertifikat kompetensi resmi."</text>
        <text x="460" y="32" fill="#94a3b8" font-size="9.5" text-anchor="middle">Simulator: SimSCADA-Air · Kode Verifikasi: SSA/NUS/2026/0001 · Validasi di portal publik tanpa login</text>
      </g>
    </g>
  </g>

  <!-- Right: Verification Checklist & Download Panel (Width: 460) -->
  <g transform="translate(1108, 190)">
    <rect width="460" height="750" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 28)">
      <text x="0" y="18" fill="#ffffff" font-size="16" font-weight="700">Verifikasi Syarat Kelulusan Jalur</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Standar Kelulusan PRD SimSCADA-Air §13</text>

      <line x1="0" y1="52" x2="404" y2="52" stroke="#334155" stroke-width="1" />

      <!-- 4 Requirements Checklist PRD §13 -->
      <g transform="translate(0, 70)">
        <!-- 1. All Missions Passed -->
        <rect width="404" height="60" rx="8" fill="#064e3b" opacity="0.4" stroke="#059669" />
        <circle cx="28" cy="30" r="14" fill="#059669" />
        <text x="28" y="35" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓</text>
        <text x="54" y="24" fill="#a7f3d0" font-size="12" font-weight="700">1. Semua Misi Wajib Lulus</text>
        <text x="54" y="42" fill="#ffffff" font-size="11">17 dari 17 Misi Diselesaikan (100% Lulus)</text>

        <!-- 2. Graduation Mission >= 80 -->
        <rect y="72" width="404" height="60" rx="8" fill="#064e3b" opacity="0.4" stroke="#059669" />
        <circle cx="28" cy="102" r="14" fill="#059669" />
        <text x="28" y="107" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓</text>
        <text x="54" y="96" fill="#a7f3d0" font-size="12" font-weight="700">2. Misi Kelulusan Skor ≥ 80</text>
        <text x="54" y="114" fill="#ffffff" font-size="11">Skor TRP-02: 86 / 100 (Ambang KKM ≥80 Tercapai)</text>

        <!-- 3. Post-Test >= 70 -->
        <rect y="144" width="404" height="60" rx="8" fill="#064e3b" opacity="0.4" stroke="#059669" />
        <circle cx="28" cy="174" r="14" fill="#059669" />
        <text x="28" y="179" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓</text>
        <text x="54" y="168" fill="#a7f3d0" font-size="12" font-weight="700">3. Post-Test Akhir ≥ 70</text>
        <text x="54" y="186" fill="#ffffff" font-size="11">Skor Post-Test: 84 / 100 (Kenaikan T1: +50%)</text>

        <!-- 4. Instructor Approval -->
        <rect y="216" width="404" height="60" rx="8" fill="#064e3b" opacity="0.4" stroke="#059669" />
        <circle cx="28" cy="246" r="14" fill="#059669" />
        <text x="28" y="251" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓</text>
        <text x="54" y="240" fill="#a7f3d0" font-size="12" font-weight="700">4. Persetujuan Instruktur</text>
        <text x="54" y="258" fill="#ffffff" font-size="11">Disetujui &amp; Ditandatangani oleh Pak Budi</text>
      </g>

      <!-- Action: Download PDF -->
      <g transform="translate(0, 380)">
        <rect width="404" height="54" rx="10" fill="url(#primaryGrad)" />
        <text x="202" y="34" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">UNDUH PIAGAM (PDF RESMI) 📥</text>

        <rect y="66" width="404" height="46" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="202" y="95" fill="#cbd5e1" font-size="12.5" font-weight="600" text-anchor="middle">VERIFIKASI DI PORTAL PUBLIK (L16) ↗</text>

        <rect y="124" width="404" height="46" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="202" y="153" fill="#cbd5e1" font-size="12.5" font-weight="600" text-anchor="middle">BAGIKAN KE LINKEDIN / REKRUTER 🔗</text>
      </g>

      <!-- Anti-Slop Discipline Note PRD §13 -->
      <g transform="translate(0, 580)">
        <rect width="404" height="110" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">CATATAN KETENTUAN HUKUM (PRD §13):</text>
        <text x="16" y="44" fill="#94a3b8" font-size="11">Piagam tidak memuat NIP aparatur atau rincian nilai</text>
        <text x="16" y="62" fill="#94a3b8" font-size="11">angka untuk menjaga privasi peserta. Piagam dapat</text>
        <text x="16" y="80" fill="#94a3b8" font-size="11">dicabut oleh Admin Lembaga jika ditemukan pelanggaran.</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L8: PIAGAM KELULUSAN RESMI TERBIT (SimSCADA-Air v1.0)")

def generate_l8b():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Madya · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Status Piagam: Menunggu Persetujuan Instruktur", "Alur Verifikasi Dua Tahap PRD SimSCADA-Air §13 · Tombol Unduh Nonaktif Sampai Disetujui", 120)

    content = f"""{hdr}
{title}

  <!-- Pending Notice Banner PRD §13 -->
  <g transform="translate(32, 195)">
    <rect width="1536" height="74" rx="10" fill="#451a03" stroke="#d97706" stroke-width="2" filter="url(#glowAmber)" />
    <!-- Hourglass Icon -->
    <circle cx="48" cy="37" r="22" fill="#78350f" />
    <text x="48" y="44" fill="#fde68a" font-size="20" text-anchor="middle">⏳</text>
    
    <text x="86" y="32" fill="#fef3c7" font-size="14" font-weight="700">STATUS PIAGAM: MENUNGGU PERSETUJUAN &amp; VALIDASI INSTRUKTUR KELAS (PAK BUDI)</text>
    <text x="86" y="52" fill="#fde68a" font-size="12">Seluruh misi, Misi Kelulusan, dan Post-Test telah lulus. Pengajuan penerbitan piagam telah terkirim ke dasbor instruktur L9.</text>
    
    <rect x="1350" y="18" width="160" height="38" rx="8" fill="#78350f" stroke="#f59e0b" />
    <text x="1430" y="42" fill="#fbbf24" font-size="12.5" font-weight="700" text-anchor="middle">PENDING APPROVAL</text>
  </g>

  <!-- Left: Watermarked / Locked Piagam Preview (Width: 1040) -->
  <g transform="translate(32, 290)" opacity="0.75">
    <rect width="1040" height="650" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <rect x="20" y="20" width="1000" height="610" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6,4" />

    <!-- Watermark Diagonal Banner -->
    <g transform="translate(200, 340) rotate(-18)">
      <rect x="-80" y="-35" width="700" height="70" rx="10" fill="#ef4444" opacity="0.18" stroke="#ef4444" stroke-width="2" stroke-dasharray="8,4" />
      <text x="270" y="10" fill="#ef4444" font-size="28" font-weight="900" text-anchor="middle" letter-spacing="3">MENUNGGU VALIDASI INSTRUKTUR</text>
    </g>

    <g transform="translate(60, 50)">
      <text x="70" y="26" fill="#0f172a" font-size="20" font-weight="800">BALAI DIKLAT AIR MINUM NUSANTARA</text>
      <text x="70" y="44" fill="#64748b" font-size="11">SSA/NUS/2026/0001 (Nomor Registrasi Dicadangkan)</text>

      <text x="460" y="120" fill="#0f172a" font-size="26" font-weight="800" text-anchor="middle">PIAGAM KELULUSAN</text>
      <text x="460" y="145" fill="#0284c7" font-size="15" font-weight="700" text-anchor="middle">JALUR OPERATOR AIR MINUM TERPADU</text>

      <text x="460" y="190" fill="#64748b" font-size="13" text-anchor="middle">Diberikan kepada:</text>
      <text x="460" y="225" fill="#0f172a" font-size="24" font-weight="800" text-anchor="middle">DIMAS WAHYU PRATAMA</text>

      <!-- Signature section with Pending Stamp on Instructor side -->
      <g transform="translate(50, 380)">
        <g transform="translate(40, 0)">
          <text x="110" y="16" fill="#64748b" font-size="12" text-anchor="middle">Instruktur Penilai,</text>
          <!-- Pending stamp -->
          <rect x="25" y="28" width="170" height="34" rx="4" fill="#fef3c7" stroke="#d97706" stroke-dasharray="4,2" />
          <text x="110" y="50" fill="#b45309" font-size="11" font-weight="700" text-anchor="middle">⏳ Menunggu Verifikasi</text>
          <line x1="20" y1="75" x2="200" y2="75" stroke="#94a3b8" />
          <text x="110" y="92" fill="#0f172a" font-size="12" font-weight="700" text-anchor="middle">Budi Santoso, S.T.</text>
        </g>

        <g transform="translate(600, 0)">
          <text x="110" y="16" fill="#64748b" font-size="12" text-anchor="middle">Pimpinan Lembaga,</text>
          <path d="M 50 45 Q 100 20, 130 50 T 170 42" fill="none" stroke="#d97706" stroke-width="2" />
          <line x1="20" y1="75" x2="200" y2="75" stroke="#94a3b8" />
          <text x="110" y="92" fill="#0f172a" font-size="12" font-weight="700" text-anchor="middle">Dr. Ir. Bambang Sutrisno, M.Eng.</text>
        </g>
      </g>

      <text x="460" y="540" fill="#64748b" font-size="10" text-anchor="middle">"Piagam ini menyatakan penyelesaian pelatihan berbasis simulator dan bukan sertifikat kompetensi resmi."</text>
    </g>
  </g>

  <!-- Right: Verification Action & Disabled Download Button (Width: 460) -->
  <g transform="translate(1108, 290)">
    <rect width="460" height="650" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 28)">
      <text x="0" y="18" fill="#ffffff" font-size="16" font-weight="700">Proses Validasi Instruktur</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Kebijakan Lembaga: "Persetujuan Instruktur Wajib (L13)"</text>

      <line x1="0" y1="52" x2="404" y2="52" stroke="#334155" stroke-width="1" />

      <!-- Timeline Tracking -->
      <g transform="translate(0, 70)">
        <circle cx="16" cy="16" r="10" fill="#059669" />
        <text x="16" y="20" fill="#fff" font-size="9" text-anchor="middle">✓</text>
        <text x="36" y="15" fill="#a7f3d0" font-size="11.5" font-weight="700">Misi Terpadu Selesai (17 Misi)</text>
        <text x="36" y="30" fill="#64748b" font-size="10.5">28 Okt 2026 · 10:15 WIB</text>

        <line x1="16" y1="30" x2="16" y2="55" stroke="#059669" stroke-width="2" />

        <circle cx="16" cy="65" r="10" fill="#059669" />
        <text x="16" y="69" fill="#fff" font-size="9" text-anchor="middle">✓</text>
        <text x="36" y="64" fill="#a7f3d0" font-size="11.5" font-weight="700">Misi Kelulusan &amp; Post-Test Lulus</text>
        <text x="36" y="79" fill="#64748b" font-size="10.5">28 Okt 2026 · 11:30 WIB (Post-Test: 84)</text>

        <line x1="16" y1="80" x2="16" y2="105" stroke="#d97706" stroke-width="2" />

        <circle cx="16" cy="115" r="10" fill="#d97706" />
        <text x="16" y="119" fill="#fff" font-size="9" text-anchor="middle">⏳</text>
        <text x="36" y="114" fill="#fbbf24" font-size="11.5" font-weight="700">Menunggu Tanda Tangan Pak Budi</text>
        <text x="36" y="129" fill="#fde68a" font-size="10.5">Instruktur sedang meninjau audit replay sesi</text>
      </g>

      <!-- Disabled Download Button PRD §13 -->
      <g transform="translate(0, 240)">
        <rect width="404" height="54" rx="10" fill="#1e293b" stroke="#334155" />
        <text x="202" y="28" fill="#64748b" font-size="14" font-weight="700" text-anchor="middle">UNDUH PIAGAM PDF (TERKUNCI 🔒)</text>
        <text x="202" y="44" fill="#ef4444" font-size="10.5" text-anchor="middle">Tombol aktif setelah instruktur menyetujui kelulusan</text>

        <rect y="70" width="404" height="46" rx="8" fill="#0284c7" />
        <text x="202" y="98" fill="#ffffff" font-size="12.5" font-weight="700" text-anchor="middle">KIRIM PENGINGAT KE INSTRUKTUR 🔔</text>
      </g>

      <g transform="translate(0, 420)">
        <rect width="404" height="150" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">KENAPA MEMBUTUHKAN PERSETUJUAN?</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="11">Admin Balai Diklat Nusantara mewajibkan instruktur</text>
        <text x="16" y="66" fill="#cbd5e1" font-size="11">memverifikasi konsistensi SOP peserta pada Misi</text>
        <text x="16" y="86" fill="#cbd5e1" font-size="11">Kelulusan sebelum piagam berkode QR diterbitkan</text>
        <text x="16" y="106" fill="#cbd5e1" font-size="11">secara permanen ke database publik.</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L8b: STATUS PIAGAM MENUNGGU PERSETUJUAN (SimSCADA-Air v1.0)")

def generate_l9():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · Angkatan 1", name="Budi Santoso, S.T.", initials="BS")
    # Generous title vertical offset to prevent any collision
    title = page_title_block("Dasbor Pengawasan Kelas Instruktur", "Matriks Kemajuan Peserta × Misi · Deteksi Otomatis Peserta Tertinggal (Lagging Alerts) (PRD §12)", 120)

    content = f"""{hdr}
{title}

  <!-- Quick Action & Filter Bar (Width: 1536) -->
  <g transform="translate(32, 195)">
    <rect width="1536" height="52" rx="8" fill="#0f172a" stroke="#334155" />
    
    <text x="20" y="32" fill="#94a3b8" font-size="12">Kelompok Binaan:</text>
    <rect x="135" y="10" width="190" height="32" rx="6" fill="#1e293b" stroke="#0284c7" />
    <text x="150" y="31" fill="#38bdf8" font-size="12" font-weight="700">Angkatan 1 (24 Peserta)</text>

    <text x="350" y="32" fill="#94a3b8" font-size="12">Jalur Belajar:</text>
    <rect x="435" y="10" width="220" height="32" rx="6" fill="#1e293b" stroke="#334155" />
    <text x="450" y="31" fill="#ffffff" font-size="12">Operator IPA (9 Misi) ▾</text>

    <!-- 5 Instructor Action Buttons PRD §12 -->
    <g transform="translate(740, 10)">
      <rect width="150" height="32" rx="6" fill="#0284c7" />
      <text x="75" y="21" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">+ Tugaskan Skenario</text>

      <rect x="160" width="130" height="32" rx="6" fill="#065f46" />
      <text x="225" y="21" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">🔓 Buka Kunci</text>

      <rect x="300" width="140" height="32" rx="6" fill="#1e1b4b" stroke="#6366f1" />
      <text x="370" y="21" fill="#c7d2fe" font-size="11" font-weight="700" text-anchor="middle">✓ Setujui Piagam (1)</text>

      <rect x="450" width="140" height="32" rx="6" fill="#451a03" stroke="#d97706" />
      <text x="520" y="21" fill="#fde68a" font-size="11" font-weight="700" text-anchor="middle">▶ Putar Ulang (L11)</text>

      <rect x="600" width="180" height="32" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="690" y="21" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">📝 Beri Catatan Evaluasi</text>
    </g>
  </g>

  <!-- Lagging Alert Banner PRD §12 (Definition: Failed same mission 3 times) -->
  <g transform="translate(32, 260)">
    <rect width="1536" height="42" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5" />
    <text x="20" y="26" fill="#fca5a5" font-size="12" font-weight="700">⚠️ PERINGATAN PESERTA TERTINGGAL (PRD §12):</text>
    <text x="280" y="26" fill="#ffffff" font-size="12">1 Peserta (<tspan font-weight="700" fill="#fca5a5">peserta.ipa - Rian</tspan>) belum lulus misi <tspan font-weight="700" fill="#fca5a5">IPA-07 (Pompa Trip)</tspan> sebanyak 3 kali berturut-turut. Intervensi buka kunci atau bimbingan disarankan.</text>
  </g>

  <!-- Main Roster & Mission Matrix Table PRD §12 (Width: 1536) -->
  <g transform="translate(32, 315)">
    <rect width="1536" height="630" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <!-- Table Header Columns -->
    <rect width="1536" height="44" rx="12" fill="#0f172a" />
    <text x="24" y="28" fill="#94a3b8" font-size="11" font-weight="700">NAMA PESERTA / AKUN</text>
    <text x="240" y="28" fill="#94a3b8" font-size="11" font-weight="700">MISI AKTIF</text>
    <text x="420" y="28" fill="#94a3b8" font-size="11" font-weight="700">SKOR TERAKHIR</text>
    <text x="560" y="28" fill="#94a3b8" font-size="11" font-weight="700">BINTANG</text>
    <text x="680" y="28" fill="#94a3b8" font-size="11" font-weight="700">AKTIVITAS</text>
    <text x="800" y="28" fill="#94a3b8" font-size="11" font-weight="700">STATUS PESERTA</text>
    <text x="1000" y="28" fill="#38bdf8" font-size="11" font-weight="700">MATRIKS PROGRES MISI JALUR (IPA-01 s/d IPA-09)</text>
    <text x="1410" y="28" fill="#94a3b8" font-size="11" font-weight="700">AKSI</text>

    <line x1="0" y1="44" x2="1536" y2="44" stroke="#1e293b" />

    <!-- ROW 1: Dimas Wahyu Pratama (peserta.ipa / Progres Baik) -->
    <g transform="translate(0, 52)">
      <rect width="1536" height="74" fill="#0c2538" opacity="0.6" stroke="#0284c7" stroke-width="1" />
      <text x="24" y="32" fill="#ffffff" font-size="13" font-weight="700">Dimas Wahyu Pratama</text>
      <text x="24" y="52" fill="#38bdf8" font-size="11">peserta.ipa · Operator Muda</text>

      <text x="240" y="32" fill="#38bdf8" font-size="12" font-weight="700">IPA-06: Lonjakan Baku</text>
      <text x="240" y="52" fill="#94a3b8" font-size="10.5">Sesi Contoh Berhasil</text>

      <text x="420" y="36" fill="#38bdf8" font-size="18" font-weight="800">88 <tspan font-size="11">/ 100</tspan></text>
      <text x="560" y="36" fill="#f59e0b" font-size="16">★★☆</text>
      <text x="680" y="36" fill="#34d399" font-size="11.5">Hari ini (08:30)</text>

      <!-- Status Badge -->
      <rect x="800" y="20" width="130" height="26" rx="6" fill="#065f46" />
      <text x="865" y="37" fill="#a7f3d0" font-size="11" font-weight="700" text-anchor="middle">Lulus IPA-06 ✓</text>

      <!-- Mini Matrix for Dimas (IPA 1-9) -->
      <g transform="translate(1000, 24)">
        <!-- 01: 3★, 02: 2★, 03: 2★, 04: 2★, 05: 2★, 06: 2★, 07: 1★, 08: Lock, 09: Lock -->
        <rect width="32" height="26" rx="4" fill="#059669" /><text x="16" y="17" fill="#fff" font-size="10" text-anchor="middle">01★3</text>
        <rect x="36" width="32" height="26" rx="4" fill="#059669" /><text x="52" y="17" fill="#fff" font-size="10" text-anchor="middle">02★2</text>
        <rect x="72" width="32" height="26" rx="4" fill="#059669" /><text x="88" y="17" fill="#fff" font-size="10" text-anchor="middle">03★2</text>
        <rect x="108" width="32" height="26" rx="4" fill="#059669" /><text x="124" y="17" fill="#fff" font-size="10" text-anchor="middle">04★2</text>
        <rect x="144" width="32" height="26" rx="4" fill="#059669" /><text x="160" y="17" fill="#fff" font-size="10" text-anchor="middle">05★2</text>
        <rect x="180" width="32" height="26" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" /><text x="196" y="17" fill="#fff" font-size="10" text-anchor="middle">06★2</text>
        <rect x="216" width="32" height="26" rx="4" fill="#d97706" /><text x="232" y="17" fill="#fff" font-size="10" text-anchor="middle">07★1</text>
        <rect x="252" width="32" height="26" rx="4" fill="#0c4a6e" /><text x="268" y="17" fill="#38bdf8" font-size="10" text-anchor="middle">08⏳</text>
        <rect x="288" width="32" height="26" rx="4" fill="#1e293b" /><text x="304" y="17" fill="#64748b" font-size="10" text-anchor="middle">09🔒</text>
      </g>

      <!-- Action Button -->
      <rect x="1400" y="20" width="105" height="28" rx="6" fill="#0284c7" />
      <text x="1452" y="38" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Replay (L11)</text>
    </g>

    <!-- ROW 2: Peserta Lulus (Menunggu Tanda Tangan Piagam) -->
    <g transform="translate(0, 134)">
      <rect width="1536" height="74" fill="#1e1b4b" opacity="0.4" stroke="#6366f1" stroke-width="1" />
      <text x="24" y="32" fill="#ffffff" font-size="13" font-weight="700">peserta.lulus</text>
      <text x="24" y="52" fill="#a5b4fc" font-size="11">Andi Kurniawan · Operator Madya</text>

      <text x="240" y="32" fill="#a5b4fc" font-size="12" font-weight="700">TRP-02: Kelulusan</text>
      <text x="240" y="52" fill="#34d399" font-size="10.5">Semua 17 Misi Lulus</text>

      <text x="420" y="36" fill="#34d399" font-size="18" font-weight="800">86 <tspan font-size="11">/ 100</tspan></text>
      <text x="560" y="36" fill="#f59e0b" font-size="16">★★☆</text>
      <text x="680" y="36" fill="#cbd5e1" font-size="11.5">Kemarin</text>

      <!-- Status Badge -->
      <rect x="800" y="20" width="160" height="26" rx="6" fill="#d97706" />
      <text x="880" y="37" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">Menunggu Pengesahan</text>

      <!-- Matrix: All green -->
      <g transform="translate(1000, 24)">
        <rect width="320" height="26" rx="4" fill="#059669" />
        <text x="160" y="17" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">✓ SEMUA 17 MISI LULUS (48 BINTANG)</text>
      </g>

      <rect x="1400" y="20" width="105" height="28" rx="6" fill="#059669" />
      <text x="1452" y="38" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">SETUJUI PIAGAM</text>
    </g>

    <!-- ROW 3: Peserta Tertinggal (Lagging Case PRD §12) -->
    <g transform="translate(0, 216)">
      <rect width="1536" height="74" fill="#450a0a" opacity="0.3" stroke="#ef4444" stroke-width="1" />
      <text x="24" y="32" fill="#ffffff" font-size="13" font-weight="700">Rian Pratama</text>
      <text x="24" y="52" fill="#fca5a5" font-size="11">peserta.ipa · Operator Magang</text>

      <text x="240" y="32" fill="#ef4444" font-size="12" font-weight="700">IPA-07: Pompa Trip</text>
      <text x="240" y="52" fill="#fca5a5" font-size="10.5">Gagal 3x Percobaan berturut</text>

      <text x="420" y="36" fill="#ef4444" font-size="18" font-weight="800">58 <tspan font-size="11">/ 100</tspan></text>
      <text x="560" y="36" fill="#64748b" font-size="16">☆☆☆</text>
      <text x="680" y="36" fill="#cbd5e1" font-size="11.5">3 hari lalu</text>

      <!-- Lagging Badge -->
      <rect x="800" y="20" width="145" height="26" rx="6" fill="#ef4444" />
      <text x="872" y="37" fill="#ffffff" font-size="10.5" font-weight="800" text-anchor="middle">TERTINGGAL (3x GAGAL)</text>

      <!-- Matrix with red at IPA-07 -->
      <g transform="translate(1000, 24)">
        <rect width="32" height="26" rx="4" fill="#059669" /><text x="16" y="17" fill="#fff" font-size="10" text-anchor="middle">01★</text>
        <rect x="36" width="32" height="26" rx="4" fill="#059669" /><text x="52" y="17" fill="#fff" font-size="10" text-anchor="middle">02★</text>
        <rect x="72" width="32" height="26" rx="4" fill="#059669" /><text x="88" y="17" fill="#fff" font-size="10" text-anchor="middle">03★</text>
        <rect x="108" width="32" height="26" rx="4" fill="#059669" /><text x="124" y="17" fill="#fff" font-size="10" text-anchor="middle">04★</text>
        <rect x="144" width="32" height="26" rx="4" fill="#059669" /><text x="160" y="17" fill="#fff" font-size="10" text-anchor="middle">05★</text>
        <rect x="180" width="32" height="26" rx="4" fill="#059669" /><text x="196" y="17" fill="#fff" font-size="10" text-anchor="middle">06★</text>
        <rect x="216" width="32" height="26" rx="4" fill="#ef4444" stroke="#ffffff" stroke-width="1.5" /><text x="232" y="17" fill="#fff" font-size="10" font-weight="800" text-anchor="middle">07✗</text>
        <rect x="252" width="32" height="26" rx="4" fill="#1e293b" /><text x="268" y="17" fill="#64748b" font-size="10" text-anchor="middle">08🔒</text>
        <rect x="288" width="32" height="26" rx="4" fill="#1e293b" /><text x="304" y="17" fill="#64748b" font-size="10" text-anchor="middle">09🔒</text>
      </g>

      <rect x="1400" y="20" width="105" height="28" rx="6" fill="#ef4444" />
      <text x="1452" y="38" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Buka Kunci</text>
    </g>

    <!-- ROW 4: Peserta Distribusi -->
    <g transform="translate(0, 298)">
      <rect width="1536" height="74" fill="#0f172a" />
      <text x="24" y="32" fill="#ffffff" font-size="13" font-weight="700">peserta.distribusi</text>
      <text x="24" y="52" fill="#94a3b8" font-size="11">Siti Aminah · Operator Muda</text>

      <text x="240" y="32" fill="#cbd5e1" font-size="12">DST-05: Kebocoran Pipa</text>
      <text x="240" y="52" fill="#94a3b8" font-size="10.5">Jalur Distribusi</text>

      <text x="420" y="36" fill="#38bdf8" font-size="18" font-weight="800">82 <tspan font-size="11">/ 100</tspan></text>
      <text x="560" y="36" fill="#f59e0b" font-size="16">★☆☆</text>
      <text x="680" y="36" fill="#cbd5e1" font-size="11.5">2 hari lalu</text>

      <rect x="800" y="20" width="130" height="26" rx="6" fill="#065f46" />
      <text x="865" y="37" fill="#a7f3d0" font-size="11" font-weight="700" text-anchor="middle">Aktif Berjalan</text>

      <g transform="translate(1000, 24)">
        <rect width="220" height="26" rx="4" fill="#0f172a" stroke="#1e293b" />
        <text x="110" y="17" fill="#38bdf8" font-size="10.5" text-anchor="middle">DST 01-04 Lulus · Sisa 3 Misi</text>
      </g>

      <rect x="1400" y="20" width="105" height="28" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="1452" y="38" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Detail Roster</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L9: DASBOR PENGAWASAN KELAS INSTRUKTUR (SimSCADA-Air v1.0)")

print("Generating L7, L8, L8b, L9...")
with open(os.path.join(OUTPUT_DIR, "mockup_l7_badges_leaderboard.svg"), "w") as f:
    f.write(generate_l7())
with open(os.path.join(OUTPUT_DIR, "mockup_l8_certificate.svg"), "w") as f:
    f.write(generate_l8())
with open(os.path.join(OUTPUT_DIR, "mockup_l8b_certificate_pending.svg"), "w") as f:
    f.write(generate_l8b())
with open(os.path.join(OUTPUT_DIR, "mockup_l9_instructor_dashboard.svg"), "w") as f:
    f.write(generate_l9())
print("L7, L8, L8b, L9 generated successfully.")

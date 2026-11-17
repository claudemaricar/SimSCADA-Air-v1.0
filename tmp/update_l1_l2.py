#!/usr/bin/env python3
import os, sys, re
import xml.etree.ElementTree as ET

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)

def sanitize_xml(svg_str):
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)

# Import existing generate_l1 from tmp/gen_l1_l2.py
sys.path.append("tmp")
import gen_l1_l2

def generate_l1():
    # Call original gen_l1_l2.generate_l1()
    return gen_l1_l2.generate_l1()

def generate_l2():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Beranda Peserta &amp; Peta Misi Jalur IPA", "Jalur Aktif: Operator IPA (9 Misi) · 7 Misi Lulus · 14 Bintang · 820 XP (PRD §7, §8, §11)", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: Profile Card, Level, Stats, Competency Map & Smart Advisor (Width: 420) -->
  <g transform="translate(32, 190)">
    
    <!-- 1. Profile & Level Card (Height: 330) -->
    <rect width="420" height="330" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <circle cx="32" cy="32" r="28" fill="#0284c7" />
      <text x="32" y="39" fill="#ffffff" font-size="18" font-weight="700" text-anchor="middle">DW</text>
      <text x="76" y="24" fill="#f8fafc" font-size="16" font-weight="700">Dimas Wahyu Pratama</text>
      <text x="76" y="42" fill="#94a3b8" font-size="11.5">Balai Diklat Air Minum Nusantara</text>
      <text x="76" y="58" fill="#38bdf8" font-size="11.5" font-weight="600">Angkatan 1 · ID: <tspan font-family="monospace">peserta.ipa</tspan></text>

      <line x1="0" y1="72" x2="372" y2="72" stroke="#334155" stroke-width="1" />

      <!-- Level & XP Progression PRD §8 -->
      <g transform="translate(0, 84)">
        <text x="0" y="14" fill="#94a3b8" font-size="11" font-weight="600">LEVEL OPERATOR (PRD §8):</text>
        <rect x="0" y="24" width="160" height="28" rx="6" fill="#0284c7" opacity="0.25" stroke="#0284c7" />
        <text x="80" y="43" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Operator Muda</text>

        <text x="180" y="14" fill="#94a3b8" font-size="11" font-weight="600">TOTAL XP: <tspan fill="#f59e0b" font-weight="700">820 XP</tspan></text>
        <rect x="180" y="26" width="192" height="10" rx="5" fill="#0f172a" />
        <rect x="180" y="26" width="102" height="10" rx="5" fill="url(#goldGrad)" />
        <text x="180" y="48" fill="#64748b" font-size="9.5">820 / 1.200 XP (Sisa 380 XP ke Operator Madya)</text>
      </g>

      <!-- 4 Stats Counters: Misi, Bintang, Lencana, Peringkat -->
      <g transform="translate(0, 150)">
        <rect width="86" height="58" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="43" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">Misi Lulus</text>
        <text x="43" y="44" fill="#38bdf8" font-size="17" font-weight="700" text-anchor="middle">7 / 9</text>

        <rect x="96" width="86" height="58" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="139" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">Bintang</text>
        <text x="139" y="44" fill="#f59e0b" font-size="17" font-weight="700" text-anchor="middle">14 ★</text>

        <rect x="192" width="86" height="58" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="235" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">Lencana</text>
        <text x="235" y="44" fill="#10b981" font-size="17" font-weight="700" text-anchor="middle">3 / 8</text>

        <rect x="288" width="84" height="58" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="330" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">Peringkat</text>
        <text x="330" y="44" fill="#c084fc" font-size="17" font-weight="700" text-anchor="middle">#2</text>
      </g>

      <!-- Piagam Status Card PRD §11 -->
      <g transform="translate(0, 222)">
        <rect width="372" height="48" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1" />
        <text x="14" y="20" fill="#c7d2fe" font-size="11" font-weight="700">STATUS PIAGAM KELULUSAN:</text>
        <text x="14" y="36" fill="#a5b4fc" font-size="11.5">Belum Memenuhi (Sisa 2 Misi Jalur IPA: IPA-08 &amp; IPA-09)</text>
        <text x="355" y="30" fill="#818cf8" font-size="15" text-anchor="end">🔒</text>
      </g>
    </g>

    <!-- 2. Peta Capaian Kompetensi & Tren Skor (Height: 250) -->
    <g transform="translate(0, 345)">
      <rect width="420" height="250" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(24, 18)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">PETA CAPAIAN KOMPETENSI (5 DOMAIN PRD):</text>
        
        <!-- Bar 1: Operasi Unit IPA (85%) -->
        <text x="0" y="42" fill="#cbd5e1" font-size="10.5">Operasi Unit IPA</text>
        <text x="372" y="42" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="end">85%</text>
        <rect x="0" y="48" width="372" height="7" rx="3.5" fill="#0f172a" />
        <rect x="0" y="48" width="316" height="7" rx="3.5" fill="#0284c7" />

        <!-- Bar 2: Alarm SCADA ISA-18.2 (78%) -->
        <text x="0" y="72" fill="#cbd5e1" font-size="10.5">Respons Alarm SCADA (ISA-18.2)</text>
        <text x="372" y="72" fill="#f59e0b" font-size="10.5" font-weight="700" text-anchor="end">78%</text>
        <rect x="0" y="78" width="372" height="7" rx="3.5" fill="#0f172a" />
        <rect x="0" y="78" width="290" height="7" rx="3.5" fill="#f59e0b" />

        <!-- Bar 3: Mutu Air Permenkes (88%) -->
        <text x="0" y="102" fill="#cbd5e1" font-size="10.5">Kualitas Mutu Air (Permenkes 2/2023)</text>
        <text x="372" y="102" fill="#10b981" font-size="10.5" font-weight="700" text-anchor="end">88%</text>
        <rect x="0" y="108" width="372" height="7" rx="3.5" fill="#0f172a" />
        <rect x="0" y="108" width="327" height="7" rx="3.5" fill="#10b981" />

        <!-- Bar 4: SOP & K3 Operasional (92%) -->
        <text x="0" y="132" fill="#cbd5e1" font-size="10.5">SOP &amp; K3 Operasional</text>
        <text x="372" y="132" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="end">92%</text>
        <rect x="0" y="138" width="372" height="7" rx="3.5" fill="#0f172a" />
        <rect x="0" y="138" width="342" height="7" rx="3.5" fill="#34d399" />

        <!-- Bar 5: Efisiensi Energi & Dosing (72%) -->
        <text x="0" y="162" fill="#cbd5e1" font-size="10.5">Efisiensi Kimia &amp; Energi</text>
        <text x="372" y="162" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="end">72%</text>
        <rect x="0" y="168" width="372" height="7" rx="3.5" fill="#0f172a" />
        <rect x="0" y="168" width="268" height="7" rx="3.5" fill="#0284c7" />

        <!-- Sparkline Tren Skor 7 Misi (96, 92, 88, 85, 86, 88, 76) -->
        <g transform="translate(0, 185)">
          <line x1="0" y1="0" x2="372" y2="0" stroke="#334155" stroke-width="1" />
          <text x="0" y="16" fill="#94a3b8" font-size="10" font-weight="600">TREN SKOR 7 MISI (IPA-01 s/d IPA-07):</text>
          <path d="M 0 35 L 50 30 L 100 36 L 150 40 L 200 38 L 260 36 L 330 48" fill="none" stroke="#38bdf8" stroke-width="2" />
          <circle cx="0" cy="35" r="3" fill="#38bdf8" /><text x="0" y="27" fill="#94a3b8" font-size="8.5">96</text>
          <circle cx="50" cy="30" r="3" fill="#38bdf8" /><text x="50" y="22" fill="#94a3b8" font-size="8.5">92</text>
          <circle cx="100" cy="36" r="3" fill="#38bdf8" /><text x="100" y="28" fill="#94a3b8" font-size="8.5">88</text>
          <circle cx="150" cy="40" r="3" fill="#38bdf8" /><text x="150" y="32" fill="#94a3b8" font-size="8.5">85</text>
          <circle cx="200" cy="38" r="3" fill="#38bdf8" /><text x="200" y="30" fill="#94a3b8" font-size="8.5">86</text>
          <circle cx="260" cy="36" r="3" fill="#38bdf8" /><text x="260" y="28" fill="#38bdf8" font-size="8.5" font-weight="700">88</text>
          <circle cx="330" cy="48" r="3" fill="#f59e0b" /><text x="330" y="42" fill="#f59e0b" font-size="8.5">76</text>
        </g>
      </g>
    </g>

    <!-- 3. Smart Advisor & Pre-Test Card (Height: 160) -->
    <g transform="translate(0, 610)">
      <rect width="420" height="160" rx="14" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
      <g transform="translate(20, 16)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">💡 SARAN BELAJAR OTOMATIS (PRD §11):</text>
        <text x="0" y="38" fill="#e2e8f0" font-size="11" font-weight="600">"Waktu respons Anda pada misi gangguan rata-rata</text>
        <text x="0" y="54" fill="#e2e8f0" font-size="11" font-weight="600">2× target skenario. Ulangi latihan penanganan</text>
        <text x="0" y="70" fill="#e2e8f0" font-size="11" font-weight="600">pompa trip di IPA-07 sebelum Misi Kelulusan IPA-09."</text>
        
        <rect x="0" y="86" width="380" height="34" rx="6" fill="#0284c7" />
        <text x="190" y="108" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">LATIHAN ULANG: IPA-07 (POMPA TRIP) →</text>
      </g>
    </g>
  </g>

  <!-- Right Section: 5-Tier Mission Roadmap (PRD §7: 9 Misi Jalur IPA) (Width: 1092) -->
  <g transform="translate(476, 190)">
    <rect width="1092" height="770" rx="14" fill="url(#cardDark)" stroke="#334155" stroke-width="1.5" />
    
    <!-- Roadmap Header -->
    <g transform="translate(28, 20)">
      <text x="0" y="18" fill="#f8fafc" font-size="16" font-weight="700">PETA MISI JALUR OPERATOR IPA (9 MISI BERJENJANG)</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Aturan Bintang: &lt;70 Belum Lulus · 70–84 (1★) · 85–94 (2★) · ≥95 (3★). Misi Kelulusan lulus jika skor ≥80.</text>
    </g>

    <!-- TIER 1: PENGENALAN (MUDAH) -->
    <g transform="translate(28, 70)">
      <rect width="1036" height="96" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="96" rx="4" fill="#0284c7" />
      <text x="24" y="22" fill="#38bdf8" font-size="11.5" font-weight="700">TINGKAT 1: PENGENALAN (MUDAH · 1,0x XP · TANPA GANGGUAN)</text>
      
      <!-- Card IPA-01 -->
      <g transform="translate(24, 30)">
        <rect width="360" height="52" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <circle cx="26" cy="26" r="12" fill="#059669" /><text x="26" y="30" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">✓</text>
        <text x="48" y="20" fill="#ffffff" font-size="11.5" font-weight="700">IPA-01: Kenali Ruang Kendali</text>
        <text x="48" y="36" fill="#34d399" font-size="10.5">Skor: 96 · 3★ (★★★) · +96 XP</text>
        <text x="340" y="32" fill="#f59e0b" font-size="12" text-anchor="end">★★★</text>
      </g>
    </g>

    <!-- TIER 2: OPERASI NORMAL (SEDANG) -->
    <g transform="translate(28, 180)">
      <rect width="1036" height="115" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="115" rx="4" fill="#059669" />
      <text x="24" y="22" fill="#34d399" font-size="11.5" font-weight="700">TINGKAT 2: OPERASI NORMAL (SEDANG · 1,5x XP)</text>

      <!-- Card IPA-02 -->
      <g transform="translate(24, 32)">
        <rect width="235" height="68" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="20" fill="#ffffff" font-size="11" font-weight="700">IPA-02: Menyalakan Intake</text>
        <text x="14" y="36" fill="#94a3b8" font-size="10">Debit &amp; start pompa intake</text>
        <text x="14" y="54" fill="#34d399" font-size="10.5" font-weight="600">Skor: 92 (★★☆) · +138 XP</text>
      </g>

      <!-- Card IPA-03 -->
      <g transform="translate(275, 32)">
        <rect width="235" height="68" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="20" fill="#ffffff" font-size="11" font-weight="700">IPA-03: Dosis Koagulan</text>
        <text x="14" y="36" fill="#94a3b8" font-size="10">Kekeruhan air olahan &lt;3 NTU</text>
        <text x="14" y="54" fill="#34d399" font-size="10.5" font-weight="600">Skor: 88 (★★☆) · +132 XP</text>
      </g>

      <!-- Card IPA-04 -->
      <g transform="translate(526, 32)">
        <rect width="235" height="68" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="20" fill="#ffffff" font-size="11" font-weight="700">IPA-04: Jaga Filter &amp; Cuci</text>
        <text x="14" y="36" fill="#94a3b8" font-size="10">Headloss &amp; pencucian balik</text>
        <text x="14" y="54" fill="#34d399" font-size="10.5" font-weight="600">Skor: 85 (★★☆) · +128 XP</text>
      </g>

      <!-- Card IPA-05 -->
      <g transform="translate(777, 32)">
        <rect width="235" height="68" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="20" fill="#ffffff" font-size="11" font-weight="700">IPA-05: Klorinasi Tepat</text>
        <text x="14" y="36" fill="#94a3b8" font-size="10">Sisa klor 0,2–0,5 mg/L</text>
        <text x="14" y="54" fill="#34d399" font-size="10.5" font-weight="600">Skor: 86 (★★☆) · +129 XP</text>
      </g>
    </g>

    <!-- TIER 3: GANGGUAN TUNGGAL (SULIT) -->
    <g transform="translate(28, 310)">
      <rect width="1036" height="145" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="145" rx="4" fill="#f59e0b" />
      <text x="24" y="22" fill="#fbbf24" font-size="11.5" font-weight="700">TINGKAT 3: GANGGUAN TUNGGAL (SULIT · 2,0x XP · 5 GANGGUAN UTAMA PRD §7)</text>

      <!-- Card IPA-06: Sesi Contoh Konsisten PRD -->
      <g transform="translate(24, 32)">
        <rect width="320" height="96" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <rect x="12" y="10" width="75" height="18" rx="4" fill="#0284c7" />
        <text x="49" y="23" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle">SESI CONTOH</text>
        <text x="94" y="24" fill="#38bdf8" font-size="11.5" font-weight="700">IPA-06: Lonjakan Kekeruhan</text>
        <text x="12" y="46" fill="#cbd5e1" font-size="10.5">Air baku 185 NTU · Naikkan dosis &amp; pH</text>
        <text x="12" y="66" fill="#f59e0b" font-size="11.5" font-weight="700">Skor: 88 · 2★ (★★☆) · +176 XP</text>
        <text x="12" y="84" fill="#10b981" font-size="10">✓ Lulus Baik (Durasi 08:30) · Lencana Respons Kilat</text>
      </g>

      <!-- Card IPA-07: Pompa Trip -->
      <g transform="translate(360, 32)">
        <rect width="320" height="96" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
        <text x="12" y="24" fill="#ffffff" font-size="11.5" font-weight="700">IPA-07: Gangguan Pompa Trip</text>
        <text x="12" y="46" fill="#cbd5e1" font-size="10.5">Alihkan ke pompa cadangan &amp; reset</text>
        <text x="12" y="66" fill="#f59e0b" font-size="11.5" font-weight="700">Skor: 76 · 1★ (★☆☆) · +152 XP</text>
        <text x="12" y="84" fill="#fbbf24" font-size="10">⚠️ Lulus KKM (Perlu perbaikan respons)</text>
      </g>

      <!-- Card IPA-08: Dosis Klor Drop (Aktif Berikutnya) -->
      <g transform="translate(696, 32)">
        <rect width="316" height="96" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2" />
        <rect x="12" y="10" width="80" height="18" rx="4" fill="#38bdf8" />
        <text x="52" y="23" fill="#082f49" font-size="9.5" font-weight="700" text-anchor="middle">MISI BERIKUT</text>
        <text x="100" y="24" fill="#ffffff" font-size="11.5" font-weight="700">IPA-08: Dosis Klor Drop</text>
        <text x="12" y="46" fill="#bae6fd" font-size="10.5">Koreksi setpoint klor &amp; pantau reservoir</text>
        <text x="12" y="66" fill="#7dd3fc" font-size="10.5">Status: Siap Dikerjakan (Terbuka)</text>
        <rect x="12" y="72" width="150" height="18" rx="4" fill="#0284c7" />
        <text x="87" y="85" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">MULAI MISI INI →</text>
      </g>
    </g>

    <!-- TIER 4: GANGGUAN BERANTAI (KHUSUS TERPADU) -->
    <g transform="translate(28, 470)">
      <rect width="1036" height="75" rx="10" fill="#090d16" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="75" rx="4" fill="#64748b" />
      <text x="24" y="22" fill="#94a3b8" font-size="11.5" font-weight="700">TINGKAT 4: GANGGUAN BERANTAI (SANGAT SULIT · KHUSUS JALUR TERPADU TRP-01)</text>
      <text x="24" y="44" fill="#64748b" font-size="11">Jalur Operator IPA melompat langsung dari Tingkat 3 ke Misi Kelulusan Ujian (IPA-09).</text>
      <text x="24" y="60" fill="#0284c7" font-size="10.5">Misi TRP-01 "Hulu ke Hilir" hanya tersedia di Jalur Air Minum Terpadu (17 Misi).</text>
    </g>

    <!-- TIER 5: MISI KELULUSAN (UJIAN) -->
    <g transform="translate(28, 560)">
      <rect width="1036" height="130" rx="10" fill="#1e1b4b" stroke="#4338ca" stroke-width="1.5" />
      <rect x="0" y="0" width="8" height="130" rx="4" fill="#818cf8" />
      <text x="24" y="24" fill="#c7d2fe" font-size="12" font-weight="700">TINGKAT 5: MISI KELULUSAN JALUR IPA (UJIAN AKHIR · BATAS WAKTU &amp; TANPA PETUNJUK · 3,0x XP)</text>
      
      <g transform="translate(24, 36)">
        <rect width="580" height="78" rx="8" fill="#0f172a" stroke="#334155" />
        <text x="16" y="24" fill="#ffffff" font-size="13" font-weight="700">IPA-09: Misi Kelulusan Operator IPA (Ujian Praktik)</text>
        <text x="16" y="42" fill="#94a3b8" font-size="11">Skenario: Lonjakan kekeruhan ekstrem disusul pompa trip serentak tanpa petunjuk.</text>
        <text x="16" y="62" fill="#fbbf24" font-size="10.5" font-weight="600">Ambang Kelulusan: Skor Minimal ≥ 80 (PRD §8) · Pengali XP: 3,0x (Ujian)</text>
        <text x="545" y="45" fill="#ef4444" font-size="20" text-anchor="middle">🔒</text>
      </g>

      <g transform="translate(620, 36)">
        <rect width="392" height="78" rx="8" fill="#0f172a" stroke="#334155" />
        <text x="16" y="22" fill="#38bdf8" font-size="11.5" font-weight="700">SYARAT BUKA KUNCI IPA-09:</text>
        <text x="16" y="42" fill="#34d399" font-size="10.5">✓ IPA-01 s/d IPA-07 Lulus (14 Bintang Terkumpul)</text>
        <text x="16" y="60" fill="#f59e0b" font-size="10.5">⏳ Selesaikan IPA-08 (Dosis Klor Drop)</text>
      </g>
    </g>

    <!-- Bottom: Unlocked Badges Bar PRD §8 -->
    <g transform="translate(28, 705)">
      <rect width="1036" height="48" rx="8" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11" font-weight="700">LENCANA DIMAS (3 DARI 8 TERBUKA PRD §8):</text>
      
      <rect x="290" y="10" width="180" height="28" rx="6" fill="#064e3b" stroke="#059669" />
      <text x="380" y="28" fill="#a7f3d0" font-size="10.5" font-weight="700" text-anchor="middle">🧭 Penjelajah Titik Kontrol</text>

      <rect x="480" y="10" width="150" height="28" rx="6" fill="#064e3b" stroke="#059669" />
      <text x="555" y="28" fill="#a7f3d0" font-size="10.5" font-weight="700" text-anchor="middle">⚡ Respons Kilat</text>

      <rect x="640" y="10" width="175" height="28" rx="6" fill="#064e3b" stroke="#059669" />
      <text x="727" y="28" fill="#a7f3d0" font-size="10.5" font-weight="700" text-anchor="middle">🔔 Tanpa Alarm Terlewat</text>

      <text x="1016" y="28" fill="#64748b" font-size="10.5" text-anchor="end">+ 5 Lencana Terkunci (Lihat di L7)</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L2: BERANDA PESERTA & ROADMAP MISI (SimSCADA-Air v1.0)")

print("Generating L1 & L2 directly to public/...")
l1_svg = sanitize_xml(generate_l1())
l2_svg = sanitize_xml(generate_l2())

with open(os.path.join(PUBLIC_DIR, "mockup_l1_login.svg"), "w", encoding="utf-8") as f:
    f.write(l1_svg)
with open(os.path.join(PUBLIC_DIR, "mockup_l2_trainee_dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(l2_svg)

ET.parse(os.path.join(PUBLIC_DIR, "mockup_l1_login.svg"))
ET.parse(os.path.join(PUBLIC_DIR, "mockup_l2_trainee_dashboard.svg"))
print("L1 and L2 successfully generated and validated in public/!")

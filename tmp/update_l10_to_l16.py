#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 5: L10, L11, L12, L13, L14, L15, L16
Directly generated into public/ with strict PRD v1.0 compliance, proper coordinate offsets,
elimination of text overlap, and complete XML validation.
"""
import os
import re
import xml.etree.ElementTree as ET

OUTPUT_DIR = os.path.join(os.getcwd(), "public")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_xml(text):
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)

def svg_wrap(content, width=1920, height=1080):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#080e1a" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#06b6d4" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#fbbf24" />
    </linearGradient>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bgGrad)" />
{content}
</svg>"""
    return sanitize_xml(svg)

def header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · SPAM", name="Budi Santoso, S.T.", initials="BS"):
    return f"""  <!-- Standard Tenant Header PRD §6 -->
  <g transform="translate(32, 24)">
    <rect width="1856" height="64" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    <circle cx="44" cy="32" r="20" fill="#0284c7" />
    <path d="M44 18 C44 18 34 29 34 35 C34 40.5 38.5 45 44 45 C49.5 45 54 40.5 54 35 C54 29 44 18 44 18 Z" fill="#ffffff" />
    <text x="76" y="28" fill="#ffffff" font-size="16" font-weight="700">{lembaga}</text>
    <text x="76" y="46" fill="#38bdf8" font-size="11" font-weight="500">Platform Simulasi SCADA SPAM · <tspan fill="#64748b">Didukung oleh SimSCADA-Air</tspan></text>
    
    <g transform="translate(1420, 14)">
      <rect width="404" height="36" rx="18" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="18" r="14" fill="#0369a1" />
      <text x="20" y="22" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">{initials}</text>
      <text x="44" y="17" fill="#f8fafc" font-size="12" font-weight="600">{name}</text>
      <text x="44" y="30" fill="#94a3b8" font-size="10">{role}</text>
      <rect x="310" y="8" width="82" height="20" rx="10" fill="#b91c1c" />
      <text x="351" y="22" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">KELUAR</text>
    </g>
  </g>"""

def page_title_block(title, subtitle, y=112):
    return f"""  <!-- Page Title Block -->
  <g transform="translate(32, {y})">
    <text x="0" y="22" fill="#ffffff" font-size="20" font-weight="700">{title}</text>
    <text x="0" y="42" fill="#94a3b8" font-size="12.5">{subtitle}</text>
  </g>"""

# ==================== L10: MANAGE SCENARIOS ====================
def generate_l10():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · SPAM", name="Budi Santoso, S.T.", initials="BS")
    title = page_title_block("Kelola Skenario Gangguan Kustom", "Authoring Tool Skenario Gangguan (FR-23) · Katalog Misi PRD §7 · Target Respons Alarm = 60 Detik", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Grid: Left = Authoring Form (Width 960), Right = Scenario Catalog (Width 864) -->
  <g transform="translate(32, 180)">
    <!-- LEFT CARD: AUTHORING FORM -->
    <rect width="960" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(32, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Formulir Perancangan Skenario Baru (Authoring Tool FR-23)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Rancang parameter hidrolika dan gangguan kimia proses air minum untuk latihan spesifik</text>
      <line x1="0" y1="56" x2="896" y2="56" stroke="#334155" stroke-width="1" />

      <!-- Field 1: Judul Skenario -->
      <g transform="translate(0, 75)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">JUDUL SKENARIO GANGGUAN:</text>
        <rect x="0" y="26" width="896" height="42" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="52" fill="#ffffff" font-size="13">Lonjakan Kekeruhan Air Baku Akibat Hujan Lebat di Hulu (SOP-IPA-06)</text>
      </g>

      <!-- Field 2: Difficulty & XP Multiplier PRD §7 -->
      <g transform="translate(0, 160)">
        <text x="0" y="16" fill="#f59e0b" font-size="12" font-weight="700">TINGKAT KESULITAN &amp; PENGALI XP (PRD SIMSCADA-AIR v1.0 §7):</text>
        <rect x="0" y="26" width="435" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
        <text x="16" y="52" fill="#fbbf24" font-size="13" font-weight="700">Tingkat 3: Sulit (Pengali XP = 2,0x) ▾</text>

        <rect x="460" y="26" width="436" height="42" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="476" y="52" fill="#94a3b8" font-size="11.5">Katalog PRD: Mudah (1x) · Sedang (1,5x) · Sulit (2x) · S.Sulit (2,5x) · Ujian (3x)</text>
      </g>

      <!-- Field 3: Target Response Time & Track Target -->
      <g transform="translate(0, 245)">
        <g transform="translate(0, 0)">
          <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">TARGET WAKTU RESPONS ALARM (PRD §8):</text>
          <rect x="0" y="26" width="435" height="42" rx="6" fill="#0f172a" stroke="#0284c7" />
          <text x="16" y="52" fill="#38bdf8" font-size="13" font-weight="700">60 Detik (Syarat Respons Kilat: &lt;30 Detik)</text>
        </g>
        <g transform="translate(460, 0)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">JALUR PELATIHAN TERKAIT:</text>
          <rect x="0" y="26" width="436" height="42" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="52" fill="#ffffff" font-size="13">Jalur IPA (Pengolahan Air Minum) · Kode IPA-06</text>
        </g>
      </g>

      <!-- Field 4: Initial Parameters & Fault Injection -->
      <g transform="translate(0, 335)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">KONDISI AWAL &amp; INJEKSI GANGGUAN HIDROLIKA / KIMIA:</text>
        <rect x="0" y="26" width="896" height="135" rx="6" fill="#0f172a" stroke="#334155" />
        <g transform="translate(16, 20)">
          <text x="0" y="16" fill="#94a3b8" font-size="11.5">• Waktu Pemicu Gangguan: <tspan fill="#ffffff" font-weight="700">Menit 01:00</tspan> sejak simulasi dimulai.</text>
          <text x="0" y="38" fill="#94a3b8" font-size="11.5">• Parameter Berubah: <tspan fill="#f87171" font-weight="700">Kekeruhan Air Baku melonjak dari 15 NTU ke 45 NTU</tspan>.</text>
          <text x="0" y="60" fill="#94a3b8" font-size="11.5">• Pemicu Alarm: <tspan fill="#fbbf24" font-weight="700">Kekeruhan Keluaran Filter ≥3,0 NTU (Tinggi) pada menit 01:10</tspan>.</text>
          <text x="0" y="82" fill="#94a3b8" font-size="11.5">• Kriteria Auto-Clear: <tspan fill="#34d399" font-weight="700">Kekeruhan air olahan kembali stabil &lt;1,5 NTU selama 30 detik berturut-turut</tspan>.</text>
        </g>
      </g>

      <!-- Field 5: SOP Steps & Checklist -->
      <g transform="translate(0, 510)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">TINDAKAN MITIGASI SOP RESMI YANG DIHARAPKAN:</text>
        <rect x="0" y="26" width="896" height="120" rx="6" fill="#0f172a" stroke="#334155" />
        <g transform="translate(16, 20)">
          <text x="0" y="16" fill="#cbd5e1" font-size="11.5">1. Tekan tombol ACK Alarm sebelum 60 detik (target Respons Kilat: &lt;30 detik).</text>
          <text x="0" y="38" fill="#cbd5e1" font-size="11.5">2. Naikkan setpoint dosis koagulan aluminium sulfat dari 25 mg/L ke 45–50 mg/L.</text>
          <text x="0" y="60" fill="#cbd5e1" font-size="11.5">3. Naikkan kecepatan pengaduk cepat koagulasi (flash mixer) ke 100 RPM.</text>
          <text x="0" y="82" fill="#cbd5e1" font-size="11.5">4. Pantau kestabilan flok &amp; pastikan kekeruhan filtrasi turun di bawah 1,5 NTU.</text>
        </g>
      </g>

      <!-- Action Buttons -->
      <g transform="translate(0, 680)">
        <rect width="200" height="44" rx="8" fill="#0284c7" />
        <text x="100" y="27" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Simpan Skenario (FR-23)</text>

        <rect x="220" y="0" width="160" height="44" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="300" y="27" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">Uji di Simulator</text>

        <rect x="400" y="0" width="160" height="44" rx="8" fill="#1e293b" stroke="#b91c1c" />
        <text x="480" y="27" fill="#f87171" font-size="13" font-weight="600" text-anchor="middle">Batalkan</text>
      </g>
    </g>

    <!-- RIGHT CARD: SCENARIO CATALOG PRD §7 -->
    <g transform="translate(992, 0)">
      <rect width="864" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(28, 26)">
        <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Katalog Misi &amp; Skenario Bawaan (PRD §7)</text>
        <text x="0" y="40" fill="#94a3b8" font-size="12">Daftar lengkap 17 skenario simulasi berbasis kurikulum diklat SPAM</text>
        <line x1="0" y1="56" x2="808" y2="56" stroke="#334155" stroke-width="1" />

        <!-- Track Tabs -->
        <g transform="translate(0, 68)">
          <rect x="0" y="0" width="190" height="32" rx="6" fill="#0284c7" />
          <text x="95" y="20" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">Jalur IPA (9 Misi)</text>

          <rect x="205" y="0" width="220" height="32" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="315" y="20" fill="#94a3b8" font-size="11.5" text-anchor="middle">Jalur Distribusi (7 Misi)</text>

          <rect x="440" y="0" width="220" height="32" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="550" y="20" fill="#94a3b8" font-size="11.5" text-anchor="middle">Jalur Terpadu (17 Misi)</text>
        </g>

        <!-- Scenario Item 1: IPA-01 -->
        <g transform="translate(0, 118)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#334155" />
          <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="700">IPA-01: Pengenalan SCADA &amp; Navigasi HMI SPAM</text>
          <text x="20" y="48" fill="#94a3b8" font-size="11">Tingkat 1: Pengenalan (Mudah · 1,0x XP) · Tanpa gangguan · Eksplorasi titik kontrol</text>
          <rect x="710" y="18" width="80" height="28" rx="4" fill="#1e293b" stroke="#334155" />
          <text x="750" y="36" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Ubah</text>
        </g>

        <!-- Scenario Item 2: IPA-02 -->
        <g transform="translate(0, 192)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#334155" />
          <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="700">IPA-02: Start-Up &amp; Operasi Normal Instalasi Pengolahan</text>
          <text x="20" y="48" fill="#94a3b8" font-size="11">Tingkat 2: Operasi Normal (Sedang · 1,5x XP) · Pengendalian debit intake &amp; aerasi</text>
          <rect x="710" y="18" width="80" height="28" rx="4" fill="#1e293b" stroke="#334155" />
          <text x="750" y="36" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Ubah</text>
        </g>

        <!-- Scenario Item 3: IPA-06 (CURRENT FOCUS) -->
        <g transform="translate(0, 266)">
          <rect width="808" height="74" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
          <text x="20" y="28" fill="#fbbf24" font-size="12.5" font-weight="700">IPA-06: Gangguan: Lonjakan Kekeruhan Air Baku (Skenario Demo)</text>
          <text x="20" y="48" fill="#f8fafc" font-size="11">Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP) · Target Respons: 60 Detik · Dosis Koagulan</text>
          <text x="20" y="64" fill="#34d399" font-size="10.5">✓ Dipakai pada sesi evaluasi Dimas Wahyu Pratama (Skor 88 · 2★ · +176 XP)</text>
          <rect x="710" y="22" width="80" height="28" rx="4" fill="#f59e0b" />
          <text x="750" y="40" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">Aktif ▾</text>
        </g>

        <!-- Scenario Item 4: IPA-07 -->
        <g transform="translate(0, 350)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#334155" />
          <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="700">IPA-07: Gangguan: Pompa Dosing Koagulan Mengalami Trip</text>
          <text x="20" y="48" fill="#94a3b8" font-size="11">Tingkat 3: Gangguan Tunggal (Sulit · 2,0x XP) · Pengalihan pompa standby &amp; SOP bypass</text>
          <rect x="710" y="18" width="80" height="28" rx="4" fill="#1e293b" stroke="#334155" />
          <text x="750" y="36" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Ubah</text>
        </g>

        <!-- Scenario Item 5: IPA-09 -->
        <g transform="translate(0, 424)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#dc2626" />
          <text x="20" y="28" fill="#f87171" font-size="12" font-weight="700">IPA-09: Misi Kelulusan Ujian Komprehensif Jalur IPA</text>
          <text x="20" y="48" fill="#94a3b8" font-size="11">Tingkat 5: Misi Kelulusan (Ujian · 3,0x XP) · Ambang KKM Skor ≥80 · Tanpa Petunjuk</text>
          <rect x="710" y="18" width="80" height="28" rx="4" fill="#1e293b" stroke="#334155" />
          <text x="750" y="36" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Ubah</text>
        </g>

        <!-- Scenario Item 6: TRP-01 -->
        <g transform="translate(0, 498)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#8b5cf6" />
          <text x="20" y="28" fill="#c084fc" font-size="12" font-weight="700">TRP-01: Gangguan Berantai: Mati Listrik Genset &amp; Water Hammer</text>
          <text x="20" y="48" fill="#94a3b8" font-size="11">Tingkat 4: Gangguan Berantai (Sangat Sulit · 2,5x XP) · Khusus Jalur Terpadu 17 Misi</text>
          <rect x="710" y="18" width="80" height="28" rx="4" fill="#1e293b" stroke="#334155" />
          <text x="750" y="36" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Ubah</text>
        </g>

        <!-- Summary Note -->
        <g transform="translate(0, 580)">
          <rect width="808" height="150" rx="8" fill="#1e293b" stroke="#334155" />
          <g transform="translate(20, 20)">
            <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">Ketentuan Skenario Sesuai PRD SimSCADA-Air v1.0 §7 &amp; §10:</text>
            <text x="0" y="40" fill="#cbd5e1" font-size="11.5">• Waktu target skenario menentukan validitas perolehan lencana <tspan fill="#ffffff" font-weight="600">Respons Kilat</tspan> (&lt;50% × 60s = 30s).</text>
            <text x="0" y="60" fill="#cbd5e1" font-size="11.5">• Pengali XP otomatis diterapkan pada skor akhir 4 komponen evaluasi (0–100).</text>
            <text x="0" y="80" fill="#cbd5e1" font-size="11.5">• Seluruh instruktur di lembaga berhak menambah atau mengubah skenario kustom (FR-23).</text>
          </g>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L11: SESSION REPLAY ====================
def generate_l11():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · SPAM", name="Budi Santoso, S.T.", initials="BS")
    title = page_title_block("Replay Sesi Skenario (Event &amp; Process Review)", "Audit Rekaman Skenario IPA-06 · Dimas Wahyu Pratama (peserta.ipa) · Respons 25 Detik (Target: 60s)", 112)
    
    content = f"""{hdr}{title}
  <!-- Session Header Card (Height 86, Width 1856) -->
  <g transform="translate(32, 175)">
    <rect width="1856" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">SKENARIO &amp; OPERATOR</text>
      <text x="0" y="44" fill="#ffffff" font-size="20" font-weight="800">IPA-06: Lonjakan Kekeruhan Air Baku <tspan fill="#38bdf8" font-size="14" font-weight="600">· Dimas Wahyu Pratama (Angkatan 2)</tspan></text>
      
      <text x="780" y="24" fill="#94a3b8" font-size="11.5">WAKTU SESI: <tspan fill="#ffffff" font-weight="700">08 Menit 30 Detik</tspan></text>
      <text x="780" y="46" fill="#94a3b8" font-size="11.5">SKOR AKHIR: <tspan fill="#34d399" font-weight="800">88 / 100</tspan> (2★ · 176 XP)</text>

      <text x="1140" y="24" fill="#94a3b8" font-size="11.5">RESPONS ALARM PERTAMA: <tspan fill="#34d399" font-weight="700">25 Detik</tspan></text>
      <text x="1140" y="46" fill="#94a3b8" font-size="11.5">TARGET SKENARIO: <tspan fill="#fbbf24" font-weight="700">60 Detik</tspan> (Respons Kilat ✓)</text>

      <rect x="1560" y="14" width="130" height="36" rx="6" fill="#0284c7" />
      <text x="1625" y="37" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Putar Ulang ▶</text>

      <rect x="1705" y="14" width="125" height="36" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="1767" y="37" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Kecepatan 2x ▾</text>
    </g>
  </g>

  <!-- TIMELINE SCRUBBER WITH STAGGERED MARKERS (Width 1856, Height 140) -->
  <!-- Staggered markers prevent label collision: odd markers y=-12, even markers y=28 -->
  <g transform="translate(32, 275)">
    <rect width="1856" height="130" rx="10" fill="#0f172a" stroke="#334155" />
    <g transform="translate(30, 24)">
      <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">Garis Waktu Kejadian Skenario (Scrubber Interaktif)</text>
      <text x="400" y="16" fill="#94a3b8" font-size="11.5">Klik penanda peristiwa di bawah untuk melompat langsung ke saat kejadian</text>
      
      <!-- Base Scrubber Bar (Width 1796) -->
      <g transform="translate(0, 52)">
        <rect width="1796" height="12" rx="6" fill="#1e293b" />
        <rect width="1796" height="12" rx="6" fill="#0284c7" fill-opacity="0.6" />
        
        <!-- MARKER 1: 00:00 (Mulai) - Stagger TOP (y = -12) -->
        <g transform="translate(20, 0)">
          <circle cx="0" cy="6" r="6" fill="#38bdf8" />
          <line x1="0" y1="0" x2="0" y2="-12" stroke="#38bdf8" stroke-width="1.5" />
          <text x="0" y="-18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">00:00 Mulai</text>
        </g>

        <!-- MARKER 2: 01:00 (Gangguan) - Stagger BOTTOM (y = 28) -->
        <g transform="translate(210, 0)">
          <circle cx="0" cy="6" r="6" fill="#f87171" />
          <line x1="0" y1="12" x2="0" y2="24" stroke="#f87171" stroke-width="1.5" />
          <text x="0" y="38" fill="#f87171" font-size="10" font-weight="700" text-anchor="middle">01:00 Gangguan 45 NTU</text>
        </g>

        <!-- MARKER 3: 01:10 (Alarm Kekeruhan Tinggi) - Stagger TOP (y = -12) -->
        <g transform="translate(260, 0)">
          <circle cx="0" cy="6" r="6" fill="#fbbf24" />
          <line x1="0" y1="0" x2="0" y2="-12" stroke="#fbbf24" stroke-width="1.5" />
          <text x="0" y="-18" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">01:10 Alarm Kekeruhan</text>
        </g>

        <!-- MARKER 4: 01:25 (ACK Operator) - Stagger BOTTOM (y = 28) -->
        <g transform="translate(320, 0)">
          <circle cx="0" cy="6" r="6" fill="#34d399" />
          <line x1="0" y1="12" x2="0" y2="24" stroke="#34d399" stroke-width="1.5" />
          <text x="0" y="38" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">01:25 ACK (25s)</text>
        </g>

        <!-- MARKER 5: 01:45 (Dosis 48 mg/L) - Stagger TOP (y = -12) -->
        <g transform="translate(420, 0)">
          <circle cx="0" cy="6" r="6" fill="#38bdf8" />
          <line x1="0" y1="0" x2="0" y2="-12" stroke="#38bdf8" stroke-width="1.5" />
          <text x="0" y="-18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">01:45 Dosis 48 mg/L</text>
        </g>

        <!-- MARKER 6: 02:30 (RPM 100) - Stagger BOTTOM (y = 28) -->
        <g transform="translate(560, 0)">
          <circle cx="0" cy="6" r="6" fill="#a855f7" />
          <line x1="0" y1="12" x2="0" y2="24" stroke="#a855f7" stroke-width="1.5" />
          <text x="0" y="38" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">02:30 Flash Mixer 100 RPM</text>
        </g>

        <!-- MARKER 7: 04:10 (Kekeruhan 2,1 NTU) - Stagger TOP (y = -12) -->
        <g transform="translate(900, 0)">
          <circle cx="0" cy="6" r="6" fill="#38bdf8" />
          <line x1="0" y1="0" x2="0" y2="-12" stroke="#38bdf8" stroke-width="1.5" />
          <text x="0" y="-18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">04:10 Mutu Turun 2,1 NTU</text>
        </g>

        <!-- MARKER 8: 06:20 (Auto-Clear 1,2 NTU) - Stagger BOTTOM (y = 28) -->
        <g transform="translate(1360, 0)">
          <circle cx="0" cy="6" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2" />
          <line x1="0" y1="12" x2="0" y2="24" stroke="#10b981" stroke-width="1.5" />
          <text x="0" y="38" fill="#34d399" font-size="10.5" font-weight="800" text-anchor="middle">06:20 Auto-Clear 1,2 NTU</text>
        </g>

        <!-- MARKER 9: 08:30 (Selesai) - Stagger TOP (y = -12) -->
        <g transform="translate(1780, 0)">
          <circle cx="0" cy="6" r="6" fill="#0284c7" />
          <line x1="0" y1="0" x2="0" y2="-12" stroke="#0284c7" stroke-width="1.5" />
          <text x="0" y="-18" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">08:30 Selesai</text>
        </g>
      </g>
    </g>
  </g>

  <!-- SPLIT SCREEN: LEFT = HMI SCADA SNAPSHOT (Width 1120), RIGHT = AUDIT LOG (Width 704) -->
  <g transform="translate(32, 420)">
    <!-- LEFT CARD: SCADA SNAPSHOT AT 02:00 -->
    <rect width="1120" height="620" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#ffffff" font-size="14" font-weight="700">Pratinjau Layar HMI SCADA saat Kejadian (Tepat Menit 02:00)</text>
      <text x="0" y="36" fill="#94a3b8" font-size="11.5">Kondisi: Alarm Kekeruhan Tinggi diakui (ACK), operator sedang menaikkan dosis koagulan</text>
      
      <!-- Mini HMI Diagram Box -->
      <g transform="translate(0, 50)">
        <rect width="1072" height="420" rx="8" fill="#0b1120" stroke="#1e293b" />
        
        <!-- Active Alarm Strip at 02:00 -->
        <rect x="16" y="16" width="1040" height="38" rx="6" fill="#78350f" stroke="#f59e0b" />
        <text x="32" y="40" fill="#fbbf24" font-size="11.5" font-weight="700">▲ TINGGI · ALM-IPA-03: Kekeruhan Air Olahan 3,4 NTU ≥ 3,0 NTU (Diakui / ACK oleh DW pada 01:25)</text>

        <!-- Process Units -->
        <!-- Unit 1: Intake -->
        <g transform="translate(30, 80)">
          <rect width="220" height="180" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">01. INTAKE AIR BAKU</text>
          <text x="16" y="50" fill="#94a3b8" font-size="10.5">Kekeruhan: <tspan fill="#f87171" font-weight="700">45,0 NTU (Lonjakan)</tspan></text>
          <text x="16" y="72" fill="#94a3b8" font-size="10.5">Debit Intake: <tspan fill="#ffffff">150 L/dtk</tspan></text>
          <text x="16" y="94" fill="#94a3b8" font-size="10.5">pH Air Baku: <tspan fill="#ffffff">7,2</tspan></text>
          <text x="16" y="116" fill="#94a3b8" font-size="10.5">Pompa Intake 1: <tspan fill="#34d399">RUNNING</tspan></text>
          <text x="16" y="138" fill="#94a3b8" font-size="10.5">Pompa Intake 2: <tspan fill="#64748b">STANDBY</tspan></text>
        </g>

        <!-- Unit 2: Koagulasi & Flokulasi -->
        <g transform="translate(280, 80)">
          <rect width="250" height="180" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
          <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">02. KOAGULASI &amp; FLOKULASI</text>
          <text x="16" y="50" fill="#94a3b8" font-size="10.5">Dosis Koagulan: <tspan fill="#38bdf8" font-weight="700">48 mg/L</tspan> (Naik)</text>
          <text x="16" y="72" fill="#94a3b8" font-size="10.5">Penyesuai pH: <tspan fill="#ffffff">12 mg/L</tspan></text>
          <text x="16" y="94" fill="#94a3b8" font-size="10.5">Pengaduk Cepat: <tspan fill="#34d399">100 RPM</tspan></text>
          <text x="16" y="116" fill="#94a3b8" font-size="10.5">Pengaduk Lambat: <tspan fill="#34d399">30 RPM</tspan></text>
          <text x="16" y="138" fill="#94a3b8" font-size="10.5">Flok: <tspan fill="#34d399">Mulai Terbentuk</tspan></text>
        </g>

        <!-- Unit 3: Sedimentasi & Filtrasi -->
        <g transform="translate(560, 80)">
          <rect width="240" height="180" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
          <text x="16" y="24" fill="#fbbf24" font-size="11" font-weight="700">03. SEDIMENTASI &amp; FILTRASI</text>
          <text x="16" y="50" fill="#94a3b8" font-size="10.5">Kekeruhan Filter: <tspan fill="#f59e0b" font-weight="700">3,4 NTU</tspan></text>
          <text x="16" y="72" fill="#94a3b8" font-size="10.5">Ambang Normal: <tspan fill="#34d399">&lt;1,5 NTU</tspan></text>
          <text x="16" y="94" fill="#94a3b8" font-size="10.5">Status Filter 1: <tspan fill="#34d399">FILTERING</tspan></text>
          <text x="16" y="116" fill="#94a3b8" font-size="10.5">Status Filter 2: <tspan fill="#34d399">FILTERING</tspan></text>
          <text x="16" y="138" fill="#94a3b8" font-size="10.5">Kekeruhan: <tspan fill="#fbbf24">Sedang Menurun</tspan></text>
        </g>

        <!-- Unit 4: Reservoir & Desinfeksi -->
        <g transform="translate(830, 80)">
          <rect width="210" height="180" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">04. RESERVOIR AIR BERSIH</text>
          <text x="16" y="50" fill="#94a3b8" font-size="10.5">Level Reservoir: <tspan fill="#ffffff">4,2 m (84%)</tspan></text>
          <text x="16" y="72" fill="#94a3b8" font-size="10.5">Dosis Klor: <tspan fill="#ffffff">2,0 mg/L</tspan></text>
          <text x="16" y="94" fill="#94a3b8" font-size="10.5">Sisa Klor: <tspan fill="#34d399">0,6 mg/L</tspan></text>
          <text x="16" y="116" fill="#94a3b8" font-size="10.5">Inflow: <tspan fill="#ffffff">150 L/dtk</tspan></text>
        </g>

        <!-- Telemetry Graph Summary inside snapshot -->
        <g transform="translate(30, 280)">
          <rect width="1010" height="120" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="22" fill="#cbd5e1" font-size="11" font-weight="600">Tren Kekeruhan Air Olahan Sepanjang Sesi (NTU vs Waktu):</text>
          <!-- Simulated Trend Line -->
          <path d="M 40 90 L 150 90 L 220 30 L 320 32 L 440 40 L 600 65 L 800 85 L 980 88" fill="none" stroke="#f59e0b" stroke-width="2.5" />
          <line x1="40" y1="50" x2="980" y2="50" stroke="#f87171" stroke-dasharray="4,4" />
          <text x="990" y="54" fill="#f87171" font-size="10">Ambang 3,0 NTU</text>
          <text x="150" y="105" fill="#94a3b8" font-size="9.5">01:00 Gangguan</text>
          <text x="320" y="105" fill="#38bdf8" font-size="9.5">01:45 Dosis 48</text>
          <text x="800" y="105" fill="#34d399" font-size="9.5">06:20 Normal 1,2 NTU</text>
        </g>
      </g>

      <!-- Bottom evaluation summary -->
      <g transform="translate(0, 490)">
        <rect width="1072" height="105" rx="8" fill="#1e293b" stroke="#334155" />
        <g transform="translate(20, 16)">
          <text x="0" y="16" fill="#34d399" font-size="12" font-weight="700">✓ Evaluasi Instruktur Budi Santoso, S.T.:</text>
          <text x="0" y="38" fill="#cbd5e1" font-size="11">Operator merespons sangat sigap (25 detik), tepat 41,7% dari batas toleransi skenario 60 detik.</text>
          <text x="0" y="58" fill="#cbd5e1" font-size="11">Dosis koagulan dinaikkan secara proporsional sesuai jar-test tabel darurat tanpa terjadi overdosing.</text>
          <text x="0" y="78" fill="#38bdf8" font-size="11">Lencana "Respons Kilat" dan "Tanpa Alarm Terlewat" valid diberikan otomatis oleh sistem.</text>
        </g>
      </g>
    </g>

    <!-- RIGHT CARD: AUDIT LOG (Width 704) -->
    <g transform="translate(1152, 0)">
      <rect width="704" height="620" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#ffffff" font-size="14" font-weight="700">Log Kejadian &amp; Audit Intervensi Operator</text>
        <text x="0" y="36" fill="#94a3b8" font-size="11.5">Sinkronisasi matematis dengan L6, L5, dan L4</text>
        <line x1="0" y1="50" x2="656" y2="50" stroke="#334155" />

        <!-- Log Items -->
        <g transform="translate(0, 65)">
          <!-- Event 1 -->
          <g transform="translate(0, 0)">
            <text x="0" y="16" fill="#38bdf8" font-size="11" font-weight="700">00:00:00</text>
            <text x="70" y="16" fill="#ffffff" font-size="11" font-weight="600">Simulasi Dimulai (SOP Normal)</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Air baku 15 NTU · Dosis koagulan 25 mg/L · Filter 0,8 NTU</text>
          </g>

          <!-- Event 2 -->
          <g transform="translate(0, 50)">
            <text x="0" y="16" fill="#f87171" font-size="11" font-weight="700">00:01:00</text>
            <text x="70" y="16" fill="#f87171" font-size="11" font-weight="600">GANGGUAN DIINJEKSI MESIN</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Kekeruhan air baku melonjak cepat ke 45,0 NTU</text>
          </g>

          <!-- Event 3 -->
          <g transform="translate(0, 100)">
            <text x="0" y="16" fill="#fbbf24" font-size="11" font-weight="700">00:01:10</text>
            <text x="70" y="16" fill="#fbbf24" font-size="11" font-weight="600">ALARM TINGGI AKTIF (ALM-IPA-03)</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Kekeruhan air olahan keluaran filter menyentuh 3,4 NTU ≥ 3,0</text>
          </g>

          <!-- Event 4 -->
          <g transform="translate(0, 150)">
            <text x="0" y="16" fill="#34d399" font-size="11" font-weight="700">00:01:25</text>
            <text x="70" y="16" fill="#34d399" font-size="11" font-weight="700">ACK ALARM DITERIMA (25 DETIK)</text>
            <text x="70" y="32" fill="#34d399" font-size="10">Operator menekan ACK. Respons 25s &lt; 50% × 60s (Target Tercapai)</text>
          </g>

          <!-- Event 5 -->
          <g transform="translate(0, 200)">
            <text x="0" y="16" fill="#38bdf8" font-size="11" font-weight="700">00:01:45</text>
            <text x="70" y="16" fill="#ffffff" font-size="11" font-weight="600">INTERVENSI DOSIS KOAGULAN</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Operator menaikkan setpoint koagulan: 25 mg/L → 48 mg/L</text>
          </g>

          <!-- Event 6 -->
          <g transform="translate(0, 250)">
            <text x="0" y="16" fill="#a855f7" font-size="11" font-weight="700">00:02:30</text>
            <text x="70" y="16" fill="#ffffff" font-size="11" font-weight="600">PENGADUKAN CEPAT DINAIKKAN</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Kecepatan flash mixer disetel ke 100 RPM</text>
          </g>

          <!-- Event 7 -->
          <g transform="translate(0, 300)">
            <text x="0" y="16" fill="#38bdf8" font-size="11" font-weight="700">00:04:10</text>
            <text x="70" y="16" fill="#ffffff" font-size="11" font-weight="600">RESPONS PROSES FLOKULASI</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Flok mengendap optimal, kekeruhan filtrasi turun ke 2,1 NTU</text>
          </g>

          <!-- Event 8 -->
          <g transform="translate(0, 350)">
            <text x="0" y="16" fill="#10b981" font-size="11" font-weight="700">00:06:20</text>
            <text x="70" y="16" fill="#34d399" font-size="11" font-weight="700">AUTO-CLEAR ALARM SELESAI</text>
            <text x="70" y="32" fill="#34d399" font-size="10">Kekeruhan stabil 1,2 NTU (&lt;1,5 NTU). Alarm pulih otomatis</text>
          </g>

          <!-- Event 9 -->
          <g transform="translate(0, 400)">
            <text x="0" y="16" fill="#0284c7" font-size="11" font-weight="700">00:08:30</text>
            <text x="70" y="16" fill="#ffffff" font-size="11" font-weight="700">SIMULASI SELESAI DENGAN SUKSES</text>
            <text x="70" y="32" fill="#94a3b8" font-size="10">Skor Total: 88 · Komponen: Mutu 23/25, Waktu 25/25, Dosis 22/25, SOP 18/25</text>
          </g>
        </g>

        <!-- Export Log Button -->
        <g transform="translate(0, 520)">
          <rect width="656" height="38" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="328" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">Ekspor Berkas Audit Log (CSV / JSON)</text>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L12: MANAGE USERS & GROUPS ====================
def generate_l12():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Admin Lembaga · NUS", name="Admin Nusantara", initials="AN")
    title = page_title_block("Kelola Pengguna, Akun Demo &amp; Kelompok Belajar", "Manajemen Kursi Lisensi (FR-20) · Balai Diklat Air Minum Nusantara · Kuota: 46 / 50 Kursi Terpakai", 112)
    
    content = f"""{hdr}{title}
  <!-- Stats & License Bar (Height 86, Width 1856) -->
  <g transform="translate(32, 175)">
    <!-- Card 1: Kursi Lisensi -->
    <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">PENGGUNAAN KURSI LISENSI</text>
      <text x="0" y="44" fill="#38bdf8" font-size="24" font-weight="800">46 <tspan fill="#ffffff" font-size="18">/ 50 Kursi</tspan></text>
      <text x="210" y="44" fill="#34d399" font-size="12" font-weight="600">4 Kursi Tersedia (92%)</text>
    </g>

    <!-- Card 2: Peserta Aktif 14 Hari -->
    <g transform="translate(470, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">PESERTA AKTIF (LOGIN 14 HR TERAKHIR)</text>
        <text x="0" y="44" fill="#34d399" font-size="24" font-weight="800">42 Peserta</text>
        <text x="180" y="44" fill="#94a3b8" font-size="11.5">Dari 46 akun terdaftar</text>
      </g>
    </g>

    <!-- Card 3: Kelompok Terdaftar -->
    <g transform="translate(940, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">KELOMPOK BELAJAR AKTIF</text>
        <text x="0" y="44" fill="#ffffff" font-size="22" font-weight="800">2 Kelompok</text>
        <text x="160" y="44" fill="#cbd5e1" font-size="11.5">Angkatan 1 (24) &amp; Angkatan 2 (22)</text>
      </g>
    </g>

    <!-- Card 4: Action Buttons Restored -->
    <g transform="translate(1410, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(20, 22)">
        <rect width="190" height="42" rx="6" fill="#0284c7" />
        <text x="95" y="26" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">+ Tambah Pengguna</text>

        <rect x="205" y="0" width="190" height="42" rx="6" fill="#0f172a" stroke="#38bdf8" />
        <text x="300" y="26" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">📥 Impor CSV (FR-20)</text>
      </g>
    </g>
  </g>

  <!-- MAIN SECTION: LEFT = USERS TABLE (Width 1240), RIGHT = GROUP MANAGEMENT (Width 584) -->
  <g transform="translate(32, 275)">
    <!-- LEFT CARD: USERS TABLE -->
    <rect width="1240" height="765" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#ffffff" font-size="15" font-weight="700">Daftar Akun Pengguna Lembaga (10 Akun Demo PRD §5 + Peserta Contoh)</text>
      <text x="0" y="36" fill="#94a3b8" font-size="11.5">Menampilkan akun demo resmi PRD dan ringkasan 39 peserta contoh lainnya (Total 46 Akun Terpakai)</text>
      
      <!-- TABLE HEADER -->
      <g transform="translate(0, 52)">
        <rect width="1192" height="38" rx="6" fill="#0f172a" />
        <text x="20" y="24" fill="#64748b" font-size="11" font-weight="700">NAMA LENGKAP &amp; USERNAME</text>
        <text x="310" y="24" fill="#64748b" font-size="11" font-weight="700">PERAN (5 PERAN PRD)</text>
        <text x="490" y="24" fill="#64748b" font-size="11" font-weight="700">KELOMPOK</text>
        <text x="660" y="24" fill="#64748b" font-size="11" font-weight="700">TERAKHIR AKTIF</text>
        <text x="830" y="24" fill="#64748b" font-size="11" font-weight="700">STATUS</text>
        <text x="960" y="24" fill="#64748b" font-size="11" font-weight="700">AKSI AKUN (RESTORED)</text>
      </g>

      <!-- ROW 1: admin.nusantara -->
      <g transform="translate(0, 96)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Admin Nusantara <tspan fill="#38bdf8" font-size="10.5">(admin.nusantara)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">admin@nusantara.diklat.id</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#1e3a8a" />
        <text x="375" y="30" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Admin Lembaga</text>

        <text x="490" y="31" fill="#94a3b8" font-size="11">Pengelola Lembaga</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">Hari ini, 09:15</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <!-- Actions -->
        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 2: pimpinan.nusantara -->
      <g transform="translate(0, 154)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Ir. H. Bambang Sutrisno, M.Eng. <tspan fill="#38bdf8" font-size="10.5">(pimpinan.nusantara)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">kepala@nusantara.diklat.id</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#374151" />
        <text x="375" y="30" fill="#f3f4f6" font-size="10.5" font-weight="700" text-anchor="middle">Pimpinan Lembaga</text>

        <text x="490" y="31" fill="#94a3b8" font-size="11">Direksi Diklat</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">Kemarin, 14:20</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 3: instruktur.nusantara -->
      <g transform="translate(0, 212)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Budi Santoso, S.T. <tspan fill="#38bdf8" font-size="10.5">(instruktur.nusantara)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">instruktur@nusantara.diklat.id</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#164e63" />
        <text x="375" y="30" fill="#67e8f9" font-size="10.5" font-weight="700" text-anchor="middle">Instruktur</text>

        <text x="490" y="31" fill="#cbd5e1" font-size="11">Angkatan 1 &amp; 2</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">Hari ini, 08:30</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 4: peserta.lulus -->
      <g transform="translate(0, 270)">
        <rect width="1192" height="52" rx="6" fill="#1e293b" stroke="#f59e0b" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Andi Kurniawan <tspan fill="#fbbf24" font-size="10.5">(peserta.lulus)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">andi@peserta.nusantara.id · Piagam: SSA/NUS/2026/0001</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#581c87" />
        <text x="375" y="30" fill="#d8b4fe" font-size="10.5" font-weight="700" text-anchor="middle">Operator Ahli</text>

        <text x="490" y="31" fill="#cbd5e1" font-size="11">Angkatan 1</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">2 jam lalu</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Lulus ✓</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 5: peserta.ipa -->
      <g transform="translate(0, 328)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
        <text x="20" y="23" fill="#38bdf8" font-size="12" font-weight="700">Dimas Wahyu Pratama <tspan fill="#ffffff" font-size="10.5">(peserta.ipa)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">dimas@peserta.nusantara.id · Jalur IPA (7/9 Selesai)</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#1e3a8a" />
        <text x="375" y="30" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

        <text x="490" y="31" fill="#cbd5e1" font-size="11">Angkatan 2</text>
        <text x="660" y="31" fill="#34d399" font-size="11">Sedang Online</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 6: peserta.distribusi -->
      <g transform="translate(0, 386)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Siti Rahmawati <tspan fill="#38bdf8" font-size="10.5">(peserta.distribusi)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">siti@peserta.nusantara.id · Jalur Distribusi (5/7)</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#1e3a8a" />
        <text x="375" y="30" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

        <text x="490" y="31" fill="#cbd5e1" font-size="11">Angkatan 2</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">Kemarin</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 7: peserta.baru -->
      <g transform="translate(0, 444)">
        <rect width="1192" height="52" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="20" y="23" fill="#ffffff" font-size="12" font-weight="700">Budi Baru <tspan fill="#38bdf8" font-size="10.5">(peserta.baru)</tspan></text>
        <text x="20" y="39" fill="#94a3b8" font-size="10">budi.baru@peserta.nusantara.id · Baru Pre-test</text>

        <rect x="310" y="14" width="130" height="24" rx="4" fill="#334155" />
        <text x="375" y="30" fill="#94a3b8" font-size="10.5" font-weight="700" text-anchor="middle">Operator Magang</text>

        <text x="490" y="31" fill="#cbd5e1" font-size="11">Angkatan 2</text>
        <text x="660" y="31" fill="#cbd5e1" font-size="11">3 hari lalu</text>
        
        <rect x="830" y="15" width="65" height="22" rx="4" fill="#065f46" />
        <text x="862" y="30" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Aktif</text>

        <text x="960" y="31" fill="#38bdf8" font-size="11" font-weight="600">Ubah</text>
        <text x="1010" y="31" fill="#94a3b8" font-size="11">Reset</text>
        <text x="1070" y="31" fill="#64748b" font-size="11">Nonaktifkan</text>
      </g>

      <!-- ROW 8: SUMMARY ROW +39 PESERTA CONTOH (EXACT MATHEMATICAL TOTAL = 46) -->
      <g transform="translate(0, 502)">
        <rect width="1192" height="58" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="4,3" />
        <text x="20" y="26" fill="#38bdf8" font-size="13" font-weight="700">+ 39 Peserta Contoh Lainnya (Tercatat dalam Sistem)</text>
        <text x="20" y="44" fill="#94a3b8" font-size="11">Terbagi dalam: 22 Peserta di Angkatan 1 (Terpadu) dan 17 Peserta di Angkatan 2 (IPA/Distribusi)</text>
        
        <text x="560" y="35" fill="#ffffff" font-size="12" font-weight="600">35 Aktif · 4 Nonaktif</text>
        
        <rect x="760" y="16" width="140" height="26" rx="4" fill="#0f172a" stroke="#334155" />
        <text x="830" y="33" fill="#cbd5e1" font-size="10.5" font-weight="600" text-anchor="middle">Lihat Semua (46)</text>

        <text x="960" y="35" fill="#38bdf8" font-size="11" font-weight="600">Kelola Masal ▾</text>
      </g>

      <!-- TABLE FOOTER PAGINATION -->
      <g transform="translate(0, 580)">
        <text x="0" y="20" fill="#94a3b8" font-size="11.5">Menampilkan 7 akun demo utama + 39 peserta contoh (Total: 46 dari 50 kursi lisensi Balai Diklat Nusantara)</text>
      </g>
    </g>

    <!-- RIGHT CARD: GROUP MANAGEMENT (Width 584) -->
    <g transform="translate(1272, 0)">
      <rect width="584" height="765" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#ffffff" font-size="15" font-weight="700">Manajemen Kelompok Belajar (FR-20)</text>
        <text x="0" y="36" fill="#94a3b8" font-size="11.5">Pengelompokan siswa untuk penugasan modul dan pemantauan</text>
        <line x1="0" y1="52" x2="536" y2="52" stroke="#334155" />

        <!-- GROUP 1: Angkatan 2 - Operator IPA -->
        <g transform="translate(0, 70)">
          <rect width="536" height="135" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
          <g transform="translate(16, 18)">
            <text x="0" y="16" fill="#38bdf8" font-size="13" font-weight="700">Angkatan 2 - Operator IPA</text>
            <text x="0" y="36" fill="#cbd5e1" font-size="11.5">Jumlah Siswa: <tspan fill="#ffffff" font-weight="700">22 Peserta</tspan> (Termasuk Dimas, Siti, Budi Baru)</text>
            <text x="0" y="56" fill="#94a3b8" font-size="11">Instruktur Pengampu: <tspan fill="#ffffff">Budi Santoso, S.T.</tspan></text>
            <text x="0" y="76" fill="#94a3b8" font-size="11">Jalur Kurikulum: Jalur IPA (9 Misi) &amp; Distribusi (7 Misi)</text>

            <!-- Actions Restored -->
            <g transform="translate(0, 88)">
              <rect width="70" height="24" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="35" y="16" fill="#38bdf8" font-size="10.5" font-weight="600" text-anchor="middle">Ubah</text>

              <rect x="80" y="0" width="70" height="24" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="115" y="16" fill="#94a3b8" font-size="10.5" text-anchor="middle">Arsip</text>

              <text x="170" y="16" fill="#34d399" font-size="11" font-weight="600">✓ Aktif</text>
            </g>
          </g>
        </g>

        <!-- GROUP 2: Angkatan 1 - Operator Terpadu -->
        <g transform="translate(0, 225)">
          <rect width="536" height="135" rx="8" fill="#0f172a" stroke="#334155" />
          <g transform="translate(16, 18)">
            <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">Angkatan 1 - Operator Terpadu</text>
            <text x="0" y="36" fill="#cbd5e1" font-size="11.5">Jumlah Siswa: <tspan fill="#ffffff" font-weight="700">24 Peserta</tspan> (Termasuk Andi, Rian)</text>
            <text x="0" y="56" fill="#94a3b8" font-size="11">Instruktur Pengampu: <tspan fill="#ffffff">Budi Santoso, S.T.</tspan></text>
            <text x="0" y="76" fill="#94a3b8" font-size="11">Jalur Kurikulum: Jalur Terpadu 17 Misi (Kelulusan)</text>

            <g transform="translate(0, 88)">
              <rect width="70" height="24" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="35" y="16" fill="#38bdf8" font-size="10.5" font-weight="600" text-anchor="middle">Ubah</text>

              <rect x="80" y="0" width="70" height="24" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="115" y="16" fill="#94a3b8" font-size="10.5" text-anchor="middle">Arsip</text>

              <text x="170" y="16" fill="#34d399" font-size="11" font-weight="600">✓ Selesai / Arsip</text>
            </g>
          </g>
        </g>

        <!-- Create New Group Button Restored -->
        <g transform="translate(0, 380)">
          <rect width="536" height="44" rx="8" fill="#0284c7" />
          <text x="268" y="27" fill="#ffffff" font-size="12.5" font-weight="700" text-anchor="middle">+ Buat Kelompok Belajar Baru (FR-20)</text>
        </g>

        <!-- Group Policy Note -->
        <g transform="translate(0, 445)">
          <rect width="536" height="160" rx="8" fill="#1e293b" stroke="#334155" />
          <g transform="translate(18, 18)">
            <text x="0" y="16" fill="#38bdf8" font-size="11.5" font-weight="700">Aturan Lisensi Multi-Kelompok:</text>
            <text x="0" y="38" fill="#cbd5e1" font-size="11">• Siswa dapat dipindahkan antar-kelompok tanpa menghapus riwayat nilai dan XP.</text>
            <text x="0" y="58" fill="#cbd5e1" font-size="11">• Kelompok yang diarsipkan tidak mengurangi kuota lisensi jika akun siswa dinonaktifkan.</text>
            <text x="0" y="78" fill="#cbd5e1" font-size="11">• Papan peringkat (FR-21) dapat difilter per masing-masing kelompok belajar.</text>
          </g>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L13: TENANT SETTINGS ====================
def generate_l13():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Admin Lembaga · NUS", name="Admin Nusantara", initials="AN")
    title = page_title_block("Pengaturan Lembaga &amp; Standar Evaluasi", "Konfigurasi Bobot Skor, KKM, Logo Lembaga, Saklar Papan Peringkat (FR-21) &amp; Penanda Tangan", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Grid: Left = Scoring & KKM with SUB-CARDS (Width 960), Right = Branding & Signers (Width 864) -->
  <g transform="translate(32, 180)">
    <!-- LEFT CARD: SCORING & KKM (Width 960) -->
    <rect width="960" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(32, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Standar Ambang Kelulusan &amp; Bobot Komponen Evaluasi (PRD §8)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Kriteria kelulusan otomatis mesin simulasi SCADA SPAM untuk seluruh modul</text>
      <line x1="0" y1="56" x2="896" y2="56" stroke="#334155" stroke-width="1" />

      <!-- SECTION 1: 3 KKM SUB-CARDS FIXED (WRAPPED IN <g transform="translate(...)"> TO PREVENT TEXT OVERLAP) -->
      <g transform="translate(0, 75)">
        <text x="0" y="16" fill="#fbbf24" font-size="12.5" font-weight="700">AMBANG KELULUSAN (KKM) &amp; BINTANG KELAYAKAN:</text>
        
        <!-- CARD 1: Misi Latihan (70) -->
        <g transform="translate(0, 26)">
          <rect width="285" height="120" rx="8" fill="#0f172a" stroke="#334155" />
          <g transform="translate(16, 16)">
            <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">MISI LATIHAN (1★)</text>
            <text x="0" y="44" fill="#ffffff" font-size="24" font-weight="800">Skor ≥ 70</text>
            <text x="0" y="66" fill="#38bdf8" font-size="11">Syarat Bintang 1 (70–84)</text>
            <text x="0" y="82" fill="#64748b" font-size="10">Membuka skenario berikutnya</text>
          </g>
        </g>

        <!-- CARD 2: Misi Kelulusan Ujian (80) -->
        <g transform="translate(305, 26)">
          <rect width="285" height="120" rx="8" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
          <g transform="translate(16, 16)">
            <text x="0" y="16" fill="#fbbf24" font-size="11" font-weight="700">MISI KELULUSAN UJIAN (KKM)</text>
            <text x="0" y="44" fill="#fbbf24" font-size="24" font-weight="800">Skor ≥ 80</text>
            <text x="0" y="66" fill="#fbbf24" font-size="11">Syarat Terbit Piagam PRD §8</text>
            <text x="0" y="82" fill="#64748b" font-size="10">Ujian IPA-09 &amp; TRP-02</text>
          </g>
        </g>

        <!-- CARD 3: Predikat Bintang 3 (95) -->
        <g transform="translate(610, 26)">
          <rect width="286" height="120" rx="8" fill="#0f172a" stroke="#059669" stroke-width="1.5" />
          <g transform="translate(16, 16)">
            <text x="0" y="16" fill="#34d399" font-size="11" font-weight="700">PREDIKAT SANGAT BAIK (3★)</text>
            <text x="0" y="44" fill="#34d399" font-size="24" font-weight="800">Skor ≥ 95</text>
            <text x="0" y="66" fill="#34d399" font-size="11">Pencapaian Tertinggi</text>
            <text x="0" y="82" fill="#64748b" font-size="10">Syarat Lencana 3 Bintang</text>
          </g>
        </g>
      </g>

      <!-- SECTION 2: 4 COMPONENT WEIGHTS -->
      <g transform="translate(0, 255)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12.5" font-weight="700">BOBOT 4 KOMPONEN PENILAIAN OTOMATIS (PRD §8):</text>
        
        <!-- Comp 1: Stabilitas Mutu (30%) -->
        <g transform="translate(0, 30)">
          <rect width="896" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="20" y="31" fill="#ffffff" font-size="12" font-weight="700">1. Stabilitas Parameter Kualitas &amp; Tekanan Air</text>
          <rect x="740" y="12" width="70" height="28" rx="4" fill="#0284c7" />
          <text x="775" y="30" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">30%</text>
          <text x="825" y="31" fill="#94a3b8" font-size="11">Maks 30 Pts</text>
        </g>

        <!-- Comp 2: Kecepatan Respons (25%) -->
        <g transform="translate(0, 92)">
          <rect width="896" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="20" y="31" fill="#ffffff" font-size="12" font-weight="700">2. Kecepatan Respons Tanggap Darurat Alarm</text>
          <rect x="740" y="12" width="70" height="28" rx="4" fill="#0284c7" />
          <text x="775" y="30" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">25%</text>
          <text x="825" y="31" fill="#94a3b8" font-size="11">Maks 25 Pts</text>
        </g>

        <!-- Comp 3: Efisiensi Kimia & Energi (25%) -->
        <g transform="translate(0, 154)">
          <rect width="896" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="20" y="31" fill="#ffffff" font-size="12" font-weight="700">3. Efisiensi Penggunaan Bahan Kimia &amp; Energi Pompa</text>
          <rect x="740" y="12" width="70" height="28" rx="4" fill="#0284c7" />
          <text x="775" y="30" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">25%</text>
          <text x="825" y="31" fill="#94a3b8" font-size="11">Maks 25 Pts</text>
        </g>

        <!-- Comp 4: Prosedur Operasional Standar (20%) -->
        <g transform="translate(0, 216)">
          <rect width="896" height="52" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="20" y="31" fill="#ffffff" font-size="12" font-weight="700">4. Kepatuhan Urutan Prosedur Operasional Standar (SOP)</text>
          <rect x="740" y="12" width="70" height="28" rx="4" fill="#0284c7" />
          <text x="775" y="30" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">20%</text>
          <text x="825" y="31" fill="#94a3b8" font-size="11">Maks 20 Pts</text>
        </g>
      </g>

      <!-- SECTION 3: PENALTY & HINT CONFIG -->
      <g transform="translate(0, 560)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12.5" font-weight="700">PENGURANG NILAI PETUNJUK &amp; REMEDIAL:</text>
        <rect x="0" y="26" width="896" height="90" rx="6" fill="#0f172a" stroke="#334155" />
        <g transform="translate(20, 20)">
          <text x="0" y="16" fill="#cbd5e1" font-size="11.5">• Penalti Tombol Petunjuk: <tspan fill="#f87171" font-weight="700">−5 Poin per klik</tspan> (Nonaktifkan di Misi Kelulusan Ujian).</text>
          <text x="0" y="38" fill="#cbd5e1" font-size="11.5">• Kesempatan Remedial: <tspan fill="#38bdf8" font-weight="700">Tidak terbatas</tspan> (Sistem mencatat skor tertinggi untuk piagam).</text>
          <text x="0" y="58" fill="#cbd5e1" font-size="11.5">• Pengali XP: Diatur otomatis oleh tingkat kesulitan skenario PRD §7 (1,0x s/d 3,0x).</text>
        </g>
      </g>

      <!-- Save Button -->
      <g transform="translate(0, 710)">
        <rect width="220" height="44" rx="8" fill="#0284c7" />
        <text x="110" y="27" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Simpan Konfigurasi</text>
      </g>
    </g>

    <!-- RIGHT CARD: BRANDING, LEADERBOARD TOGGLE & SIGNERS (Width 864) -->
    <g transform="translate(992, 0)">
      <rect width="864" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(28, 26)">
        <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Identitas Lembaga, Logo &amp; Tanda Tangan Piagam</text>
        <text x="0" y="40" fill="#94a3b8" font-size="12">Informasi resmi yang tercetak pada sertifikat piagam kelulusan (PRD §6)</text>
        <line x1="0" y1="56" x2="808" y2="56" stroke="#334155" stroke-width="1" />

        <!-- 1. UPLOAD LOGO LEMBAGA RESTORED -->
        <g transform="translate(0, 70)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">LOGO RESMI LEMBAGA (PNG / SVG MAKS 2MB):</text>
          <rect x="0" y="26" width="808" height="110" rx="8" fill="#0f172a" stroke="#334155" />
          <g transform="translate(20, 20)">
            <!-- Preview Logo Nusantara -->
            <circle cx="35" cy="35" r="30" fill="#0284c7" />
            <path d="M35 15 C35 15 23 30 23 38 C23 45 28 50 35 50 C42 50 47 45 47 38 C47 30 35 15 35 15 Z" fill="#ffffff" />
            
            <text x="85" y="26" fill="#ffffff" font-size="13" font-weight="700">logo_balai_diklat_nusantara.svg</text>
            <text x="85" y="46" fill="#34d399" font-size="11">✓ Terunggah &amp; Digunakan di Header serta Piagam Resmi</text>
            
            <rect x="620" y="18" width="150" height="34" rx="6" fill="#1e293b" stroke="#38bdf8" />
            <text x="695" y="39" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">Ganti Logo...</text>
          </g>
        </g>

        <!-- 2. SAKLAR PAPAN PERINGKAT FR-21 RESTORED -->
        <g transform="translate(0, 215)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">PRIVASI &amp; PAPAN PERINGKAT ANTAR-PESERTA (FR-21):</text>
          <rect x="0" y="26" width="808" height="90" rx="8" fill="#0f172a" stroke="#334155" />
          <g transform="translate(20, 20)">
            <text x="0" y="20" fill="#ffffff" font-size="13" font-weight="700">Tampilkan Papan Peringkat Kompetensi Peserta</text>
            <text x="0" y="40" fill="#94a3b8" font-size="11">Aktifkan gamifikasi peringkat antar-peserta dalam lembaga Balai Diklat Nusantara</text>

            <!-- Toggle Switch ON -->
            <rect x="680" y="10" width="80" height="32" rx="16" fill="#0284c7" />
            <circle cx="736" cy="26" r="12" fill="#ffffff" />
            <text x="702" y="30" fill="#ffffff" font-size="10" font-weight="800">ON</text>
          </g>
        </g>

        <!-- 3. PENANDA TANGAN PIAGAM RESTORED -->
        <g transform="translate(0, 340)">
          <text x="0" y="16" fill="#fbbf24" font-size="12" font-weight="700">PENANDA TANGAN PIAGAM KELULUSAN RESMI (PRD §6):</text>
          
          <!-- Signer 1: Instruktur Penilai -->
          <g transform="translate(0, 26)">
            <rect width="808" height="95" rx="8" fill="#0f172a" stroke="#334155" />
            <g transform="translate(16, 16)">
              <text x="0" y="16" fill="#38bdf8" font-size="11.5" font-weight="700">1. INSTRUKTUR PENILAI / PENGUJI:</text>
              <text x="0" y="40" fill="#ffffff" font-size="13" font-weight="700">Budi Santoso, S.T.</text>
              <text x="0" y="58" fill="#94a3b8" font-size="11">Jabatan: Instruktur Utama SPAM · NIP: 19820412 200801 1 005</text>
              <rect x="680" y="16" width="100" height="30" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="730" y="35" fill="#cbd5e1" font-size="11" text-anchor="middle">Ubah Data</text>
            </g>
          </g>

          <!-- Signer 2: Kepala Lembaga -->
          <g transform="translate(0, 135)">
            <rect width="808" height="95" rx="8" fill="#0f172a" stroke="#334155" />
            <g transform="translate(16, 16)">
              <text x="0" y="16" fill="#38bdf8" font-size="11.5" font-weight="700">2. PIMPINAN / KEPALA LEMBAGA DIKLAT:</text>
              <text x="0" y="40" fill="#ffffff" font-size="13" font-weight="700">Ir. H. Bambang Sutrisno, M.Eng.</text>
              <text x="0" y="58" fill="#94a3b8" font-size="11">Jabatan: Kepala Balai Diklat Air Minum Nusantara · NIP: 19710815 199603 1 002</text>
              <rect x="680" y="16" width="100" height="30" rx="4" fill="#1e293b" stroke="#334155" />
              <text x="730" y="35" fill="#cbd5e1" font-size="11" text-anchor="middle">Ubah Data</text>
            </g>
          </g>
        </g>

        <!-- Preview Button -->
        <g transform="translate(0, 600)">
          <rect width="808" height="50" rx="8" fill="#1e293b" stroke="#f59e0b" />
          <g transform="translate(20, 15)">
            <text x="0" y="20" fill="#fbbf24" font-size="12" font-weight="700">Lihat Contoh Piagam Sesuai Pengaturan Ini →</text>
            <rect x="640" y="0" width="140" height="32" rx="6" fill="#f59e0b" />
            <text x="710" y="20" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">Pratinjau (L8)</text>
          </g>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L14: TENANT EVALUATION ====================
def generate_l14():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Pimpinan Lembaga · NUS", name="Ir. H. Bambang Sutrisno, M.Eng.", initials="BS")
    title = page_title_block("Evaluasi &amp; Utilisasi Lembaga Diklat SPAM", "Dashboard Eksekutif Target Keberhasilan (PRD §3 Target T1–T4) · 42 Peserta Aktif (Login 14 Hari)", 112)
    
    content = f"""{hdr}{title}
  <!-- 4 Target KPI Cards PRD §3 (Height 130, Width 1856) -->
  <g transform="translate(32, 175)">
    <!-- TARGET T1: PRE-TO-POST IMPROVEMENT -->
    <rect width="446" height="130" rx="10" fill="url(#cardGrad)" stroke="#10b981" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#34d399" font-size="12" font-weight="700">TARGET T1: PENINGKATAN PRE-TO-POST</text>
      <text x="0" y="46" fill="#ffffff" font-size="28" font-weight="800">+50,5%</text>
      <rect x="140" y="28" width="90" height="24" rx="4" fill="#065f46" />
      <text x="185" y="44" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">TARGET: ≥25%</text>
      <text x="0" y="76" fill="#cbd5e1" font-size="11">Rata-rata Pre-Test: <tspan fill="#ffffff" font-weight="600">54,2</tspan> → Post-Test: <tspan fill="#34d399" font-weight="700">81,6</tspan></text>
      <text x="0" y="94" fill="#94a3b8" font-size="10.5">Kenaikan riil +27,4 poin · Seluruh 42 peserta aktif</text>
    </g>

    <!-- TARGET T2: MISSION COMPLETION RATE -->
    <g transform="translate(470, 0)">
      <rect width="446" height="130" rx="10" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">TARGET T2: PENYELESAIAN MISI JALUR</text>
        <text x="0" y="46" fill="#ffffff" font-size="28" font-weight="800">83,3%</text>
        <rect x="120" y="28" width="90" height="24" rx="4" fill="#0369a1" />
        <text x="165" y="44" fill="#bae6fd" font-size="11" font-weight="700" text-anchor="middle">TARGET: ≥70%</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11"><tspan fill="#34d399" font-weight="700">35 dari 42</tspan> peserta aktif menyelesaikan ≥80% misi</text>
        <text x="0" y="94" fill="#94a3b8" font-size="10.5">Sisa 7 peserta masih menyelesaikan modul latihan</text>
      </g>
    </g>

    <!-- TARGET T3: EMERGENCY RESPONSE TIME -->
    <g transform="translate(940, 0)">
      <rect width="446" height="130" rx="10" fill="url(#cardGrad)" stroke="#f59e0b" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#fbbf24" font-size="12" font-weight="700">TARGET T3: WAKTU TANGGAP DARURAT</text>
        <text x="0" y="46" fill="#ffffff" font-size="28" font-weight="800">28,4 dtk</text>
        <rect x="145" y="28" width="90" height="24" rx="4" fill="#78350f" />
        <text x="190" y="44" fill="#fde68a" font-size="11" font-weight="700" text-anchor="middle">TARGET: &lt;45s</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11">Rata-rata respons alarm pertama pada skenario gangguan</text>
        <text x="0" y="94" fill="#94a3b8" font-size="10.5">Contoh: Dimas Wahyu 25 dtk pada skenario IPA-06</text>
      </g>
    </g>

    <!-- TARGET T4: GRADUATION / CERTIFICATION PASS RATE -->
    <g transform="translate(1410, 0)">
      <rect width="446" height="130" rx="10" fill="url(#cardGrad)" stroke="#a855f7" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#c084fc" font-size="12" font-weight="700">TARGET T4: TINGKAT KELULUSAN (KKM ≥80)</text>
        <text x="0" y="46" fill="#ffffff" font-size="28" font-weight="800">76,2%</text>
        <rect x="120" y="28" width="90" height="24" rx="4" fill="#581c87" />
        <text x="165" y="44" fill="#e9d5ff" font-size="11" font-weight="700" text-anchor="middle">TARGET: ≥60%</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11"><tspan fill="#34d399" font-weight="700">32 dari 42</tspan> peserta aktif memenuhi ambang skor ≥80</text>
        <text x="0" y="94" fill="#94a3b8" font-size="10.5">Piagam resmi terbit &amp; siap diterbitkan bagi peserta lulus</text>
      </g>
    </g>
  </g>

  <!-- SPLIT CHARTS: LEFT = COMPETENCY BY EQUIPMENT (Width 960), RIGHT = LICENSE UTILIZATION (Width 864) -->
  <g transform="translate(32, 325)">
    <!-- LEFT CARD: COMPETENCY DOMAIN PERFORMANCE -->
    <rect width="960" height="715" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(28, 24)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Penguasaan Kompetensi Berdasarkan Titik Kontrol (PRD §9)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Rata-rata performa 42 peserta aktif pada masing-masing unit operasi SPAM</text>
      <line x1="0" y1="56" x2="904" y2="56" stroke="#334155" />

      <!-- Domain 1: Koagulasi & Jar-test Dosing -->
      <g transform="translate(0, 80)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="600">1. Pengendalian Dosis Koagulan &amp; Penyesuai pH (Flash Mixing)</text>
        <text x="780" y="16" fill="#34d399" font-size="14" font-weight="700">89,2%</text>
        <rect x="0" y="28" width="904" height="14" rx="7" fill="#0f172a" />
        <rect x="0" y="28" width="806" height="14" rx="7" fill="#10b981" />
        <text x="0" y="58" fill="#94a3b8" font-size="11">Rata-rata akurasi dosis kimia terhadap lonjakan kekeruhan air baku</text>
      </g>

      <!-- Domain 2: Filtrasi & Backwash -->
      <g transform="translate(0, 160)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="600">2. Filtrasi Pasir Cepat &amp; Prosedur Pencucian Balik (Backwash)</text>
        <text x="780" y="16" fill="#38bdf8" font-size="14" font-weight="700">84,6%</text>
        <rect x="0" y="28" width="904" height="14" rx="7" fill="#0f172a" />
        <rect x="0" y="28" width="765" height="14" rx="7" fill="#0284c7" />
        <text x="0" y="58" fill="#94a3b8" font-size="11">Ketepatan waktu backwash saat headloss tinggi atau kekeruhan filtrasi mendekati 1,5 NTU</text>
      </g>

      <!-- Domain 3: Desinfeksi Klorinasi -->
      <g transform="translate(0, 240)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="600">3. Injeksi Klor &amp; Pemantauan Sisa Klor Bebas (Reservoir &amp; Jaringan)</text>
        <text x="780" y="16" fill="#38bdf8" font-size="14" font-weight="700">86,1%</text>
        <rect x="0" y="28" width="904" height="14" rx="7" fill="#0f172a" />
        <rect x="0" y="28" width="778" height="14" rx="7" fill="#0284c7" />
        <text x="0" y="58" fill="#94a3b8" font-size="11">Kepatuhan ambang Permenkes: 0,2–0,5 mg/L di ujung jaringan distribusi</text>
      </g>

      <!-- Domain 4: Manajemen Pompa Distribusi & PRV -->
      <g transform="translate(0, 320)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="600">4. Manajemen Tekanan Pompa Distribusi &amp; Valve PRV (Jalur Distribusi)</text>
        <text x="780" y="16" fill="#fbbf24" font-size="14" font-weight="700">74,8%</text>
        <rect x="0" y="28" width="904" height="14" rx="7" fill="#0f172a" />
        <rect x="0" y="28" width="676" height="14" rx="7" fill="#f59e0b" />
        <text x="0" y="58" fill="#94a3b8" font-size="11">Perlu penguatan pada mitigasi water hammer dan isolasi zona kebocoran</text>
      </g>

      <!-- Executive Recommendations Box -->
      <g transform="translate(0, 420)">
        <rect width="904" height="230" rx="8" fill="#0f172a" stroke="#334155" />
        <g transform="translate(20, 20)">
          <text x="0" y="16" fill="#fbbf24" font-size="13" font-weight="700">Rekomendasi Strategis untuk Pimpinan Lembaga Diklat:</text>
          <text x="0" y="42" fill="#cbd5e1" font-size="11.5">1. <tspan fill="#ffffff" font-weight="600">Tingkat Utilisasi Tinggi (92% Kursi):</tspan> Dari 50 kuota lisensi, 46 telah terdaftar dengan 42 peserta aktif login dalam 14 hari terakhir.</text>
          <text x="0" y="66" fill="#cbd5e1" font-size="11.5">2. <tspan fill="#34d399" font-weight="600">Seluruh KPI PRD §3 Terpenuhi:</tspan> Peningkatan Pre-to-Post (+50,5%), penyelesaian misi (83,3%), dan kelulusan (76,2%) melampaui target minimum.</text>
          <text x="0" y="90" fill="#cbd5e1" font-size="11.5">3. <tspan fill="#38bdf8" font-weight="600">Rencana Pembukaan Angkatan 3:</tspan> Sisa 4 kursi lisensi dapat dialokasikan segera untuk peserta baru, atau upgrade kuota lisensi ke 100 kursi.</text>
          <text x="0" y="114" fill="#cbd5e1" font-size="11.5">4. <tspan fill="#cbd5e1" font-weight="600">Kesiapan Sertifikasi:</tspan> Sebanyak 32 peserta telah lulus KKM dan siap menerima Piagam Kelulusan resmi.</text>
        </g>
      </g>
    </g>

    <!-- RIGHT CARD: LICENSE UTILIZATION & MONTHLY TREND (Width 864) -->
    <g transform="translate(992, 0)">
      <rect width="864" height="715" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(28, 24)">
        <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Utilisasi Lisensi Lembaga &amp; Tren Aktivitas Bulanan</text>
        <text x="0" y="40" fill="#94a3b8" font-size="12">Kesesuaian kuota 50 kursi lisensi Balai Diklat Air Minum Nusantara</text>
        <line x1="0" y1="56" x2="808" y2="56" stroke="#334155" />

        <!-- License Ring & Breakdown -->
        <g transform="translate(0, 75)">
          <rect width="808" height="150" rx="8" fill="#0f172a" stroke="#334155" />
          <g transform="translate(30, 25)">
            <!-- Circular Progress Representation -->
            <circle cx="50" cy="50" r="42" fill="none" stroke="#1e293b" stroke-width="14" />
            <circle cx="50" cy="50" r="42" fill="none" stroke="#0284c7" stroke-width="14" stroke-dasharray="242 264" />
            <text x="50" y="56" fill="#ffffff" font-size="18" font-weight="800" text-anchor="middle">92%</text>

            <g transform="translate(130, 10)">
              <text x="0" y="16" fill="#ffffff" font-size="15" font-weight="700">Paket Lisensi Lembaga: 50 Kursi (Aktif)</text>
              <text x="0" y="38" fill="#cbd5e1" font-size="12">• Kursi Terdaftar: <tspan fill="#38bdf8" font-weight="700">46 Kursi</tspan> (42 Peserta Aktif 14 hr + 4 Akun Staf/Penguji)</text>
              <text x="0" y="58" fill="#cbd5e1" font-size="12">• Kursi Tersedia: <tspan fill="#34d399" font-weight="700">4 Kursi Kosong</tspan> (Dapat ditambahkan sewaktu-waktu)</text>
              <text x="0" y="78" fill="#94a3b8" font-size="11">Masa Berlaku Lisensi: <tspan fill="#ffffff">Hingga 31 Desember 2026</tspan> (Paket Lengkap: IPA + DST + Terpadu)</text>
            </g>
          </g>
        </g>

        <!-- Monthly Simulation Activity Graph -->
        <g transform="translate(0, 245)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12.5" font-weight="700">TREN SESI SIMULASI PER BULAN (TOTAL 1.480 SESI):</text>
          <rect x="0" y="28" width="808" height="240" rx="8" fill="#0f172a" stroke="#334155" />
          
          <!-- Simulated Bar Graph -->
          <g transform="translate(60, 50)">
            <!-- Bar 1: Nov 2025 -->
            <rect x="0" y="90" width="60" height="70" rx="4" fill="#334155" />
            <text x="30" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">180</text>
            <text x="30" y="180" fill="#64748b" font-size="10" text-anchor="middle">Nov 25</text>

            <!-- Bar 2: Des 2025 -->
            <rect x="120" y="60" width="60" height="100" rx="4" fill="#334155" />
            <text x="150" y="50" fill="#94a3b8" font-size="11" text-anchor="middle">290</text>
            <text x="150" y="180" fill="#64748b" font-size="10" text-anchor="middle">Des 25</text>

            <!-- Bar 3: Jan 2026 -->
            <rect x="240" y="40" width="60" height="120" rx="4" fill="#0369a1" />
            <text x="270" y="30" fill="#38bdf8" font-size="11" text-anchor="middle">380</text>
            <text x="270" y="180" fill="#64748b" font-size="10" text-anchor="middle">Jan 26</text>

            <!-- Bar 4: Feb 2026 -->
            <rect x="360" y="20" width="60" height="140" rx="4" fill="#0284c7" />
            <text x="390" y="10" fill="#38bdf8" font-size="11" text-anchor="middle">450</text>
            <text x="390" y="180" fill="#64748b" font-size="10" text-anchor="middle">Feb 26</text>

            <!-- Bar 5: Mar 2026 (Ongoing) -->
            <rect x="480" y="50" width="60" height="110" rx="4" fill="#34d399" />
            <text x="510" y="40" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">180*</text>
            <text x="510" y="180" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Mar 26</text>
          </g>
        </g>

        <!-- Executive Export Button -->
        <g transform="translate(0, 520)">
          <rect width="808" height="50" rx="8" fill="#0284c7" />
          <text x="404" y="31" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Unduh Laporan Evaluasi Eksekutif (PDF / XLSX)</text>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L15: SUPER ADMIN ====================
def generate_l15():
    # Super Admin Custom Header
    hdr = f"""  <!-- Super Admin Header -->
  <g transform="translate(32, 24)">
    <rect width="1856" height="64" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    <circle cx="44" cy="32" r="20" fill="#6366f1" />
    <text x="44" y="38" fill="#ffffff" font-size="16" font-weight="800" text-anchor="middle">SA</text>
    <text x="76" y="28" fill="#ffffff" font-size="16" font-weight="700">SimSCADA-Air Portal Super Admin Multi-Tenant</text>
    <text x="76" y="46" fill="#a5b4fc" font-size="11" font-weight="500">Platform Management System · <tspan fill="#64748b">Mode Pengelola Pusat</tspan></text>
    
    <g transform="translate(1520, 14)">
      <rect width="304" height="36" rx="18" fill="#1e293b" stroke="#334155" />
      <circle cx="20" cy="18" r="14" fill="#4338ca" />
      <text x="20" y="22" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">SA</text>
      <text x="44" y="23" fill="#f8fafc" font-size="12" font-weight="600">Super Administrator</text>
      <rect x="210" y="8" width="82" height="20" rx="10" fill="#b91c1c" />
      <text x="251" y="22" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">KELUAR</text>
    </g>
  </g>"""

    # Title block positioned at y=112 to prevent any collision
    title = page_title_block("Manajemen Tenant Multi-Lembaga &amp; Alokasi Lisensi", "Pengawasan Kuota Lembaga Diklat SPAM · Isolasi Database (FR-21) · Paket Jalur Nusantara = IPA + Distribusi + Terpadu", 112)
    
    content = f"""{hdr}{title}
  <!-- Stats Bar Super Admin (Height 86, Width 1856, Positioned at y=175) -->
  <g transform="translate(32, 175)">
    <!-- Card 1: Total Tenants -->
    <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">TOTAL LEMBAGA (TENANT)</text>
      <text x="0" y="44" fill="#ffffff" font-size="24" font-weight="800">2 Lembaga <tspan fill="#34d399" font-size="13">Aktif</tspan></text>
      <text x="180" y="44" fill="#cbd5e1" font-size="11.5">NUS (50) &amp; TRM (50)</text>
    </g>

    <!-- Card 2: Total Kursi Terdistribusi -->
    <g transform="translate(470, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#6366f1" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#a5b4fc" font-size="11.5" font-weight="600">TOTAL ALOKASI KURSI LISENSI</text>
        <text x="0" y="44" fill="#818cf8" font-size="24" font-weight="800">100 Kursi</text>
        <text x="160" y="44" fill="#34d399" font-size="11.5">64 Terpakai (64,0%)</text>
      </g>
    </g>

    <!-- Card 3: Peserta Aktif Platform -->
    <g transform="translate(940, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">PESERTA AKTIF (14 HR TERAKHIR)</text>
        <text x="0" y="44" fill="#ffffff" font-size="24" font-weight="800">58 Peserta</text>
        <text x="160" y="44" fill="#cbd5e1" font-size="11.5">42 Nusantara · 16 Tirta</text>
      </g>
    </g>

    <!-- Card 4: Action Add Tenant -->
    <g transform="translate(1410, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 22)">
        <rect width="398" height="42" rx="8" fill="#4f46e5" />
        <text x="199" y="26" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">+ Tambah Lembaga Baru (Onboarding Tenant)</text>
      </g>
    </g>
  </g>

  <!-- MAIN TENANT LIST (Width 1856, Height 765) -->
  <g transform="translate(32, 275)">
    <rect width="1856" height="765" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#ffffff" font-size="16" font-weight="700">Daftar Tenant Lembaga Pelatihan SPAM Terdaftar (PRD §5)</text>
      <text x="0" y="36" fill="#94a3b8" font-size="12">Pengaturan isolasi database per tenant, alokasi paket jalur pelatihan, dan kuota lisensi</text>
      
      <!-- TENANT 1: BALAI DIKLAT AIR MINUM NUSANTARA (NUS) -->
      <g transform="translate(0, 56)">
        <rect width="1808" height="280" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
        <g transform="translate(24, 20)">
          <!-- Tenant Header -->
          <circle cx="30" cy="30" r="26" fill="#0284c7" />
          <path d="M30 14 C30 14 20 26 20 32 C20 38 24.5 42 30 42 C35.5 42 40 38 40 32 C40 26 30 14 30 14 Z" fill="#ffffff" />
          
          <text x="70" y="24" fill="#ffffff" font-size="16" font-weight="800">Balai Diklat Air Minum Nusantara</text>
          <text x="70" y="44" fill="#38bdf8" font-size="12" font-weight="600">Kode Tenant: <tspan fill="#ffffff">NUS</tspan> · Domain: nusantara.simscada.id · Database ID: db_tenant_nusantara</text>

          <rect x="1650" y="10" width="120" height="32" rx="6" fill="#065f46" />
          <text x="1710" y="30" fill="#34d399" font-size="11.5" font-weight="700" text-anchor="middle">STATUS: AKTIF</text>

          <line x1="0" y1="65" x2="1760" y2="65" stroke="#1e293b" />

          <!-- Details 4 Columns -->
          <g transform="translate(0, 85)">
            <!-- Col 1: License Seats -->
            <g transform="translate(0, 0)">
              <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">KUOTA KURSI LISENSI</text>
              <text x="0" y="42" fill="#38bdf8" font-size="22" font-weight="800">46 <tspan fill="#ffffff" font-size="16">/ 50 Terpakai</tspan></text>
              <text x="0" y="64" fill="#34d399" font-size="11">42 Peserta Aktif (14 hr terakhir)</text>
              <text x="0" y="80" fill="#64748b" font-size="10.5">Sisa 4 kursi lisensi tersedia</text>
            </g>

            <!-- Col 2: Package Track PRD REQUIREMENT: IPA + DISTRIBUSI + TERPADU -->
            <g transform="translate(380, 0)">
              <text x="0" y="16" fill="#f59e0b" font-size="11" font-weight="700">PAKET JALUR TERBUKA (PRD REVISI §7):</text>
              <rect x="0" y="26" width="360" height="32" rx="6" fill="#1e293b" stroke="#f59e0b" />
              <text x="180" y="47" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">IPA + DISTRIBUSI + TERPADU (3 JALUR)</text>
              <text x="0" y="76" fill="#cbd5e1" font-size="11">Total 17 Misi Termasuk TRP-01 &amp; TRP-02</text>
            </g>

            <!-- Col 3: Admin & Signers -->
            <g transform="translate(800, 0)">
              <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">PENGELOLA UTAMA</text>
              <text x="0" y="38" fill="#ffffff" font-size="12" font-weight="600">Admin: <tspan fill="#38bdf8">admin.nusantara</tspan></text>
              <text x="0" y="58" fill="#ffffff" font-size="12" font-weight="600">Pimpinan: <tspan fill="#cbd5e1">Ir. H. Bambang Sutrisno, M.Eng.</tspan></text>
              <text x="0" y="78" fill="#ffffff" font-size="12" font-weight="600">Instruktur: <tspan fill="#cbd5e1">Budi Santoso, S.T.</tspan></text>
            </g>

            <!-- Col 4: Action Buttons -->
            <g transform="translate(1360, 0)">
              <rect width="180" height="36" rx="6" fill="#0284c7" />
              <text x="90" y="23" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Kelola Lisensi &amp; Kursi</text>

              <rect x="200" y="0" width="180" height="36" rx="6" fill="#1e293b" stroke="#334155" />
              <text x="290" y="23" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Masuk Sebagai Tenant</text>

              <rect x="0" y="48" width="380" height="36" rx="6" fill="#0f172a" stroke="#475569" />
              <text x="190" y="71" fill="#94a3b8" font-size="11" text-anchor="middle">Lihat Log Audit &amp; Backup Data (FR-21)</text>
            </g>
          </g>
        </g>
      </g>

      <!-- TENANT 2: PUSAT PELATIHAN TIRTA MANDIRI (TRM) -->
      <g transform="translate(0, 360)">
        <rect width="1808" height="280" rx="10" fill="#0f172a" stroke="#334155" />
        <g transform="translate(24, 20)">
          <!-- Tenant Header -->
          <circle cx="30" cy="30" r="26" fill="#0d9488" />
          <path d="M30 14 C30 14 20 26 20 32 C20 38 24.5 42 30 42 C35.5 42 40 38 40 32 C40 26 30 14 30 14 Z" fill="#ffffff" />
          
          <text x="70" y="24" fill="#ffffff" font-size="16" font-weight="800">Pusat Pelatihan Tirta Mandiri</text>
          <text x="70" y="44" fill="#2dd4bf" font-size="12" font-weight="600">Kode Tenant: <tspan fill="#ffffff">TRM</tspan> · Domain: tirtamandiri.simscada.id · Database ID: db_tenant_tirtamandiri</text>

          <rect x="1650" y="10" width="120" height="32" rx="6" fill="#065f46" />
          <text x="1710" y="30" fill="#34d399" font-size="11.5" font-weight="700" text-anchor="middle">STATUS: AKTIF</text>

          <line x1="0" y1="65" x2="1760" y2="65" stroke="#1e293b" />

          <!-- Details 4 Columns -->
          <g transform="translate(0, 85)">
            <!-- Col 1: License Seats -->
            <g transform="translate(0, 0)">
              <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">KUOTA KURSI LISENSI</text>
              <text x="0" y="42" fill="#2dd4bf" font-size="22" font-weight="800">18 <tspan fill="#ffffff" font-size="16">/ 50 Terpakai</tspan></text>
              <text x="0" y="64" fill="#34d399" font-size="11">16 Peserta Aktif (14 hr terakhir)</text>
              <text x="0" y="80" fill="#64748b" font-size="10.5">Sisa 32 kursi lisensi tersedia</text>
            </g>

            <!-- Col 2: Package Track: IPA + DISTRIBUSI -->
            <g transform="translate(380, 0)">
              <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">PAKET JALUR TERBUKA:</text>
              <rect x="0" y="26" width="360" height="32" rx="6" fill="#1e293b" stroke="#334155" />
              <text x="180" y="47" fill="#2dd4bf" font-size="12" font-weight="700" text-anchor="middle">IPA + DISTRIBUSI (2 JALUR)</text>
              <text x="0" y="76" fill="#cbd5e1" font-size="11">Jalur Terpadu Tidak Termasuk Paket Lisensi</text>
            </g>

            <!-- Col 3: Admin & Signers -->
            <g transform="translate(800, 0)">
              <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">PENGELOLA UTAMA</text>
              <text x="0" y="38" fill="#ffffff" font-size="12" font-weight="600">Admin: <tspan fill="#2dd4bf">admin.tirta</tspan></text>
              <text x="0" y="58" fill="#ffffff" font-size="12" font-weight="600">Peserta Demo: <tspan fill="#cbd5e1">peserta.tirta</tspan></text>
              <text x="0" y="78" fill="#64748b" font-size="11">1 Kelompok Belajar Aktif</text>
            </g>

            <!-- Col 4: Action Buttons -->
            <g transform="translate(1360, 0)">
              <rect width="180" height="36" rx="6" fill="#0d9488" />
              <text x="90" y="23" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Kelola Lisensi &amp; Kursi</text>

              <rect x="200" y="0" width="180" height="36" rx="6" fill="#1e293b" stroke="#334155" />
              <text x="290" y="23" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Masuk Sebagai Tenant</text>

              <rect x="0" y="48" width="380" height="36" rx="6" fill="#0f172a" stroke="#475569" />
              <text x="190" y="71" fill="#94a3b8" font-size="11" text-anchor="middle">Lihat Log Audit &amp; Backup Data (FR-21)</text>
            </g>
          </g>
        </g>
      </g>

      <!-- Footer Info -->
      <g transform="translate(0, 660)">
        <text x="20" y="24" fill="#94a3b8" font-size="11.5">Kebijakan Multi-Tenant SimSCADA-Air: Setiap tenant memiliki skema database terisolasi penuh, aturan KKM mandiri, dan papan peringkat terisolasi (FR-21).</text>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L16: PUBLIC VERIFICATION ====================
def generate_l16():
    # Public Portal Header (No trainee login, public standalone page)
    hdr = f"""  <!-- Public Verification Header -->
  <g transform="translate(32, 24)">
    <rect width="1856" height="64" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    <circle cx="44" cy="32" r="20" fill="#0284c7" />
    <path d="M44 18 C44 18 34 29 34 35 C34 40.5 38.5 45 44 45 C49.5 45 54 40.5 54 35 C54 29 44 18 44 18 Z" fill="#ffffff" />
    <text x="76" y="28" fill="#ffffff" font-size="16" font-weight="700">Portal Publik Verifikasi Piagam Kelulusan SimSCADA-Air</text>
    <text x="76" y="46" fill="#38bdf8" font-size="11" font-weight="500">Layanan Otentikasi Sertifikat Operator SCADA SPAM · <tspan fill="#64748b">Akses Terbuka untuk Industri &amp; Publik</tspan></text>
    
    <g transform="translate(1550, 14)">
      <rect width="270" height="36" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="135" y="23" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Kembali ke Halaman Login (L1)</text>
    </g>
  </g>"""

    # Title block positioned at y=112 to eliminate any header collision
    title = page_title_block("Verifikasi Keaslian Piagam Kelulusan Operator", "Pemeriksaan Validitas Sertifikat Resmi Balai Diklat Air Minum Nusantara · Data Terotentikasi", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Verification Card (Width 1400, Centered at x=260, Positioned at y=175) -->
  <g transform="translate(260, 175)">
    <rect width="1400" height="865" rx="16" fill="url(#cardGrad)" stroke="#10b981" stroke-width="2" />
    <g transform="translate(40, 30)">
      
      <!-- SUCCESS VALIDATION BANNER -->
      <rect width="1320" height="60" rx="8" fill="#065f46" stroke="#10b981" stroke-width="1.5" />
      <circle cx="36" cy="30" r="16" fill="#10b981" />
      <text x="36" y="36" fill="#ffffff" font-size="16" font-weight="800" text-anchor="middle">✓</text>
      
      <text x="68" y="28" fill="#ffffff" font-size="15" font-weight="800">PIAGAM KELULUSAN TERVERIFIKASI SAH DAN ASLI</text>
      <text x="68" y="48" fill="#a7f3d0" font-size="12">Sertifikat terdaftar di basis data pusat SimSCADA-Air dan diterbitkan resmi oleh Balai Diklat Air Minum Nusantara.</text>

      <rect x="1140" y="14" width="160" height="32" rx="6" fill="#0f172a" stroke="#34d399" />
      <text x="1220" y="34" fill="#34d399" font-size="11.5" font-weight="700" text-anchor="middle">STATUS: VALID ✓</text>

      <!-- VERIFIED DETAILS GRID -->
      <g transform="translate(0, 85)">
        <!-- Left: Certificate Details Form (Width 820) -->
        <g transform="translate(0, 0)">
          <rect width="820" height="520" rx="10" fill="#0f172a" stroke="#334155" />
          <g transform="translate(28, 24)">
            <text x="0" y="16" fill="#fbbf24" font-size="13" font-weight="700">RINCIAN DATA PEMEGANG PIAGAM:</text>
            <line x1="0" y1="28" x2="764" y2="28" stroke="#1e293b" />

            <!-- Row 1: Nomor Register & Tanggal -->
            <g transform="translate(0, 45)">
              <text x="0" y="16" fill="#94a3b8" font-size="11.5">Nomor Registrasi Piagam:</text>
              <text x="0" y="38" fill="#ffffff" font-size="16" font-weight="800">SSA/NUS/2026/0001</text>

              <text x="400" y="16" fill="#94a3b8" font-size="11.5">Tanggal Penerbitan:</text>
              <text x="400" y="38" fill="#ffffff" font-size="15" font-weight="700">15 Maret 2026</text>
            </g>

            <!-- Row 2: Nama Peserta & ID -->
            <g transform="translate(0, 115)">
              <text x="0" y="16" fill="#94a3b8" font-size="11.5">Nama Lengkap Operator:</text>
              <text x="0" y="38" fill="#38bdf8" font-size="18" font-weight="800">ANDI KURNIAWAN</text>

              <text x="400" y="16" fill="#94a3b8" font-size="11.5">ID Peserta / Akun Demo:</text>
              <text x="400" y="38" fill="#cbd5e1" font-size="14" font-weight="600">NUS-2026-004 (peserta.lulus)</text>
            </g>

            <!-- Row 3: Lembaga Penerbit -->
            <g transform="translate(0, 185)">
              <text x="0" y="16" fill="#94a3b8" font-size="11.5">Lembaga Penyelenggara Diklat:</text>
              <text x="0" y="38" fill="#ffffff" font-size="14.5" font-weight="700">Balai Diklat Air Minum Nusantara</text>

              <text x="400" y="16" fill="#94a3b8" font-size="11.5">Kelompok Pelatihan:</text>
              <text x="400" y="38" fill="#cbd5e1" font-size="13">Angkatan 1 - Operator Terpadu</text>
            </g>

            <!-- Row 4: Program Jalur -->
            <g transform="translate(0, 255)">
              <text x="0" y="16" fill="#94a3b8" font-size="11.5">Program Pelatihan Diselesaikan:</text>
              <text x="0" y="38" fill="#fbbf24" font-size="14" font-weight="700">JALUR TERPADU (IPA &amp; DISTRIBUSI) - 17 MISI</text>
            </g>

            <!-- Row 5: Prestasi & Nilai -->
            <g transform="translate(0, 325)">
              <rect width="764" height="80" rx="8" fill="#1e293b" stroke="#334155" />
              <g transform="translate(20, 16)">
                <text x="0" y="16" fill="#94a3b8" font-size="11">SKOR AKHIR</text>
                <text x="0" y="42" fill="#34d399" font-size="20" font-weight="800">96 / 100</text>

                <text x="180" y="16" fill="#94a3b8" font-size="11">PREDIKAT</text>
                <text x="180" y="42" fill="#fbbf24" font-size="18" font-weight="800">★★★ (Sangat Baik)</text>

                <text x="420" y="16" fill="#94a3b8" font-size="11">TOTAL AKUMULASI XP</text>
                <text x="420" y="42" fill="#38bdf8" font-size="18" font-weight="800">3.820 XP</text>

                <text x="620" y="16" fill="#94a3b8" font-size="11">JENJANG JABATAN</text>
                <text x="620" y="42" fill="#d8b4fe" font-size="16" font-weight="800">Operator Ahli</text>
              </g>
            </g>

            <!-- Row 6: Penanda Tangan -->
            <g transform="translate(0, 425)">
              <text x="0" y="16" fill="#cbd5e1" font-size="11">Disahkan Oleh: <tspan fill="#ffffff" font-weight="600">Budi Santoso, S.T.</tspan> (Instruktur Utama) dan <tspan fill="#ffffff" font-weight="600">Ir. H. Bambang Sutrisno, M.Eng.</tspan> (Kepala Balai Diklat)</text>
            </g>
          </g>
        </g>

        <!-- Right: QR Code & Public Authenticity Badge (Width 470) -->
        <g transform="translate(850, 0)">
          <rect width="470" height="520" rx="10" fill="#0f172a" stroke="#334155" />
          <g transform="translate(35, 30)">
            <text x="200" y="20" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">Segel Otentikasi Digital SimSCADA-Air</text>
            
            <!-- Big QR Graphic Simulation -->
            <g transform="translate(100, 40)">
              <rect width="200" height="200" rx="10" fill="#ffffff" />
              <!-- Outer Targets -->
              <rect x="20" y="20" width="45" height="45" fill="#000000" />
              <rect x="28" y="28" width="29" height="29" fill="#ffffff" />
              <rect x="35" y="35" width="15" height="15" fill="#000000" />

              <rect x="135" y="20" width="45" height="45" fill="#000000" />
              <rect x="143" y="28" width="29" height="29" fill="#ffffff" />
              <rect x="150" y="35" width="15" height="15" fill="#000000" />

              <rect x="20" y="135" width="45" height="45" fill="#000000" />
              <rect x="28" y="143" width="29" height="29" fill="#ffffff" />
              <rect x="35" y="150" width="15" height="15" fill="#000000" />

              <!-- QR Pattern Bits -->
              <rect x="80" y="30" width="20" height="20" fill="#000000" />
              <rect x="90" y="60" width="30" height="25" fill="#000000" />
              <rect x="140" y="90" width="25" height="25" fill="#000000" />
              <rect x="75" y="120" width="35" height="20" fill="#000000" />
              <rect x="120" y="135" width="40" height="25" fill="#000000" />
              <rect x="85" y="155" width="25" height="25" fill="#000000" />
            </g>

            <text x="200" y="270" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">URL Verifikasi Resmi:</text>
            <text x="200" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">https://simscada.id/verifikasi/SSA-NUS-2026-0001</text>

            <rect x="40" y="320" width="320" height="42" rx="6" fill="#0284c7" />
            <text x="200" y="346" fill="#ffffff" font-size="12.5" font-weight="700" text-anchor="middle">Unduh Salinan Piagam Sah (PDF)</text>

            <rect x="40" y="375" width="320" height="42" rx="6" fill="#1e293b" stroke="#334155" />
            <text x="200" y="401" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Salin Tautan Verifikasi</text>
          </g>
        </g>
      </g>

      <!-- Search Other Certificate Box Bottom -->
      <g transform="translate(0, 620)">
        <rect width="1320" height="85" rx="8" fill="#0f172a" stroke="#334155" />
        <g transform="translate(24, 20)">
          <text x="0" y="16" fill="#cbd5e1" font-size="12" font-weight="700">Verifikasi Nomor Piagam Lainnya:</text>
          
          <rect x="0" y="26" width="500" height="34" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="16" y="48" fill="#64748b" font-size="12">Masukkan nomor piagam (contoh: SSA/NUS/2026/0002)...</text>

          <rect x="520" y="26" width="140" height="34" rx="6" fill="#0284c7" />
          <text x="590" y="48" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Cari Sertifikat</text>

          <text x="700" y="48" fill="#94a3b8" font-size="11">Catatan: Piagam berstatus "Menunggu Persetujuan" (L8b) belum dapat diverifikasi secara publik.</text>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

def main():
    generators = [
        ("mockup_l10_manage_scenarios.svg", generate_l10),
        ("mockup_l11_session_replay.svg", generate_l11),
        ("mockup_l12_manage_users.svg", generate_l12),
        ("mockup_l13_tenant_settings.svg", generate_l13),
        ("mockup_l14_tenant_evaluation.svg", generate_l14),
        ("mockup_l15_superadmin.svg", generate_l15),
        ("mockup_l16_public_verification.svg", generate_l16),
    ]
    for filename, fn in generators:
        filepath = os.path.join(OUTPUT_DIR, filename)
        content = fn()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        # Validate XML
        try:
            ET.parse(filepath)
            print(f"SUCCESS: {filename} written and validated in public/!")
        except Exception as e:
            print(f"ERROR validating {filename}: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == "__main__":
    main()

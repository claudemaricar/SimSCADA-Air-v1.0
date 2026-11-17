#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 4: L7, L8, L8b, L9
Directly generated into public/ with strict PRD v1.0 compliance and full XML validation.
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
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bgGrad)" />
{content}
</svg>"""
    return sanitize_xml(svg)

def header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 2", name="Dimas Wahyu Pratama", initials="DW"):
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

# ==================== L7: BADGES & LEADERBOARD ====================
def generate_l7():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 2", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Galeri Lencana &amp; Papan Peringkat Kompetensi", "8 Lencana Resmi PRD §8 · Papan Peringkat Terisolasi Antar-Lembaga (FR-21) · Dimas Wahyu Pratama (peserta.ipa)", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Grid: Left = 8 Badges PRD §8 (Width 960), Right = Leaderboard (Width 864) -->
  <g transform="translate(32, 180)">
    <!-- LEFT CARD: 8 BADGES -->
    <rect width="960" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(32, 24)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">8 Lencana Prestasi Operator (PRD SimSCADA-Air v1.0 §8)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Pencapaian berbasis kriteria obyektif simulasi SCADA · 3 Terbuka, 5 Sedang Berjalan/Terkunci</text>
      <line x1="0" y1="56" x2="896" y2="56" stroke="#334155" stroke-width="1" />

      <!-- GRID 2 columns x 4 rows -->
      <!-- ROW 1 -->
      <!-- 1. Penjelajah Titik Kontrol (UNLOCKED) -->
      <g transform="translate(0, 75)">
        <rect width="435" height="155" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="30" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="63" fill="#ffffff" font-size="22" text-anchor="middle">🔍</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>
        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Penjelajah Titik Kontrol</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="10.5">Buka narasi &amp; pelajari seluruh titik kontrol</text>
        <text x="96" y="86" fill="#cbd5e1" font-size="10.5">unit IPA dan Distribusi secara mandiri.</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#10b981" />
        <text x="96" y="125" fill="#34d399" font-size="10" font-weight="600">Selesai 100% · Terbuka pada 10 Mar 2026</text>
      </g>

      <!-- 2. Respons Kilat (UNLOCKED) -->
      <g transform="translate(460, 75)">
        <rect width="435" height="155" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="30" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="63" fill="#ffffff" font-size="22" text-anchor="middle">⚡</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>
        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Respons Kilat</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="10.5">Merespons alarm pertama &lt;50% dari target.</text>
        <text x="96" y="86" fill="#cbd5e1" font-size="10.5">IPA-06: Target 60 dtk · Respons 25 dtk (&lt;30s).</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#10b981" />
        <text x="96" y="125" fill="#34d399" font-size="10" font-weight="600">25s dari target 60s (41,7%) · Diraih di IPA-06</text>
      </g>

      <!-- ROW 2 -->
      <!-- 3. Tanpa Alarm Terlewat (UNLOCKED) -->
      <g transform="translate(0, 245)">
        <rect width="435" height="155" rx="10" fill="#0f172a" stroke="#059669" stroke-width="2" />
        <circle cx="50" cy="55" r="30" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <text x="50" y="63" fill="#ffffff" font-size="22" text-anchor="middle">🛡️</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#059669" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">TERBUKA ✓</text>
        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Tanpa Alarm Terlewat</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="10.5">Menyelesaikan sesi tanpa ada alarm</text>
        <text x="96" y="86" fill="#cbd5e1" font-size="10.5">yang terlewat atau tidak diakui (ACK).</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#10b981" />
        <text x="96" y="125" fill="#34d399" font-size="10" font-weight="600">0 Alarm Terlewat · Terbuka pada IPA-06</text>
      </g>

      <!-- 4. Penjaga Mutu Air (IN PROGRESS 80%) -->
      <g transform="translate(460, 245)">
        <rect width="435" height="155" rx="10" fill="#0f172a" stroke="#d97706" stroke-width="1.5" />
        <circle cx="50" cy="55" r="30" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
        <text x="50" y="63" fill="#ffffff" font-size="22" text-anchor="middle">💧</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#d97706" />
        <text x="367" y="29" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">80% PROGRES</text>
        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Penjaga Mutu Air</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="10.5">Pertahankan kekeruhan air olahan &lt;1,5 NTU</text>
        <text x="96" y="86" fill="#cbd5e1" font-size="10.5">sepanjang sesi evaluasi misi.</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <rect x="96" y="102" width="255" height="6" rx="3" fill="#f59e0b" />
        <text x="96" y="125" fill="#fbbf24" font-size="10" font-weight="600">6 dari 7 misi IPA mempertahankan mutu &lt;1,5 NTU</text>
      </g>

      <!-- ROW 3 -->
      <!-- 5. Penjaga Tekanan (LOCKED - TRACK DISTRIBUSI) -->
      <g transform="translate(0, 415)">
        <rect width="435" height="155" rx="10" fill="#0b1120" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="30" fill="#1e293b" stroke="#475569" stroke-width="1" />
        <text x="50" y="63" fill="#64748b" font-size="22" text-anchor="middle">🔒</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#334155" />
        <text x="367" y="29" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>
        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Penjaga Tekanan</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="10.5">Menjaga fluktuasi tekanan zona distribusi</text>
        <text x="96" y="86" fill="#64748b" font-size="10.5">dalam toleransi ketat ±0,2 bar.</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <text x="96" y="125" fill="#64748b" font-size="10">Kunci: Buka Jalur Distribusi (DST-01 s/d DST-07)</text>
      </g>

      <!-- 6. Tiga Bintang IPA / Distribusi (IN PROGRESS) -->
      <g transform="translate(460, 415)">
        <rect width="435" height="155" rx="10" fill="#0f172a" stroke="#334155" />
        <circle cx="50" cy="55" r="30" fill="#1e293b" stroke="#475569" stroke-width="1" />
        <text x="50" y="63" fill="#fbbf24" font-size="22" text-anchor="middle">⭐</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#334155" />
        <text x="367" y="29" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">PROGRES 1/9</text>
        <text x="96" y="32" fill="#f8fafc" font-size="13" font-weight="700">Tiga Bintang IPA</text>
        <text x="96" y="52" fill="#38bdf8" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#cbd5e1" font-size="10.5">Raih bintang 3 (skor ≥95) pada seluruh</text>
        <text x="96" y="86" fill="#cbd5e1" font-size="10.5">9 misi Jalur Pengolahan Air Minum (IPA).</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <rect x="96" y="102" width="35" height="6" rx="3" fill="#f59e0b" />
        <text x="96" y="125" fill="#94a3b8" font-size="10">1 misi 3★ (IPA-01) · 5 misi 2★ · 1 misi 1★</text>
      </g>

      <!-- ROW 4 -->
      <!-- 7. Hulu ke Hilir (LOCKED) -->
      <g transform="translate(0, 585)">
        <rect width="435" height="155" rx="10" fill="#0b1120" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="30" fill="#1e293b" stroke="#475569" stroke-width="1" />
        <text x="50" y="63" fill="#64748b" font-size="22" text-anchor="middle">🌊</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#334155" />
        <text x="367" y="29" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>
        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Hulu ke Hilir</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="10.5">Lulus seluruh 17 misi Jalur Terpadu</text>
        <text x="96" y="86" fill="#64748b" font-size="10.5">dari IPA-01 hingga TRP-02.</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <text x="96" y="125" fill="#64748b" font-size="10">Kunci: Buka &amp; Selesaikan Jalur Terpadu 17 Misi</text>
      </g>

      <!-- 8. Lulus Tanpa Petunjuk (LOCKED) -->
      <g transform="translate(460, 585)">
        <rect width="435" height="155" rx="10" fill="#0b1120" stroke="#334155" stroke-dasharray="4,4" />
        <circle cx="50" cy="55" r="30" fill="#1e293b" stroke="#475569" stroke-width="1" />
        <text x="50" y="63" fill="#64748b" font-size="22" text-anchor="middle">🎯</text>
        <rect x="320" y="14" width="95" height="22" rx="4" fill="#334155" />
        <text x="367" y="29" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">TERKUNCI</text>
        <text x="96" y="32" fill="#94a3b8" font-size="13" font-weight="700">Lulus Tanpa Petunjuk</text>
        <text x="96" y="52" fill="#64748b" font-size="11" font-weight="600">Syarat Resmi PRD §8:</text>
        <text x="96" y="70" fill="#64748b" font-size="10.5">Lulus Misi Kelulusan tanpa menggunakan</text>
        <text x="96" y="86" fill="#64748b" font-size="10.5">bantuan tombol petunjuk (−5 poin).</text>
        <rect x="96" y="102" width="319" height="6" rx="3" fill="#1e293b" />
        <text x="96" y="125" fill="#64748b" font-size="10">Tersedia pada Misi Kelulusan Ujian (IPA-09 / TRP-02)</text>
      </g>

      <!-- Bottom Note -->
      <g transform="translate(0, 760)">
        <rect width="896" height="50" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="20" y="30" fill="#38bdf8" font-size="12" font-weight="600">💡 Info Sistem Gamifikasi:</text>
        <text x="180" y="30" fill="#94a3b8" font-size="12">Lencana diverifikasi otomatis oleh mesin evaluasi saat kriteria PRD §8 terpenuhi. Tidak ada intervensi manual.</text>
      </g>
    </g>

    <!-- RIGHT CARD: LEADERBOARD (Width 864) -->
    <g transform="translate(992, 0)">
      <rect width="864" height="860" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(28, 24)">
        <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Papan Peringkat Kompetensi Operator</text>
        <text x="0" y="40" fill="#94a3b8" font-size="12">Terisolasi Balai Diklat Air Minum Nusantara (FR-21) · 42 Peserta Aktif</text>
        <line x1="0" y1="56" x2="808" y2="56" stroke="#334155" stroke-width="1" />

        <!-- TABS FILTER -->
        <g transform="translate(0, 68)">
          <!-- Scope Tabs -->
          <rect x="0" y="0" width="160" height="32" rx="6" fill="#0284c7" />
          <text x="80" y="20" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">Seluruh Lembaga</text>
          
          <rect x="168" y="0" width="170" height="32" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="253" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">Angkatan 2 (IPA)</text>

          <!-- Time Tabs -->
          <rect x="520" y="0" width="140" height="32" rx="6" fill="#0284c7" />
          <text x="590" y="20" fill="#ffffff" font-size="11.5" font-weight="700" text-anchor="middle">Sepanjang Waktu</text>

          <rect x="668" y="0" width="140" height="32" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="738" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">Minggu Ini</text>
        </g>

        <!-- TABLE HEADER -->
        <g transform="translate(0, 118)">
          <rect width="808" height="36" rx="6" fill="#0f172a" />
          <text x="24" y="23" fill="#64748b" font-size="11" font-weight="700">POS</text>
          <text x="80" y="23" fill="#64748b" font-size="11" font-weight="700">NAMA OPERATOR</text>
          <text x="310" y="23" fill="#64748b" font-size="11" font-weight="700">TINGKAT / LEVEL</text>
          <text x="490" y="23" fill="#64748b" font-size="11" font-weight="700">BINTANG</text>
          <text x="610" y="23" fill="#64748b" font-size="11" font-weight="700">TOTAL XP</text>
          <text x="730" y="23" fill="#64748b" font-size="11" font-weight="700">STATUS</text>
        </g>

        <!-- RANK 1: Andi Kurniawan (peserta.lulus) -->
        <g transform="translate(0, 162)">
          <rect width="808" height="64" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
          <circle cx="36" cy="32" r="16" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
          <text x="36" y="37" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">🥇1</text>
          
          <text x="80" y="26" fill="#ffffff" font-size="13" font-weight="700">Andi Kurniawan <tspan fill="#fbbf24" font-size="11">(peserta.lulus)</tspan></text>
          <text x="80" y="46" fill="#94a3b8" font-size="11">Angkatan 1 · Jalur Terpadu (17 Misi Lulus)</text>
          
          <rect x="310" y="16" width="130" height="24" rx="4" fill="#581c87" />
          <text x="375" y="32" fill="#d8b4fe" font-size="11" font-weight="700" text-anchor="middle">Operator Ahli</text>
          <text x="310" y="52" fill="#a855f7" font-size="10">≥3.500 XP (Tertinggi)</text>

          <text x="490" y="34" fill="#fbbf24" font-size="14" font-weight="700">48 ★</text>
          <text x="490" y="50" fill="#94a3b8" font-size="10">17 Misi</text>

          <text x="610" y="34" fill="#38bdf8" font-size="14" font-weight="700">3.820 XP</text>
          <text x="610" y="50" fill="#64748b" font-size="10">Pengali maks 3x</text>

          <rect x="715" y="20" width="80" height="24" rx="4" fill="#065f46" />
          <text x="755" y="36" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Piagam Terbit</text>
        </g>

        <!-- RANK 2: Dimas Wahyu Pratama (peserta.ipa - CURRENT USER) -->
        <g transform="translate(0, 234)">
          <rect width="808" height="64" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
          <circle cx="36" cy="32" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
          <text x="36" y="37" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">🥈2</text>
          
          <text x="80" y="26" fill="#38bdf8" font-size="13" font-weight="700">Dimas Wahyu Pratama <tspan fill="#34d399" font-size="11">(Anda · peserta.ipa)</tspan></text>
          <text x="80" y="46" fill="#94a3b8" font-size="11">Angkatan 2 · Jalur IPA (7 dari 9 Misi Lulus)</text>
          
          <rect x="310" y="16" width="130" height="24" rx="4" fill="#1e3a8a" />
          <text x="375" y="32" fill="#93c5fd" font-size="11" font-weight="700" text-anchor="middle">Operator Muda</text>
          <text x="310" y="52" fill="#60a5fa" font-size="10">400–1.199 XP (Sisa 380 ke Madya)</text>

          <text x="490" y="34" fill="#fbbf24" font-size="14" font-weight="700">14 ★</text>
          <text x="490" y="50" fill="#94a3b8" font-size="10">7 Misi</text>

          <text x="610" y="34" fill="#38bdf8" font-size="14" font-weight="700">820 XP</text>
          <text x="610" y="50" fill="#64748b" font-size="10">+176 dari IPA-06</text>

          <rect x="715" y="20" width="80" height="24" rx="4" fill="#854d0e" />
          <text x="755" y="36" fill="#fef08a" font-size="10" font-weight="700" text-anchor="middle">Aktif Belajar</text>
        </g>

        <!-- RANK 3: Siti Rahmawati (peserta.distribusi) -->
        <g transform="translate(0, 306)">
          <rect width="808" height="60" rx="8" fill="#1e293b" stroke="#334155" />
          <circle cx="36" cy="30" r="14" fill="#334155" />
          <text x="36" y="35" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">🥉3</text>
          
          <text x="80" y="24" fill="#f8fafc" font-size="12.5" font-weight="600">Siti Rahmawati <tspan fill="#94a3b8" font-size="10">(peserta.distribusi)</tspan></text>
          <text x="80" y="42" fill="#64748b" font-size="10.5">Angkatan 2 · Jalur Distribusi (5 dari 7 Misi)</text>
          
          <rect x="310" y="14" width="130" height="22" rx="4" fill="#1e3a8a" />
          <text x="375" y="29" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

          <text x="490" y="32" fill="#fbbf24" font-size="13" font-weight="700">12 ★</text>
          <text x="610" y="32" fill="#38bdf8" font-size="13" font-weight="700">750 XP</text>

          <rect x="715" y="18" width="80" height="22" rx="4" fill="#854d0e" />
          <text x="755" y="33" fill="#fef08a" font-size="10" font-weight="700" text-anchor="middle">Aktif Belajar</text>
        </g>

        <!-- RANK 4: Rian Hidayat (peserta contoh - Angkatan 1) -->
        <g transform="translate(0, 374)">
          <rect width="808" height="60" rx="8" fill="#1e293b" stroke="#334155" />
          <circle cx="36" cy="30" r="14" fill="#334155" />
          <text x="36" y="35" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle">4</text>
          
          <text x="80" y="24" fill="#f8fafc" font-size="12.5" font-weight="600">Rian Hidayat <tspan fill="#64748b" font-size="10">(peserta contoh · Angkatan 1)</tspan></text>
          <text x="80" y="42" fill="#64748b" font-size="10.5">Angkatan 1 · Jalur IPA (9 dari 9 Misi - Ujian Selesai)</text>
          
          <rect x="310" y="14" width="130" height="22" rx="4" fill="#1e3a8a" />
          <text x="375" y="29" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

          <text x="490" y="32" fill="#fbbf24" font-size="13" font-weight="700">10 ★</text>
          <text x="610" y="32" fill="#38bdf8" font-size="13" font-weight="700">620 XP</text>

          <rect x="715" y="18" width="80" height="22" rx="4" fill="#78350f" />
          <text x="755" y="33" fill="#fef08a" font-size="9.5" font-weight="700" text-anchor="middle">Menunggu Acc</text>
        </g>

        <!-- RANK 5: Eko Prasetyo (peserta contoh) -->
        <g transform="translate(0, 442)">
          <rect width="808" height="60" rx="8" fill="#1e293b" stroke="#334155" />
          <circle cx="36" cy="30" r="14" fill="#334155" />
          <text x="36" y="35" fill="#94a3b8" font-size="11" font-weight="600" text-anchor="middle">5</text>
          
          <text x="80" y="24" fill="#f8fafc" font-size="12.5" font-weight="600">Eko Prasetyo <tspan fill="#64748b" font-size="10">(peserta contoh · Angkatan 1)</tspan></text>
          <text x="80" y="42" fill="#64748b" font-size="10.5">Angkatan 1 · Jalur Distribusi (4 dari 7 Misi)</text>
          
          <rect x="310" y="14" width="130" height="22" rx="4" fill="#1e3a8a" />
          <text x="375" y="29" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

          <text x="490" y="32" fill="#fbbf24" font-size="13" font-weight="700">8 ★</text>
          <text x="610" y="32" fill="#38bdf8" font-size="13" font-weight="700">490 XP</text>

          <rect x="715" y="18" width="80" height="22" rx="4" fill="#854d0e" />
          <text x="755" y="33" fill="#fef08a" font-size="10" font-weight="700" text-anchor="middle">Aktif Belajar</text>
        </g>

        <!-- Ellipsis / Truncation indicator -->
        <g transform="translate(0, 510)">
          <rect width="808" height="40" rx="6" fill="#0f172a" />
          <text x="404" y="25" fill="#64748b" font-size="11" text-anchor="middle">• • • 36 Peserta Lainnya Berada di Rentang 50 s/d 420 XP • • •</text>
        </g>

        <!-- RANK 42: Budi Baru (peserta.baru) -->
        <g transform="translate(0, 560)">
          <rect width="808" height="60" rx="8" fill="#1e293b" stroke="#334155" />
          <circle cx="36" cy="30" r="14" fill="#1e293b" stroke="#475569" stroke-width="1" />
          <text x="36" y="35" fill="#64748b" font-size="11" text-anchor="middle">42</text>
          
          <text x="80" y="24" fill="#94a3b8" font-size="12.5" font-weight="600">Budi Baru <tspan fill="#64748b" font-size="10">(peserta.baru)</tspan></text>
          <text x="80" y="42" fill="#64748b" font-size="10.5">Angkatan 2 · Belum Memulai Misi (Baru Pre-Test 52/100)</text>
          
          <rect x="310" y="14" width="130" height="22" rx="4" fill="#334155" />
          <text x="375" y="29" fill="#94a3b8" font-size="10.5" font-weight="700" text-anchor="middle">Operator Magang</text>

          <text x="490" y="32" fill="#64748b" font-size="13">0 ★</text>
          <text x="610" y="32" fill="#64748b" font-size="13">0 XP</text>

          <rect x="715" y="18" width="80" height="22" rx="4" fill="#334155" />
          <text x="755" y="33" fill="#cbd5e1" font-size="10" text-anchor="middle">Belum Mulai</text>
        </g>

        <!-- PRIVACY NOTE PRD FR-21 -->
        <g transform="translate(0, 640)">
          <rect width="808" height="170" rx="10" fill="#0b1120" stroke="#1e293b" />
          <g transform="translate(20, 20)">
            <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">🛡️ Kebijakan Isolasi Data &amp; Privasi Antar-Lembaga (PRD §5 &amp; FR-21):</text>
            <text x="0" y="40" fill="#cbd5e1" font-size="11.5">• Papan peringkat hanya menampilkan peserta dari lembaga Anda (<tspan fill="#ffffff" font-weight="600">Balai Diklat Air Minum Nusantara</tspan>).</text>
            <text x="0" y="60" fill="#cbd5e1" font-size="11.5">• Peserta dari <tspan fill="#94a3b8">Pusat Pelatihan Tirta Mandiri</tspan> atau lembaga lain terisolasi total demi kerahasiaan evaluasi.</text>
            <text x="0" y="80" fill="#cbd5e1" font-size="11.5">• Admin Lembaga memiliki kendali saklar penuh untuk mengaktifkan/menonaktifkan fitur ini di menu Pengaturan.</text>
            <text x="0" y="105" fill="#f59e0b" font-size="11" font-weight="600">Tangga Jenjang Jabatan Operator (PRD §8):</text>
            <text x="0" y="125" fill="#94a3b8" font-size="10.5">Magang (0 XP) → Muda (400 XP) → Madya (1.200 XP) → Utama (2.500 XP) → Ahli (3.500 XP)</text>
          </g>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L8: CERTIFICATE ISSUED ====================
def generate_l8():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Ahli · Angkatan 1", name="Andi Kurniawan", initials="AK")
    title = page_title_block("Piagam Kelulusan Operator SCADA SPAM", "Status: Piagam Kelulusan Terbit · Terverifikasi Sistem SimSCADA-Air · Andi Kurniawan (peserta.lulus)", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Certificate Container (Width 1400, Height 860, Centered at x=260) -->
  <g transform="translate(260, 180)">
    <!-- Outer Card Frame with Guilloche border styling -->
    <rect width="1400" height="860" rx="16" fill="#0f172a" stroke="#d97706" stroke-width="3" />
    <rect x="12" y="12" width="1376" height="836" rx="12" fill="none" stroke="#78350f" stroke-width="1.5" stroke-dasharray="6,3" />

    <!-- Action Bar Top Right -->
    <g transform="translate(1030, 36)">
      <rect width="180" height="42" rx="8" fill="#0284c7" />
      <text x="90" y="26" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Unduh Piagam (PDF)</text>

      <rect x="195" y="0" width="140" height="42" rx="8" fill="#1e293b" stroke="#334155" />
      <text x="265" y="26" fill="#f8fafc" font-size="13" font-weight="600" text-anchor="middle">Bagikan URL</text>
    </g>

    <!-- Certificate Body -->
    <g transform="translate(80, 50)">
      <!-- Lembaga Logo & Name Header -->
      <circle cx="620" cy="40" r="32" fill="#0284c7" />
      <path d="M620 18 C620 18 604 36 604 46 C604 55 611 62 620 62 C629 62 636 55 636 46 C636 36 620 18 620 18 Z" fill="#ffffff" />
      
      <text x="620" y="96" fill="#ffffff" font-size="20" font-weight="800" text-anchor="middle">BALAI DIKLAT AIR MINUM NUSANTARA</text>
      <text x="620" y="118" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">PUSAT PENDIDIKAN DAN PELATIHAN OPERATOR SISTEM PENYEDIAAN AIR MINUM</text>
      <text x="620" y="136" fill="#94a3b8" font-size="10.5" text-anchor="middle">Didukung oleh Platform Pembelajaran Mandiri SimSCADA-Air v1.0</text>
      
      <line x1="220" y1="152" x2="1020" y2="152" stroke="#d97706" stroke-width="1.5" />

      <!-- Certificate Title -->
      <text x="620" y="196" fill="#fbbf24" font-size="28" font-weight="800" text-anchor="middle" letter-spacing="2">PIAGAM KELULUSAN</text>
      <text x="620" y="222" fill="#94a3b8" font-size="13" text-anchor="middle">Nomor Register: <tspan fill="#ffffff" font-weight="700">SSA/NUS/2026/0001</tspan> · Status: <tspan fill="#34d399" font-weight="700">TERBIT &amp; VALID</tspan></text>

      <!-- Recipient Statement -->
      <text x="620" y="270" fill="#cbd5e1" font-size="14" text-anchor="middle">Diberikan dengan bangga kepada:</text>
      <text x="620" y="316" fill="#ffffff" font-size="34" font-weight="800" text-anchor="middle">ANDI KURNIAWAN</text>
      <text x="620" y="342" fill="#38bdf8" font-size="13" font-weight="600" text-anchor="middle">ID Peserta: NUS-2026-004 · Akun: peserta.lulus · Angkatan 1</text>

      <text x="620" y="380" fill="#cbd5e1" font-size="13.5" text-anchor="middle">Atas keberhasilannya menyelesaikan seluruh rangkaian uji simulasi dan memenuhi standar kompetensi:</text>
      <text x="620" y="412" fill="#fbbf24" font-size="19" font-weight="800" text-anchor="middle">JALUR TERPADU (PENGOLAHAN IPA &amp; JARINGAN DISTRIBUSI)</text>
      <text x="620" y="434" fill="#94a3b8" font-size="12" text-anchor="middle">Mencakup 17 Skenario Gangguan Dinamis, Pengendalian Koagulasi-Filter, dan Manajemen Tekanan Pompa Distribusi</text>

      <!-- Scores & Achievements Box -->
      <g transform="translate(160, 456)">
        <rect width="920" height="110" rx="10" fill="#1e293b" stroke="#334155" />
        
        <g transform="translate(35, 20)">
          <text x="80" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">SKOR AKHIR POST-TEST</text>
          <text x="80" y="52" fill="#34d399" font-size="26" font-weight="800" text-anchor="middle">96 / 100</text>
          <text x="80" y="74" fill="#64748b" font-size="10.5" text-anchor="middle">KKM: 80 · +34 Poin Pre</text>
        </g>
        <line x1="245" y1="15" x2="245" y2="95" stroke="#334155" />

        <g transform="translate(265, 20)">
          <text x="80" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">BINTANG &amp; PREDIKAT</text>
          <text x="80" y="52" fill="#fbbf24" font-size="24" font-weight="800" text-anchor="middle">★★★</text>
          <text x="80" y="74" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Sangat Baik (≥95)</text>
        </g>
        <line x1="475" y1="15" x2="475" y2="95" stroke="#334155" />

        <g transform="translate(495, 20)">
          <text x="80" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">TOTAL AKUMULASI XP</text>
          <text x="80" y="52" fill="#38bdf8" font-size="24" font-weight="800" text-anchor="middle">3.820 XP</text>
          <text x="80" y="74" fill="#0284c7" font-size="11" font-weight="700" text-anchor="middle">Level: Operator Ahli</text>
        </g>
        <line x1="705" y1="15" x2="705" y2="95" stroke="#334155" />

        <g transform="translate(725, 20)">
          <text x="80" y="20" fill="#94a3b8" font-size="11" text-anchor="middle">STATUS KELULUSAN</text>
          <rect x="15" y="32" width="130" height="28" rx="6" fill="#065f46" />
          <text x="80" y="51" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">LULUS RESMI</text>
          <text x="80" y="74" fill="#64748b" font-size="10.5" text-anchor="middle">15 Maret 2026</text>
        </g>
      </g>

      <!-- Signatures and QR Code Area -->
      <g transform="translate(100, 595)">
        <!-- Left: Penilai / Instruktur Utama PRD §6 -->
        <g transform="translate(40, 0)">
          <text x="120" y="16" fill="#94a3b8" font-size="11.5" text-anchor="middle">Instruktur Penilai,</text>
          <!-- Signature Mock Graphic -->
          <path d="M60 55 Q 90 20, 120 50 T 180 40" fill="none" stroke="#38bdf8" stroke-width="2" />
          <line x1="20" y1="75" x2="220" y2="75" stroke="#475569" stroke-width="1" />
          <text x="120" y="94" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Budi Santoso, S.T.</text>
          <text x="120" y="110" fill="#94a3b8" font-size="11" text-anchor="middle">Instruktur Utama SPAM</text>
          <text x="120" y="126" fill="#64748b" font-size="10" text-anchor="middle">NIP. 19820412 200801 1 005</text>
        </g>

        <!-- Center: QR Code Verification -->
        <g transform="translate(440, 0)">
          <rect x="40" y="0" width="100" height="100" rx="8" fill="#ffffff" />
          <!-- QR pattern simulation -->
          <rect x="50" y="10" width="24" height="24" fill="#000000" />
          <rect x="54" y="14" width="16" height="16" fill="#ffffff" />
          <rect x="58" y="18" width="8" height="8" fill="#000000" />

          <rect x="106" y="10" width="24" height="24" fill="#000000" />
          <rect x="110" y="14" width="16" height="16" fill="#ffffff" />
          <rect x="114" y="18" width="8" height="8" fill="#000000" />

          <rect x="50" y="66" width="24" height="24" fill="#000000" />
          <rect x="54" y="70" width="16" height="16" fill="#ffffff" />
          <rect x="58" y="74" width="8" height="8" fill="#000000" />

          <rect x="80" y="20" width="12" height="12" fill="#000000" />
          <rect x="94" y="34" width="14" height="14" fill="#000000" />
          <rect x="80" y="60" width="18" height="8" fill="#000000" />
          <rect x="104" y="66" width="12" height="12" fill="#000000" />

          <text x="90" y="116" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle">Pindai Verifikasi</text>
          <text x="90" y="130" fill="#64748b" font-size="9.5" text-anchor="middle">simscada.id/verifikasi</text>
        </g>

        <!-- Right: Pimpinan Lembaga PRD §6 -->
        <g transform="translate(740, 0)">
          <text x="130" y="16" fill="#94a3b8" font-size="11.5" text-anchor="middle">Kepala Balai Diklat,</text>
          <!-- Signature Mock Graphic -->
          <path d="M70 50 Q 110 25, 140 55 T 200 45" fill="none" stroke="#f59e0b" stroke-width="2" />
          <line x1="30" y1="75" x2="230" y2="75" stroke="#475569" stroke-width="1" />
          <text x="130" y="94" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">Ir. H. Bambang Sutrisno, M.Eng.</text>
          <text x="130" y="110" fill="#94a3b8" font-size="11" text-anchor="middle">Kepala Balai Diklat Air Minum Nusantara</text>
          <text x="130" y="126" fill="#64748b" font-size="10" text-anchor="middle">NIP. 19710815 199603 1 002</text>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L8b: CERTIFICATE PENDING APPROVAL ====================
def generate_l8b():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Rian Hidayat", initials="RH")
    title = page_title_block("Pratinjau Status Pengajuan Piagam Kelulusan", "Status: Menunggu Verifikasi &amp; Persetujuan Instruktur · Rian Hidayat (peserta contoh - Angkatan 1)", 112)
    
    content = f"""{hdr}{title}
  <!-- Main Certificate Container with Watermark (Width 1400, Height 860, Centered at x=260) -->
  <g transform="translate(260, 180)">
    <!-- Outer Card Frame with Pending Alert -->
    <rect width="1400" height="860" rx="16" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5" />
    <rect x="12" y="12" width="1376" height="836" rx="12" fill="none" stroke="#78350f" stroke-width="1.5" stroke-dasharray="6,4" />

    <!-- PENDING BANNER TOP -->
    <g transform="translate(40, 28)">
      <rect width="1320" height="48" rx="8" fill="#78350f" stroke="#f59e0b" stroke-width="1.5" />
      <text x="24" y="30" fill="#fbbf24" font-size="13" font-weight="800">⏳ STATUS: MENUNGGU PERSETUJUAN INSTRUKTUR (DRAFT VERIFIKASI)</text>
      <text x="620" y="30" fill="#fef08a" font-size="12">Post-test (82/100) dan Misi Kelulusan IPA-09 telah diserahkan. Menunggu validasi instruktur Budi Santoso, S.T.</text>
      
      <rect x="1190" y="10" width="115" height="28" rx="6" fill="#334155" />
      <text x="1247" y="28" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Unduh Nonaktif</text>
    </g>

    <!-- WATERMARK DRAFT ACROSS CERTIFICATE -->
    <g transform="translate(700, 480) rotate(-25)">
      <text x="0" y="0" fill="#f59e0b" fill-opacity="0.08" font-size="110" font-weight="900" text-anchor="middle" letter-spacing="10">DRAFT · MENUNGGU ACC</text>
    </g>

    <!-- Certificate Body Draft -->
    <g transform="translate(80, 95)">
      <circle cx="620" cy="40" r="30" fill="#334155" />
      <path d="M620 20 C620 20 606 36 606 46 C606 54 612 60 620 60 C628 60 634 54 634 46 C634 36 620 20 620 20 Z" fill="#94a3b8" />
      
      <text x="620" y="92" fill="#ffffff" font-size="19" font-weight="800" text-anchor="middle">BALAI DIKLAT AIR MINUM NUSANTARA</text>
      <text x="620" y="112" fill="#94a3b8" font-size="11.5" text-anchor="middle">Pusat Pendidikan dan Pelatihan Operator Sistem Penyediaan Air Minum</text>
      
      <line x1="260" y1="130" x2="980" y2="130" stroke="#475569" stroke-width="1" />

      <text x="620" y="172" fill="#cbd5e1" font-size="26" font-weight="800" text-anchor="middle" letter-spacing="2">PIAGAM KELULUSAN (DRAFT)</text>
      <text x="620" y="196" fill="#f59e0b" font-size="12.5" font-weight="600" text-anchor="middle">Nomor Registrasi Dicadangkan: <tspan fill="#ffffff" font-weight="700">SSA/NUS/2026/0002 (Pending)</tspan></text>

      <text x="620" y="240" fill="#94a3b8" font-size="13" text-anchor="middle">Diberikan kepada:</text>
      <text x="620" y="280" fill="#ffffff" font-size="30" font-weight="800" text-anchor="middle">RIAN HIDAYAT</text>
      <text x="620" y="304" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">ID Peserta: NUS-2026-008 · Peserta Contoh · Angkatan 1</text>

      <text x="620" y="342" fill="#cbd5e1" font-size="13" text-anchor="middle">Telah menyelesaikan evaluasi dan persyaratan kelulusan:</text>
      <text x="620" y="370" fill="#fbbf24" font-size="17" font-weight="800" text-anchor="middle">JALUR PENGOLAHAN AIR MINUM (IPA) - 9 MISI</text>

      <!-- Scores Box -->
      <g transform="translate(180, 400)">
        <rect width="880" height="95" rx="8" fill="#1e293b" stroke="#334155" />
        
        <g transform="translate(35, 16)">
          <text x="75" y="18" fill="#94a3b8" font-size="11" text-anchor="middle">NILAI POST-TEST</text>
          <text x="75" y="46" fill="#34d399" font-size="22" font-weight="800" text-anchor="middle">82 / 100</text>
          <text x="75" y="66" fill="#64748b" font-size="10" text-anchor="middle">Lulus KKM (≥80)</text>
        </g>
        <line x1="225" y1="12" x2="225" y2="82" stroke="#334155" />

        <g transform="translate(250, 16)">
          <text x="75" y="18" fill="#94a3b8" font-size="11" text-anchor="middle">BINTANG &amp; PREDIKAT</text>
          <text x="75" y="46" fill="#fbbf24" font-size="20" font-weight="800" text-anchor="middle">★</text>
          <text x="75" y="66" fill="#f59e0b" font-size="10.5" font-weight="700" text-anchor="middle">Cukup (70–84)</text>
        </g>
        <line x1="445" y1="12" x2="445" y2="82" stroke="#334155" />

        <g transform="translate(470, 16)">
          <text x="75" y="18" fill="#94a3b8" font-size="11" text-anchor="middle">TOTAL XP</text>
          <text x="75" y="46" fill="#38bdf8" font-size="20" font-weight="800" text-anchor="middle">620 XP</text>
          <text x="75" y="66" fill="#64748b" font-size="10" text-anchor="middle">Operator Muda</text>
        </g>
        <line x1="665" y1="12" x2="665" y2="82" stroke="#334155" />

        <g transform="translate(690, 16)">
          <text x="75" y="18" fill="#94a3b8" font-size="11" text-anchor="middle">STATUS BERKAS</text>
          <rect x="15" y="28" width="120" height="26" rx="4" fill="#78350f" />
          <text x="75" y="45" fill="#fef08a" font-size="10.5" font-weight="800" text-anchor="middle">MENUNGGU ACC</text>
          <text x="75" y="66" fill="#f59e0b" font-size="10" text-anchor="middle">Diserahkan Hari Ini</text>
        </g>
      </g>

      <!-- Signatures Preview (Greyed out / Waiting) -->
      <g transform="translate(120, 530)">
        <g transform="translate(40, 0)">
          <text x="120" y="16" fill="#64748b" font-size="11.5" text-anchor="middle">Instruktur Penilai (Validasi Diperlukan),</text>
          <rect x="40" y="30" width="160" height="40" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-dasharray="3,3" />
          <text x="120" y="55" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Menunggu Tinjauan</text>
          <line x1="20" y1="80" x2="220" y2="80" stroke="#475569" stroke-width="1" />
          <text x="120" y="98" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Budi Santoso, S.T.</text>
        </g>

        <g transform="translate(420, 10)">
          <rect x="30" y="10" width="80" height="80" rx="6" fill="#1e293b" stroke="#334155" />
          <text x="70" y="55" fill="#64748b" font-size="10" text-anchor="middle">QR Terkunci</text>
        </g>

        <g transform="translate(700, 0)">
          <text x="130" y="16" fill="#64748b" font-size="11.5" text-anchor="middle">Kepala Balai Diklat,</text>
          <rect x="50" y="30" width="160" height="40" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="3,3" />
          <text x="130" y="55" fill="#64748b" font-size="11" text-anchor="middle">Menunggu Acc Penilai</text>
          <line x1="30" y1="80" x2="230" y2="80" stroke="#475569" stroke-width="1" />
          <text x="130" y="98" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Ir. H. Bambang Sutrisno, M.Eng.</text>
        </g>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

# ==================== L9: INSTRUCTOR DASHBOARD ====================
def generate_l9():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · SPAM", name="Budi Santoso, S.T.", initials="BS")
    title = page_title_block("Dashboard Instruktur &amp; Matriks Progres Peserta", "Pemantauan Kompetensi Siswa · Balai Diklat Air Minum Nusantara · 42 Peserta Aktif (2 Kelompok)", 112)
    
    content = f"""{hdr}{title}
  <!-- Stat Summary Bar (Top Grid, Height 86, Width 1856) -->
  <g transform="translate(32, 175)">
    <!-- Card 1: Total Peserta -->
    <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
    <g transform="translate(24, 20)">
      <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">TOTAL PESERTA LEMBAGA</text>
      <text x="0" y="44" fill="#ffffff" font-size="24" font-weight="800">46 <tspan fill="#38bdf8" font-size="14" font-weight="600">Terdaftar</tspan></text>
      <text x="210" y="44" fill="#34d399" font-size="12" font-weight="600">42 Aktif (14 hr terakhir)</text>
    </g>

    <!-- Card 2: Kelompok Belajar -->
    <g transform="translate(470, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">KELOMPOK BINAAN</text>
        <text x="0" y="44" fill="#38bdf8" font-size="20" font-weight="800">2 Kelompok</text>
        <text x="170" y="44" fill="#94a3b8" font-size="11.5">Angkatan 1 (24) · Angkatan 2 (22)</text>
      </g>
    </g>

    <!-- Card 3: Rata-rata Kenaikan Nilai (T1) -->
    <g transform="translate(940, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#94a3b8" font-size="11.5" font-weight="600">PENINGKATAN PRE-TO-POST (T1)</text>
        <text x="0" y="44" fill="#34d399" font-size="24" font-weight="800">+50,5%</text>
        <text x="140" y="44" fill="#64748b" font-size="11.5">Pre 54,2 → Post 81,6 (Target 25%)</text>
      </g>
    </g>

    <!-- Card 4: Piagam & Antrean Approval -->
    <g transform="translate(1410, 0)">
      <rect width="446" height="86" rx="10" fill="url(#cardGrad)" stroke="#f59e0b" stroke-width="1.5" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#fbbf24" font-size="11.5" font-weight="700">STATUS PIAGAM KELULUSAN</text>
        <text x="0" y="44" fill="#34d399" font-size="22" font-weight="800">1 Terbit <tspan fill="#fbbf24" font-size="14" font-weight="600">· 1 Menunggu ACC</tspan></text>
        <rect x="270" y="12" width="130" height="28" rx="6" fill="#f59e0b" />
        <text x="335" y="30" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">SETUJUI SEKARANG</text>
      </g>
    </g>
  </g>

  <!-- Filter & Action Controls Bar (Height 50, Width 1856) -->
  <g transform="translate(32, 275)">
    <rect width="1856" height="50" rx="8" fill="#1e293b" stroke="#334155" />
    <g transform="translate(20, 10)">
      <text x="0" y="20" fill="#94a3b8" font-size="12" font-weight="600">Filter Kelompok:</text>
      <rect x="110" y="2" width="220" height="28" rx="4" fill="#0284c7" />
      <text x="220" y="20" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Semua Kelompok (46 Siswa) ▾</text>

      <rect x="345" y="2" width="180" height="28" rx="4" fill="#0f172a" stroke="#334155" />
      <text x="435" y="20" fill="#cbd5e1" font-size="11" text-anchor="middle">Angkatan 2 - Operator IPA</text>

      <rect x="540" y="2" width="200" height="28" rx="4" fill="#0f172a" stroke="#334155" />
      <text x="640" y="20" fill="#cbd5e1" font-size="11" text-anchor="middle">Angkatan 1 - Operator Terpadu</text>

      <!-- Action Buttons on Right -->
      <g transform="translate(1320, 0)">
        <rect width="140" height="30" rx="6" fill="#0f172a" stroke="#38bdf8" />
        <text x="70" y="19" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Ekspor Nilai (CSV)</text>

        <rect x="155" y="0" width="170" height="30" rx="6" fill="#0284c7" />
        <text x="240" y="19" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Replay Sesi Skenario (L11)</text>

        <rect x="340" y="0" width="160" height="30" rx="6" fill="#f59e0b" />
        <text x="420" y="19" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">Verifikasi Piagam (L8b)</text>
      </g>
    </g>
  </g>

  <!-- Main Progress Table PRD §7 Catalog (Width 1856, Height 700) -->
  <g transform="translate(32, 340)">
    <rect width="1856" height="700" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <!-- TABLE HEADER -->
    <g transform="translate(20, 16)">
      <rect width="1816" height="42" rx="6" fill="#0f172a" />
      <text x="24" y="26" fill="#64748b" font-size="11" font-weight="700">PESERTA &amp; AKUN DEMO</text>
      <text x="240" y="26" fill="#64748b" font-size="11" font-weight="700">KELOMPOK / JALUR</text>
      <text x="430" y="26" fill="#64748b" font-size="11" font-weight="700">PRE / POST</text>
      <text x="560" y="26" fill="#64748b" font-size="11" font-weight="700">MATRIKS PROGRES MISI PRD §7 (IPA-01 s/d IPA-09 / DST)</text>
      <text x="1360" y="26" fill="#64748b" font-size="11" font-weight="700">BINTANG</text>
      <text x="1460" y="26" fill="#64748b" font-size="11" font-weight="700">TOTAL XP</text>
      <text x="1590" y="26" fill="#64748b" font-size="11" font-weight="700">LEVEL</text>
      <text x="1710" y="26" fill="#64748b" font-size="11" font-weight="700">STATUS PIAGAM</text>
    </g>

    <!-- ROW 1: Andi Kurniawan (peserta.lulus) -->
    <g transform="translate(20, 68)">
      <rect width="1816" height="74" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
      
      <!-- Participant Info -->
      <circle cx="36" cy="37" r="16" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
      <text x="36" y="42" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">AK</text>
      <text x="64" y="30" fill="#ffffff" font-size="13" font-weight="700">Andi Kurniawan <tspan fill="#fbbf24" font-size="10.5">(peserta.lulus)</tspan></text>
      <text x="64" y="48" fill="#94a3b8" font-size="10.5">ID: NUS-2026-004 · Terakhir login 2 jam lalu</text>

      <text x="240" y="30" fill="#cbd5e1" font-size="11.5" font-weight="600">Angkatan 1</text>
      <text x="240" y="48" fill="#38bdf8" font-size="10.5">Jalur Terpadu (17 Misi Lulus)</text>

      <text x="430" y="30" fill="#94a3b8" font-size="11">Pre: <tspan fill="#ffffff" font-weight="600">62</tspan> / Post: <tspan fill="#34d399" font-weight="700">96</tspan></text>
      <text x="430" y="48" fill="#34d399" font-size="10.5">Δ +54,8% (Lulus KKM 80)</text>

      <!-- Matrix of 9 Missions: All Passed 3 Stars -->
      <g transform="translate(560, 20)">
        <g transform="translate(0,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-01</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(82,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-02</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(164,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-03</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(246,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-04</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(328,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-05</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(410,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-06</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(492,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-07</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(574,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-08</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(656,0)"><rect width="90" height="34" rx="4" fill="#065f46" /><text x="45" y="16" fill="#34d399" font-size="9" font-weight="800" text-anchor="middle">TRP-02 (Ujian)</text><text x="45" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
      </g>

      <text x="1360" y="42" fill="#fbbf24" font-size="14" font-weight="700">48 ★</text>
      <text x="1460" y="42" fill="#38bdf8" font-size="14" font-weight="700">3.820 XP</text>
      
      <rect x="1580" y="24" width="105" height="26" rx="4" fill="#581c87" />
      <text x="1632" y="41" fill="#d8b4fe" font-size="10.5" font-weight="700" text-anchor="middle">Operator Ahli</text>

      <rect x="1700" y="24" width="95" height="26" rx="4" fill="#065f46" />
      <text x="1747" y="41" fill="#34d399" font-size="10.5" font-weight="700" text-anchor="middle">Piagam Terbit ✓</text>
    </g>

    <!-- ROW 2: Dimas Wahyu Pratama (peserta.ipa) -->
    <g transform="translate(20, 150)">
      <rect width="1816" height="74" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      
      <circle cx="36" cy="37" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="36" y="42" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">DW</text>
      <text x="64" y="30" fill="#38bdf8" font-size="13" font-weight="700">Dimas Wahyu Pratama <tspan fill="#34d399" font-size="10.5">(peserta.ipa)</tspan></text>
      <text x="64" y="48" fill="#94a3b8" font-size="10.5">ID: NUS-2026-012 · Sesi terakhir: IPA-06 (Skor 88)</text>

      <text x="240" y="30" fill="#cbd5e1" font-size="11.5" font-weight="600">Angkatan 2</text>
      <text x="240" y="48" fill="#38bdf8" font-size="10.5">Jalur IPA (7 dari 9 Misi Lulus)</text>

      <text x="430" y="30" fill="#94a3b8" font-size="11">Pre: <tspan fill="#ffffff" font-weight="600">56</tspan> / Post: <tspan fill="#64748b">Belum</tspan></text>
      <text x="430" y="48" fill="#f59e0b" font-size="10.5">77,8% Jalur Selesai</text>

      <!-- Matrix of 9 Missions: 14 Stars total (3, 2, 2, 2, 2, 2, 1, 0, 0) -->
      <g transform="translate(560, 20)">
        <g transform="translate(0,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-01</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(82,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-02</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(164,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-03</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(246,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-04</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(328,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-05</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(410,0)"><rect width="76" height="34" rx="4" fill="#065f46" stroke="#38bdf8" /><text x="38" y="16" fill="#38bdf8" font-size="9" font-weight="800" text-anchor="middle">IPA-06</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(492,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">IPA-07</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(574,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#f59e0b" /><text x="38" y="16" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">IPA-08</text><text x="38" y="28" fill="#94a3b8" font-size="9" text-anchor="middle">Buka</text></g>
        <g transform="translate(656,0)"><rect width="90" height="34" rx="4" fill="#0f172a" stroke="#334155" /><text x="45" y="16" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">IPA-09 (Ujian)</text><text x="45" y="28" fill="#64748b" font-size="9" text-anchor="middle">Kunci</text></g>
      </g>

      <text x="1360" y="42" fill="#fbbf24" font-size="14" font-weight="700">14 ★</text>
      <text x="1460" y="42" fill="#38bdf8" font-size="14" font-weight="700">820 XP</text>
      
      <rect x="1580" y="24" width="105" height="26" rx="4" fill="#1e3a8a" />
      <text x="1632" y="41" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

      <rect x="1700" y="24" width="95" height="26" rx="4" fill="#1e293b" stroke="#64748b" />
      <text x="1747" y="41" fill="#94a3b8" font-size="10" text-anchor="middle">Belum Memenuhi</text>
    </g>

    <!-- ROW 3: Siti Rahmawati (peserta.distribusi) -->
    <g transform="translate(20, 232)">
      <rect width="1816" height="74" rx="6" fill="#1e293b" stroke="#334155" />
      
      <circle cx="36" cy="37" r="16" fill="#334155" />
      <text x="36" y="42" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">SR</text>
      <text x="64" y="30" fill="#ffffff" font-size="13" font-weight="600">Siti Rahmawati <tspan fill="#94a3b8" font-size="10.5">(peserta.distribusi)</tspan></text>
      <text x="64" y="48" fill="#94a3b8" font-size="10.5">ID: NUS-2026-015 · Sesi terakhir: DST-05 (Skor 86)</text>

      <text x="240" y="30" fill="#cbd5e1" font-size="11.5" font-weight="600">Angkatan 2</text>
      <text x="240" y="48" fill="#38bdf8" font-size="10.5">Jalur Distribusi (5 dari 7 Misi)</text>

      <text x="430" y="30" fill="#94a3b8" font-size="11">Pre: <tspan fill="#ffffff" font-weight="600">58</tspan> / Post: <tspan fill="#64748b">Belum</tspan></text>
      <text x="430" y="48" fill="#f59e0b" font-size="10.5">71,4% Jalur Selesai</text>

      <!-- Matrix: Distribution Track (DST-01 to DST-07) -->
      <g transform="translate(560, 20)">
        <g transform="translate(0,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DST-01</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★★</text></g>
        <g transform="translate(82,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DST-02</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(164,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DST-03</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(246,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DST-04</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(328,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">DST-05</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(410,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#f59e0b" /><text x="38" y="16" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">DST-06</text><text x="38" y="28" fill="#94a3b8" font-size="9" text-anchor="middle">Buka</text></g>
        <g transform="translate(492,0)"><rect width="90" height="34" rx="4" fill="#0f172a" stroke="#334155" /><text x="45" y="16" fill="#64748b" font-size="9" font-weight="600" text-anchor="middle">DST-07 (Ujian)</text><text x="45" y="28" fill="#64748b" font-size="9" text-anchor="middle">Kunci</text></g>
      </g>

      <text x="1360" y="42" fill="#fbbf24" font-size="14" font-weight="700">12 ★</text>
      <text x="1460" y="42" fill="#38bdf8" font-size="14" font-weight="700">750 XP</text>
      
      <rect x="1580" y="24" width="105" height="26" rx="4" fill="#1e3a8a" />
      <text x="1632" y="41" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

      <rect x="1700" y="24" width="95" height="26" rx="4" fill="#1e293b" stroke="#64748b" />
      <text x="1747" y="41" fill="#94a3b8" font-size="10" text-anchor="middle">Belum Memenuhi</text>
    </g>

    <!-- ROW 4: Rian Hidayat (peserta contoh - Angkatan 1 - PENDING APPROVAL) -->
    <g transform="translate(20, 314)">
      <rect width="1816" height="74" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
      
      <circle cx="36" cy="37" r="16" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
      <text x="36" y="42" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">RH</text>
      <text x="64" y="30" fill="#ffffff" font-size="13" font-weight="600">Rian Hidayat <tspan fill="#f59e0b" font-size="10.5">(peserta contoh · Angkatan 1)</tspan></text>
      <text x="64" y="48" fill="#94a3b8" font-size="10.5">ID: NUS-2026-008 · Telah menyelesaikan seluruh 9 misi IPA</text>

      <text x="240" y="30" fill="#cbd5e1" font-size="11.5" font-weight="600">Angkatan 1</text>
      <text x="240" y="48" fill="#38bdf8" font-size="10.5">Jalur IPA (9 dari 9 Misi Selesai)</text>

      <text x="430" y="30" fill="#94a3b8" font-size="11">Pre: <tspan fill="#ffffff" font-weight="600">54</tspan> / Post: <tspan fill="#34d399" font-weight="700">82</tspan></text>
      <text x="430" y="48" fill="#34d399" font-size="10.5">Δ +51,9% (Lulus KKM 80)</text>

      <!-- Matrix 9 Missions: All 9 Passed (Total 10 Stars) -->
      <g transform="translate(560, 20)">
        <g transform="translate(0,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-01</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★★☆</text></g>
        <g transform="translate(82,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-02</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(164,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-03</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(246,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-04</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(328,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-05</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(410,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-06</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(492,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-07</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(574,0)"><rect width="76" height="34" rx="4" fill="#065f46" /><text x="38" y="16" fill="#34d399" font-size="9" text-anchor="middle">IPA-08</text><text x="38" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
        <g transform="translate(656,0)"><rect width="90" height="34" rx="4" fill="#065f46" stroke="#f59e0b" stroke-width="1.5" /><text x="45" y="16" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">IPA-09 (Ujian)</text><text x="45" y="28" fill="#fbbf24" font-size="9" text-anchor="middle">★☆☆</text></g>
      </g>

      <text x="1360" y="42" fill="#fbbf24" font-size="14" font-weight="700">10 ★</text>
      <text x="1460" y="42" fill="#38bdf8" font-size="14" font-weight="700">620 XP</text>
      
      <rect x="1580" y="24" width="105" height="26" rx="4" fill="#1e3a8a" />
      <text x="1632" y="41" fill="#93c5fd" font-size="10.5" font-weight="700" text-anchor="middle">Operator Muda</text>

      <rect x="1700" y="24" width="95" height="26" rx="4" fill="#78350f" stroke="#f59e0b" />
      <text x="1747" y="41" fill="#fef08a" font-size="10" font-weight="800" text-anchor="middle">Tinjau &amp; ACC ▾</text>
    </g>

    <!-- ROW 5: Budi Baru (peserta.baru) -->
    <g transform="translate(20, 396)">
      <rect width="1816" height="74" rx="6" fill="#0f172a" stroke="#334155" />
      
      <circle cx="36" cy="37" r="16" fill="#1e293b" />
      <text x="36" y="42" fill="#64748b" font-size="11" text-anchor="middle">BB</text>
      <text x="64" y="30" fill="#94a3b8" font-size="13" font-weight="600">Budi Baru <tspan fill="#64748b" font-size="10.5">(peserta.baru)</tspan></text>
      <text x="64" y="48" fill="#64748b" font-size="10.5">ID: NUS-2026-030 · Siswa baru, belum memulai skenario</text>

      <text x="240" y="30" fill="#64748b" font-size="11.5">Angkatan 2</text>
      <text x="240" y="48" fill="#64748b" font-size="10.5">Jalur Belum Dipilih</text>

      <text x="430" y="30" fill="#64748b" font-size="11">Pre: <tspan fill="#ffffff" font-weight="600">52</tspan> / Post: -</text>
      <text x="430" y="48" fill="#64748b" font-size="10.5">Pre-test selesai</text>

      <!-- Matrix: All Locked -->
      <g transform="translate(560, 20)">
        <g transform="translate(0,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-01 (Kunci)</text></g>
        <g transform="translate(82,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-02</text></g>
        <g transform="translate(164,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-03</text></g>
        <g transform="translate(246,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-04</text></g>
        <g transform="translate(328,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-05</text></g>
        <g transform="translate(410,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-06</text></g>
        <g transform="translate(492,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-07</text></g>
        <g transform="translate(574,0)"><rect width="76" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="38" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-08</text></g>
        <g transform="translate(656,0)"><rect width="90" height="34" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2" /><text x="45" y="21" fill="#64748b" font-size="9" text-anchor="middle">IPA-09 (Ujian)</text></g>
      </g>

      <text x="1360" y="42" fill="#64748b" font-size="14">0 ★</text>
      <text x="1460" y="42" fill="#64748b" font-size="14">0 XP</text>
      
      <rect x="1580" y="24" width="105" height="26" rx="4" fill="#334155" />
      <text x="1632" y="41" fill="#94a3b8" font-size="10.5" text-anchor="middle">Operator Magang</text>

      <rect x="1700" y="24" width="95" height="26" rx="4" fill="#0f172a" stroke="#334155" />
      <text x="1747" y="41" fill="#64748b" font-size="10" text-anchor="middle">Belum Mulai</text>
    </g>

    <!-- SUMMARY ROW: +41 Peserta Contoh Lainnya -->
    <g transform="translate(20, 480)">
      <rect width="1816" height="50" rx="6" fill="#0f172a" stroke="#1e293b" />
      <text x="36" y="30" fill="#38bdf8" font-size="12" font-weight="700">+ 41 Peserta Contoh Lainnya</text>
      <text x="240" y="30" fill="#94a3b8" font-size="11.5">Angkatan 1 (22 siswa aktif) dan Angkatan 2 (19 siswa aktif) · Berada di rentang 80 s/d 580 XP</text>
      <text x="1360" y="30" fill="#fbbf24" font-size="12" font-weight="700">Rata-rata: 7,4 ★</text>
      <text x="1460" y="30" fill="#38bdf8" font-size="12" font-weight="700">Rata-rata: 420 XP</text>
      <text x="1710" y="30" fill="#64748b" font-size="11">Total: 46 Siswa</text>
    </g>

    <!-- INSTRUCTOR HELPER FOOTER -->
    <g transform="translate(20, 545)">
      <rect width="1816" height="135" rx="8" fill="#1e293b" stroke="#334155" />
      <g transform="translate(24, 20)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">Panduan Tindakan Evaluasi Instruktur:</text>
        <text x="0" y="38" fill="#cbd5e1" font-size="11.5">1. <tspan fill="#fbbf24" font-weight="700">Verifikasi Piagam (Rian Hidayat):</tspan> Siswa telah menuntaskan seluruh 9 misi IPA dan post-test 82. Klik tombol "Tinjau &amp; ACC" untuk menyetujui penerbitan Piagam SSA/NUS/2026/0002.</text>
        <text x="0" y="60" fill="#cbd5e1" font-size="11.5">2. <tspan fill="#38bdf8" font-weight="700">Replay Sesi (Dimas Wahyu Pratama):</tspan> Pada skenario IPA-06, Dimas berhasil mengatasi lonjakan kekeruhan 45 NTU dalam 6 menit 20 detik (Respons 25s, Skor 88, 2★). Tinjau rekaman SCADA di menu Replay.</text>
        <text x="0" y="82" fill="#cbd5e1" font-size="11.5">3. <tspan fill="#34d399" font-weight="700">Ekspor Portofolio Nilai:</tspan> Unduh berkas CSV rekapitulasi nilai 4 komponen (Stabilitas Mutu, Waktu Respons, Efisiensi Kimia, Prosedur Alarm) untuk arsip sertifikasi Balai Diklat.</text>
      </g>
    </g>
  </g>"""
    return svg_wrap(content)

def main():
    generators = [
        ("mockup_l7_badges_leaderboard.svg", generate_l7),
        ("mockup_l8_certificate.svg", generate_l8),
        ("mockup_l8b_certificate_pending.svg", generate_l8b),
        ("mockup_l9_instructor_dashboard.svg", generate_l9),
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
            sys.exit(1)

if __name__ == "__main__":
    main()

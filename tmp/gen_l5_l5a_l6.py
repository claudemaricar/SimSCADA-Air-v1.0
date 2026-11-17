#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 3: L5, L5a, L6
"""
import os
import sys

OUTPUT_DIR = "public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

def generate_l5():
    content = f"""  <!-- Simulator Custom Header PRD §6 & §9 -->
  <g transform="translate(0, 40)">
    <rect width="1600" height="66" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
    
    <!-- Tenant Branding -->
    <g transform="translate(24, 11)">
      <rect width="44" height="44" rx="10" fill="#0284c7" />
      <path d="M 22 10 C 22 10, 14 22, 14 28 A 8 8 0 0 0 30 28 C 30 22, 22 10, 22 10 Z" fill="#ffffff" />
      <text x="56" y="20" fill="#f8fafc" font-size="16" font-weight="700">Balai Diklat Air Minum Nusantara</text>
      <text x="56" y="37" fill="#38bdf8" font-size="11" font-weight="500">Misi IPA-06: Gangguan Lonjakan Kekeruhan Air Baku (Tingkat 3 Sulit)</text>
    </g>

    <!-- Center Status: Timer & Score PRD §9 -->
    <g transform="translate(760, 14)">
      <rect width="140" height="38" rx="8" fill="#0f172a" stroke="#334155" />
      <text x="16" y="24" fill="#94a3b8" font-size="11">⏱️ Waktu:</text>
      <text x="70" y="25" fill="#f8fafc" font-size="16" font-weight="700" font-family="monospace">08:30</text>

      <rect x="155" width="165" height="38" rx="8" fill="#0c2538" stroke="#0284c7" />
      <text x="170" y="24" fill="#38bdf8" font-size="11">Skor Sementara:</text>
      <text x="272" y="25" fill="#38bdf8" font-size="17" font-weight="700">88 <tspan font-size="11">/ 100</tspan></text>
    </g>

    <!-- Header Right Buttons: Hint (-5 Poin) & Selesai -->
    <g transform="translate(1290, 14)">
      <rect width="140" height="38" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1" />
      <text x="70" y="24" fill="#fbbf24" font-size="11.5" font-weight="600" text-anchor="middle">💡 Petunjuk (−5 pt)</text>

      <rect x="155" width="125" height="38" rx="8" fill="#ef4444" />
      <text x="217" y="24" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">SELESAI MISI</text>
    </g>
  </g>

  <!-- Top Active Alarm Banner PRD §10 (ISA-18.2 Priority Header) -->
  <g transform="translate(32, 116)">
    <rect width="1536" height="42" rx="6" fill="#7c2d12" stroke="#ea580c" stroke-width="1.5" filter="url(#glowAmber)" />
    <!-- Flashing High Alarm Triangle Symbol -->
    <polygon points="24,32 35,12 46,32" fill="#ea580c" stroke="#ffffff" stroke-width="1.5" />
    <text x="35" y="28" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">!</text>
    <text x="56" y="26" fill="#ffffff" font-size="12.5" font-weight="700">ALARM TINGGI: Kekeruhan Air Olahan Masuk Reservoir 3,4 NTU (Batas Permenkes: &lt; 3,0 NTU) · Status: Diakui oleh Operator</text>
    <text x="1520" y="26" fill="#ffedd5" font-size="11" font-weight="600" text-anchor="end">Auto-Clear Aktif setelah Kekeruhan ≤ 2,7 NTU stabil 10 dtk</text>
  </g>

  <!-- Main HMI Process Diagram Area (Left, Width: 1120) -->
  <g transform="translate(32, 168)">
    <rect width="1120" height="570" rx="12" fill="#080e1a" stroke="#1e293b" stroke-width="1.5" />
    
    <!-- Title of Diagram Area -->
    <text x="20" y="26" fill="#94a3b8" font-size="12" font-weight="700">DIAGRAM MIMIC PROSES TERPADU: INSTALASI PENGOLAHAN AIR (IPA) AKTIF</text>
    <rect x="860" y="10" width="240" height="24" rx="12" fill="#1e293b" />
    <text x="980" y="26" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">JALUR IPA · SIKLUS REAL-TIME 1 Hz</text>

    <!-- Process Flow Pipe Lines Behind Units -->
    <path d="M 90 220 L 220 220 L 360 220 L 510 220 L 670 220 L 820 220 L 980 220" fill="none" stroke="#0284c7" stroke-width="8" opacity="0.6" />
    <!-- Reduced distribution pipe to the right -->
    <path d="M 980 220 L 1080 220" fill="none" stroke="#334155" stroke-width="6" opacity="0.4" stroke-dasharray="6,4" />

    <!-- 1. INTAKE & AIR BAKU (Active) -->
    <g transform="translate(30, 80)">
      <rect width="150" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="75" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">1. INTAKE SUNGAI</text>
      <line x1="10" y1="34" x2="140" y2="34" stroke="#1e293b" />
      
      <!-- Icon "i" for Narrative Pop-up L5a -->
      <circle cx="132" cy="18" r="8" fill="#0284c7" />
      <text x="132" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="58" fill="#94a3b8" font-size="10">Debit Air Baku:</text>
      <text x="14" y="78" fill="#ffffff" font-size="14" font-weight="700">75,0 <tspan font-size="10" fill="#94a3b8">L/s</tspan></text>

      <text x="14" y="104" fill="#94a3b8" font-size="10">Kekeruhan Baku:</text>
      <text x="14" y="124" fill="#f59e0b" font-size="14" font-weight="700">185 NTU</text>
      <circle cx="120" cy="118" r="6" fill="#f59e0b" />
      <text x="120" y="122" fill="#000" font-size="8" font-weight="800" text-anchor="middle">!</text>

      <line x1="10" y1="140" x2="140" y2="140" stroke="#1e293b" />
      <text x="14" y="160" fill="#94a3b8" font-size="10">Pompa Intake 1:</text>
      <rect x="14" y="168" width="60" height="20" rx="4" fill="#064e3b" />
      <text x="44" y="182" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">RUN (DUTY)</text>

      <text x="14" y="206" fill="#94a3b8" font-size="10">Pompa Intake 2:</text>
      <rect x="14" y="214" width="70" height="20" rx="4" fill="#1e293b" />
      <text x="49" y="228" fill="#94a3b8" font-size="10" text-anchor="middle">STANDBY</text>

      <rect x="14" y="244" width="122" height="24" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="75" y="260" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Reset Pompa ↺</text>
    </g>

    <!-- 2. FLASH MIXER KOAGULASI (Selected Unit -> Pop-up L5a Target) -->
    <g transform="translate(195, 80)">
      <rect width="150" height="280" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" filter="url(#glowCyan)" />
      <text x="75" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">2. KOAGULASI</text>
      <line x1="10" y1="34" x2="140" y2="34" stroke="#1e293b" />

      <!-- Clickable "i" Info Icon -->
      <circle cx="132" cy="18" r="8" fill="#38bdf8" />
      <text x="132" y="22" fill="#0b1120" font-size="9" font-weight="800" text-anchor="middle">i</text>

      <!-- Target indicator for L5a -->
      <rect x="10" y="44" width="130" height="22" rx="4" fill="#0284c7" />
      <text x="75" y="59" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">UNIT TERPILIH 👈</text>

      <text x="14" y="88" fill="#94a3b8" font-size="10">Dosis Koagulan PAC:</text>
      <text x="14" y="108" fill="#38bdf8" font-size="16" font-weight="700">48,0 <tspan font-size="10" fill="#94a3b8">mg/L</tspan></text>
      <text x="14" y="124" fill="#10b981" font-size="9.5">(SOP disesuaikan ↑)</text>

      <text x="14" y="148" fill="#94a3b8" font-size="10">Derajat pH Air:</text>
      <text x="14" y="168" fill="#10b981" font-size="15" font-weight="700">7,20 <tspan font-size="10" fill="#94a3b8">pH</tspan></text>
      <text x="14" y="184" fill="#94a3b8" font-size="9.5">Penyesuai: Kapur Aktif</text>

      <line x1="10" y1="198" x2="140" y2="198" stroke="#1e293b" />
      <text x="14" y="218" fill="#94a3b8" font-size="10">Pengaduk Cepat:</text>
      <rect x="14" y="226" width="122" height="24" rx="4" fill="#064e3b" />
      <text x="75" y="242" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">MOTOR ON (120 RPM)</text>
      <text x="14" y="268" fill="#64748b" font-size="9">Klik "i" buka Narasi Pop-up</text>
    </g>

    <!-- 3. FLOKULASI (Active) -->
    <g transform="translate(360, 80)">
      <rect width="145" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">3. FLOKULASI</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" />
      <text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="58" fill="#94a3b8" font-size="10">Pengaduk Lambat:</text>
      <text x="14" y="78" fill="#ffffff" font-size="13" font-weight="600">3 Kompartemen</text>

      <text x="14" y="104" fill="#94a3b8" font-size="10">Kecepatan Stage 1:</text>
      <text x="14" y="122" fill="#34d399" font-size="12" font-weight="700">45 RPM (Cepat)</text>

      <text x="14" y="146" fill="#94a3b8" font-size="10">Kecepatan Stage 2:</text>
      <text x="14" y="164" fill="#34d399" font-size="12" font-weight="700">30 RPM (Sedang)</text>

      <text x="14" y="188" fill="#94a3b8" font-size="10">Kecepatan Stage 3:</text>
      <text x="14" y="206" fill="#34d399" font-size="12" font-weight="700">15 RPM (Lambat)</text>

      <line x1="10" y1="220" x2="135" y2="220" stroke="#1e293b" />
      <text x="14" y="240" fill="#94a3b8" font-size="10">Kondisi Flok:</text>
      <text x="14" y="258" fill="#34d399" font-size="11" font-weight="700">✓ Terbentuk Sempurna</text>
    </g>

    <!-- 4. SEDIMENTASI TUBE SETTLER -->
    <g transform="translate(520, 80)">
      <rect width="145" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">4. SEDIMENTASI</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" />
      <text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="58" fill="#94a3b8" font-size="10">Kekeruhan Keluar:</text>
      <text x="14" y="78" fill="#f59e0b" font-size="15" font-weight="700">12,4 NTU</text>
      <text x="14" y="94" fill="#34d399" font-size="9.5">Tren: Menurun ↓</text>

      <text x="14" y="118" fill="#94a3b8" font-size="10">Level Selimut Lumpur:</text>
      <text x="14" y="138" fill="#f8fafc" font-size="13" font-weight="600">1,4 Meter</text>

      <line x1="10" y1="155" x2="135" y2="155" stroke="#1e293b" />
      <text x="14" y="175" fill="#94a3b8" font-size="10">Katup Pembuang Lumpur:</text>
      <rect x="14" y="186" width="117" height="34" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="72" y="207" fill="#cbd5e1" font-size="10.5" font-weight="600" text-anchor="middle">BLOWDOWN (BUANG)</text>
      <text x="14" y="240" fill="#64748b" font-size="9.5">Interval berkala aktif</text>
    </g>

    <!-- 5. FILTRASI PASIR CEPAT -->
    <g transform="translate(680, 80)">
      <rect width="145" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">5. FILTRASI CEPAT</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" />
      <text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="58" fill="#94a3b8" font-size="10">Kekeruhan Olahan:</text>
      <text x="14" y="78" fill="#f59e0b" font-size="15" font-weight="700">2,4 NTU</text>
      <text x="14" y="94" fill="#34d399" font-size="9.5">Target &lt; 3 NTU (Pulih)</text>

      <text x="14" y="118" fill="#94a3b8" font-size="10">Headloss Filter 1–4:</text>
      <text x="14" y="138" fill="#f8fafc" font-size="13" font-weight="600">1,8 / 2,5 Meter</text>

      <line x1="10" y1="155" x2="135" y2="155" stroke="#1e293b" />
      <text x="14" y="175" fill="#94a3b8" font-size="10">Pencucian Filter:</text>
      <rect x="14" y="186" width="117" height="34" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="72" y="207" fill="#cbd5e1" font-size="10.5" font-weight="600" text-anchor="middle">MULAI BACKWASH</text>
      <text x="14" y="240" fill="#64748b" font-size="9.5">Backwash F1-F4 siap</text>
    </g>

    <!-- 6. DESINFEKSI & RESERVOIR -->
    <g transform="translate(840, 80)">
      <rect width="145" height="280" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">6. DESINFEKSI &amp; TANK</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" />
      <text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="58" fill="#94a3b8" font-size="10">Dosis Injeksi Klor:</text>
      <text x="14" y="78" fill="#38bdf8" font-size="14" font-weight="700">1,20 <tspan font-size="10" fill="#94a3b8">mg/L</tspan></text>

      <text x="14" y="104" fill="#94a3b8" font-size="10">Sisa Klor Bebas:</text>
      <text x="14" y="124" fill="#10b981" font-size="14" font-weight="700">0,38 <tspan font-size="10" fill="#94a3b8">mg/L</tspan></text>
      <text x="14" y="138" fill="#94a3b8" font-size="9.5">Rentang: 0,2–0,5 mg/L</text>

      <line x1="10" y1="155" x2="135" y2="155" stroke="#1e293b" />
      <text x="14" y="175" fill="#94a3b8" font-size="10">Level Reservoir:</text>
      <text x="14" y="195" fill="#f8fafc" font-size="14" font-weight="700">3,85 Meter (77%)</text>

      <text x="14" y="220" fill="#94a3b8" font-size="10">Valve Masuk / Keluar:</text>
      <text x="14" y="238" fill="#34d399" font-size="11" font-weight="700">BUKA PENUH (100%)</text>
    </g>

    <!-- 7. JARINGAN DISTRIBUSI (DIMMED / NONAKTIF PADA JALUR IPA PRD §9) -->
    <g transform="translate(1000, 80)" opacity="0.35">
      <rect width="105" height="280" rx="8" fill="#090d16" stroke="#475569" stroke-width="1" stroke-dasharray="4,4" />
      <text x="52" y="24" fill="#64748b" font-size="10.5" font-weight="700" text-anchor="middle">7. DISTRIBUSI</text>
      <text x="52" y="38" fill="#ef4444" font-size="9" text-anchor="middle">(NONAKTIF)</text>
      <line x1="8" y1="44" x2="97" y2="44" stroke="#334155" />

      <text x="10" y="66" fill="#64748b" font-size="9">Pompa Dist:</text>
      <text x="10" y="82" fill="#64748b" font-size="10">2 Unit Jalan</text>

      <text x="10" y="106" fill="#64748b" font-size="9">Valve Zona:</text>
      <text x="10" y="122" fill="#64748b" font-size="10">Z1-Z3 Terbuka</text>

      <text x="10" y="146" fill="#64748b" font-size="9">PRV Tekanan:</text>
      <text x="10" y="162" fill="#64748b" font-size="10">2,50 bar</text>

      <line x1="8" y1="180" x2="97" y2="180" stroke="#334155" />
      <text x="52" y="210" fill="#94a3b8" font-size="9" text-anchor="middle">Hanya Aktif</text>
      <text x="52" y="226" fill="#94a3b8" font-size="9" text-anchor="middle">pada Jalur</text>
      <text x="52" y="242" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">Distribusi /</text>
      <text x="52" y="258" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">Terpadu</text>
    </g>

    <!-- Network Monitoring Point PRD §9 (Always Visible) -->
    <g transform="translate(30, 380)">
      <rect width="1075" height="50" rx="8" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="30" fill="#38bdf8" font-size="11.5" font-weight="700">TITIK PANTAU JARINGAN HILIR (PRD §9):</text>
      <text x="290" y="30" fill="#cbd5e1" font-size="11.5">Tekanan Rata-Rata: <tspan fill="#34d399" font-weight="700">2,85 bar</tspan></text>
      <text x="520" y="30" fill="#cbd5e1" font-size="11.5">Debit Total Zona: <tspan fill="#38bdf8" font-weight="700">120,4 L/s</tspan></text>
      <text x="750" y="30" fill="#cbd5e1" font-size="11.5">Sisa Klor Ujung: <tspan fill="#10b981" font-weight="700">0,28 mg/L</tspan> (Permenkes: ≥ 0,2 mg/L ✓)</text>
    </g>

    <!-- Bottom 10-Minute Historical Trend PRD §9 -->
    <g transform="translate(30, 445)">
      <rect width="1075" height="110" rx="8" fill="#090d16" stroke="#1e293b" />
      <text x="16" y="20" fill="#94a3b8" font-size="11" font-weight="700">GRAFIK TREN 10 MENIT: KEKERUHAN AIR BAKU (KUNING) vs KEKERUHAN AIR OLAHAN (CYAN) &amp; DOSIS KOAGULAN (BIRU)</text>
      
      <!-- Trend Curves -->
      <!-- Air Baku: jumps from 15 to 185 at minute 01:15 then stabilizes -->
      <path d="M 40 85 L 140 85 L 180 28 L 600 30 L 750 45 L 1020 70" fill="none" stroke="#f59e0b" stroke-width="2" />
      <!-- Air Olahan: spikes to 3.4 at minute 01:45 then drops to 2.4 -->
      <path d="M 40 92 L 180 92 L 230 42 L 320 55 L 550 78 L 800 86 L 1020 88" fill="none" stroke="#06b6d4" stroke-width="2.5" />
      <!-- Permenkes 3.0 NTU Threshold Line (Red Dash) -->
      <line x1="40" y1="50" x2="1020" y2="50" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
      <text x="1025" y="53" fill="#ef4444" font-size="9" font-weight="700">3 NTU</text>

      <text x="50" y="104" fill="#64748b" font-size="9.5">00:00 (Mulai)</text>
      <text x="180" y="104" fill="#f59e0b" font-size="9.5">01:15 (Lonjakan Baku 185 NTU)</text>
      <text x="450" y="104" fill="#38bdf8" font-size="9.5">02:10 (Dosis Naik 48 mg/L)</text>
      <text x="800" y="104" fill="#34d399" font-size="9.5">06:10 (Pulih &lt;2,7 NTU)</text>
      <text x="980" y="104" fill="#64748b" font-size="9.5">08:30 (Selesai)</text>
    </g>
  </g>

  <!-- Control Panel Right PRD §9 (Width: 400) -->
  <g transform="translate(1168, 168)">
    <rect width="400" height="570" rx="12" fill="url(#cardGrad)" stroke="#38bdf8" stroke-width="1.5" />
    
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="15" font-weight="700">PANEL KENDALI TITIK KONTROL</text>
      <text x="0" y="36" fill="#38bdf8" font-size="12" font-weight="600">Unit Aktif: Flash Mixer Koagulasi</text>
      
      <line x1="0" y1="50" x2="352" y2="50" stroke="#334155" stroke-width="1" />

      <!-- Controller 1: Dosis Koagulan PAC -->
      <g transform="translate(0, 65)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">SETPOINT DOSIS KOAGULAN (PAC):</text>
        <text x="350" y="16" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="end">48,0 mg/L</text>

        <!-- Slider Bar -->
        <rect x="0" y="28" width="352" height="12" rx="6" fill="#0f172a" />
        <rect x="0" y="28" width="260" height="12" rx="6" fill="url(#primaryGrad)" />
        <circle cx="260" cy="34" r="10" fill="#ffffff" stroke="#0284c7" stroke-width="3" />

        <text x="0" y="58" fill="#64748b" font-size="10">Min: 10 mg/L</text>
        <text x="176" y="58" fill="#10b981" font-size="10" text-anchor="middle">SOP Banjir: 45–50 mg/L</text>
        <text x="352" y="58" fill="#64748b" font-size="10" text-anchor="end">Max: 80 mg/L</text>
      </g>

      <!-- Controller 2: Penyesuai pH (Kapur / Soda Ash) -->
      <g transform="translate(0, 150)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">DOSIS PENYESUAI pH (KAPUR):</text>
        <text x="350" y="16" fill="#10b981" font-size="14" font-weight="700" text-anchor="end">8,5 mg/L</text>

        <rect x="0" y="28" width="352" height="12" rx="6" fill="#0f172a" />
        <rect x="0" y="28" width="180" height="12" rx="6" fill="url(#emeraldGrad)" />
        <circle cx="180" cy="34" r="10" fill="#ffffff" stroke="#059669" stroke-width="3" />

        <text x="0" y="58" fill="#64748b" font-size="10">Target pH: 7,20 (Rentang Aman: 6,5–8,5)</text>
      </g>

      <!-- Controller 3: Motor Pengaduk Cepat -->
      <g transform="translate(0, 230)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">MOTOR FLASH MIXER:</text>
        <rect x="0" y="28" width="170" height="38" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1.5" />
        <text x="85" y="52" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">ON (120 RPM)</text>

        <rect x="182" y="28" width="170" height="38" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="267" y="52" fill="#94a3b8" font-size="12" font-weight="600" text-anchor="middle">OFF (STOP)</text>
      </g>

      <!-- Controller 4: PRV & Valve Standar PRD §9 -->
      <g transform="translate(0, 315)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">SETPOINT PRV (TEKANAN JARINGAN):</text>
        <rect x="0" y="26" width="352" height="38" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="50" fill="#ffffff" font-size="13" font-weight="700">2,50 bar</text>
        <text x="336" y="50" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="end">Satuan: Bar (PRD §9)</text>
      </g>

      <!-- Launch Pop-up Narrative L5a Button -->
      <g transform="translate(0, 400)">
        <rect width="352" height="46" rx="8" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.5" />
        <circle cx="28" cy="23" r="10" fill="#38bdf8" />
        <text x="28" y="27" fill="#082f49" font-size="12" font-weight="800" text-anchor="middle">i</text>
        <text x="48" y="28" fill="#ffffff" font-size="12.5" font-weight="700">BUKA NARASI TITIK KONTROL KOAGULASI</text>
        <text x="48" y="40" fill="#7dd3fc" font-size="10">Tanpa pengurangan skor · SOP Lembaga</text>
      </g>

      <text x="176" y="475" fill="#64748b" font-size="10.5" text-anchor="middle">Setiap perubahan setpoint dicatat dalam log audit sesi L11.</text>
    </g>
  </g>

  <!-- Alarm Table ISA-18.2 Bottom Panel PRD §10 (Width: 1536) -->
  <g transform="translate(32, 750)">
    <rect width="1536" height="210" rx="10" fill="#090d16" stroke="#1e293b" stroke-width="1.5" />
    
    <!-- Table Header Bar -->
    <rect width="1536" height="34" rx="10" fill="#0f172a" />
    <text x="20" y="22" fill="#38bdf8" font-size="11" font-weight="700">DAFTAR ALARM SISTEM (4 STATUS STANDAR PRD §10: AKTIF BLM DIAKUI · AKTIF DIAKUI · PULIH BLM CLEAR · CLEAR)</text>

    <!-- Table Columns -->
    <text x="20" y="54" fill="#94a3b8" font-size="10" font-weight="700">WAKTU</text>
    <text x="90" y="54" fill="#94a3b8" font-size="10" font-weight="700">BENTUK / PRIORITAS</text>
    <text x="240" y="54" fill="#94a3b8" font-size="10" font-weight="700">TITIK KONTROL</text>
    <text x="440" y="54" fill="#94a3b8" font-size="10" font-weight="700">PESAN ALARM &amp; NILAI PROSES</text>
    <text x="960" y="54" fill="#94a3b8" font-size="10" font-weight="700">STATUS ALARM</text>
    <text x="1220" y="54" fill="#94a3b8" font-size="10" font-weight="700">AKSI OPERATOR</text>

    <line x1="20" y1="64" x2="1516" y2="64" stroke="#1e293b" />

    <!-- Alarm Row 1: High Alarm (Aktif Diakui) -->
    <g transform="translate(20, 72)">
      <text x="0" y="20" fill="#cbd5e1" font-size="11">01:45</text>
      
      <!-- Triangle Shape -->
      <polygon points="76,22 84,6 92,22" fill="#ea580c" />
      <text x="84" y="20" fill="#fff" font-size="8" font-weight="900" text-anchor="middle">!</text>
      <text x="100" y="20" fill="#ea580c" font-size="11" font-weight="700">TINGGI</text>

      <text x="220" y="20" fill="#ffffff" font-size="11">Filtrasi (Air Olahan)</text>
      <text x="420" y="20" fill="#ffedd5" font-size="11">Kekeruhan air olahan ≥ 3 NTU (Terukur: 3,4 NTU)</text>

      <!-- Status Badge -->
      <rect x="940" y="4" width="130" height="22" rx="4" fill="#451a03" stroke="#d97706" />
      <text x="1005" y="19" fill="#fde68a" font-size="10" font-weight="700" text-anchor="middle">Aktif, Diakui</text>

      <!-- Action Buttons -->
      <rect x="1200" y="4" width="70" height="22" rx="4" fill="#1e293b" />
      <text x="1235" y="19" fill="#64748b" font-size="10" text-anchor="middle">Diakui ✓</text>

      <!-- Disabled Clear button with tooltip message -->
      <rect x="1280" y="4" width="160" height="22" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="1360" y="19" fill="#64748b" font-size="9.5" text-anchor="middle">Clear (Penyebab blm selesai)</text>
    </g>

    <!-- Alarm Row 2: Medium Alarm (Pulih Belum di-Clear) -->
    <g transform="translate(20, 108)">
      <text x="0" y="20" fill="#cbd5e1" font-size="11">01:15</text>
      
      <!-- Circle Shape -->
      <circle cx="84" cy="14" r="8" fill="#f59e0b" />
      <text x="84" y="18" fill="#000" font-size="9" font-weight="800" text-anchor="middle">i</text>
      <text x="100" y="20" fill="#f59e0b" font-size="11" font-weight="700">SEDANG</text>

      <text x="220" y="20" fill="#ffffff" font-size="11">Intake Air Baku</text>
      <text x="420" y="20" fill="#cbd5e1" font-size="11">Kekeruhan air baku tinggi (185 NTU, tren turun ke 25 NTU)</text>

      <!-- Status Badge -->
      <rect x="940" y="4" width="140" height="22" rx="4" fill="#064e3b" stroke="#059669" />
      <text x="1010" y="19" fill="#a7f3d0" font-size="10" font-weight="700" text-anchor="middle">Pulih, Belum di-Clear</text>

      <!-- Clear Button Active -->
      <rect x="1200" y="4" width="90" height="22" rx="4" fill="#059669" />
      <text x="1245" y="19" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">CLEAR MANUAL</text>
    </g>

    <!-- Alarm Row 3: Critical Info Note PRD §10 -->
    <g transform="translate(20, 144)">
      <text x="0" y="20" fill="#64748b" font-size="11">00:00</text>
      <polygon points="76,22 84,6 92,22" fill="#ef4444" />
      <text x="84" y="20" fill="#fff" font-size="8" font-weight="900" text-anchor="middle">!</text>
      <text x="100" y="20" fill="#ef4444" font-size="11" font-weight="700">KRITIS</text>

      <text x="220" y="20" fill="#64748b" font-size="11">Desinfeksi / Pompa</text>
      <text x="420" y="20" fill="#64748b" font-size="11">Sisa klor &lt;0,2 mg/L dan pompa trip memicu alarm Kritis (Terkunci / Latched: Reset Pompa lalu Clear)</text>
      <text x="940" y="20" fill="#64748b" font-size="10">Kondisi Normal</text>
      <text x="1200" y="20" fill="#64748b" font-size="10">Standar ISA-18.2</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L5: WORKSPACE SIMULATOR SCADA HMI (SimSCADA-Air v1.0)")

def generate_l5a():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Pop-Up Narasi Titik Kontrol: Koagulasi", "6 Bagian Lengkap PRD §9 + Catatan SOP Lokal Lembaga · Akses 'i' Tidak Mengurangi Skor", 120)

    content = f"""{hdr}
{title}

  <!-- Underneath Backdrop: Dimmed SCADA Workspace to show pop-up context -->
  <rect x="32" y="185" width="1536" height="775" rx="14" fill="#050a14" opacity="0.8" stroke="#1e293b" />
  
  <!-- Interactive Cursor Tooltip on SCADA Mimic PRD §9 -->
  <g transform="translate(100, 210)">
    <rect width="280" height="52" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" filter="url(#dropShadow)" />
    <text x="14" y="22" fill="#38bdf8" font-size="11" font-weight="700">KURSOR DIARAHKAN KE TITIK KONTROL:</text>
    <text x="14" y="40" fill="#ffffff" font-size="12">Flash Mixer Koagulasi · 48 mg/L PAC · pH 7,20</text>
    <polygon points="60,52 70,62 80,52" fill="#1e293b" />
  </g>

  <!-- Main Modal Container (6 Sections PRD §9, Width: 1100, Centered at x=250, y=190) -->
  <g transform="translate(250, 190)" filter="url(#dropShadow)">
    <rect width="1100" height="770" rx="16" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="2.5" />
    
    <!-- Modal Header -->
    <g transform="translate(32, 24)">
      <rect width="40" height="40" rx="10" fill="#0284c7" />
      <text x="20" y="27" fill="#ffffff" font-size="20" font-weight="800" text-anchor="middle">i</text>
      
      <text x="56" y="22" fill="#ffffff" font-size="19" font-weight="700">NARASI TITIK KONTROL: KOAGULASI &amp; PENGADUK CEPAT</text>
      <text x="56" y="38" fill="#38bdf8" font-size="12">Unit Proses Utama IPA · Akses informasi ini tidak mengurangi nilai evaluasi Anda</text>

      <!-- Close Button "X" -->
      <rect x="990" y="0" width="36" height="36" rx="8" fill="#1e293b" stroke="#334155" />
      <text x="1008" y="24" fill="#94a3b8" font-size="16" font-weight="700" text-anchor="middle">✕</text>

      <line x1="0" y1="52" x2="1036" y2="52" stroke="#334155" stroke-width="1" />
    </g>

    <!-- 6 SECTIONS OF PRD §9 (2 Column Layout) -->
    
    <!-- LEFT COLUMN (Sections 1, 2, 3) -->
    <g transform="translate(32, 90)">
      
      <!-- 1. APA INI (+ SKEMA VEKTOR) -->
      <g transform="translate(0, 0)">
        <rect width="500" height="175" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">1. APA INI (DEFINISI &amp; SKEMA PROSES):</text>
        <text x="16" y="44" fill="#cbd5e1" font-size="11.5" line-height="1.4">Unit pembubuhan bahan kimia koagulan (PAC/Tawas) disertai pengadukan</text>
        <text x="16" y="62" fill="#cbd5e1" font-size="11.5">cepat (flash mixing) untuk mendestabilisasi muatan listrik partikel koloid</text>
        <text x="16" y="80" fill="#cbd5e1" font-size="11.5">penyebab kekeruhan agar dapat bergabung membentuk flok.</text>

        <!-- Schematic Diagram Box -->
        <g transform="translate(16, 92)">
          <rect width="468" height="68" rx="6" fill="#090d16" stroke="#334155" />
          <!-- Pipe Inflow -->
          <line x1="20" y1="34" x2="140" y2="34" stroke="#0284c7" stroke-width="4" />
          <text x="30" y="24" fill="#7dd3fc" font-size="9.5">Air Baku (Intake)</text>
          <!-- Dosing Point -->
          <circle cx="160" cy="18" r="8" fill="#f59e0b" />
          <line x1="160" y1="26" x2="160" y2="34" stroke="#f59e0b" stroke-width="2" />
          <text x="160" y="10" fill="#f59e0b" font-size="9" text-anchor="middle">Injeksi PAC</text>
          <!-- Flash Mixer Impeller -->
          <rect x="200" y="15" width="60" height="38" rx="4" fill="#1e293b" stroke="#0284c7" />
          <text x="230" y="32" fill="#38bdf8" font-size="9" text-anchor="middle">Impeller</text>
          <text x="230" y="44" fill="#fff" font-size="8.5" text-anchor="middle">120 RPM</text>
          <!-- Pipe Outflow to Flocculator -->
          <line x1="260" y1="34" x2="440" y2="34" stroke="#0284c7" stroke-width="4" />
          <text x="320" y="24" fill="#34d399" font-size="9.5">Ke Bak Flokulasi ➔</text>
        </g>
      </g>

      <!-- 2. YANG DIPANTAU (PARAMETER, SATUAN, RENTANG, SAAT INI) -->
      <g transform="translate(0, 190)">
        <rect width="500" height="185" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">2. YANG DIPANTAU (MONITORED PARAMETERS):</text>
        
        <!-- Table PRD §9 -->
        <g transform="translate(16, 32)">
          <rect width="468" height="24" rx="4" fill="#1e293b" />
          <text x="10" y="16" fill="#94a3b8" font-size="10" font-weight="700">PARAMETER</text>
          <text x="150" y="16" fill="#94a3b8" font-size="10" font-weight="700">RENTANG NORMAL</text>
          <text x="320" y="16" fill="#94a3b8" font-size="10" font-weight="700">NILAI SAAT INI</text>

          <text x="10" y="44" fill="#cbd5e1" font-size="11">Kekeruhan Baku</text>
          <text x="150" y="44" fill="#cbd5e1" font-size="11">15 – 50 NTU</text>
          <text x="320" y="44" fill="#f59e0b" font-size="11" font-weight="700">185 NTU (Tinggi!)</text>

          <text x="10" y="70" fill="#cbd5e1" font-size="11">Dosis Koagulan</text>
          <text x="150" y="70" fill="#cbd5e1" font-size="11">15 – 50 mg/L</text>
          <text x="320" y="70" fill="#38bdf8" font-size="11" font-weight="700">48,0 mg/L (Dinaikkan)</text>

          <text x="10" y="96" fill="#cbd5e1" font-size="11">Derajat pH</text>
          <text x="150" y="96" fill="#cbd5e1" font-size="11">6,5 – 8,5 (Permenkes)</text>
          <text x="320" y="96" fill="#10b981" font-size="11" font-weight="700">7,20 pH (Normal ✓)</text>

          <text x="10" y="122" fill="#cbd5e1" font-size="11">Kecepatan Mixer</text>
          <text x="150" y="122" fill="#cbd5e1" font-size="11">100 – 150 RPM</text>
          <text x="320" y="122" fill="#34d399" font-size="11" font-weight="700">120 RPM (Aktif)</text>
        </g>
      </g>

      <!-- 3. YANG BISA DIKENDALIKAN -->
      <g transform="translate(0, 390)">
        <rect width="500" height="135" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">3. YANG BISA DIKENDALIKAN (CONTROLS):</text>
        <text x="16" y="46" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#38bdf8">Setpoint Dosis Koagulan:</tspan> Mengatur output stroke pompa dosing PAC.</text>
        <text x="16" y="68" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#10b981">Dosis Penyesuai pH:</tspan> Injeksi larutan kapur jika pH air baku drop &lt;6,5.</text>
        <text x="16" y="90" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#f59e0b">Saklar On/Off Mixer:</tspan> Memastikan pengadukan cepat seketika saat injeksi.</text>
      </g>
    </g>

    <!-- RIGHT COLUMN (Sections 4, 5, 6 + Catatan SOP Lokal Lembaga) -->
    <g transform="translate(564, 90)">
      
      <!-- 4. DAMPAK KE HILIR -->
      <g transform="translate(0, 0)">
        <rect width="504" height="130" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">4. DAMPAK KE HILIR (DOWNSTREAM IMPACT):</text>
        <text x="16" y="44" fill="#cbd5e1" font-size="11.5">• <tspan font-weight="700" fill="#ef4444">Underdosing:</tspan> Flok tidak terbentuk sempurna, kekeruhan lolos melewati bak sedimentasi dan membebani filter pasir hingga jenuh seketika.</text>
        <text x="16" y="82" fill="#cbd5e1" font-size="11.5">• <tspan font-weight="700" fill="#f59e0b">Overdosing:</tspan> Pemborosan bahan kimia, pH air olahan anjlok tajam, dan timbulan lumpur berlebih yang mempercepat sedimentasi meluap.</text>
      </g>

      <!-- 5. GANGGUAN UMUM & SOP SINGKAT -->
      <g transform="translate(0, 145)">
        <rect width="504" height="155" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">5. GANGGUAN UMUM &amp; SOP SINGKAT (PRD §9 &amp; §10):</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="11.5">1. <tspan font-weight="700" fill="#ffffff">Lonjakan Kekeruhan Air Baku:</tspan> Segera naikkan dosis PAC bertahap (misal 20 ke 48 mg/L) berdasarkan tabel kurva jar test.</text>
        <text x="16" y="74" fill="#cbd5e1" font-size="11.5">2. <tspan font-weight="700" fill="#ffffff">Pompa Dosing Macet/Buntu:</tspan> Pindahkan ke pompa injeksi cadangan (standby) dan lakukan flushing pipa injeksi.</text>
        <text x="16" y="102" fill="#cbd5e1" font-size="11.5">3. <tspan font-weight="700" fill="#ffffff">pH Drop:</tspan> Tambahkan pembubuhan kapur untuk mempertahankan pH 6,5–8,5.</text>
      </g>

      <!-- 6. PELAJARI LEBIH LANJUT -->
      <g transform="translate(0, 315)">
        <rect width="504" height="60" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">6. PELAJARI LEBIH LANJUT:</text>
        <text x="16" y="44" fill="#cbd5e1" font-size="11">Modul Teori IPA-03 (Koagulasi) &amp; Standar Permenkes No. 2/2023 Bab II</text>
      </g>

      <!-- KOTAK KHUSUS: CATATAN SOP LOKAL LEMBAGA PRD §9 -->
      <g transform="translate(0, 390)">
        <rect width="504" height="135" rx="10" fill="#064e3b" opacity="0.5" stroke="#059669" stroke-width="1.5" />
        <text x="16" y="24" fill="#a7f3d0" font-size="12" font-weight="700">🏢 CATATAN SOP LOKAL LEMBAGA (BALAI NUSANTARA):</text>
        <text x="16" y="48" fill="#ffffff" font-size="11.5" font-weight="500">"Di instalasi latih IPA Balai Nusantara, injeksi koagulan memakai</text>
        <text x="16" y="68" fill="#ffffff" font-size="11.5" font-weight="500">dosing pump membran otomatis dengan kalibrasi larutan PAC 10%.</text>
        <text x="16" y="88" fill="#ffffff" font-size="11.5" font-weight="500">Batas minimum tangki harian PAC adalah 20% sebelum pengisian ulang."</text>
        <text x="16" y="114" fill="#6ee7b7" font-size="10">Dikonfigurasi oleh Admin Lembaga di Layar L13</text>
      </g>
    </g>

    <!-- Modal Footer -->
    <g transform="translate(32, 640)">
      <line x1="0" y1="0" x2="1036" y2="0" stroke="#334155" stroke-width="1" />
      <text x="0" y="28" fill="#94a3b8" font-size="12">Membuka narasi ini dicatat dalam sistem untuk syarat perolehan Lencana <tspan fill="#38bdf8" font-weight="700">"Penjelajah Titik Kontrol"</tspan> (PRD §8).</text>
      
      <rect x="850" y="10" width="186" height="40" rx="8" fill="#0284c7" />
      <text x="943" y="35" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">KEMBALI KE WORKSPACE</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L5a: POP-UP NARASI TITIK KONTROL KOAGULASI (SimSCADA-Air v1.0)")

def generate_l6():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Hasil Evaluasi Simulasi &amp; Umpan Balik Skor", "Sesi Konsisten: IPA-06 Gangguan Lonjakan Kekeruhan Air Baku (Durasi 08:30) · PRD §8", 120)

    content = f"""{hdr}
{title}

  <!-- Left Main Column: 4 Component Score & Mentor Debriefing (Width: 960) -->
  <g transform="translate(32, 190)">
    <rect width="960" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 28)">
      <!-- Mission Outcome Header -->
      <rect width="130" height="26" rx="6" fill="#059669" />
      <text x="65" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">MISI SELESAI: LULUS</text>
      
      <text x="145" y="18" fill="#ffffff" font-size="18" font-weight="700">IPA-06: Gangguan Lonjakan Kekeruhan Air Baku</text>

      <!-- Overall Score Display PRD §8 -->
      <g transform="translate(0, 45)">
        <rect width="896" height="105" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
        
        <!-- Big Score Number -->
        <text x="32" y="65" fill="#38bdf8" font-size="52" font-weight="800">88 <tspan font-size="20" fill="#94a3b8">/ 100</tspan></text>
        <text x="32" y="90" fill="#34d399" font-size="14" font-weight="700">PREDIKAT: LULUS DENGAN BAIK</text>

        <!-- Stars (85-94 = 2 Stars) -->
        <g transform="translate(330, 26)">
          <text x="0" y="24" fill="#94a3b8" font-size="11" font-weight="700">PEROLEHAN BINTANG (PRD §8):</text>
          <text x="0" y="58" fill="#f59e0b" font-size="34">★★☆</text>
          <text x="0" y="78" fill="#94a3b8" font-size="10.5">2 Bintang (Rentang Skor 85–94)</text>
        </g>

        <!-- XP Multiplier Box -->
        <g transform="translate(620, 26)">
          <text x="0" y="24" fill="#94a3b8" font-size="11" font-weight="700">PEROLEHAN XP (PENGALI SULIT 2,0x):</text>
          <text x="0" y="58" fill="#f59e0b" font-size="28" font-weight="800">+176 XP</text>
          <text x="0" y="78" fill="#38bdf8" font-size="10.5">+80 XP Kuis Pra-Misi = Total 256 XP</text>
        </g>
      </g>

      <!-- 4 Components Score Breakdown PRD §8 -->
      <g transform="translate(0, 175)">
        <text x="0" y="16" fill="#f8fafc" font-size="14" font-weight="700">RINCIAN 4 KOMPONEN PENILAIAN OTOMATIS (PRD §8):</text>
        
        <g transform="translate(0, 28)">
          <!-- Comp 1: Ketepatan (40%) -->
          <rect width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Ketepatan Tindakan (40%)</text>
          <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">38 <tspan font-size="13" fill="#94a3b8">/ 40</tspan></text>
          <text x="14" y="78" fill="#34d399" font-size="10.5">95% SOP Skenario Benar</text>

          <!-- Comp 2: Respons (25%) -->
          <rect x="228" width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Waktu Respons (25%)</text>
          <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">22 <tspan font-size="13" fill="#94a3b8">/ 25</tspan></text>
          <text x="14" y="78" fill="#34d399" font-size="10.5">Respons 25s (&lt; 45s target)</text>

          <!-- Comp 3: Stabilitas (20%) -->
          <rect x="456" width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Stabilitas Mutu (20%)</text>
          <text x="14" y="54" fill="#f59e0b" font-size="24" font-weight="700">15 <tspan font-size="13" fill="#94a3b8">/ 20</tspan></text>
          <text x="14" y="78" fill="#cbd5e1" font-size="10.5">75% Durasi di Rentang Baku</text>

          <!-- Comp 4: Alarm (15%) -->
          <rect x="684" width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Penanganan Alarm (15%)</text>
          <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">13 <tspan font-size="13" fill="#94a3b8">/ 15</tspan></text>
          <text x="14" y="78" fill="#34d399" font-size="10.5">Semua Diakui &amp; Clear</text>
        </g>
      </g>

      <!-- Chronological Action Audit Log (Consistent with L11 Replay) -->
      <g transform="translate(0, 325)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">LOG URUTAN TINDAKAN DAN EVALUASI DETIK-PER-DETIK (SAMA DENGAN L11):</text>
        
        <rect y="28" width="896" height="175" rx="8" fill="#090d16" stroke="#1e293b" />
        <g transform="translate(16, 44)">
          <text x="0" y="16" fill="#34d399" font-size="11">✓ 01:15</text>
          <text x="70" y="16" fill="#cbd5e1" font-size="11">Alarm Kekeruhan Air Baku Tinggi (185 NTU) muncul.</text>

          <text x="0" y="38" fill="#34d399" font-size="11">✓ 01:28</text>
          <text x="70" y="38" fill="#cbd5e1" font-size="11">Operator mengakui (ACK) alarm dalam 13 detik (Sangat Cepat &lt; 30s).</text>

          <text x="0" y="60" fill="#f59e0b" font-size="11">⚠️ 01:45</text>
          <text x="70" y="60" fill="#cbd5e1" font-size="11">Kekeruhan air olahan menembus 3,4 NTU (≥ 3,0 NTU batas Permenkes).</text>

          <text x="0" y="82" fill="#34d399" font-size="11">✓ 02:10</text>
          <text x="70" y="82" fill="#cbd5e1" font-size="11">Tindakan koreksi: Dosis koagulan dinaikkan ke 48 mg/L &amp; pH distabilkan ke 7,20.</text>

          <text x="0" y="104" fill="#34d399" font-size="11">✓ 02:40</text>
          <text x="70" y="104" fill="#cbd5e1" font-size="11">Debit intake diturunkan dari 100 L/s ke 75 L/s untuk memberi waktu pengendapan.</text>

          <text x="0" y="126" fill="#34d399" font-size="11">✓ 06:10</text>
          <text x="70" y="126" fill="#cbd5e1" font-size="11">Kekeruhan air olahan kembali stabil di 2,4 NTU (&lt; 2,7 NTU deadband selama 10 detik).</text>

          <text x="0" y="148" fill="#34d399" font-size="11">✓ 06:20</text>
          <text x="70" y="148" fill="#38bdf8" font-size="11">Alarm Tinggi clear otomatis setelah tindakan pemulihan yang tepat dari peserta.</text>
        </g>
      </g>

      <!-- Debriefing from Senior Operator Mentor Pak Slamet PRD §9 -->
      <g transform="translate(0, 535)">
        <rect width="896" height="150" rx="10" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
        <circle cx="48" cy="48" r="28" fill="#0369a1" />
        <text x="48" y="55" fill="#ffffff" font-size="22" text-anchor="middle">👨‍🏫</text>
        
        <text x="92" y="30" fill="#38bdf8" font-size="13" font-weight="700">DEBRIEFING TOKOH MENTOR: OPERATOR SENIOR (PAK SLAMET)</text>
        <text x="92" y="52" fill="#ffffff" font-size="12" font-weight="500">"Kerja bagus Dimas! Keputusan Anda menaikkan dosis koagulan ke 48 mg/L dan menurunkan</text>
        <text x="92" y="70" fill="#ffffff" font-size="12" font-weight="500">debit ke 75 L/s adalah keputusan taktis yang sangat tepat. Air olahan berhasil dipulihkan ke 2,4 NTU</text>
        <text x="92" y="88" fill="#ffffff" font-size="12" font-weight="500">sebelum reservoir terkontaminasi. Catatan kecil: awasi headloss filter berikutnya karena lumpur</text>
        <text x="92" y="106" fill="#ffffff" font-size="12" font-weight="500">yang masuk cukup tebal. Anda siap melangkah ke misi berikutnya!"</text>
      </g>
    </g>
  </g>

  <!-- Right Column: New Badges & Actions PRD §8 (Width: 540) -->
  <g transform="translate(1028, 190)">
    <rect width="540" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 28)">
      <!-- New Badge Unlocked Card PRD §8 -->
      <rect width="484" height="195" rx="12" fill="#1e1b4b" stroke="#6366f1" stroke-width="2" />
      <g transform="translate(24, 20)">
        <rect width="130" height="24" rx="6" fill="#4338ca" />
        <text x="65" y="16" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">🎉 LENCANA BARU!</text>
        
        <!-- Big Badge Icon -->
        <circle cx="48" cy="85" r="32" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
        <text x="48" y="93" fill="#ffffff" font-size="28" text-anchor="middle">⚡</text>

        <text x="96" y="75" fill="#f8fafc" font-size="17" font-weight="700">Respons Kilat</text>
        <text x="96" y="95" fill="#38bdf8" font-size="12" font-weight="600">Syarat PRD §8:</text>
        <text x="96" y="112" fill="#cbd5e1" font-size="11">Tindakan benar pertama &lt; 50% waktu target</text>
        <text x="96" y="128" fill="#34d399" font-size="11">Tercapai: 25 Detik (Target Skenario: 60s)</text>
      </g>

      <!-- Level Operator Progression -->
      <g transform="translate(0, 220)">
        <rect width="484" height="180" rx="10" fill="#0f172a" stroke="#1e293b" />
        <g transform="translate(20, 20)">
          <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="700">PROGRES LEVEL OPERATOR (PRD §8):</text>
          <text x="0" y="44" fill="#ffffff" font-size="16" font-weight="700">Operator Muda (820 XP)</text>
          
          <rect x="0" y="58" width="444" height="14" rx="7" fill="#1e293b" />
          <rect x="0" y="58" width="190" height="14" rx="7" fill="url(#goldGrad)" />
          
          <text x="0" y="92" fill="#cbd5e1" font-size="11">Sisa: <tspan fill="#f59e0b" font-weight="700">380 XP</tspan> menuju Level <tspan fill="#38bdf8" font-weight="700">Operator Madya (1.200 XP)</tspan></text>
          <text x="0" y="112" fill="#94a3b8" font-size="10.5">Tingkatan Level: Magang (0) ➔ Muda (400) ➔ Madya (1.200) ➔ Utama (2.500) ➔ Ahli (3.500)</text>
        </g>
      </g>

      <!-- Action Buttons -->
      <g transform="translate(0, 430)">
        <rect width="484" height="52" rx="10" fill="url(#primaryGrad)" />
        <text x="242" y="32" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">LANJUT KE MISI BERIKUTNYA (IPA-07) →</text>

        <rect y="64" width="484" height="46" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="242" y="93" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">ULANGI MISI INI UNTUK CAPAI 3 BINTANG (≥95)</text>

        <rect y="122" width="484" height="46" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="242" y="151" fill="#cbd5e1" font-size="13" font-weight="600" text-anchor="middle">KEMBALI KE BERANDA ROADMAP (L2)</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L6: HASIL SIMULASI & UMPAN BALIK SKOR (SimSCADA-Air v1.0)")

print("Generating L5, L5a, L6...")
with open(os.path.join(OUTPUT_DIR, "mockup_l5_scada_workspace.svg"), "w") as f:
    f.write(generate_l5())
with open(os.path.join(OUTPUT_DIR, "mockup_l5a_control_narrative.svg"), "w") as f:
    f.write(generate_l5a())
with open(os.path.join(OUTPUT_DIR, "mockup_l6_results_scoring.svg"), "w") as f:
    f.write(generate_l6())
print("L5, L5a, L6 generated successfully.")

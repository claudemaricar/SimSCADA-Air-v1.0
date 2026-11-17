#!/usr/bin/env python3
import os, sys, re
import xml.etree.ElementTree as ET

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)

def sanitize_xml(svg_str):
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)

sys.path.append("tmp")
import gen_l5_l5a_l6

def generate_l5():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    
    # Custom SCADA Workspace Header PRD §6 with active timer 02:00
    scada_top_bar = f"""  <!-- SCADA Workspace Action Bar PRD §6 (Timer: 02:00 Active Alarm) -->
  <g transform="translate(0, 106)">
    <rect width="1600" height="52" fill="#030712" stroke="#1e293b" stroke-width="1" />
    
    <!-- Active Mission Indicator -->
    <g transform="translate(32, 10)">
      <rect width="360" height="32" rx="6" fill="#1e293b" stroke="#0284c7" />
      <text x="14" y="21" fill="#38bdf8" font-size="12" font-weight="700">MISI: IPA-06 Lonjakan Kekeruhan Air Baku</text>
    </g>

    <!-- Session Countdown Timer: 02:00 (Sesuai Log Gangguan PRD §10) -->
    <g transform="translate(420, 10)">
      <rect width="220" height="32" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
      <text x="110" y="21" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">⏱️ WAKTU: 02:00 / 10:00</text>
    </g>

    <!-- Live Provisional Score -->
    <g transform="translate(660, 10)">
      <rect width="180" height="32" rx="6" fill="#0f172a" stroke="#10b981" />
      <text x="90" y="21" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">SKOR SEMENTARA: 92</text>
    </g>

    <!-- Petunjuk (-5 Poin) & Selesai Buttons -->
    <g transform="translate(1220, 10)">
      <rect width="180" height="32" rx="6" fill="#1e293b" stroke="#f59e0b" />
      <text x="90" y="21" fill="#fbbf24" font-size="11.5" font-weight="600" text-anchor="middle">💡 Petunjuk (-5 Poin)</text>

      <rect x="195" width="150" height="32" rx="6" fill="#dc2626" />
      <text x="270" y="21" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">SELESAI SIMULASI</text>
    </g>
  </g>"""

    content = f"""{hdr}
{scada_top_bar}

  <!-- Active Alarm Banner PRD §10 (Active & Acknowledged at 02:00) -->
  <g transform="translate(32, 164)">
    <rect width="1536" height="38" rx="8" fill="#451a03" stroke="#ea580c" stroke-width="1.5" filter="url(#glowAmber)" />
    
    <!-- Triangle Alarm Symbol -->
    <polygon points="24,28 35,10 46,28" fill="#ea580c" stroke="#ffffff" stroke-width="1.5" />
    <text x="35" y="25" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">!</text>
    <text x="56" y="24" fill="#ffffff" font-size="12.5" font-weight="700">ALARM TINGGI: Kekeruhan Air Olahan Masuk Reservoir 3,4 NTU (Batas Permenkes: &lt; 3,0 NTU) · Status: Diakui oleh Operator (ACK pada 01:25)</text>
    <text x="1520" y="24" fill="#ffedd5" font-size="11" font-weight="600" text-anchor="end">Auto-Clear Aktif setelah Kekeruhan ≤ 2,7 NTU stabil 10 dtk</text>
  </g>

  <!-- Main HMI Process Diagram Area (Left, Width: 1120) -->
  <g transform="translate(32, 210)">
    <rect width="1120" height="528" rx="12" fill="#080e1a" stroke="#1e293b" stroke-width="1.5" />
    
    <!-- Title of Diagram Area -->
    <text x="20" y="26" fill="#94a3b8" font-size="12" font-weight="700">DIAGRAM MIMIC PROSES TERPADU: INSTALASI PENGOLAHAN AIR (IPA) AKTIF</text>
    <rect x="860" y="10" width="240" height="24" rx="12" fill="#1e293b" />
    <text x="980" y="26" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">JALUR IPA · SIKLUS REAL-TIME 1 Hz</text>

    <!-- Process Flow Pipe Lines Behind Units -->
    <path d="M 90 200 L 220 200 L 360 200 L 510 200 L 670 200 L 820 200 L 980 200" fill="none" stroke="#0284c7" stroke-width="8" opacity="0.6" />
    <!-- Reduced distribution pipe to the right (Dimmed for IPA) -->
    <path d="M 980 200 L 1080 200" fill="none" stroke="#334155" stroke-width="6" opacity="0.4" stroke-dasharray="6,4" />

    <!-- 1. INTAKE & AIR BAKU -->
    <g transform="translate(30, 60)">
      <rect width="150" height="260" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="75" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">1. INTAKE SUNGAI</text>
      <line x1="10" y1="34" x2="140" y2="34" stroke="#1e293b" />
      
      <circle cx="132" cy="18" r="8" fill="#0284c7" /><text x="132" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>

      <text x="14" y="56" fill="#94a3b8" font-size="10">Debit Air Baku:</text>
      <text x="14" y="76" fill="#ffffff" font-size="14" font-weight="700">75,0 <tspan font-size="10" fill="#94a3b8">L/s</tspan></text>

      <text x="14" y="100" fill="#94a3b8" font-size="10">Kekeruhan Baku:</text>
      <text x="14" y="120" fill="#f59e0b" font-size="14" font-weight="700">185 NTU</text>
      <circle cx="120" cy="114" r="6" fill="#f59e0b" /><text x="120" y="118" fill="#000" font-size="8" font-weight="800" text-anchor="middle">!</text>

      <line x1="10" y1="135" x2="140" y2="135" stroke="#1e293b" />
      <text x="14" y="155" fill="#94a3b8" font-size="10">Pompa Intake 1:</text>
      <rect x="14" y="163" width="60" height="20" rx="4" fill="#064e3b" />
      <text x="44" y="177" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">RUN</text>

      <text x="14" y="200" fill="#94a3b8" font-size="10">Pompa Intake 2:</text>
      <rect x="14" y="208" width="70" height="20" rx="4" fill="#1e293b" />
      <text x="49" y="222" fill="#94a3b8" font-size="10" text-anchor="middle">STANDBY</text>

      <rect x="14" y="234" width="122" height="20" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="75" y="248" fill="#cbd5e1" font-size="9" text-anchor="middle">Reset Pompa ↺</text>
    </g>

    <!-- 2. FLASH MIXER KOAGULASI (Selected Unit -> Pop-up L5a Target) -->
    <g transform="translate(195, 60)">
      <rect width="150" height="260" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" filter="url(#glowCyan)" />
      <text x="75" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">2. KOAGULASI</text>
      <line x1="10" y1="34" x2="140" y2="34" stroke="#1e293b" />

      <!-- Clickable "i" Info Icon -->
      <circle cx="132" cy="18" r="8" fill="#38bdf8" />
      <text x="132" y="22" fill="#0b1120" font-size="9" font-weight="800" text-anchor="middle">i</text>

      <rect x="10" y="44" width="130" height="20" rx="4" fill="#0284c7" />
      <text x="75" y="58" fill="#ffffff" font-size="9.5" font-weight="700" text-anchor="middle">UNIT TERPILIH 👈</text>

      <text x="14" y="82" fill="#94a3b8" font-size="10">Dosis Koagulan PAC:</text>
      <text x="14" y="102" fill="#38bdf8" font-size="15" font-weight="700">48,0 <tspan font-size="10" fill="#94a3b8">mg/L</tspan></text>
      <text x="14" y="118" fill="#10b981" font-size="9">(SOP Disesuaikan ↑)</text>

      <text x="14" y="140" fill="#94a3b8" font-size="10">Derajat pH Air:</text>
      <text x="14" y="158" fill="#10b981" font-size="14" font-weight="700">7,20 <tspan font-size="10" fill="#94a3b8">pH</tspan></text>
      <text x="14" y="174" fill="#94a3b8" font-size="9">Penyesuai: Kapur</text>

      <line x1="10" y1="188" x2="140" y2="188" stroke="#1e293b" />
      <text x="14" y="206" fill="#94a3b8" font-size="10">Pengaduk Cepat:</text>
      <rect x="14" y="214" width="122" height="22" rx="4" fill="#064e3b" />
      <text x="75" y="229" fill="#34d399" font-size="9.5" font-weight="700" text-anchor="middle">ON (120 RPM)</text>
      <text x="14" y="250" fill="#64748b" font-size="8.5">Klik "i" buka Narasi L5a</text>
    </g>

    <!-- 3. FLOKULASI -->
    <g transform="translate(360, 60)">
      <rect width="145" height="260" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">3. FLOKULASI</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" /><text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>
      <text x="14" y="58" fill="#94a3b8" font-size="10">Pengaduk Lambat:</text>
      <text x="14" y="78" fill="#ffffff" font-size="12" font-weight="600">3 Kompartemen</text>

      <text x="14" y="104" fill="#94a3b8" font-size="10">Stage 1: <tspan fill="#34d399" font-weight="700">45 RPM</tspan></text>
      <text x="14" y="124" fill="#94a3b8" font-size="10">Stage 2: <tspan fill="#34d399" font-weight="700">30 RPM</tspan></text>
      <text x="14" y="144" fill="#94a3b8" font-size="10">Stage 3: <tspan fill="#34d399" font-weight="700">15 RPM</tspan></text>

      <line x1="10" y1="160" x2="135" y2="160" stroke="#1e293b" />
      <text x="14" y="180" fill="#94a3b8" font-size="10">Kondisi Flok:</text>
      <text x="14" y="200" fill="#34d399" font-size="11" font-weight="700">✓ Terbentuk Baik</text>
    </g>

    <!-- 4. SEDIMENTASI TUBE SETTLER -->
    <g transform="translate(520, 60)">
      <rect width="145" height="260" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">4. SEDIMENTASI</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" /><text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>
      <text x="14" y="58" fill="#94a3b8" font-size="10">Kekeruhan Keluar:</text>
      <text x="14" y="78" fill="#f59e0b" font-size="14" font-weight="700">12,4 NTU</text>
      <text x="14" y="94" fill="#34d399" font-size="9">Tren: Menurun ↓</text>

      <text x="14" y="118" fill="#94a3b8" font-size="10">Selimut Lumpur:</text>
      <text x="14" y="136" fill="#f8fafc" font-size="12" font-weight="600">1,4 Meter</text>

      <line x1="10" y1="150" x2="135" y2="150" stroke="#1e293b" />
      <text x="14" y="170" fill="#94a3b8" font-size="10">Blowdown Lumpur:</text>
      <rect x="14" y="180" width="117" height="28" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="72" y="198" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle">BLOWDOWN (BUANG)</text>
    </g>

    <!-- 5. FILTRASI PASIR CEPAT -->
    <g transform="translate(680, 60)">
      <rect width="145" height="260" rx="8" fill="#0f172a" stroke="#ea580c" stroke-width="2" />
      <text x="72" y="24" fill="#ea580c" font-size="11.5" font-weight="700" text-anchor="middle">5. FILTRASI</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" /><text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>
      <text x="14" y="58" fill="#94a3b8" font-size="10">Kekeruhan Olahan:</text>
      <text x="14" y="78" fill="#ef4444" font-size="15" font-weight="800">3,4 NTU</text>
      <text x="14" y="94" fill="#ef4444" font-size="9">≥3 NTU (Alarm Tinggi)</text>

      <text x="14" y="118" fill="#94a3b8" font-size="10">Headloss Filter:</text>
      <text x="14" y="136" fill="#f59e0b" font-size="12" font-weight="600">1,6 Meter</text>

      <line x1="10" y1="150" x2="135" y2="150" stroke="#1e293b" />
      <text x="14" y="170" fill="#94a3b8" font-size="10">Pencucian Balik:</text>
      <rect x="14" y="180" width="117" height="28" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="72" y="198" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle">BACKWASH FILTER</text>
    </g>

    <!-- 6. RESERVOIR & DESINFEKSI (Active) -->
    <g transform="translate(840, 60)">
      <rect width="145" height="260" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
      <text x="72" y="24" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">6. RESERVOIR</text>
      <line x1="10" y1="34" x2="135" y2="34" stroke="#1e293b" />

      <circle cx="127" cy="18" r="8" fill="#0284c7" /><text x="127" y="22" fill="#fff" font-size="9" font-weight="700" text-anchor="middle">i</text>
      <text x="14" y="58" fill="#94a3b8" font-size="10">Level Air Reservoir:</text>
      <text x="14" y="78" fill="#ffffff" font-size="13" font-weight="600">4,20 / 5,00 m</text>

      <text x="14" y="104" fill="#94a3b8" font-size="10">Sisa Klorin Ujung:</text>
      <text x="14" y="122" fill="#10b981" font-size="13" font-weight="700">0,38 mg/L</text>
      <text x="14" y="138" fill="#34d399" font-size="9">Rentang: 0,2–0,5</text>

      <line x1="10" y1="150" x2="135" y2="150" stroke="#1e293b" />
      <text x="14" y="170" fill="#94a3b8" font-size="10">Katup Masuk/Keluar:</text>
      <rect x="14" y="180" width="117" height="28" rx="4" fill="#064e3b" />
      <text x="72" y="198" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">VALVE TERBUKA</text>
    </g>

    <!-- 7. UNIT DISTRIBUSI (DIMMED FOR IPA MISSION) -->
    <g transform="translate(1000, 60)" opacity="0.45">
      <rect width="105" height="260" rx="8" fill="#090d16" stroke="#334155" stroke-dasharray="4,3" />
      <text x="52" y="24" fill="#64748b" font-size="10.5" font-weight="700" text-anchor="middle">7. JARINGAN</text>
      <line x1="8" y1="34" x2="97" y2="34" stroke="#1e293b" />
      <text x="10" y="70" fill="#64748b" font-size="9.5">Nonaktif di Jalur IPA</text>
      <text x="10" y="90" fill="#64748b" font-size="9.5">(Khusus Jalur Distribusi &amp; Terpadu)</text>
      <text x="10" y="130" fill="#475569" font-size="9">Pompa Dist: OFF</text>
      <text x="10" y="150" fill="#475569" font-size="9">PRV: Standby</text>
    </g>

    <!-- Bottom Trend Chart inside Mimic -->
    <g transform="translate(30, 335)">
      <rect width="1060" height="175" rx="8" fill="#050912" stroke="#1e293b" />
      <text x="16" y="22" fill="#94a3b8" font-size="11" font-weight="700">TREN KEKERUHAN AIR OLAHAN (REAL-TIME 1 Hz):</text>
      
      <!-- Graph Lines -->
      <line x1="40" y1="40" x2="1020" y2="40" stroke="#1e293b" />
      <line x1="40" y1="90" x2="1020" y2="90" stroke="#1e293b" />
      <line x1="40" y1="140" x2="1020" y2="140" stroke="#334155" stroke-width="1.5" />

      <!-- Curve -->
      <path d="M 40 130 L 150 130 L 180 80 L 220 50 L 350 55 L 500 70 L 750 110 L 980 120" fill="none" stroke="#38bdf8" stroke-width="2.5" />
      <!-- Red Permenkes Limit line -->
      <line x1="40" y1="65" x2="1020" y2="65" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
      <text x="1025" y="68" fill="#ef4444" font-size="9" font-weight="700">3,0 NTU</text>

      <text x="50" y="158" fill="#64748b" font-size="9">00:00</text>
      <text x="180" y="158" fill="#f59e0b" font-size="9">01:15 (Lonjakan Baku)</text>
      <text x="350" y="158" fill="#ffffff" font-size="9" font-weight="700">02:00 (Posisi Saat Ini)</text>
      <text x="750" y="158" fill="#34d399" font-size="9">06:10 (Pulih &lt;2,7 NTU)</text>
      <text x="980" y="158" fill="#64748b" font-size="9">08:30 (Selesai)</text>
    </g>
  </g>

  <!-- Control Panel Right PRD §9 (Width: 400) -->
  <g transform="translate(1168, 210)">
    <rect width="400" height="528" rx="12" fill="url(#cardGrad)" stroke="#38bdf8" stroke-width="1.5" />
    
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="15" font-weight="700">PANEL KENDALI TITIK KONTROL</text>
      <text x="0" y="36" fill="#38bdf8" font-size="12" font-weight="600">Unit Terpilih: Flash Mixer Koagulasi</text>
      
      <line x1="0" y1="50" x2="352" y2="50" stroke="#334155" stroke-width="1" />

      <!-- Controller 1: Dosis Koagulan PAC -->
      <g transform="translate(0, 65)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">SETPOINT DOSIS KOAGULAN (PAC):</text>
        <text x="350" y="16" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="end">48,0 mg/L</text>

        <rect x="0" y="28" width="352" height="12" rx="6" fill="#0f172a" />
        <rect x="0" y="28" width="260" height="12" rx="6" fill="url(#primaryGrad)" />
        <circle cx="260" cy="34" r="10" fill="#ffffff" stroke="#0284c7" stroke-width="3" />

        <text x="0" y="58" fill="#64748b" font-size="10">Min: 10 mg/L</text>
        <text x="176" y="58" fill="#10b981" font-size="10" text-anchor="middle">SOP Banjir: 45–50 mg/L</text>
        <text x="352" y="58" fill="#64748b" font-size="10" text-anchor="end">Max: 80 mg/L</text>
      </g>

      <!-- Controller 2: Penyesuai pH (Kapur / Soda Ash) -->
      <g transform="translate(0, 145)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">DOSIS PENYESUAI pH (KAPUR):</text>
        <text x="350" y="16" fill="#10b981" font-size="14" font-weight="700" text-anchor="end">8,5 mg/L</text>

        <rect x="0" y="28" width="352" height="12" rx="6" fill="#0f172a" />
        <rect x="0" y="28" width="180" height="12" rx="6" fill="url(#emeraldGrad)" />
        <circle cx="180" cy="34" r="10" fill="#ffffff" stroke="#059669" stroke-width="3" />

        <text x="0" y="58" fill="#64748b" font-size="10">Target pH: 7,20 (Rentang Aman: 6,5–8,5)</text>
      </g>

      <!-- Controller 3: Motor Pengaduk Cepat -->
      <g transform="translate(0, 225)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">MOTOR FLASH MIXER:</text>
        <rect x="0" y="26" width="170" height="36" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1.5" />
        <text x="85" y="49" fill="#34d399" font-size="11.5" font-weight="700" text-anchor="middle">ON (120 RPM)</text>

        <rect x="182" y="26" width="170" height="36" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="267" y="49" fill="#94a3b8" font-size="11.5" font-weight="600" text-anchor="middle">OFF (STOP)</text>
      </g>

      <!-- Controller 4: Dosing Desinfeksi Klorin (PRD §9) - PRV HIDDEN FOR IPA -->
      <g transform="translate(0, 305)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">DOSING DESINFEKSI KLORIN (PRD §9):</text>
        <rect x="0" y="26" width="352" height="36" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="49" fill="#ffffff" font-size="12.5" font-weight="700">1,20 mg/L (Sisa Klor: 0,38 mg/L)</text>
        <text x="336" y="49" fill="#34d399" font-size="10.5" font-weight="600" text-anchor="end">SOP Aman ✓</text>
      </g>

      <!-- Launch Pop-up Narrative L5a Button -->
      <g transform="translate(0, 385)">
        <rect width="352" height="46" rx="8" fill="#0c4a6e" stroke="#0284c7" stroke-width="1.5" />
        <circle cx="28" cy="23" r="10" fill="#38bdf8" /><text x="28" y="27" fill="#082f49" font-size="12" font-weight="800" text-anchor="middle">i</text>
        <text x="48" y="27" fill="#ffffff" font-size="12" font-weight="700">BUKA NARASI TITIK KONTROL KOAGULASI</text>
        <text x="48" y="40" fill="#7dd3fc" font-size="10">Tanpa pengurangan skor · SOP Lembaga</text>
      </g>

      <text x="176" y="465" fill="#64748b" font-size="10" text-anchor="middle">PRV disembunyikan pada Misi IPA (Hanya di Jalur Distribusi).</text>
    </g>
  </g>

  <!-- Alarm Table ISA-18.2 Bottom Panel PRD §10 (Width: 1536) -->
  <g transform="translate(32, 755)">
    <rect width="1536" height="205" rx="10" fill="#090d16" stroke="#1e293b" stroke-width="1.5" />
    
    <!-- Table Header Bar -->
    <rect width="1536" height="32" rx="10" fill="#0f172a" />
    <text x="20" y="21" fill="#38bdf8" font-size="11" font-weight="700">DAFTAR ALARM SISTEM (4 STATUS STANDAR PRD §10: AKTIF BLM DIAKUI · AKTIF DIAKUI · PULIH BLM CLEAR · CLEAR)</text>

    <!-- Table Columns -->
    <text x="20" y="52" fill="#94a3b8" font-size="10" font-weight="700">WAKTU</text>
    <text x="90" y="52" fill="#94a3b8" font-size="10" font-weight="700">BENTUK / PRIORITAS</text>
    <text x="240" y="52" fill="#94a3b8" font-size="10" font-weight="700">TITIK KONTROL</text>
    <text x="440" y="52" fill="#94a3b8" font-size="10" font-weight="700">PESAN ALARM &amp; NILAI PROSES</text>
    <text x="960" y="52" fill="#94a3b8" font-size="10" font-weight="700">STATUS ALARM</text>
    <text x="1220" y="52" fill="#94a3b8" font-size="10" font-weight="700">AKSI OPERATOR</text>

    <line x1="20" y1="62" x2="1516" y2="62" stroke="#1e293b" />

    <!-- Alarm Row 1: High Alarm (Aktif Diakui, Clear Disabled) -->
    <g transform="translate(20, 72)">
      <text x="0" y="20" fill="#cbd5e1" font-size="11">01:45</text>
      
      <polygon points="76,22 84,6 92,22" fill="#ea580c" /><text x="84" y="20" fill="#fff" font-size="8" font-weight="900" text-anchor="middle">!</text>
      <text x="100" y="20" fill="#ea580c" font-size="11" font-weight="700">TINGGI</text>

      <text x="220" y="20" fill="#ffffff" font-size="11">Filtrasi (Air Olahan)</text>
      <text x="420" y="20" fill="#ffedd5" font-size="11">Kekeruhan air olahan ≥ 3 NTU (Terukur: 3,4 NTU)</text>

      <rect x="940" y="4" width="130" height="22" rx="4" fill="#451a03" stroke="#d97706" />
      <text x="1005" y="19" fill="#fde68a" font-size="10" font-weight="700" text-anchor="middle">Aktif, Diakui</text>

      <rect x="1200" y="4" width="70" height="22" rx="4" fill="#1e293b" />
      <text x="1235" y="19" fill="#64748b" font-size="10" text-anchor="middle">Diakui ✓</text>

      <!-- Disabled Clear Button with Explanation -->
      <rect x="1280" y="4" width="220" height="22" rx="4" fill="#1e293b" stroke="#334155" />
      <text x="1390" y="19" fill="#64748b" font-size="9" text-anchor="middle">Clear (Penyebab blm selesai: 3,4 NTU ≥ 3,0)</text>
    </g>

    <!-- Alarm Row 2: Medium Alarm (Pulih Belum di-Clear) -->
    <g transform="translate(20, 115)">
      <text x="0" y="20" fill="#cbd5e1" font-size="11">01:15</text>
      
      <circle cx="84" cy="14" r="8" fill="#f59e0b" /><text x="84" y="18" fill="#000" font-size="9" font-weight="800" text-anchor="middle">i</text>
      <text x="100" y="20" fill="#f59e0b" font-size="11" font-weight="700">SEDANG</text>

      <text x="220" y="20" fill="#ffffff" font-size="11">Intake Air Baku</text>
      <text x="420" y="20" fill="#cbd5e1" font-size="11">Kekeruhan air baku tinggi (185 NTU, tren mulai turun)</text>

      <rect x="940" y="4" width="140" height="22" rx="4" fill="#064e3b" stroke="#059669" />
      <text x="1010" y="19" fill="#a7f3d0" font-size="10" font-weight="700" text-anchor="middle">Pulih, Belum di-Clear</text>

      <rect x="1200" y="4" width="90" height="22" rx="4" fill="#059669" />
      <text x="1245" y="19" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">CLEAR MANUAL</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L5: WORKSPACE SIMULATOR SCADA HMI (SimSCADA-Air v1.0)")

def generate_l5a():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Pop-Up Narasi Titik Kontrol: Koagulasi", "6 Bagian Lengkap PRD §9 + Catatan SOP Lokal Lembaga · Akses 'i' Tidak Mengurangi Skor", 120)

    content = f"""{hdr}
{title}

  <!-- Underneath Backdrop: Dimmed SCADA Workspace -->
  <rect x="32" y="185" width="1536" height="775" rx="14" fill="#050a14" opacity="0.8" stroke="#1e293b" />
  
  <!-- Interactive Cursor Tooltip on SCADA Mimic PRD §9 -->
  <g transform="translate(100, 210)">
    <rect width="280" height="52" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" filter="url(#dropShadow)" />
    <text x="14" y="22" fill="#38bdf8" font-size="11" font-weight="700">KURSOR DIARAHKAN KE TITIK KONTROL:</text>
    <text x="14" y="40" fill="#ffffff" font-size="12">Flash Mixer Koagulasi · 48 mg/L PAC · pH 7,20</text>
    <polygon points="60,52 70,62 80,52" fill="#1e293b" />
  </g>

  <!-- Main Modal Container (Width: 1100, Centered at x=250, y=190) -->
  <g transform="translate(250, 190)" filter="url(#dropShadow)">
    <rect width="1100" height="770" rx="16" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="2.5" />
    
    <!-- Modal Header -->
    <g transform="translate(32, 28)">
      <rect width="48" height="48" rx="10" fill="#0284c7" />
      <text x="24" y="32" fill="#ffffff" font-size="22" font-weight="900" text-anchor="middle">i</text>
      <text x="64" y="24" fill="#ffffff" font-size="19" font-weight="700">Narasi Detail Titik Kontrol: Flash Mixer Koagulasi</text>
      <text x="64" y="44" fill="#38bdf8" font-size="12">Unit Operasi Kimia-Fisik · Pembubuhan Koagulan PAC &amp; Pengadukan Cepat (PRD §9)</text>

      <rect x="990" y="8" width="36" height="36" rx="8" fill="#1e293b" stroke="#475569" />
      <text x="1008" y="31" fill="#cbd5e1" font-size="16" font-weight="700" text-anchor="middle">✕</text>
      <line x1="0" y1="64" x2="1036" y2="64" stroke="#334155" stroke-width="1" />
    </g>

    <!-- LEFT COLUMN (Sections 1, 2, 3) -->
    <g transform="translate(32, 105)">
      
      <!-- 1. APA INI & FUNGSINYA (+ Skema) -->
      <g transform="translate(0, 0)">
        <rect width="500" height="155" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">1. APA INI &amp; FUNGSINYA (DESKRIPSI PROSES):</text>
        <text x="16" y="44" fill="#ffffff" font-size="11.5">Flash Mixer adalah unit pengaduk berkecepatan tinggi</text>
        <text x="16" y="62" fill="#ffffff" font-size="11.5">(G &gt; 750 s⁻¹) untuk mendispersikan koagulan PAC secara merata</text>
        <text x="16" y="80" fill="#ffffff" font-size="11.5">ke seluruh aliran air baku dalam hitungan detik (&lt;60 detik).</text>
        <text x="16" y="104" fill="#94a3b8" font-size="11">Tujuan: Destabilisasi muatan listrik koloid penyebab kekeruhan.</text>

        <!-- Mini Diagram Graphic -->
        <g transform="translate(320, 20)">
          <rect width="160" height="115" rx="6" fill="#1e293b" stroke="#334155" />
          <path d="M 20 60 L 80 60 L 140 60" stroke="#0284c7" stroke-width="4" />
          <line x1="80" y1="20" x2="80" y2="50" stroke="#38bdf8" stroke-width="3" stroke-dasharray="2,2" />
          <circle cx="80" cy="60" r="14" fill="#0284c7" />
          <text x="80" y="64" fill="#ffffff" font-size="9" text-anchor="middle">MIXER</text>
          <text x="80" y="96" fill="#38bdf8" font-size="8.5" text-anchor="middle">Injeksi PAC 48 mg/L</text>
        </g>
      </g>

      <!-- 2. YANG DIPANTAU -->
      <g transform="translate(0, 170)">
        <rect width="500" height="185" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">2. YANG DIPANTAU (MONITORED PARAMETERS):</text>
        
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
          <text x="320" y="70" fill="#38bdf8" font-size="11" font-weight="700">48,0 mg/L (Disesuaikan)</text>

          <text x="10" y="96" fill="#cbd5e1" font-size="11">Derajat pH</text>
          <text x="150" y="96" fill="#cbd5e1" font-size="11">6,5 – 8,5 (Permenkes)</text>
          <text x="320" y="96" fill="#10b981" font-size="11" font-weight="700">7,20 pH (Normal ✓)</text>

          <text x="10" y="122" fill="#cbd5e1" font-size="11">Kecepatan Mixer</text>
          <text x="150" y="122" fill="#cbd5e1" font-size="11">100 – 150 RPM</text>
          <text x="320" y="122" fill="#34d399" font-size="11" font-weight="700">120 RPM (Aktif)</text>
        </g>
      </g>

      <!-- 3. YANG BISA DIKENDALIKAN -->
      <g transform="translate(0, 370)">
        <rect width="500" height="145" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">3. YANG BISA DIKENDALIKAN (CONTROLS):</text>
        <text x="16" y="46" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#38bdf8">Setpoint Dosis Koagulan:</tspan> Stroke pompa dosing PAC.</text>
        <text x="16" y="70" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#10b981">Dosis Penyesuai pH:</tspan> Injeksi kapur jika pH air baku drop &lt;6,5.</text>
        <text x="16" y="94" fill="#ffffff" font-size="11.5">• <tspan font-weight="700" fill="#f59e0b">Saklar On/Off Mixer:</tspan> Pengadukan seketika saat injeksi bahan.</text>
      </g>
    </g>

    <!-- RIGHT COLUMN (Sections 4, 5, 6 + Catatan SOP Lokal Lembaga) - FIXED MULTILINE -->
    <g transform="translate(564, 105)">
      
      <!-- 4. DAMPAK KE HILIR (Clean Wrapped Lines) -->
      <g transform="translate(0, 0)">
        <rect width="504" height="155" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">4. DAMPAK KE HILIR (DOWNSTREAM IMPACT):</text>
        
        <text x="16" y="44" fill="#ef4444" font-size="11" font-weight="700">• Underdosing Koagulan:</text>
        <text x="24" y="60" fill="#cbd5e1" font-size="10.5">Flok tidak terbentuk sempurna, kekeruhan lolos melewati bak</text>
        <text x="24" y="74" fill="#cbd5e1" font-size="10.5">sedimentasi dan membebani filter pasir cepat hingga cepat jenuh.</text>

        <text x="16" y="98" fill="#f59e0b" font-size="11" font-weight="700">• Overdosing Koagulan:</text>
        <text x="24" y="114" fill="#cbd5e1" font-size="10.5">Pemborosan bahan kimia, pH air olahan anjlok tajam, dan lumpur</text>
        <text x="24" y="128" fill="#cbd5e1" font-size="10.5">berlebih yang mempercepat sedimentasi meluap ke filter.</text>
      </g>

      <!-- 5. GANGGUAN UMUM & SOP SINGKAT (Clean Wrapped Lines) -->
      <g transform="translate(0, 170)">
        <rect width="504" height="155" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="22" fill="#38bdf8" font-size="12" font-weight="700">5. GANGGUAN UMUM &amp; SOP SINGKAT (PRD §9 &amp; §10):</text>
        
        <text x="16" y="44" fill="#ffffff" font-size="10.5">1. <tspan font-weight="700" fill="#38bdf8">Lonjakan Kekeruhan Baku:</tspan> Naikkan dosis PAC (misal 20 ke 48 mg/L)</text>
        <text x="32" y="58" fill="#94a3b8" font-size="10">sesuai kurva jar test; pantau pembentukan flok.</text>

        <text x="16" y="78" fill="#ffffff" font-size="10.5">2. <tspan font-weight="700" fill="#f59e0b">Pompa Dosing Macet:</tspan> Pindahkan ke pompa injeksi cadangan (standby)</text>
        <text x="32" y="92" fill="#94a3b8" font-size="10">lalu lakukan flushing pipa injeksi kimia.</text>

        <text x="16" y="112" fill="#ffffff" font-size="10.5">3. <tspan font-weight="700" fill="#10b981">pH Drop:</tspan> Tambahkan kapur agar pH tetap di rentang 6,5–8,5.</text>
      </g>

      <!-- 6. PELAJARI LEBIH LANJUT -->
      <g transform="translate(0, 340)">
        <rect width="504" height="50" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="16" y="20" fill="#38bdf8" font-size="11" font-weight="700">6. PELAJARI LEBIH LANJUT:</text>
        <text x="16" y="36" fill="#cbd5e1" font-size="10.5">Modul Teori IPA-03 (Koagulasi) &amp; Standar Permenkes No. 2/2023 Bab II</text>
      </g>

      <!-- KOTAK KHUSUS: CATATAN SOP LOKAL LEMBAGA PRD §9 -->
      <g transform="translate(0, 405)">
        <rect width="504" height="110" rx="10" fill="#064e3b" opacity="0.5" stroke="#059669" stroke-width="1.5" />
        <text x="16" y="22" fill="#a7f3d0" font-size="11.5" font-weight="700">🏢 CATATAN SOP LOKAL LEMBAGA (BALAI NUSANTARA):</text>
        <text x="16" y="42" fill="#ffffff" font-size="10.5">"Injeksi koagulan memakai dosing pump otomatis dengan kalibrasi</text>
        <text x="16" y="58" fill="#ffffff" font-size="10.5">larutan PAC 10%. Batas minimum tangki harian adalah 20%."</text>
        <text x="16" y="86" fill="#6ee7b7" font-size="10">Dikonfigurasi oleh Admin Lembaga di Layar L13</text>
      </g>
    </g>

    <!-- Modal Footer -->
    <g transform="translate(32, 655)">
      <line x1="0" y1="0" x2="1036" y2="0" stroke="#334155" stroke-width="1" />
      <text x="0" y="26" fill="#94a3b8" font-size="11.5">Membuka narasi ini dicatat dalam sistem untuk syarat perolehan Lencana <tspan fill="#38bdf8" font-weight="700">"Penjelajah Titik Kontrol"</tspan> (PRD §8).</text>
      
      <rect x="850" y="8" width="186" height="38" rx="8" fill="#0284c7" />
      <text x="943" y="32" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">KEMBALI KE WORKSPACE</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L5a: POP-UP NARASI TITIK KONTROL KOAGULASI (SimSCADA-Air v1.0)")

def generate_l6():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Hasil Evaluasi Simulasi &amp; Umpan Balik Skor", "Sesi Konsisten: IPA-06 Gangguan Lonjakan Kekeruhan Air Baku (Durasi 08:30) · PRD §8", 120)

    content = f"""{hdr}
{title}

  <!-- Left Main Column: 4 Component Score & Action Log (Width: 960) -->
  <g transform="translate(32, 190)">
    <rect width="960" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 26)">
      <!-- Top Score Summary Banner -->
      <g transform="translate(0, 0)">
        <rect width="896" height="105" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
        
        <g transform="translate(24, 20)">
          <text x="0" y="18" fill="#94a3b8" font-size="11" font-weight="700">SKOR KELULUSAN AKHIR SIMULASI (PRD §8):</text>
          <text x="0" y="58" fill="#38bdf8" font-size="44" font-weight="900">88 <tspan font-size="18" fill="#94a3b8">/ 100</tspan></text>
          
          <rect x="180" y="24" width="160" height="36" rx="8" fill="#065f46" />
          <text x="260" y="47" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">LULUS (2★ BINTANG)</text>

          <text x="360" y="32" fill="#cbd5e1" font-size="11">Aturan Bintang: &lt;70 Belum Lulus · 70–84 (1★) · <tspan fill="#f59e0b" font-weight="700">85–94 (2★)</tspan> · ≥95 (3★)</text>
          <text x="360" y="54" fill="#f59e0b" font-size="13" font-weight="700">★★☆ (Dua Bintang)</text>

          <rect x="730" y="16" width="140" height="48" rx="8" fill="#1e1b4b" stroke="#6366f1" />
          <text x="800" y="34" fill="#a5b4fc" font-size="10.5" text-anchor="middle">XP DIPEROLEH (2,0x):</text>
          <text x="800" y="54" fill="#fbbf24" font-size="16" font-weight="800" text-anchor="middle">+176 XP</text>
        </g>
      </g>

      <!-- 4 Components Score Breakdown (FIXED: Wrap each card in <g transform="translate(...)">) -->
      <g transform="translate(0, 135)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">RINCIAN 4 KOMPONEN PENILAIAN OTOMATIS (PRD §8):</text>
        
        <g transform="translate(0, 26)">
          <!-- Comp 1: Ketepatan (40%) -->
          <g transform="translate(0, 0)">
            <rect width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Ketepatan Tindakan (40%)</text>
            <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">38 <tspan font-size="13" fill="#94a3b8">/ 40</tspan></text>
            <text x="14" y="78" fill="#34d399" font-size="10.5">95% SOP Skenario Benar</text>
          </g>

          <!-- Comp 2: Respons (25%) - Skenario Target 60s PRD §8 -->
          <g transform="translate(228, 0)">
            <rect width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Waktu Respons (25%)</text>
            <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">22 <tspan font-size="13" fill="#94a3b8">/ 25</tspan></text>
            <text x="14" y="78" fill="#34d399" font-size="10.5">Respons 25s (&lt; 50% target 60s)</text>
          </g>

          <!-- Comp 3: Stabilitas (20%) -->
          <g transform="translate(456, 0)">
            <rect width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Stabilitas Mutu (20%)</text>
            <text x="14" y="54" fill="#f59e0b" font-size="24" font-weight="700">15 <tspan font-size="13" fill="#94a3b8">/ 20</tspan></text>
            <text x="14" y="78" fill="#cbd5e1" font-size="10.5">75% Durasi di Rentang Baku</text>
          </g>

          <!-- Comp 4: Alarm (15%) -->
          <g transform="translate(684, 0)">
            <rect width="212" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Penanganan Alarm (15%)</text>
            <text x="14" y="54" fill="#38bdf8" font-size="24" font-weight="700">13 <tspan font-size="13" fill="#94a3b8">/ 15</tspan></text>
            <text x="14" y="78" fill="#34d399" font-size="10.5">Semua Diakui &amp; Auto-Clear</text>
          </g>
        </g>
      </g>

      <!-- Chronological Action Audit Log (Identical with L11) -->
      <g transform="translate(0, 285)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">LOG URUTAN TINDAKAN DAN EVALUASI DETIK-PER-DETIK (SAMA DENGAN L11):</text>
        
        <rect y="26" width="896" height="230" rx="8" fill="#090d16" stroke="#1e293b" />
        <g transform="translate(16, 44)">
          <text x="0" y="16" fill="#34d399" font-size="11.5">✓ 01:25 · [Ketepatan] Operator mengakui (ACK) alarm Kekeruhan Air Baku Tinggi dalam 25 detik (+15 Poin)</text>
          <text x="0" y="42" fill="#34d399" font-size="11.5">✓ 02:10 · [Ketepatan] Menyesuaikan setpoint dosis koagulan PAC dari 20 mg/L ke 48 mg/L (+15 Poin)</text>
          <text x="0" y="68" fill="#34d399" font-size="11.5">✓ 02:25 · [Ketepatan] Mengaktifkan dosis penyesuai pH kapur ke 8,5 mg/L untuk menjaga pH 7,20 (+10 Poin)</text>
          <text x="0" y="94" fill="#f59e0b" font-size="11.5">⚠️ 03:00 · [Waktu Respons] Dosis koagulan membutuhkan waktu 45 detik untuk stabil di unit koagulasi (-3 Poin)</text>
          <text x="0" y="120" fill="#34d399" font-size="11.5">✓ 06:10 · [Stabilitas Mutu] Kekeruhan air olahan turun ke 2,4 NTU (&lt; 2,7 NTU stabil 10 detik) (+15 Poin)</text>
          <text x="0" y="146" fill="#34d399" font-size="11.5">✓ 06:20 · [Alarm SCADA] Alarm Tinggi auto-clear secara sempurna sesuai standar ISA-18.2 (+10 Poin)</text>
          <text x="0" y="172" fill="#38bdf8" font-size="11.5">ℹ️ 08:30 · Simulasi selesai normal dengan parameter mutu stabil memenuhi standar Permenkes No. 2/2023.</text>
        </g>
      </g>

      <!-- Senior Mentor Debriefing Box -->
      <g transform="translate(0, 565)">
        <rect width="896" height="150" rx="10" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
        <g transform="translate(20, 18)">
          <text x="0" y="16" fill="#38bdf8" font-size="13" font-weight="700">💬 DEBRIEFING EVALUASI MENTOR (OPERATOR SENIOR):</text>
          <text x="0" y="42" fill="#ffffff" font-size="12">"Kerja luar biasa, Dimas! Anda langsung merespons lonjakan kekeruhan air baku dalam 25 detik</text>
          <text x="0" y="62" fill="#ffffff" font-size="12">(&lt; 50% target skenario 60 detik) sehingga berhak atas Lencana 'Respons Kilat'.</text>
          <text x="0" y="82" fill="#ffffff" font-size="12">Penyesuaian pH kapur Anda sangat tepat mencegah flok pecah di bak flokulasi."</text>
          <text x="0" y="112" fill="#7dd3fc" font-size="11" font-weight="600">Catatan: Lanjutkan ke Misi IPA-07 (Pompa Intake Trip) untuk mengasah alih pompa standby.</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Right Column: Badge Unlocked Popup & Post-Mission Navigation (Width: 544) -->
  <g transform="translate(1024, 190)">
    
    <!-- Badge Unlocked Card PRD §8 (Respons Kilat) -->
    <rect width="544" height="240" rx="14" fill="#1e1b4b" stroke="#6366f1" stroke-width="2" filter="url(#dropShadow)" />
    <g transform="translate(24, 20)">
      <rect width="130" height="24" rx="6" fill="#4338ca" />
      <text x="65" y="16" fill="#c7d2fe" font-size="11" font-weight="800" text-anchor="middle">★ LENCANA BARU!</text>
      
      <g transform="translate(0, 36)">
        <circle cx="36" cy="36" r="32" fill="#059669" stroke="#34d399" stroke-width="2" />
        <text x="36" y="44" fill="#ffffff" font-size="28" text-anchor="middle">⚡</text>

        <text x="84" y="26" fill="#ffffff" font-size="17" font-weight="700">Respons Kilat</text>
        <text x="84" y="46" fill="#a7f3d0" font-size="11.5">Atasi gangguan dalam &lt; 50% target waktu</text>
        <text x="84" y="64" fill="#cbd5e1" font-size="11">Target Skenario: <tspan font-weight="700">60 Detik</tspan> · Realisasi: <tspan font-weight="700" fill="#34d399">25 Detik</tspan></text>
      </g>

      <line x1="0" y1="125" x2="496" y2="125" stroke="#334155" stroke-width="1" />
      
      <text x="0" y="152" fill="#e2e8f0" font-size="11.5">Total Lencana Anda: <tspan font-weight="700" fill="#38bdf8">3 dari 8 Lencana PRD Terbuka</tspan></text>
      <text x="0" y="172" fill="#94a3b8" font-size="11">Lihat lemari lencana &amp; papan peringkat lengkap di menu L7.</text>
    </g>

    <!-- Post-Mission Next Step Actions -->
    <g transform="translate(0, 260)">
      <rect width="544" height="510" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      
      <g transform="translate(28, 28)">
        <text x="0" y="18" fill="#ffffff" font-size="16" font-weight="700">Langkah Berikutnya:</text>
        <text x="0" y="38" fill="#94a3b8" font-size="12">Progres Anda telah tersimpan otomatis ke server.</text>

        <g transform="translate(0, 60)">
          <!-- Action 1: Putar Ulang Sesi (L11 Replay) -->
          <rect width="488" height="58" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
          <circle cx="30" cy="29" r="14" fill="#0284c7" /><text x="30" y="34" fill="#fff" font-size="12" text-anchor="middle">▶</text>
          <text x="56" y="26" fill="#ffffff" font-size="13" font-weight="700">Putar Ulang Sesi Simulasi (L11 Replay)</text>
          <text x="56" y="44" fill="#94a3b8" font-size="11">Tinjau grafik parameter 1 Hz dan evaluasi tindakan</text>
        </g>

        <g transform="translate(0, 130)">
          <!-- Action 2: Lanjut Misi Berikut (IPA-07) -->
          <rect width="488" height="58" rx="8" fill="url(#primaryGrad)" />
          <circle cx="30" cy="29" r="14" fill="#ffffff" /><text x="30" y="34" fill="#0284c7" font-size="14" font-weight="800" text-anchor="middle">→</text>
          <text x="56" y="26" fill="#ffffff" font-size="13" font-weight="700">Lanjut ke Misi Berikut: IPA-07 (Pompa Trip)</text>
          <text x="56" y="44" fill="#bae6fd" font-size="11">Buka modul materi &amp; kuis pra-misi tingkat 3</text>
        </g>

        <g transform="translate(0, 200)">
          <!-- Action 3: Kembali ke Beranda (L2) -->
          <rect width="488" height="58" rx="8" fill="#1e293b" stroke="#334155" />
          <circle cx="30" cy="29" r="14" fill="#334155" /><text x="30" y="34" fill="#fff" font-size="12" text-anchor="middle">⌂</text>
          <text x="56" y="26" fill="#cbd5e1" font-size="13" font-weight="700">Kembali ke Beranda Peserta (L2)</text>
          <text x="56" y="44" fill="#64748b" font-size="11">Periksa peta capaian dan XP terbaru</text>
        </g>

        <g transform="translate(0, 280)">
          <rect width="488" height="150" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">CATATAN EVALUASI OTOMATIS SISTEM:</text>
          <text x="16" y="46" fill="#94a3b8" font-size="11">• Status Sesi: Lulus Baik (Skor 88 ≥ Ambang 70)</text>
          <text x="16" y="66" fill="#94a3b8" font-size="11">• Pengali XP: 2,0x (Tingkat Sulit) = +176 XP</text>
          <text x="16" y="86" fill="#94a3b8" font-size="11">• Posisi Peringkat: #2 di Kelompok Angkatan 1</text>
          <text x="16" y="106" fill="#94a3b8" font-size="11">• Rekomendasi: Selesaikan IPA-08 untuk membuka ujian IPA-09.</text>
        </g>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L6: HASIL EVALUASI SIMULASI &amp; SKOR (SimSCADA-Air v1.0)")

print("Generating L5, L5a, L6...")
l5_svg = sanitize_xml(generate_l5())
l5a_svg = sanitize_xml(generate_l5a())
l6_svg = sanitize_xml(generate_l6())

with open(os.path.join(PUBLIC_DIR, "mockup_l5_scada_workspace.svg"), "w", encoding="utf-8") as f:
    f.write(l5_svg)
with open(os.path.join(PUBLIC_DIR, "mockup_l5a_control_narrative.svg"), "w", encoding="utf-8") as f:
    f.write(l5a_svg)
with open(os.path.join(PUBLIC_DIR, "mockup_l6_results_scoring.svg"), "w", encoding="utf-8") as f:
    f.write(l6_svg)

ET.parse(os.path.join(PUBLIC_DIR, "mockup_l5_scada_workspace.svg"))
ET.parse(os.path.join(PUBLIC_DIR, "mockup_l5a_control_narrative.svg"))
ET.parse(os.path.join(PUBLIC_DIR, "mockup_l6_results_scoring.svg"))
print("L5, L5a, L6 successfully generated and validated in public/!")

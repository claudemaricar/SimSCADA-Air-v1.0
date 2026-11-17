#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 5: L10, L11, L12, L13, L14, L15, L16
"""
import os
import sys

OUTPUT_DIR = "public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

def generate_l10():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · Angkatan 1", name="Budi Santoso, S.T.", initials="BS")
    title = page_title_block("Kelola Skenario Gangguan Kustom", "Authoring Tool Skenario Gangguan (FR-23) · Lengkap dengan Isian Tingkat Kesulitan PRD §7", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: Scenario Authoring Form (Width: 960) -->
  <g transform="translate(32, 190)">
    <rect width="960" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Formulir Perancangan Skenario Baru (Authoring Tool FR-23)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Rancang skenario kondisi abnormal berbasis hidrolika dan kimia proses air minum</text>

      <line x1="0" y1="56" x2="896" y2="56" stroke="#334155" stroke-width="1" />

      <!-- Field 1: Scenario Title -->
      <g transform="translate(0, 70)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">JUDUL SKENARIO GANGGUAN:</text>
        <rect x="0" y="26" width="896" height="42" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="52" fill="#ffffff" font-size="13">Simulasi Kebocoran Pipa Distribusi Zona 2 saat Jam Puncak Pagi</text>
      </g>

      <!-- Field 2: Difficulty Level Dropdown PRD §7 (REQUIRED ADDITION) -->
      <g transform="translate(0, 155)">
        <text x="0" y="16" fill="#f59e0b" font-size="12" font-weight="700">★ TINGKAT KESULITAN &amp; PENGALI XP (PRD SIMSCADA-AIR v1.0 §7):</text>
        <rect x="0" y="26" width="435" height="42" rx="6" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
        <text x="16" y="52" fill="#fbbf24" font-size="13" font-weight="700">Tingkat 3: Sulit (Pengali XP = 2,0x) ▾</text>
        
        <!-- Dropdown Options Preview Right -->
        <rect x="460" y="26" width="436" height="42" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="476" y="52" fill="#94a3b8" font-size="11.5">Pilihan: 1 Mudah (1x) · 2 Sedang (1.5x) · 3 Sulit (2x) · 4 Sangat Sulit (2.5x) · 5 Ujian (3x)</text>
      </g>

      <!-- Field 3: Track & Equipment -->
      <g transform="translate(0, 240)">
        <g transform="translate(0, 0)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">JALUR TERKAIT:</text>
          <rect x="0" y="26" width="435" height="42" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="52" fill="#ffffff" font-size="13">Operator Distribusi / Terpadu ▾</text>
        </g>

        <g transform="translate(460, 0)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">TITIK KONTROL TERDAMPAK:</text>
          <rect x="0" y="26" width="436" height="42" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="52" fill="#ffffff" font-size="13">Valve Isolasi Zona 2 &amp; PRV Distribusi ▾</text>
        </g>
      </g>

      <!-- Field 4: Trigger Time & Deviation Parameters -->
      <g transform="translate(0, 325)">
        <g transform="translate(0, 0)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">WAKTU PEMICU GANGGUAN:</text>
          <rect x="0" y="26" width="435" height="42" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="52" fill="#38bdf8" font-size="13" font-weight="700">Detik ke-90 (01:30) sejak mulai</text>
        </g>

        <g transform="translate(460, 0)">
          <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">AMBANG DEVIASI ALARM:</text>
          <rect x="0" y="26" width="436" height="42" rx="6" fill="#0f172a" stroke="#334155" />
          <text x="16" y="52" fill="#ef4444" font-size="13" font-weight="700">Tekanan &lt; 1,5 bar &amp; Debit &gt; 160 L/s</text>
        </g>
      </g>

      <!-- Field 5: SOP Key & Grading Penalty -->
      <g transform="translate(0, 410)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">KUNCI PENILAIAN SOP &amp; KETENTUAN PENALTI:</text>
        <rect x="0" y="26" width="896" height="85" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="50" fill="#cbd5e1" font-size="12">1. Wajib menutup valve isolasi V-Z2 dalam waktu target 60 detik (Bobot Respons 25%).</text>
        <text x="16" y="70" fill="#cbd5e1" font-size="12">2. Mematikan semua pompa distribusi dianggap tindakan tidak aman (−15 poin penalti PRD §8).</text>
        <text x="16" y="90" fill="#cbd5e1" font-size="12">3. Alarm clear otomatis saat tekanan zona pulih di rentang 2,0–3,0 bar selama 10 detik.</text>
      </g>

      <!-- Field 6: Target Kelompok Assignment -->
      <g transform="translate(0, 520)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">TUGASKAN KE KELOMPOK / ANGKATAN:</text>
        <rect x="0" y="26" width="896" height="42" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="52" fill="#38bdf8" font-size="13" font-weight="700">Angkatan 1 (24 Peserta) · Balai Diklat Air Minum Nusantara</text>
      </g>

      <!-- Submit Button -->
      <g transform="translate(0, 595)">
        <rect width="896" height="50" rx="10" fill="url(#primaryGrad)" />
        <text x="448" y="31" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">SIMPAN &amp; TERBITKAN SKENARIO KE KELAS →</text>
      </g>
    </g>
  </g>

  <!-- Right Column: Pustaka Skenario Baku vs Kustom (Width: 540) -->
  <g transform="translate(1028, 190)">
    <rect width="540" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Daftar Skenario Lembaga</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Pustaka Baku Super Admin (Read-Only) + Skenario Kustom</text>

      <line x1="0" y1="56" x2="484" y2="56" stroke="#334155" stroke-width="1" />

      <!-- Scenario 1: Baku IPA-06 -->
      <g transform="translate(0, 70)">
        <rect width="484" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
        <rect x="14" y="12" width="75" height="20" rx="4" fill="#1e1b4b" stroke="#4338ca" />
        <text x="51" y="26" fill="#c7d2fe" font-size="10" font-weight="700" text-anchor="middle">BAKU SA</text>
        <text x="96" y="28" fill="#ffffff" font-size="12.5" font-weight="700">IPA-06: Lonjakan Kekeruhan</text>
        <text x="14" y="52" fill="#94a3b8" font-size="11">Tingkat 3 Sulit (2,0x) · Kekeruhan air baku 185 NTU</text>
        <text x="14" y="74" fill="#38bdf8" font-size="11">Dipakai di Sesi Latihan Utama · Tidak dapat diubah</text>
      </g>

      <!-- Scenario 2: Baku DST-05 -->
      <g transform="translate(0, 180)">
        <rect width="484" height="95" rx="8" fill="#0f172a" stroke="#1e293b" />
        <rect x="14" y="12" width="75" height="20" rx="4" fill="#1e1b4b" stroke="#4338ca" />
        <text x="51" y="26" fill="#c7d2fe" font-size="10" font-weight="700" text-anchor="middle">BAKU SA</text>
        <text x="96" y="28" fill="#ffffff" font-size="12.5" font-weight="700">DST-05: Gangguan Kebocoran Pipa</text>
        <text x="14" y="52" fill="#94a3b8" font-size="11">Tingkat 3 Sulit (2,0x) · Tekanan drop &amp; debit melonjak</text>
        <text x="14" y="74" fill="#38bdf8" font-size="11">Dipakai di Jalur Distribusi</text>
      </g>

      <!-- Scenario 3: Kustom Lembaga Baru -->
      <g transform="translate(0, 290)">
        <rect width="484" height="110" rx="8" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
        <rect x="14" y="12" width="85" height="20" rx="4" fill="#0284c7" />
        <text x="56" y="26" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">KUSTOM NUS</text>
        <text x="106" y="28" fill="#ffffff" font-size="12.5" font-weight="700">Simulasi Kebocoran Zona 2 Puncak</text>
        <text x="14" y="52" fill="#cbd5e1" font-size="11">Tingkat 3 Sulit (2,0x) · Dibuat oleh Budi Santoso</text>
        <text x="14" y="72" fill="#a7f3d0" font-size="11">Ditugaskan ke: Angkatan 1 (Aktif)</text>
        
        <rect x="14" y="80" width="80" height="20" rx="4" fill="#1e293b" />
        <text x="54" y="94" fill="#cbd5e1" font-size="10" text-anchor="middle">Edit</text>
        <rect x="100" y="80" width="80" height="20" rx="4" fill="#1e293b" />
        <text x="140" y="94" fill="#cbd5e1" font-size="10" text-anchor="middle">Duplikasi</text>
      </g>

      <!-- Information Box PRD §6 -->
      <g transform="translate(0, 430)">
        <rect width="484" height="140" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">KEBIJAKAN KONTEN MULTI-TENANT (PRD §6):</text>
        <text x="16" y="46" fill="#94a3b8" font-size="11">Skenario kustom yang dibuat hanya dapat diakses oleh</text>
        <text x="16" y="66" fill="#94a3b8" font-size="11">peserta Balai Diklat Air Minum Nusantara dan tidak</text>
        <text x="16" y="86" fill="#94a3b8" font-size="11">akan terlihat oleh lembaga lain (Pusat Tirta Mandiri).</text>
        <text x="16" y="106" fill="#94a3b8" font-size="11">Misi baku tetap menjadi acuan uji kelulusan resmi.</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L10: KELOLA SKENARIO GANGGUAN KUSTOM (SimSCADA-Air v1.0)")

def generate_l11():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Instruktur Pengajar · Angkatan 1", name="Budi Santoso, S.T.", initials="BS")
    title = page_title_block("Investigasi Audit &amp; Putar Ulang Sesi (Replay)", "Sesi Contoh Konsisten: Dimas Wahyu Pratama · IPA-06 Lonjakan Kekeruhan (Waktu, Alarm &amp; Nilai Identik L6)", 120)

    content = f"""{hdr}
{title}

  <!-- Replay Player Top Bar & Scrubber Controls (Width: 1536) -->
  <g transform="translate(32, 190)">
    <rect width="1536" height="95" rx="12" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
    
    <!-- Player Controls Left -->
    <g transform="translate(24, 18)">
      <circle cx="20" cy="28" r="18" fill="#0284c7" />
      <text x="20" y="34" fill="#ffffff" font-size="14" text-anchor="middle">❚❚</text>
      
      <!-- Speed Buttons -->
      <rect x="50" y="14" width="45" height="28" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="72" y="32" fill="#cbd5e1" font-size="11" font-weight="700" text-anchor="middle">1x</text>

      <rect x="100" y="14" width="45" height="28" rx="6" fill="#0284c7" />
      <text x="122" y="32" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">2x ✓</text>

      <rect x="150" y="14" width="45" height="28" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="172" y="32" fill="#cbd5e1" font-size="11" font-weight="700" text-anchor="middle">3x</text>

      <!-- Time Stamp -->
      <text x="210" y="34" fill="#ffffff" font-size="16" font-weight="700" font-family="monospace">02:10 <tspan fill="#64748b" font-size="12">/ 08:30</tspan></text>
      <text x="320" y="34" fill="#f59e0b" font-size="12" font-weight="600">📍 Posisi: Operator menaikkan dosis koagulan ke 48 mg/L</text>
    </g>

    <!-- Interactive Timeline Scrubber Bar PRD §12 -->
    <g transform="translate(24, 60)">
      <rect width="1488" height="12" rx="6" fill="#1e293b" />
      <!-- Progress Bar up to 02:10 (approx 25% of 08:30) -->
      <rect width="380" height="12" rx="6" fill="url(#primaryGrad)" />
      
      <!-- Event Marker 1: 01:15 Alarm Baku (x ~ 220) -->
      <circle cx="220" cy="6" r="6" fill="#f59e0b" />
      <text x="220" y="-4" fill="#f59e0b" font-size="9" text-anchor="middle">01:15 (Alarm Baku)</text>

      <!-- Event Marker 2: 01:28 ACK (x ~ 260) -->
      <circle cx="260" cy="6" r="5" fill="#34d399" />
      <text x="260" y="24" fill="#34d399" font-size="9" text-anchor="middle">01:28 (ACK)</text>

      <!-- Event Marker 3: 01:45 Alarm Tinggi Olahan (x ~ 310) -->
      <circle cx="310" cy="6" r="6" fill="#ef4444" />
      <text x="310" y="-4" fill="#ef4444" font-size="9" text-anchor="middle">01:45 (≥3 NTU)</text>

      <!-- Current Playhead Scrubber Scrubber: 02:10 (x = 380) -->
      <circle cx="380" cy="6" r="10" fill="#ffffff" stroke="#0284c7" stroke-width="3" />

      <!-- Event Marker 4: 02:40 Intake 75 L/s (x ~ 470) -->
      <circle cx="470" cy="6" r="5" fill="#38bdf8" />
      <text x="470" y="24" fill="#38bdf8" font-size="9" text-anchor="middle">02:40 (Debit 75 L/s)</text>

      <!-- Event Marker 5: 06:10 Pulih (x ~ 1080) -->
      <circle cx="1080" cy="6" r="6" fill="#10b981" />
      <text x="1080" y="-4" fill="#10b981" font-size="9" text-anchor="middle">06:10 (2,4 NTU)</text>

      <!-- Event Marker 6: 06:20 Auto-Clear (x ~ 1110) -->
      <circle cx="1110" cy="6" r="5" fill="#10b981" />
      <text x="1110" y="24" fill="#10b981" font-size="9" text-anchor="middle">06:20 (Auto-Clear)</text>

      <text x="1480" y="24" fill="#64748b" font-size="9" text-anchor="end">08:30 (Selesai)</text>
    </g>
  </g>

  <!-- Left: Process Replay Canvas & Synchronized Curves (Width: 1040) -->
  <g transform="translate(32, 305)">
    <rect width="1040" height="655" rx="12" fill="url(#cardDark)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="15" font-weight="700">KONDISI PROSES PADA DETIK TERPILIH (02:10)</text>
      <text x="0" y="36" fill="#38bdf8" font-size="12">Nilai parameter di layar HMI saat operator mengeksekusi koreksi dosis koagulan</text>

      <!-- Process Snapshot Grid (4 Units) -->
      <g transform="translate(0, 55)">
        <!-- Box 1: Intake -->
        <rect width="235" height="110" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="14" y="24" fill="#38bdf8" font-size="12" font-weight="700">1. Intake Air Baku</text>
        <text x="14" y="48" fill="#cbd5e1" font-size="11">Debit Air: 100 L/s</text>
        <text x="14" y="70" fill="#f59e0b" font-size="13" font-weight="700">Kekeruhan: 185 NTU</text>
        <text x="14" y="92" fill="#ef4444" font-size="10.5">Alarm Sedang Diakui ✓</text>

        <!-- Box 2: Koagulasi (Action Focus) -->
        <rect x="250" width="235" height="110" rx="8" fill="#0c2538" stroke="#38bdf8" stroke-width="2" />
        <text x="264" y="24" fill="#38bdf8" font-size="12" font-weight="700">2. Koagulasi (Aktif Diubah)</text>
        <text x="264" y="48" fill="#38bdf8" font-size="14" font-weight="700">Dosis PAC: 48,0 mg/L</text>
        <text x="264" y="70" fill="#10b981" font-size="12">pH Koagulasi: 7,20</text>
        <text x="264" y="92" fill="#34d399" font-size="10.5">Tindakan SOP Tepat ✓</text>

        <!-- Box 3: Filtrasi Olahan -->
        <rect x="500" width="235" height="110" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="514" y="24" fill="#38bdf8" font-size="12" font-weight="700">3. Filtrasi Pasir Cepat</text>
        <text x="514" y="48" fill="#ef4444" font-size="14" font-weight="700">Kekeruhan: 3,4 NTU</text>
        <text x="514" y="70" fill="#94a3b8" font-size="11">Headloss: 1,6 Meter</text>
        <text x="514" y="92" fill="#ef4444" font-size="10.5">Alarm Tinggi Diakui</text>

        <!-- Box 4: Desinfeksi & Tank -->
        <rect x="750" width="235" height="110" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="764" y="24" fill="#38bdf8" font-size="12" font-weight="700">4. Desinfeksi Reservoir</text>
        <text x="764" y="48" fill="#cbd5e1" font-size="11">Dosis Klor: 1,20 mg/L</text>
        <text x="764" y="70" fill="#10b981" font-size="12">Sisa Klor: 0,38 mg/L</text>
        <text x="764" y="92" fill="#34d399" font-size="10.5">Kualitas Siap Minum</text>
      </g>

      <!-- Big Synchronized Parameter Curves Chart -->
      <g transform="translate(0, 190)">
        <rect width="990" height="425" rx="10" fill="#090d16" stroke="#1e293b" />
        <text x="20" y="26" fill="#ffffff" font-size="13" font-weight="700">GRAFIK PARAMETER REAL-TIME 1 Hz (IDENTIK L6 &amp; DATA PRD §10):</text>
        
        <!-- Legend -->
        <circle cx="600" cy="22" r="5" fill="#f59e0b" /><text x="612" y="26" fill="#cbd5e1" font-size="11">Kekeruhan Baku (NTU)</text>
        <circle cx="760" cy="22" r="5" fill="#06b6d4" /><text x="772" y="26" fill="#cbd5e1" font-size="11">Air Olahan (NTU)</text>
        <circle cx="900" cy="22" r="5" fill="#38bdf8" /><text x="912" y="26" fill="#cbd5e1" font-size="11">Dosis PAC (mg/L)</text>

        <!-- Graph Grid Lines -->
        <line x1="60" y1="60" x2="950" y2="60" stroke="#1e293b" />
        <line x1="60" y1="140" x2="950" y2="140" stroke="#1e293b" />
        <line x1="60" y1="220" x2="950" y2="220" stroke="#1e293b" />
        <line x1="60" y1="300" x2="950" y2="300" stroke="#1e293b" />
        <line x1="60" y1="370" x2="950" y2="370" stroke="#334155" stroke-width="2" />

        <!-- Vertical Scrubber Needle at 02:10 (x = 310) -->
        <line x1="310" y1="45" x2="310" y2="370" stroke="#ffffff" stroke-width="2" stroke-dasharray="4,2" />
        <rect x="270" y="40" width="80" height="20" rx="4" fill="#ffffff" />
        <text x="310" y="54" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">02:10 WAKTU</text>

        <!-- Air Baku (Yellow curve): climbs 15 to 185 at 01:15 -->
        <path d="M 60 340 L 170 340 L 220 100 L 400 105 L 600 120 L 780 200 L 950 280" fill="none" stroke="#f59e0b" stroke-width="3" />

        <!-- Dosis PAC (Blue curve): stepped from 20 to 48 at 02:10 -->
        <path d="M 60 320 L 310 320 L 310 180 L 950 180" fill="none" stroke="#38bdf8" stroke-width="3" />

        <!-- Air Olahan (Cyan curve): rises to 3.4 at 01:45, drops to 2.4 at 06:10 -->
        <path d="M 60 350 L 260 350 L 285 240 L 310 250 L 450 280 L 680 320 L 950 330" fill="none" stroke="#06b6d4" stroke-width="3.5" />

        <!-- Permenkes 3.0 NTU Threshold Line (Red) -->
        <line x1="60" y1="260" x2="950" y2="260" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="6,4" />
        <text x="945" y="255" fill="#ef4444" font-size="10" font-weight="700" text-anchor="end">Ambang Permenkes: 3,0 NTU</text>

        <!-- X Axis Labels -->
        <text x="60" y="390" fill="#64748b" font-size="10">00:00</text>
        <text x="220" y="390" fill="#f59e0b" font-size="10">01:15 (Alarm Baku)</text>
        <text x="310" y="390" fill="#ffffff" font-size="10" font-weight="700">02:10 (Koreksi)</text>
        <text x="680" y="390" fill="#34d399" font-size="10">06:10 (Pulih)</text>
        <text x="950" y="390" fill="#64748b" font-size="10" text-anchor="end">08:30 (Selesai)</text>
      </g>
    </g>
  </g>

  <!-- Right: Synchronized Action Log & Pedagogical Evaluation (Width: 460) -->
  <g transform="translate(1108, 305)">
    <rect width="460" height="655" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="15" font-weight="700">Audit Log Detik-per-Detik (PRD §10)</text>
      <text x="0" y="36" fill="#94a3b8" font-size="12">Sinkron dengan rekaman sensor &amp; alarm ISA-18.2</text>

      <line x1="0" y1="50" x2="412" y2="50" stroke="#334155" stroke-width="1" />

      <!-- Chronological Events List -->
      <g transform="translate(0, 65)">
        <rect width="412" height="48" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="14" y="20" fill="#f59e0b" font-size="11" font-weight="700">01:15 · ALARM MUNCUL (SEDANG)</text>
        <text x="14" y="36" fill="#cbd5e1" font-size="10.5">Kekeruhan air baku melonjak: 15 ➔ 185 NTU</text>

        <rect y="56" width="412" height="48" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="14" y="76" fill="#34d399" font-size="11" font-weight="700">01:28 · AKUI ALARM (ACK)</text>
        <text x="14" y="92" fill="#cbd5e1" font-size="10.5">Diakui dalam 13 detik (Target: &lt;30s ✓)</text>

        <rect y="112" width="412" height="48" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="14" y="132" fill="#ef4444" font-size="11" font-weight="700">01:45 · ALARM TINGGI MUNCUL</text>
        <text x="14" y="148" fill="#cbd5e1" font-size="10.5">Kekeruhan olahan keluar filter: 3,4 NTU</text>

        <rect y="168" width="412" height="58" rx="6" fill="#0c2538" stroke="#38bdf8" stroke-width="1.5" />
        <text x="14" y="188" fill="#38bdf8" font-size="11" font-weight="800">02:10 · TINDAKAN KOREKSI UTAMA 👈</text>
        <text x="14" y="204" fill="#ffffff" font-size="10.5">Dosis koagulan dinaikkan: 20 ➔ 48 mg/L</text>
        <text x="14" y="218" fill="#a7f3d0" font-size="10">Dosis kapur diatur untuk menjaga pH 7,20</text>

        <rect y="234" width="412" height="48" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="14" y="254" fill="#34d399" font-size="11" font-weight="700">02:40 · PENGATURAN DEBIT</text>
        <text x="14" y="270" fill="#cbd5e1" font-size="10.5">Debit intake diturunkan ke 75 L/s</text>

        <rect y="290" width="412" height="48" rx="6" fill="#064e3b" stroke="#059669" />
        <text x="14" y="310" fill="#34d399" font-size="11" font-weight="700">06:20 · AUTO-CLEAR ALARM TINGGI</text>
        <text x="14" y="326" fill="#ffffff" font-size="10.5">Kekeruhan 2,4 NTU stabil 10 dtk · Clear otomatis</text>
      </g>

      <!-- Pedagogical Note Form by Instructor Pak Budi -->
      <g transform="translate(0, 425)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">CATATAN EVALUASI INSTRUKTUR (PAK BUDI):</text>
        <rect x="0" y="26" width="412" height="95" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="12" y="46" fill="#cbd5e1" font-size="11">"Tindakan Dimas pada 02:10 sangat tepat sesuai SOP.</text>
        <text x="12" y="64" fill="#cbd5e1" font-size="11">Respons waktu 25 detik memenuhi syarat Lencana</text>
        <text x="12" y="82" fill="#cbd5e1" font-size="11">Respons Kilat. Layak direkomendasikan lulus."</text>
        
        <rect x="0" y="130" width="412" height="42" rx="6" fill="#059669" />
        <text x="206" y="156" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">SIMPAN CATATAN &amp; VALIDASI SESI ✓</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L11: PUTAR ULANG SESI SIMULASI (SimSCADA-Air v1.0)")

def generate_l12():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Admin Lembaga · Manajemen SDM", name="Rina Oktaviani", initials="RO")
    title = page_title_block("Kelola Pengguna, Kelompok &amp; Kuota Kursi", "Manajemen Akun Balai Diklat Air Minum Nusantara (NUS) · Kuota 50 Kursi (PRD §5)", 120)

    content = f"""{hdr}
{title}

  <!-- Top License & Seat Quota Summary PRD §5 (Width: 1536) -->
  <g transform="translate(32, 190)">
    <!-- Quota Card 1: Total Kursi & High Usage Warning (≥90%) -->
    <rect width="480" height="90" rx="10" fill="#451a03" stroke="#d97706" stroke-width="2" />
    <text x="20" y="28" fill="#fde68a" font-size="11" font-weight="700">ALOKASI KURSI LISENSI (PRD §5):</text>
    <text x="20" y="58" fill="#ffffff" font-size="28" font-weight="800">46 <tspan font-size="16" fill="#fde68a">/ 50 Kursi Terpakai</tspan></text>
    <rect x="330" y="16" width="130" height="24" rx="4" fill="#d97706" />
    <text x="395" y="32" fill="#ffffff" font-size="10.5" font-weight="800" text-anchor="middle">⚠️ KUOTA 92% (≥90%)</text>
    <text x="20" y="78" fill="#fef3c7" font-size="11">Sisa 4 Kursi Kosong · Segera hubungi Super Admin untuk penambahan kursi</text>

    <!-- Quota Card 2: Kelompok Belajar -->
    <g transform="translate(510, 0)">
      <rect width="480" height="90" rx="10" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11" font-weight="700">KELOMPOK AKTIF (PRD §5):</text>
      <text x="20" y="58" fill="#38bdf8" font-size="28" font-weight="800">2 Kelompok</text>
      <text x="20" y="78" fill="#cbd5e1" font-size="11">Angkatan 1 (24 Peserta) · Angkatan 2 (22 Peserta)</text>
    </g>

    <!-- Quota Card 3: Instruktur & Pimpinan -->
    <g transform="translate(1020, 0)">
      <rect width="516" height="90" rx="10" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11" font-weight="700">TENAGA PENGAJAR &amp; PIMPINAN:</text>
      <text x="20" y="58" fill="#34d399" font-size="28" font-weight="800">1 Instruktur · 1 Pimpinan</text>
      <text x="20" y="78" fill="#cbd5e1" font-size="11">Pak Budi (Instruktur Binaan) · Dr. Bambang (Pimpinan Penandatangan)</text>
    </g>
  </g>

  <!-- User & Account Management Table PRD §5 (Width: 1536) -->
  <g transform="translate(32, 300)">
    <rect width="1536" height="645" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <!-- Table Action Header -->
    <g transform="translate(24, 20)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Daftar Akun Pengguna Lembaga Nusantara (PRD SimSCADA-Air v1.0 §5)</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Semua 7 akun resmi Balai Diklat Air Minum Nusantara terisolasi dari lembaga lain</text>

      <rect x="1220" y="4" width="160" height="34" rx="6" fill="#0284c7" />
      <text x="1300" y="26" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">+ Tambah Peserta</text>

      <rect x="1395" y="4" width="95" height="34" rx="6" fill="#1e293b" stroke="#334155" />
      <text x="1442" y="26" fill="#cbd5e1" font-size="12" text-anchor="middle">Ekspor CSV</text>
    </g>

    <!-- Table Columns -->
    <g transform="translate(0, 75)">
      <rect width="1536" height="40" fill="#0f172a" />
      <text x="32" y="25" fill="#94a3b8" font-size="11" font-weight="700">USERNAME (PRD §5)</text>
      <text x="220" y="25" fill="#94a3b8" font-size="11" font-weight="700">NAMA LENGKAP</text>
      <text x="440" y="25" fill="#94a3b8" font-size="11" font-weight="700">PERAN SISTEM</text>
      <text x="640" y="25" fill="#94a3b8" font-size="11" font-weight="700">KELOMPOK</text>
      <text x="820" y="25" fill="#94a3b8" font-size="11" font-weight="700">JALUR BELAJAR</text>
      <text x="1040" y="25" fill="#94a3b8" font-size="11" font-weight="700">KONDISI DATA AWAL (PRD §5)</text>
      <text x="1380" y="25" fill="#94a3b8" font-size="11" font-weight="700">AKSI</text>

      <line x1="0" y1="40" x2="1536" y2="40" stroke="#1e293b" />

      <!-- Row 1: admin.nusantara -->
      <g transform="translate(0, 48)">
        <rect width="1536" height="54" fill="#0f172a" />
        <text x="32" y="32" fill="#38bdf8" font-size="12" font-weight="700">admin.nusantara</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Rina Oktaviani</text>
        <text x="440" y="32" fill="#34d399" font-size="12" font-weight="600">Admin Lembaga</text>
        <text x="640" y="32" fill="#94a3b8" font-size="12">Seluruh Lembaga</text>
        <text x="820" y="32" fill="#94a3b8" font-size="12">–</text>
        <text x="1040" y="32" fill="#cbd5e1" font-size="11.5">2 kelompok, 1 instruktur, 4 peserta contoh</text>
        <text x="1380" y="32" fill="#0284c7" font-size="11">Kelola Akun</text>
      </g>

      <!-- Row 2: pimpinan.nusantara -->
      <g transform="translate(0, 106)">
        <rect width="1536" height="54" fill="#1e1b4b" opacity="0.3" />
        <text x="32" y="32" fill="#c7d2fe" font-size="12" font-weight="700">pimpinan.nusantara</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Dr. Ir. Bambang Sutrisno, M.Eng.</text>
        <text x="440" y="32" fill="#c084fc" font-size="12" font-weight="600">Pimpinan Lembaga</text>
        <text x="640" y="32" fill="#94a3b8" font-size="12">Manajemen Eksekutif</text>
        <text x="820" y="32" fill="#94a3b8" font-size="12">–</text>
        <text x="1040" y="32" fill="#cbd5e1" font-size="11.5">Dashboard evaluasi terisi data angkatan contoh (T1–T4)</text>
        <text x="1380" y="32" fill="#0284c7" font-size="11">Lihat Hak</text>
      </g>

      <!-- Row 3: instruktur.nusantara -->
      <g transform="translate(0, 164)">
        <rect width="1536" height="54" fill="#0f172a" />
        <text x="32" y="32" fill="#fde68a" font-size="12" font-weight="700">instruktur.nusantara</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Budi Santoso, S.T. (Pak Budi)</text>
        <text x="440" y="32" fill="#fbbf24" font-size="12" font-weight="600">Instruktur SPAM</text>
        <text x="640" y="32" fill="#ffffff" font-size="12">Angkatan 1</text>
        <text x="820" y="32" fill="#94a3b8" font-size="12">Semua Jalur</text>
        <text x="1040" y="32" fill="#cbd5e1" font-size="11.5">Membina Angkatan 1 (Live Matrix &amp; Approval)</text>
        <text x="1380" y="32" fill="#0284c7" font-size="11">Roster Kelas</text>
      </g>

      <!-- Row 4: peserta.baru -->
      <g transform="translate(0, 222)">
        <rect width="1536" height="54" fill="#0f172a" />
        <text x="32" y="32" fill="#38bdf8" font-size="12" font-weight="700">peserta.baru</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Dimas Pratama (Akun Baru)</text>
        <text x="440" y="32" fill="#38bdf8" font-size="12">Peserta Operator</text>
        <text x="640" y="32" fill="#ffffff" font-size="12">Angkatan 1</text>
        <text x="820" y="32" fill="#818cf8" font-size="12">Air Minum Terpadu</text>
        <text x="1040" y="32" fill="#cbd5e1" font-size="11.5">Belum mulai; menampilkan pre-test dan misi pertama</text>
        <text x="1380" y="32" fill="#0284c7" font-size="11">Detail</text>
      </g>

      <!-- Row 5: peserta.ipa (Dimas Sesi Contoh) -->
      <g transform="translate(0, 280)">
        <rect width="1536" height="54" fill="#0c2538" stroke="#0284c7" stroke-width="1" />
        <text x="32" y="32" fill="#38bdf8" font-size="12" font-weight="700">peserta.ipa</text>
        <text x="220" y="32" fill="#ffffff" font-size="12" font-weight="700">Dimas Wahyu Pratama</text>
        <text x="440" y="32" fill="#38bdf8" font-size="12">Peserta Operator</text>
        <text x="640" y="32" fill="#ffffff" font-size="12">Angkatan 1</text>
        <text x="820" y="32" fill="#38bdf8" font-size="12" font-weight="700">Operator IPA</text>
        <text x="1040" y="32" fill="#a7f3d0" font-size="11.5">Di tengah jalur, beberapa misi berbintang (IPA-06 selesai)</text>
        <text x="1380" y="32" fill="#38bdf8" font-size="11" font-weight="700">Lihat Progres</text>
      </g>

      <!-- Row 6: peserta.distribusi -->
      <g transform="translate(0, 338)">
        <rect width="1536" height="54" fill="#0f172a" />
        <text x="32" y="32" fill="#38bdf8" font-size="12" font-weight="700">peserta.distribusi</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Siti Aminah</text>
        <text x="440" y="32" fill="#38bdf8" font-size="12">Peserta Operator</text>
        <text x="640" y="32" fill="#ffffff" font-size="12">Angkatan 1</text>
        <text x="820" y="32" fill="#2dd4bf" font-size="12">Operator Distribusi</text>
        <text x="1040" y="32" fill="#cbd5e1" font-size="11.5">Di tengah jalur distribusi (5 misi lulus)</text>
        <text x="1380" y="32" fill="#0284c7" font-size="11">Detail</text>
      </g>

      <!-- Row 7: peserta.lulus -->
      <g transform="translate(0, 396)">
        <rect width="1536" height="54" fill="#064e3b" opacity="0.3" />
        <text x="32" y="32" fill="#a7f3d0" font-size="12" font-weight="700">peserta.lulus</text>
        <text x="220" y="32" fill="#ffffff" font-size="12">Andi Kurniawan</text>
        <text x="440" y="32" fill="#34d399" font-size="12">Peserta Lulus</text>
        <text x="640" y="32" fill="#ffffff" font-size="12">Angkatan 1</text>
        <text x="820" y="32" fill="#818cf8" font-size="12">Air Minum Terpadu</text>
        <text x="1040" y="32" fill="#a7f3d0" font-size="11.5">Semua 17 misi lulus, piagam resmi SSA/NUS/2026/0001 terbit</text>
        <text x="1380" y="32" fill="#34d399" font-size="11" font-weight="700">Piagam (L8)</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L12: KELOLA PENGGUNA, KELOMPOK & KUOTA KURSI (SimSCADA-Air v1.0)")

def generate_l13():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Admin Lembaga · Konfigurasi Sistem", name="Rina Oktaviani", initials="RO")
    title = page_title_block("Pengaturan Lembaga, Kebijakan &amp; SOP Lokal", "Konfigurasi Tenant PRD §6 & §13: Ambang Kelulusan, Aksen Piagam, Saklar Persetujuan &amp; SOP Lokal", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: Tenant Identity & Certificate Branding PRD §6 & §13 (Width: 750) -->
  <g transform="translate(32, 190)">
    <rect width="750" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Identitas Lembaga &amp; Kustomisasi Piagam (PRD §6 &amp; §13)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Data resmi yang tampil di header aplikasi, laporan eksekutif, dan piagam kelulusan</text>

      <line x1="0" y1="56" x2="686" y2="56" stroke="#334155" stroke-width="1" />

      <!-- Field 1: Official Name -->
      <g transform="translate(0, 70)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">NAMA RESMI LEMBAGA (TENANT):</text>
        <rect x="0" y="26" width="686" height="42" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="52" fill="#ffffff" font-size="13">Balai Diklat Air Minum Nusantara (NUS)</text>
      </g>

      <!-- Field 2: Signers PRD §6 -->
      <g transform="translate(0, 155)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">PEJABAT PENANDATANGAN PIAGAM (PIMPINAN):</text>
        <rect x="0" y="26" width="686" height="42" rx="6" fill="#0f172a" stroke="#334155" />
        <text x="16" y="52" fill="#ffffff" font-size="13">Dr. Ir. Bambang Sutrisno, M.Eng. (Kepala Balai Diklat)</text>
      </g>

      <!-- Field 3: Certificate Accent Color Swatches PRD §13 (REQUIRED ADDITION) -->
      <g transform="translate(0, 240)">
        <text x="0" y="16" fill="#f59e0b" font-size="12" font-weight="700">★ WARNA AKSEN TEMPLAT PIAGAM (PRD §13):</text>
        <text x="0" y="34" fill="#94a3b8" font-size="11">Pilih warna garis tepi dan pita predikat piagam kelulusan A4:</text>
        
        <g transform="translate(0, 44)">
          <!-- Swatch 1: Navy (Active) -->
          <rect width="160" height="44" rx="6" fill="#0c4a6e" stroke="#0284c7" stroke-width="2" />
          <circle cx="24" cy="22" r="10" fill="#0284c7" />
          <text x="44" y="27" fill="#ffffff" font-size="11.5" font-weight="700">Navy Blue ✓</text>

          <!-- Swatch 2: Emerald -->
          <rect x="175" width="160" height="44" rx="6" fill="#064e3b" stroke="#059669" />
          <circle cx="199" cy="22" r="10" fill="#059669" />
          <text x="219" y="27" fill="#a7f3d0" font-size="11.5" font-weight="600">Emerald Green</text>

          <!-- Swatch 3: Gold/Amber -->
          <rect x="350" width="160" height="44" rx="6" fill="#451a03" stroke="#d97706" />
          <circle cx="374" cy="22" r="10" fill="#d97706" />
          <text x="394" y="27" fill="#fde68a" font-size="11.5" font-weight="600">Classic Gold</text>

          <!-- Swatch 4: Ruby -->
          <rect x="525" width="160" height="44" rx="6" fill="#4c0519" stroke="#e11d48" />
          <circle cx="549" cy="22" r="10" fill="#e11d48" />
          <text x="569" y="27" fill="#fecdd3" font-size="11.5" font-weight="600">Ruby Burgundy</text>
        </g>
      </g>

      <!-- Field 4: Mandatory Instructor Approval Switch PRD §13 (REQUIRED ADDITION) -->
      <g transform="translate(0, 355)">
        <rect width="686" height="85" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5" />
        <g transform="translate(20, 20)">
          <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">★ SAKLAR: "PERSETUJUAN INSTRUKTUR WAJIB" (PRD §13):</text>
          <text x="0" y="38" fill="#c7d2fe" font-size="11.5">Bila diaktifkan (ON), piagam peserta membutuhkan verifikasi &amp; tanda tangan</text>
          <text x="0" y="54" fill="#c7d2fe" font-size="11.5">instruktur di L9 sebelum tombol unduh PDF aktif (L8b Menunggu Persetujuan).</text>

          <!-- Toggle Switch Graphic (ON) -->
          <rect x="580" y="6" width="64" height="32" rx="16" fill="#059669" />
          <circle cx="626" cy="22" r="12" fill="#ffffff" />
          <text x="570" y="26" fill="#34d399" font-size="11" font-weight="800" text-anchor="end">AKTIF (ON)</text>
        </g>
      </g>

      <!-- Field 5: Passing Threshold Settings PRD §8 & §13 (REQUIRED ADDITION) -->
      <g transform="translate(0, 465)">
        <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">★ AMBANG KELULUSAN LEMBAGA (PASSING GRADE KKM):</text>
        
        <g transform="translate(0, 28)">
          <!-- KKM Misi Biasa -->
          <rect width="215" height="70" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">KKM Misi Biasa (1★)</text>
          <text x="14" y="50" fill="#38bdf8" font-size="20" font-weight="700">≥ 70 <tspan font-size="11">Poin</tspan></text>

          <!-- KKM Misi Kelulusan -->
          <rect x="235" width="215" height="70" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">KKM Misi Kelulusan</text>
          <text x="14" y="50" fill="#f59e0b" font-size="20" font-weight="700">≥ 80 <tspan font-size="11">Poin (PRD §8)</tspan></text>

          <!-- KKM Post-Test -->
          <rect x="470" width="216" height="70" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">KKM Post-Test Akhir</text>
          <text x="14" y="50" fill="#34d399" font-size="20" font-weight="700">≥ 70 <tspan font-size="11">Poin (PRD §13)</tspan></text>
        </g>
      </g>

      <!-- Save Settings Button -->
      <g transform="translate(0, 600)">
        <rect width="686" height="48" rx="8" fill="url(#primaryGrad)" />
        <text x="343" y="30" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">SIMPAN PENGATURAN LEMBAGA</text>
      </g>
    </g>
  </g>

  <!-- Right Column: Local SOP Notes per Control Point + Alarm Threshold Rule (Width: 750) -->
  <g transform="translate(818, 190)">
    <rect width="750" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 26)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Catatan SOP Lokal per Titik Kontrol (PRD §9)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Tambahkan catatan operasional khusus lembaga tanpa mengubah narasi baku Super Admin</text>

      <line x1="0" y1="56" x2="686" y2="56" stroke="#334155" stroke-width="1" />

      <!-- SOP Editor: Dropdown Select Control Point PRD §9 -->
      <g transform="translate(0, 70)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">PILIH TITIK KONTROL UNTUK DITAMBAHKAN CATATAN SOP LOKAL:</text>
        <rect x="0" y="26" width="686" height="42" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" />
        <text x="16" y="52" fill="#ffffff" font-size="13" font-weight="700">Flash Mixer Koagulasi (Pembubuhan &amp; Pengaduk Cepat) ▾</text>
      </g>

      <!-- SOP Editor: Local Notes Textarea PRD §9 -->
      <g transform="translate(0, 155)">
        <text x="0" y="16" fill="#e2e8f0" font-size="12" font-weight="700">ISI CATATAN SOP LOKAL (LANGSUNG TAMPIL DI POP-UP L5a):</text>
        <rect x="0" y="26" width="686" height="150" rx="8" fill="#0f172a" stroke="#334155" />
        <text x="16" y="54" fill="#a7f3d0" font-size="12">"Di instalasi latih IPA Balai Nusantara, injeksi koagulan memakai</text>
        <text x="16" y="74" fill="#a7f3d0" font-size="12">dosing pump membran otomatis dengan kalibrasi larutan PAC 10%.</text>
        <text x="16" y="94" fill="#a7f3d0" font-size="12">Batas minimum tangki harian PAC adalah 20% sebelum pengisian ulang."</text>
        <text x="16" y="150" fill="#64748b" font-size="11">Catatan ini otomatis muncul pada pop-up narasi titik kontrol L5a bagi semua peserta Balai Nusantara.</text>
      </g>

      <!-- REMOVAL OF DEFAULT ALARM EDITING NOTICE (CRITICAL PRD REQUIREMENT) -->
      <g transform="translate(0, 350)">
        <rect width="686" height="180" rx="10" fill="#450a0a" opacity="0.3" stroke="#ef4444" stroke-width="1.5" />
        <g transform="translate(20, 20)">
          <text x="0" y="18" fill="#fca5a5" font-size="13" font-weight="700">🔒 AMBANG BATAS ALARM BAKU TERKUNCI (PRD SIMSCADA-AIR v1.0 §6):</text>
          <text x="0" y="42" fill="#ffffff" font-size="12" font-weight="600">Pengeditan ambang alarm baku ditiadakan bagi Admin Lembaga.</text>
          <text x="0" y="62" fill="#cbd5e1" font-size="11.5">Ambang batas alarm baku (Permenkes No. 2/2023) ditetapkan terpusat</text>
          <text x="0" y="80" fill="#cbd5e1" font-size="11.5">oleh Super Admin platform demi menjamin standarisasi uji kompetensi:</text>
          <text x="0" y="102" fill="#38bdf8" font-size="11.5">• Kekeruhan air olahan: Tinggi bila ≥ 3,0 NTU (Auto-clear ≤ 2,7 NTU)</text>
          <text x="0" y="120" fill="#ef4444" font-size="11.5">• Sisa klor: Kritis bila &lt; 0,2 mg/L · Tekanan distribusi: Drop bila &lt; 1,5 bar</text>
          <text x="0" y="140" fill="#a7f3d0" font-size="11">Lembaga tidak dapat mengubah ambang baku ini.</text>
        </g>
      </g>

      <!-- Save SOP Button -->
      <g transform="translate(0, 560)">
        <rect width="686" height="48" rx="8" fill="#065f46" />
        <text x="343" y="30" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">SIMPAN CATATAN SOP KOAGULASI ✓</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L13: PENGATURAN LEMBAGA & SOP LOKAL (SimSCADA-Air v1.0)")

def generate_l14():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Pimpinan Lembaga · Evaluasi Eksekutif", name="Dr. Ir. Bambang Sutrisno, M.Eng.", initials="BS")
    title = page_title_block("Dasbor Evaluasi Lembaga &amp; ROI Pelatihan", "4 Metrik Kunci Keberhasilan (T1–T4 PRD §3) · Kartu Pemakaian Lisensi &amp; Ekspor Laporan (PRD §12)", 120)

    content = f"""{hdr}
{title}

  <!-- Filter & Period Bar PRD §12 (Width: 1536) -->
  <g transform="translate(32, 190)">
    <rect width="1536" height="50" rx="8" fill="#0f172a" stroke="#334155" />
    
    <text x="20" y="31" fill="#94a3b8" font-size="11.5">Periode:</text>
    <rect x="75" y="10" width="160" height="30" rx="4" fill="#1e293b" stroke="#334155" />
    <text x="88" y="29" fill="#ffffff" font-size="11.5">6 Bulan Terakhir ▾</text>

    <text x="260" y="31" fill="#94a3b8" font-size="11.5">Jalur:</text>
    <rect x="300" y="10" width="140" height="30" rx="4" fill="#1e293b" stroke="#334155" />
    <text x="312" y="29" fill="#ffffff" font-size="11.5">Semua Jalur ▾</text>

    <text x="460" y="31" fill="#94a3b8" font-size="11.5">Kelompok:</text>
    <rect x="530" y="10" width="150" height="30" rx="4" fill="#1e293b" stroke="#334155" />
    <text x="542" y="29" fill="#ffffff" font-size="11.5">Angkatan 1 &amp; 2 ▾</text>

    <text x="700" y="31" fill="#94a3b8" font-size="11.5">Instruktur:</text>
    <rect x="770" y="10" width="160" height="30" rx="4" fill="#1e293b" stroke="#334155" />
    <text x="782" y="29" fill="#ffffff" font-size="11.5">Budi Santoso, S.T. ▾</text>

    <!-- Export Buttons PRD §12 -->
    <rect x="1220" y="9" width="145" height="32" rx="6" fill="#1e293b" stroke="#0284c7" />
    <text x="1292" y="29" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">📊 Ekspor Excel (.xlsx)</text>

    <rect x="1375" y="9" width="145" height="32" rx="6" fill="#0284c7" />
    <text x="1447" y="29" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">📄 Ekspor PDF Berkop</text>
  </g>

  <!-- 4 PRIMARY KPI METRICS PRD §3 (T1, T2, T3, T4 - Mathematical Consistency) -->
  <g transform="translate(32, 255)">
    <!-- T1: Peningkatan Kompetensi PRD §3 -->
    <rect width="365" height="135" rx="10" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
    <g transform="translate(20, 20)">
      <text x="0" y="16" fill="#a7f3d0" font-size="11" font-weight="700">T1: PENINGKATAN KOMPETENSI (PRD §3):</text>
      <text x="0" y="52" fill="#34d399" font-size="34" font-weight="800">+28,6%</text>
      <rect x="170" y="26" width="140" height="24" rx="4" fill="#065f46" />
      <text x="240" y="42" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">TARGET: ≥ 25% (LULUS)</text>
      <text x="0" y="76" fill="#cbd5e1" font-size="11">Pre-Test Rata-Rata: <tspan font-weight="700">56,0</tspan> ➔ Post-Test: <tspan font-weight="700">72,0</tspan></text>
      <text x="0" y="94" fill="#6ee7b7" font-size="10.5">Formula: ((72 − 56) ÷ 56) × 100% = +28,6% ✓</text>
    </g>

    <!-- T2: Penguasaan 5 Gangguan Utama PRD §3 -->
    <g transform="translate(390, 0)">
      <rect width="365" height="135" rx="10" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
      <g transform="translate(20, 20)">
        <text x="0" y="16" fill="#a7f3d0" font-size="11" font-weight="700">T2: PENGUASAAN 5 GANGGUAN UTAMA:</text>
        <text x="0" y="52" fill="#34d399" font-size="34" font-weight="800">83,3%</text>
        <rect x="170" y="26" width="140" height="24" rx="4" fill="#065f46" />
        <text x="240" y="42" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">TARGET: ≥ 80% (LULUS)</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11">Lulus IPA-06, 07, 08 &amp; DST-05, 06 (≥1★)</text>
        <text x="0" y="94" fill="#6ee7b7" font-size="10.5">40 dari 48 peserta aktif lulus ke-5 gangguan</text>
      </g>
    </g>

    <!-- T3: Waktu Menuju Lulus PRD §3 -->
    <g transform="translate(780, 0)">
      <rect width="365" height="135" rx="10" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="2" />
      <g transform="translate(20, 20)">
        <text x="0" y="16" fill="#38bdf8" font-size="11" font-weight="700">T3: WAKTU MENUJU KELULUSAN:</text>
        <text x="0" y="52" fill="#38bdf8" font-size="34" font-weight="800">58 Hari</text>
        <rect x="160" y="26" width="150" height="24" rx="4" fill="#0369a1" />
        <text x="235" y="42" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">±2 BULAN (TARGET T3)</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11">Median mulai jalur hingga piagam terbit</text>
        <text x="0" y="94" fill="#7dd3fc" font-size="10.5">Turun dari orientasi konvensional (±90 hari)</text>
      </g>
    </g>

    <!-- T4: Tingkat Kelulusan PRD §3 -->
    <g transform="translate(1170, 0)">
      <rect width="366" height="135" rx="10" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
      <g transform="translate(20, 20)">
        <text x="0" y="16" fill="#a7f3d0" font-size="11" font-weight="700">T4: PENYELESAIAN JALUR (KELULUSAN):</text>
        <text x="0" y="52" fill="#34d399" font-size="34" font-weight="800">75,0%</text>
        <rect x="170" y="26" width="140" height="24" rx="4" fill="#065f46" />
        <text x="240" y="42" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">TARGET: ≥ 70% (LULUS)</text>
        <text x="0" y="76" fill="#cbd5e1" font-size="11">36 Piagam Terbit ÷ 48 Peserta Aktif</text>
        <text x="0" y="94" fill="#6ee7b7" font-size="10.5">Tingkat penyelesaian tinggi tanpa drop out</text>
      </g>
    </g>
  </g>

  <!-- SEPARATE DEDICATED CARD: PEMAKAIAN LISENSI PRD §12 (Width: 1536) -->
  <g transform="translate(32, 405)">
    <rect width="1536" height="105" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#c7d2fe" font-size="13" font-weight="700">KARTU PEMAKAIAN LISENSI &amp; NILAI INVESTASI (ROI DIKLAT PRD §12):</text>
      
      <!-- Metric 1: Seats -->
      <g transform="translate(0, 32)">
        <text x="0" y="16" fill="#a5b4fc" font-size="11">Kursi Lisensi Terpakai:</text>
        <text x="0" y="40" fill="#ffffff" font-size="20" font-weight="800">46 / 50 <tspan font-size="13" fill="#fbbf24">(92% Terpakai)</tspan></text>
      </g>

      <!-- Metric 2: Sisa Masa Lisensi -->
      <g transform="translate(380, 32)">
        <text x="0" y="16" fill="#a5b4fc" font-size="11">Sisa Masa Berlaku Lisensi:</text>
        <text x="0" y="40" fill="#34d399" font-size="20" font-weight="800">245 Hari Tersisa</text>
      </g>

      <!-- Metric 3: Total Jam Simulasi -->
      <g transform="translate(760, 32)">
        <text x="0" y="16" fill="#a5b4fc" font-size="11">Total Waktu Simulasi SCADA:</text>
        <text x="0" y="40" fill="#38bdf8" font-size="20" font-weight="800">412 Jam Praktik</text>
      </g>

      <!-- Metric 4: Peserta Aktif 14 Hari -->
      <g transform="translate(1140, 32)">
        <text x="0" y="16" fill="#a5b4fc" font-size="11">Peserta Aktif (14 Hari Terakhir):</text>
        <text x="0" y="40" fill="#ffffff" font-size="20" font-weight="800">42 Peserta Aktif</text>
      </g>
    </g>
  </g>

  <!-- Detailed Diagnostic Grid: 5 Hardest Missions + Frequent Mistakes (Width: 1536) -->
  <g transform="translate(32, 525)">
    <!-- Left: 5 Misi Paling Sulit (Gagal Percobaan Pertama) PRD §12 -->
    <rect width="750" height="420" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="14" font-weight="700">5 Misi Paling Sulit (Tingkat Gagal Percobaan Pertama PRD §12):</text>
      <text x="0" y="36" fill="#94a3b8" font-size="11.5">Bahan evaluasi materi pengajaran bagi instruktur SPAM</text>

      <line x1="0" y1="48" x2="702" y2="48" stroke="#334155" stroke-width="1" />

      <!-- Mission 1: IPA-06 -->
      <g transform="translate(0, 60)">
        <text x="0" y="16" fill="#cbd5e1" font-size="12">1. <tspan font-weight="700" fill="#ffffff">IPA-06</tspan> Gangguan Lonjakan Kekeruhan Air Baku</text>
        <text x="700" y="16" fill="#ef4444" font-size="12" font-weight="700" text-anchor="end">42% Gagal Percobaan 1</text>
        <rect y="24" width="702" height="8" rx="4" fill="#0f172a" />
        <rect y="24" width="295" height="8" rx="4" fill="#ef4444" />
      </g>

      <!-- Mission 2: DST-05 -->
      <g transform="translate(0, 115)">
        <text x="0" y="16" fill="#cbd5e1" font-size="12">2. <tspan font-weight="700" fill="#ffffff">DST-05</tspan> Gangguan Kebocoran Pipa Distribusi</text>
        <text x="700" y="16" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="end">38% Gagal Percobaan 1</text>
        <rect y="24" width="702" height="8" rx="4" fill="#0f172a" />
        <rect y="24" width="266" height="8" rx="4" fill="#f59e0b" />
      </g>

      <!-- Mission 3: TRP-01 -->
      <g transform="translate(0, 170)">
        <text x="0" y="16" fill="#cbd5e1" font-size="12">3. <tspan font-weight="700" fill="#ffffff">TRP-01</tspan> Gangguan Berantai Hulu ke Hilir</text>
        <text x="700" y="16" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="end">35% Gagal Percobaan 1</text>
        <rect y="24" width="702" height="8" rx="4" fill="#0f172a" />
        <rect y="24" width="245" height="8" rx="4" fill="#f59e0b" />
      </g>

      <!-- Mission 4: DST-06 -->
      <g transform="translate(0, 225)">
        <text x="0" y="16" fill="#cbd5e1" font-size="12">4. <tspan font-weight="700" fill="#ffffff">DST-06</tspan> Gangguan Tekanan Jaringan Drop</text>
        <text x="700" y="16" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="end">31% Gagal Percobaan 1</text>
        <rect y="24" width="702" height="8" rx="4" fill="#0f172a" />
        <rect y="24" width="217" height="8" rx="4" fill="#38bdf8" />
      </g>

      <!-- Mission 5: IPA-07 -->
      <g transform="translate(0, 280)">
        <text x="0" y="16" fill="#cbd5e1" font-size="12">5. <tspan font-weight="700" fill="#ffffff">IPA-07</tspan> Gangguan Pompa Intake Trip</text>
        <text x="700" y="16" fill="#34d399" font-size="12" font-weight="700" text-anchor="end">28% Gagal Percobaan 1</text>
        <rect y="24" width="702" height="8" rx="4" fill="#0f172a" />
        <rect y="24" width="196" height="8" rx="4" fill="#34d399" />
      </g>
    </g>
  </g>

  <!-- Right: Kesalahan Tersering & Perbandingan Angkatan PRD §12 -->
  <g transform="translate(818, 525)">
    <rect width="750" height="420" rx="10" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#ffffff" font-size="14" font-weight="700">Analisis Kesalahan Tersering &amp; Perbandingan Angkatan (PRD §12):</text>
      <text x="0" y="36" fill="#94a3b8" font-size="11.5">Bahan penyempurnaan SOP operasional dan kurikulum kelas</text>

      <line x1="0" y1="48" x2="702" y2="48" stroke="#334155" stroke-width="1" />

      <!-- Top 3 Mistakes PRD §12 -->
      <g transform="translate(0, 60)">
        <rect width="702" height="54" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="24" fill="#ef4444" font-size="12" font-weight="700">1. Terlambat Naikkan Koagulan saat Lonjakan Baku (34 Kejadian)</text>
        <text x="16" y="42" fill="#cbd5e1" font-size="11">Rata-rata respons terlambat 28 detik dari target awal.</text>

        <rect y="64" width="702" height="54" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="88" fill="#f59e0b" font-size="12" font-weight="700">2. Menekan Tombol Clear saat Kondisi Masih Abnormal (26 Kejadian)</text>
        <text x="16" y="106" fill="#cbd5e1" font-size="11">Sistem menolak dengan pesan "Penyebab belum ditangani".</text>

        <rect y="128" width="702" height="54" rx="6" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="152" fill="#38bdf8" font-size="12" font-weight="700">3. Menutup Valve Isolasi yang Salah pada Kebocoran (18 Kejadian)</text>
        <text x="16" y="170" fill="#cbd5e1" font-size="11">Mengakibatkan tekanan drop merembet ke zona pelanggan aktif.</text>
      </g>

      <!-- Comparison: Angkatan 1 vs Angkatan 2 -->
      <g transform="translate(0, 270)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">KOMPARASI KELOMPOK (ANGKATAN 1 vs ANGKATAN 2):</text>
        
        <rect y="26" width="340" height="70" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="48" fill="#ffffff" font-size="12" font-weight="700">Angkatan 1 (Budi Santoso)</text>
        <text x="16" y="68" fill="#34d399" font-size="11">Rata-Rata Skor: 84,2 · Kelulusan: 79%</text>

        <rect x="360" y="26" width="342" height="70" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="376" y="48" fill="#ffffff" font-size="12" font-weight="700">Angkatan 2 (Budi Santoso)</text>
        <text x="376" y="68" fill="#38bdf8" font-size="11">Rata-Rata Skor: 81,0 · Kelulusan: 71%</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L14: DASBOR EVALUASI LEMBAGA (SimSCADA-Air v1.0)")

def generate_l15():
    # Super Admin Platform Console
    title = page_title_block("Konsol Pengelola Lembaga &amp; Lisensi Multi-Tenant", "Super Admin Platform SimSCADA-Air · Monitoring Kapasitas &amp; Peringatan Dini Sistem (PRD §5 & §12)", 75)

    content = f"""  <!-- Super Admin Custom Header PRD §5 -->
  <g transform="translate(0, 40)">
    <rect width="1600" height="58" fill="#030712" stroke="#1e293b" stroke-width="1" />
    <g transform="translate(32, 12)">
      <rect width="36" height="36" rx="8" fill="#4338ca" />
      <text x="18" y="24" fill="#ffffff" font-size="16" font-weight="800" text-anchor="middle">👑</text>
      <text x="48" y="20" fill="#ffffff" font-size="16" font-weight="700">SimSCADA-Air Console</text>
      <text x="48" y="34" fill="#818cf8" font-size="11">KONSOL SUPER ADMIN GLOBAL · PENGELOLA MULTI-TENANT</text>
    </g>
    <g transform="translate(1380, 14)">
      <rect width="188" height="32" rx="6" fill="#1e1b4b" stroke="#4338ca" />
      <text x="94" y="21" fill="#c7d2fe" font-size="11.5" font-weight="700" text-anchor="middle">superadmin (Root)</text>
    </g>
  </g>

{title}

  <!-- TWO CRITICAL ALERT BANNERS PRD §12 (Quota >= 90% & Expiry <= 30 Days) -->
  <g transform="translate(32, 155)">
    <!-- Alert 1: Quota >= 90% (Nusantara) -->
    <rect width="750" height="65" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="2" filter="url(#glowAmber)" />
    <text x="20" y="26" fill="#fde68a" font-size="12" font-weight="800">⚠️ PERINGATAN SISTEM: KUOTA KURSI MENCAPAI AMBANG TINGGI (≥ 90%)</text>
    <text x="20" y="48" fill="#ffffff" font-size="12">Lembaga <tspan font-weight="700" fill="#fde68a">Balai Diklat Air Minum Nusantara</tspan> telah memakai <tspan font-weight="800" fill="#fde68a">46 dari 50 kursi (92%)</tspan>. Tawarkan ekspansi kuota lisensi.</text>

    <!-- Alert 2: Expiry <= 30 Days (Tirta Mandiri) -->
    <g transform="translate(786, 0)">
      <rect width="750" height="65" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)" />
      <text x="20" y="26" fill="#fca5a5" font-size="12" font-weight="800">⚠️ PERINGATAN SISTEM: MASA LISENSI AKAN BERAKHIR (≤ 30 HARI)</text>
      <text x="20" y="48" fill="#ffffff" font-size="12">Lembaga <tspan font-weight="700" fill="#fca5a5">Pusat Pelatihan Tirta Mandiri</tspan> berakhir dalam <tspan font-weight="800" fill="#fca5a5">28 Hari</tspan>. Kirimkan notifikasi penagihan perpanjangan.</text>
    </g>
  </g>

  <!-- Global Platform Overview Cards (Width: 1536) -->
  <g transform="translate(32, 235)">
    <rect width="365" height="85" rx="8" fill="#0f172a" stroke="#1e293b" />
    <text x="20" y="28" fill="#94a3b8" font-size="11">Total Lembaga Aktif</text>
    <text x="20" y="58" fill="#ffffff" font-size="24" font-weight="800">2 Lembaga Pembeli</text>

    <g transform="translate(390, 0)">
      <rect width="365" height="85" rx="8" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11">Total Kuota Kursi</text>
      <text x="20" y="58" fill="#38bdf8" font-size="24" font-weight="800">68 / 100 Kursi (68%)</text>
    </g>

    <g transform="translate(780, 0)">
      <rect width="365" height="85" rx="8" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11">Total Peserta Aktif</text>
      <text x="20" y="58" fill="#34d399" font-size="24" font-weight="800">60 Peserta Aktif</text>
    </g>

    <g transform="translate(1170, 0)">
      <rect width="366" height="85" rx="8" fill="#0f172a" stroke="#1e293b" />
      <text x="20" y="28" fill="#94a3b8" font-size="11">Total Piagam Terbit</text>
      <text x="20" y="58" fill="#f59e0b" font-size="24" font-weight="800">48 Piagam Sah</text>
    </g>
  </g>

  <!-- Table: Lembaga & Status Lisensi PRD §5 & §12 (Width: 1536) -->
  <g transform="translate(32, 335)">
    <rect width="1536" height="610" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(24, 20)">
      <text x="0" y="20" fill="#ffffff" font-size="16" font-weight="700">Daftar Lembaga Pembeli (Multi-Tenant Management PRD §5)</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Manajemen paket jalur, alokasi kuota kursi, tanggal kontrak, dan status pemakaian</text>

      <rect x="1350" y="6" width="160" height="34" rx="6" fill="#4338ca" />
      <text x="1430" y="28" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">+ Daftarkan Tenant</text>
    </g>

    <!-- Table Header Columns PRD §12 -->
    <g transform="translate(0, 75)">
      <rect width="1536" height="42" fill="#0f172a" />
      <text x="32" y="26" fill="#94a3b8" font-size="11" font-weight="700">NAMA LEMBAGA (TENANT)</text>
      <text x="280" y="26" fill="#94a3b8" font-size="11" font-weight="700">KODE</text>
      <text x="360" y="26" fill="#94a3b8" font-size="11" font-weight="700">STATUS LISENSI</text>
      <text x="500" y="26" fill="#94a3b8" font-size="11" font-weight="700">PAKET JALUR</text>
      <text x="680" y="26" fill="#94a3b8" font-size="11" font-weight="700">KURSI TERPAKAI / KUOTA</text>
      <text x="940" y="26" fill="#94a3b8" font-size="11" font-weight="700">PESERTA AKTIF</text>
      <text x="1100" y="26" fill="#94a3b8" font-size="11" font-weight="700">PIAGAM TERBIT</text>
      <text x="1260" y="26" fill="#94a3b8" font-size="11" font-weight="700">SISA LISENSI</text>
      <text x="1420" y="26" fill="#94a3b8" font-size="11" font-weight="700">AKSI</text>

      <line x1="0" y1="42" x2="1536" y2="42" stroke="#1e293b" />

      <!-- Row 1: Balai Diklat Air Minum Nusantara -->
      <g transform="translate(0, 52)">
        <rect width="1536" height="70" fill="#0f172a" />
        <text x="32" y="32" fill="#ffffff" font-size="13" font-weight="700">Balai Diklat Air Minum Nusantara</text>
        <text x="32" y="50" fill="#94a3b8" font-size="11">Admin: admin.nusantara · Pimpinan: Dr. Bambang</text>
        
        <text x="280" y="38" fill="#38bdf8" font-size="12" font-weight="700">NUS</text>

        <rect x="360" y="22" width="75" height="26" rx="4" fill="#065f46" />
        <text x="397" y="39" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">AKTIF ✓</text>

        <text x="500" y="38" fill="#c7d2fe" font-size="12" font-weight="600">Air Minum Terpadu (17 Misi)</text>

        <!-- Quota Seat (46/50 = 92% -> WARNING) -->
        <g transform="translate(680, 20)">
          <text x="0" y="16" fill="#f59e0b" font-size="13" font-weight="800">46 / 50 Kursi (92%)</text>
          <rect y="22" width="180" height="8" rx="4" fill="#1e293b" />
          <rect y="22" width="165" height="8" rx="4" fill="#f59e0b" />
          <text x="0" y="44" fill="#fde68a" font-size="9.5" font-weight="600">⚠️ Peringatan Kuota ≥90%</text>
        </g>

        <text x="940" y="38" fill="#ffffff" font-size="13" font-weight="700">42 Peserta</text>
        <text x="1100" y="38" fill="#34d399" font-size="13" font-weight="700">36 Piagam</text>

        <text x="1260" y="38" fill="#ffffff" font-size="12">245 Hari</text>

        <rect x="1410" y="22" width="90" height="28" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="1455" y="40" fill="#cbd5e1" font-size="11" font-weight="600" text-anchor="middle">Kelola Lisensi</text>
      </g>

      <!-- Row 2: Pusat Pelatihan Tirta Mandiri (Expiry <= 30 Days) -->
      <g transform="translate(0, 132)">
        <rect width="1536" height="70" fill="#450a0a" opacity="0.3" stroke="#ef4444" stroke-width="1" />
        <text x="32" y="32" fill="#ffffff" font-size="13" font-weight="700">Pusat Pelatihan Tirta Mandiri</text>
        <text x="32" y="50" fill="#94a3b8" font-size="11">Admin: admin.tirta · Uji Isolasi Multi-Tenant</text>
        
        <text x="280" y="38" fill="#38bdf8" font-size="12" font-weight="700">TRM</text>

        <rect x="360" y="22" width="75" height="26" rx="4" fill="#065f46" />
        <text x="397" y="39" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">AKTIF ✓</text>

        <text x="500" y="38" fill="#38bdf8" font-size="12" font-weight="600">Operator IPA (9 Misi)</text>

        <!-- Quota Seat (22/50 = 44%) -->
        <g transform="translate(680, 20)">
          <text x="0" y="16" fill="#ffffff" font-size="13" font-weight="700">22 / 50 Kursi (44%)</text>
          <rect y="22" width="180" height="8" rx="4" fill="#1e293b" />
          <rect y="22" width="79" height="8" rx="4" fill="#0284c7" />
          <text x="0" y="44" fill="#94a3b8" font-size="9.5">Kapasitas Aman</text>
        </g>

        <text x="940" y="38" fill="#ffffff" font-size="13" font-weight="700">18 Peserta</text>
        <text x="1100" y="38" fill="#34d399" font-size="13" font-weight="700">12 Piagam</text>

        <!-- Expiry Warning <= 30 Days -->
        <g transform="translate(1260, 20)">
          <text x="0" y="16" fill="#ef4444" font-size="13" font-weight="800">28 Hari Tersisa</text>
          <text x="0" y="34" fill="#fca5a5" font-size="10" font-weight="700">⚠️ Berakhir ≤30 Hari</text>
        </g>

        <rect x="1410" y="22" width="90" height="28" rx="6" fill="#ef4444" />
        <text x="1455" y="40" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Perpanjang</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L15: KONSOL SUPER ADMIN MULTI-TENANT (SimSCADA-Air v1.0)")

def generate_l16():
    title = page_title_block("Portal Verifikasi Keaslian Piagam Publik", "Portal Terbuka Tanpa Login untuk Rekruter, PDAM &amp; Regulator (Sesuai Ketentuan PRD §13)", 75)

    content = f"""  <!-- Public Verification Top Clean Header (No User Login Needed) -->
  <g transform="translate(0, 40)">
    <rect width="1600" height="58" fill="#030712" stroke="#1e293b" stroke-width="1" />
    <g transform="translate(32, 12)">
      <rect width="36" height="36" rx="8" fill="#0284c7" />
      <path d="M 18 8 C 18 8, 12 18, 12 23 A 6 6 0 0 0 24 23 C 24 18, 18 8, 18 8 Z" fill="#ffffff" />
      <text x="48" y="22" fill="#ffffff" font-size="16" font-weight="700">SimSCADA-Air Portal Publik</text>
      <text x="48" y="36" fill="#38bdf8" font-size="10.5">LAYANAN VERIFIKASI KEABSAHAN PIAGAM KELULUSAN OPERATOR AIR MINUM</text>
    </g>
    <rect x="1380" y="14" width="188" height="30" rx="6" fill="#1e293b" stroke="#334155" />
    <text x="1474" y="33" fill="#94a3b8" font-size="11" text-anchor="middle">AKSES PUBLIK (TANPA LOGIN)</text>
  </g>

{title}

  <!-- Search Card: Input Nomor Piagam PRD §13 -->
  <g transform="translate(32, 160)">
    <rect width="1536" height="85" rx="10" fill="#0f172a" stroke="#334155" />
    <g transform="translate(24, 22)">
      <text x="0" y="26" fill="#ffffff" font-size="13" font-weight="700">MASUKKAN NOMOR REGISTRASI PIAGAM:</text>
      
      <rect x="290" y="2" width="550" height="42" rx="6" fill="#070c18" stroke="#0284c7" stroke-width="1.5" />
      <text x="306" y="28" fill="#38bdf8" font-size="14" font-weight="700" letter-spacing="1">SSA/NUS/2026/0001</text>

      <rect x="860" y="2" width="180" height="42" rx="6" fill="url(#primaryGrad)" />
      <text x="950" y="27" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">🔍 VERIFIKASI SEKARANG</text>
    </g>
  </g>

  <!-- Main Verification Result Card (PRD §13 STRICT SPEC: ONLY REQUIRED FIELDS) -->
  <g transform="translate(32, 265)">
    <rect width="1536" height="580" rx="14" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
    
    <g transform="translate(48, 36)">
      <!-- Official Status Badge: SAH & VALID PRD §13 -->
      <g transform="translate(0, 0)">
        <rect width="280" height="44" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2" />
        <circle cx="24" cy="22" r="10" fill="#34d399" />
        <text x="24" y="26" fill="#064e3b" font-size="12" font-weight="900" text-anchor="middle">✓</text>
        <text x="46" y="28" fill="#ffffff" font-size="14" font-weight="800" letter-spacing="0.5">STATUS: SAH / VALID</text>

        <!-- Interactive Simulation Toggle (Sah vs Dicabut) -->
        <rect x="1150" y="4" width="280" height="36" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="1290" y="26" fill="#94a3b8" font-size="11" text-anchor="middle">Simulasi Status: <tspan fill="#ef4444" font-weight="700">Uji Dicabut [Toggle]</tspan></text>
      </g>

      <text x="0" y="80" fill="#ffffff" font-size="22" font-weight="700">Data Terverifikasi Resmi di Database Pusat SimSCADA-Air</text>
      <text x="0" y="102" fill="#94a3b8" font-size="12.5">Nomor Registrasi Unik: <tspan font-weight="700" fill="#38bdf8">SSA/NUS/2026/0001</tspan> · Diterbitkan secara resmi oleh Balai Diklat Air Minum Nusantara</text>

      <line x1="0" y1="120" x2="1440" y2="120" stroke="#334155" stroke-width="1" />

      <!-- Clean 5 Data Points Required by PRD §13 & User Prompt (NO NIP, NO DETAILS, NO PDF DOWNLOAD) -->
      <g transform="translate(0, 140)">
        <!-- Field 1: Nama Peserta -->
        <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">1. NAMA PESERTA LULUSAN:</text>
        <text x="20" y="52" fill="#ffffff" font-size="18" font-weight="800">DIMAS WAHYU PRATAMA</text>

        <!-- Field 2: Lembaga Penerbit -->
        <g transform="translate(740, 0)">
          <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">2. LEMBAGA PENYELENGGARA PELATIHAN:</text>
          <text x="20" y="52" fill="#38bdf8" font-size="17" font-weight="700">Balai Diklat Air Minum Nusantara (NUS)</text>
        </g>

        <!-- Field 3: Jalur Pelatihan -->
        <g transform="translate(0, 95)">
          <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">3. JALUR PEMBELAJARAN &amp; SPESIALISASI:</text>
          <text x="20" y="52" fill="#ffffff" font-size="17" font-weight="700">Operator Air Minum Terpadu (IPA &amp; Distribusi)</text>
        </g>

        <!-- Field 4: Tanggal Kelulusan -->
        <g transform="translate(740, 95)">
          <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">4. TANGGAL KELULUSAN RESMI:</text>
          <text x="20" y="52" fill="#ffffff" font-size="17" font-weight="700">28 Oktober 2026</text>
        </g>

        <!-- Field 5: Predikat Kelulusan PRD §13 -->
        <g transform="translate(0, 190)">
          <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">5. PREDIKAT KELULUSAN (PRD §13):</text>
          <text x="20" y="52" fill="#f59e0b" font-size="18" font-weight="800">Lulus dengan Baik</text>
        </g>

        <!-- Field 6: Legalitas Keabsahan -->
        <g transform="translate(740, 190)">
          <rect width="700" height="75" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="26" fill="#94a3b8" font-size="11" font-weight="700">6. STATUS KEABSAHAN &amp; INTEGRITAS:</text>
          <text x="20" y="52" fill="#34d399" font-size="17" font-weight="700">Terdaftar Aktif · Bebas Pencabutan</text>
        </g>
      </g>
    </g>
  </g>

  <!-- UN-COVERED MANDATORY DISCLAIMER FOOTER (PRD §13 & User Instruction: Catatan kaki tidak boleh tertutup) -->
  <g transform="translate(32, 870)">
    <rect width="1536" height="85" rx="10" fill="#090d16" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 20)">
      <text x="0" y="18" fill="#f8fafc" font-size="12" font-weight="700">PEMBERITAHUAN HUKUM RESMI (PRD SIMSCADA-AIR v1.0 §13):</text>
      <text x="0" y="38" fill="#cbd5e1" font-size="12.5" font-weight="600">"Piagam ini menyatakan penyelesaian pelatihan berbasis simulator dan bukan sertifikat kompetensi resmi."</text>
      <text x="0" y="54" fill="#94a3b8" font-size="11">Sertifikasi profesi resmi operator air minum tetap diselenggarakan oleh Lembaga Sertifikasi Profesi (LSP) berlisensi BNSP.</text>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L16: VERIFIKASI PIAGAM PUBLIK (SimSCADA-Air v1.0)")

print("Generating L10, L11, L12, L13, L14, L15, L16...")
with open(os.path.join(OUTPUT_DIR, "mockup_l10_manage_scenarios.svg"), "w") as f:
    f.write(generate_l10())
with open(os.path.join(OUTPUT_DIR, "mockup_l11_session_replay.svg"), "w") as f:
    f.write(generate_l11())
with open(os.path.join(OUTPUT_DIR, "mockup_l12_manage_users.svg"), "w") as f:
    f.write(generate_l12())
with open(os.path.join(OUTPUT_DIR, "mockup_l13_tenant_settings.svg"), "w") as f:
    f.write(generate_l13())
with open(os.path.join(OUTPUT_DIR, "mockup_l14_tenant_evaluation.svg"), "w") as f:
    f.write(generate_l14())
with open(os.path.join(OUTPUT_DIR, "mockup_l15_superadmin.svg"), "w") as f:
    f.write(generate_l15())
with open(os.path.join(OUTPUT_DIR, "mockup_l16_public_verification.svg"), "w") as f:
    f.write(generate_l16())
print("Batch 5 (L10 to L16) generated successfully.")

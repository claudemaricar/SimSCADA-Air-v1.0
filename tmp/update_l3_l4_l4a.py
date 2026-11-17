#!/usr/bin/env python3
import os, sys, re
import xml.etree.ElementTree as ET

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)

def sanitize_xml(svg_str):
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)

sys.path.append("tmp")
import gen_l3_l4_l4a

def generate_l3():
    return gen_l3_l4_l4a.generate_l3()

def generate_l4():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Modul Materi &amp; Kuis Pra-Misi", "Misi IPA-06: Gangguan Lonjakan Kekeruhan Air Baku (Tingkat 3 · Sulit · 2,0x XP) · PRD §7", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: SOP Study Material & Action Procedures (Width: 880) -->
  <g transform="translate(32, 190)">
    <rect width="880" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 28)">
      <text x="0" y="20" fill="#ffffff" font-size="18" font-weight="700">Materi Teori &amp; SOP: Penanganan Lonjakan Kekeruhan Air Baku</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Standar Pengolahan Fisik-Kimia Air Minum (Permenkes No. 2/2023 &amp; SNI 6774:2008)</text>

      <line x1="0" y1="58" x2="816" y2="58" stroke="#334155" stroke-width="1" />

      <!-- Mission Summary Box -->
      <g transform="translate(0, 72)">
        <rect width="816" height="88" rx="10" fill="#0c4a6e" opacity="0.3" stroke="#0284c7" stroke-width="1.5" />
        <g transform="translate(20, 18)">
          <text x="0" y="16" fill="#7dd3fc" font-size="12" font-weight="700">RINGKASAN SKENARIO MISI IPA-06 (PRD §7):</text>
          <text x="0" y="38" fill="#ffffff" font-size="12">Kekeruhan air baku sungai melonjak drastis dari <tspan font-weight="700" fill="#f59e0b">20 NTU menjadi 185 NTU</tspan> akibat hujan deras di hulu.</text>
          <text x="0" y="56" fill="#ffffff" font-size="12">Tugas Anda: Akui alarm, sesuaikan dosis koagulan PAC dan penyesuai pH kapur, jaga kekeruhan air olahan &lt;3 NTU.</text>
        </g>
      </g>

      <!-- Interactive 3 Key Operating Limits Cards (FIXED: Wrap each in <g transform="translate(...)">) -->
      <g transform="translate(0, 175)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">POIN SOP &amp; AMBANG BATAS OPERASIONAL KRITIS (PERMENKES NO. 2/2023):</text>
        
        <g transform="translate(0, 28)">
          <!-- Card 1: Batas Kekeruhan Air Olahan -->
          <g transform="translate(0, 0)">
            <rect width="260" height="74" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Batas Kekeruhan Air Olahan</text>
            <text x="14" y="48" fill="#38bdf8" font-size="18" font-weight="700">&lt; 3,0 NTU</text>
            <text x="14" y="64" fill="#ef4444" font-size="9.5">≥3 NTU: Alarm Kritis Tinggi</text>
          </g>

          <!-- Card 2: Rentang Aman pH Koagulasi -->
          <g transform="translate(276, 0)">
            <rect width="260" height="74" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Rentang Aman pH Koagulasi</text>
            <text x="14" y="48" fill="#10b981" font-size="18" font-weight="700">6,5 – 8,5</text>
            <text x="14" y="64" fill="#94a3b8" font-size="9.5">Koreksi dengan penyesuai pH</text>
          </g>

          <!-- Card 3: Target Waktu Skenario IPA-06 PRD §8 -->
          <g transform="translate(552, 0)">
            <rect width="264" height="74" rx="8" fill="#0f172a" stroke="#1e293b" />
            <text x="14" y="24" fill="#94a3b8" font-size="11">Target Waktu Skenario IPA-06</text>
            <text x="14" y="48" fill="#f59e0b" font-size="18" font-weight="700">60 Detik</text>
            <text x="14" y="64" fill="#34d399" font-size="9.5">Respons &lt;30s: Lencana Respons Kilat</text>
          </g>
        </g>

        <!-- Step-by-Step SOP -->
        <g transform="translate(0, 120)">
          <rect width="816" height="290" rx="10" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="700">LANGKAH STANDAR OPERASIONAL PROSEDUR (SOP PENANGANAN LONJAKAN KEKERUHAN):</text>
          
          <text x="20" y="60" fill="#cbd5e1" font-size="12">1. <tspan font-weight="700" fill="#ffffff">Akui Alarm (ACK):</tspan> Segera tekan tombol Akui begitu alarm "Kekeruhan Air Baku Tinggi" muncul di HMI.</text>
          <text x="20" y="85" fill="#cbd5e1" font-size="12">2. <tspan font-weight="700" fill="#ffffff">Buka Panel Koagulasi:</tspan> Klik titik kontrol Flash Mixer Koagulasi di diagram mimic HMI.</text>
          <text x="20" y="110" fill="#cbd5e1" font-size="12">3. <tspan font-weight="700" fill="#ffffff">Naikkan Dosis Koagulan:</tspan> Sesuaikan setpoint dosis PAC dari 20 mg/L ke 48 mg/L sesuai kurva jar-test.</text>
          <text x="20" y="135" fill="#cbd5e1" font-size="12">4. <tspan font-weight="700" fill="#ffffff">Koreksi pH Air:</tspan> Pastikan dosis penyesuai pH aktif agar pH bertahan stabil di angka 7,20.</text>
          <text x="20" y="160" fill="#cbd5e1" font-size="12">5. <tspan font-weight="700" fill="#ffffff">Turunkan Debit Intake (Opsional):</tspan> Jika flok lambat mengendap, kurangi debit dari 100 L/s ke 75 L/s.</text>
          <text x="20" y="185" fill="#cbd5e1" font-size="12">6. <tspan font-weight="700" fill="#ffffff">Pantau Bak Sedimentasi &amp; Filtrasi:</tspan> Awasi kekeruhan keluar sedimentasi dan kenaikan headloss filter.</text>
          <text x="20" y="210" fill="#cbd5e1" font-size="12">7. <tspan font-weight="700" fill="#ffffff">Verifikasi Pemulihan:</tspan> Alarm akan auto-clear saat kekeruhan air olahan &lt;2,7 NTU stabil 10 detik.</text>

          <rect x="20" y="235" width="776" height="40" rx="6" fill="#1e293b" />
          <text x="36" y="259" fill="#f59e0b" font-size="11.5" font-weight="600">⚠️ Catatan: Membuka narasi titik kontrol ("i") kapan saja TIDAK mengurangi skor (PRD §9).</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Right Column: Pre-Mission 5-Question Quiz PRD §7 (Width: 640) -->
  <g transform="translate(928, 190)">
    <rect width="640" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 28)">
      <text x="0" y="20" fill="#ffffff" font-size="18" font-weight="700">Kuis Pra-Misi (5 Soal Kunci)</text>
      <text x="0" y="40" fill="#94a3b8" font-size="12">Syarat Gerbang: Nilai Kuis ≥ 60 membuka Simulator · Nilai kuis memberi bonus XP</text>

      <line x1="0" y1="58" x2="584" y2="58" stroke="#334155" stroke-width="1" />

      <!-- Quiz Status Box -->
      <g transform="translate(0, 72)">
        <rect width="584" height="60" rx="8" fill="#064e3b" opacity="0.6" stroke="#059669" stroke-width="1.5" />
        <text x="18" y="26" fill="#a7f3d0" font-size="12" font-weight="700">STATUS KUIS: LULUS GERBANG (NILAI: 80 / 100)</text>
        <text x="18" y="46" fill="#ffffff" font-size="11.5">✓ 4 dari 5 Soal Benar · +80 XP telah ditambahkan ke profil Anda.</text>
        <text x="560" y="38" fill="#34d399" font-size="20" text-anchor="end">✓</text>
      </g>

      <!-- Question 1 (Sample) -->
      <g transform="translate(0, 150)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">SOAL 1 DARI 5 · BATAS MUTU KEKERUHAN</text>
        <text x="0" y="36" fill="#e2e8f0" font-size="12.5" font-weight="600">Berapa batas maksimal kekeruhan air olahan menurut Permenkes 2/2023?</text>
        
        <rect x="0" y="48" width="584" height="32" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="16" y="69" fill="#94a3b8" font-size="11">A. 5,0 NTU</text>

        <rect x="0" y="86" width="584" height="32" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1.5" />
        <text x="16" y="107" fill="#34d399" font-size="11" font-weight="700">B. 3,0 NTU (Jawaban Benar Anda ✓)</text>

        <rect x="0" y="124" width="584" height="32" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="16" y="145" fill="#94a3b8" font-size="11">C. 1,0 NTU</text>
      </g>

      <!-- Question 2 (Sample) -->
      <g transform="translate(0, 325)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">SOAL 2 DARI 5 · PENANGANAN ALARM ABNORMAL</text>
        <text x="0" y="36" fill="#e2e8f0" font-size="12.5" font-weight="600">Apa yang terjadi jika tombol "Clear Alarm" ditekan saat kekeruhan masih 3,5 NTU?</text>
        
        <rect x="0" y="48" width="584" height="32" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1.5" />
        <text x="16" y="69" fill="#34d399" font-size="11" font-weight="700">A. Ditolak: "Penyebab belum ditangani" &amp; catat penalti (Jawaban Benar ✓)</text>

        <rect x="0" y="86" width="584" height="32" rx="6" fill="#1e293b" stroke="#334155" />
        <text x="16" y="107" fill="#94a3b8" font-size="11">B. Alarm langsung hilang seketika</text>
      </g>

      <!-- Launch Simulator Action Button -->
      <g transform="translate(0, 560)">
        <rect width="584" height="54" rx="10" fill="url(#primaryGrad)" />
        <text x="292" y="34" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle" letter-spacing="0.5">MULAI SIMULATOR SCADA (IPA-06) →</text>
        
        <text x="292" y="80" fill="#94a3b8" font-size="11" text-anchor="middle">Gerbang kuis telah terpenuhi. Sesi simulator akan dibuka dengan timer 10 menit.</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L4: MODUL MATERI &amp; KUIS PRA-MISI (SimSCADA-Air v1.0)")

def generate_l4a():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Ahli · Angkatan 1", name="Andi Kurniawan", initials="AK")
    title = page_title_block("Pre-Test &amp; Post-Test Evaluasi Kompetensi", "Pengukuran Indikator Keberhasilan Metrik T1: Kenaikan Kompetensi ≥ 25% (PRD §3 &amp; §11)", 120)

    content = f"""{hdr}
{title}

  <!-- Metric T1 Formula Banner PRD §3 -->
  <g transform="translate(32, 195)">
    <rect width="1536" height="70" rx="10" fill="#1e1b4b" stroke="#4338ca" stroke-width="1.5" />
    <text x="24" y="28" fill="#c7d2fe" font-size="13" font-weight="700">METRIK KEBERHASILAN T1 (PRD §3): FORMULA KENAIKAN KOMPETENSI PELATIHAN</text>
    <text x="24" y="50" fill="#ffffff" font-size="13" font-weight="600">Peningkatan Nilai (%) = ((Skor Post-Test − Skor Pre-Test) ÷ Skor Pre-Test) × 100% · <tspan fill="#34d399">Target PRD: Kenaikan ≥ 25%</tspan></text>
    <rect x="1350" y="16" width="160" height="38" rx="8" fill="#059669" />
    <text x="1430" y="40" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">TARGET T1: ≥ 25%</text>
  </g>

  <!-- Left Card: Pre-Test Diagnostic Baseline (Dimas Wahyu Pratama / Baseline) -->
  <g transform="translate(32, 285)">
    <rect width="460" height="660" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(24, 24)">
      <rect width="120" height="24" rx="6" fill="#f59e0b" opacity="0.2" stroke="#f59e0b" />
      <text x="60" y="16" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">TAHAP AWAL</text>
      
      <text x="0" y="55" fill="#ffffff" font-size="17" font-weight="700">Pre-Test Diagnostik Awal</text>
      <text x="0" y="74" fill="#94a3b8" font-size="11.5">Peserta: Dimas Wahyu Pratama (peserta.ipa)</text>

      <line x1="0" y1="90" x2="412" y2="90" stroke="#334155" stroke-width="1" />

      <!-- Score Box -->
      <g transform="translate(0, 105)">
        <rect width="412" height="90" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="20" y="32" fill="#94a3b8" font-size="12">Skor Baseline Kompetensi Awal:</text>
        <text x="20" y="68" fill="#f59e0b" font-size="34" font-weight="800">56 <tspan font-size="16" fill="#94a3b8">/ 100</tspan></text>
        <text x="390" y="60" fill="#64748b" font-size="12" text-anchor="end">28 Okt 2026</text>
      </g>

      <!-- Competency Breakdown -->
      <g transform="translate(0, 215)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">PETA CAPAIAN KOMPETENSI AWAL:</text>
        
        <text x="0" y="44" fill="#cbd5e1" font-size="11.5">1. Operasi Normal IPA: 65%</text>
        <rect x="0" y="52" width="412" height="8" rx="4" fill="#0f172a" />
        <rect x="0" y="52" width="268" height="8" rx="4" fill="#0284c7" />

        <text x="0" y="80" fill="#cbd5e1" font-size="11.5">2. Mutu Air (Kekeruhan &amp; Klor): 50%</text>
        <rect x="0" y="88" width="412" height="8" rx="4" fill="#0f172a" />
        <rect x="0" y="88" width="206" height="8" rx="4" fill="#f59e0b" />

        <text x="0" y="116" fill="#cbd5e1" font-size="11.5">3. Tanggap Darurat &amp; Alarm: 40% (Rendah)</text>
        <rect x="0" y="124" width="412" height="8" rx="4" fill="#0f172a" />
        <rect x="0" y="124" width="165" height="8" rx="4" fill="#ef4444" />

        <text x="0" y="152" fill="#cbd5e1" font-size="11.5">4. Hidrolika Distribusi: 60%</text>
        <rect x="0" y="160" width="412" height="8" rx="4" fill="#0f172a" />
        <rect x="0" y="160" width="247" height="8" rx="4" fill="#0284c7" />
      </g>

      <!-- Summary Note -->
      <g transform="translate(0, 420)">
        <rect width="412" height="180" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="24" fill="#38bdf8" font-size="11" font-weight="700">CATATAN EVALUASI AWAL SISTEM:</text>
        <text x="16" y="46" fill="#94a3b8" font-size="11">Peserta memahami dasar pengolahan fisik namun</text>
        <text x="16" y="66" fill="#94a3b8" font-size="11">belum memiliki ketangkasan dalam mengenali kode</text>
        <text x="16" y="86" fill="#94a3b8" font-size="11">alarm ISA-18.2 dan penanganan pompa trip beruntun.</text>
        <text x="16" y="106" fill="#94a3b8" font-size="11">Direkomendasikan fokus pada modul gangguan L5.</text>
      </g>
    </g>
  </g>

  <!-- Middle: Interactive Test Workspace View (Width: 600) -->
  <g transform="translate(516, 285)">
    <rect width="600" height="660" rx="14" fill="url(#cardDark)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(28, 24)">
      <text x="0" y="18" fill="#ffffff" font-size="16" font-weight="700">Lembar Uji Kompetensi Teori &amp; Studi Kasus</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">20 Soal Pilihan Ganda Berbobot · Batas Waktu 30 Menit</text>

      <rect x="440" y="2" width="130" height="34" rx="6" fill="#0f172a" stroke="#0284c7" />
      <text x="505" y="24" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">⏱️ 18:42 Tersisa</text>

      <line x1="0" y1="52" x2="544" y2="52" stroke="#334155" stroke-width="1" />

      <!-- Sample Question -->
      <g transform="translate(0, 68)">
        <text x="0" y="16" fill="#38bdf8" font-size="12" font-weight="700">SOAL NO. 14 DARI 20 · STUDI KASUS PROSES IPA</text>
        <text x="0" y="38" fill="#f8fafc" font-size="13" font-weight="600">Jika kekeruhan air baku naik dari 20 NTU menjadi 180 NTU dalam waktu</text>
        <text x="0" y="58" fill="#f8fafc" font-size="13" font-weight="600">10 menit, tindakan awal manakah yang paling tepat sesuai SOP?</text>

        <!-- Options -->
        <rect x="0" y="78" width="544" height="42" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="16" y="104" fill="#cbd5e1" font-size="12">A. Segera menguras bak sedimentasi dengan blowdown penuh</text>

        <rect x="0" y="130" width="544" height="42" rx="8" fill="#064e3b" stroke="#059669" stroke-width="1.5" />
        <text x="16" y="156" fill="#a7f3d0" font-size="12" font-weight="700">B. Akui alarm, naikkan dosis koagulan &amp; koreksi pH, turunkan debit intake (Pilihan Anda)</text>

        <rect x="0" y="182" width="544" height="42" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="16" y="208" fill="#cbd5e1" font-size="12">C. Menutup valve masuk filter dan mematikan seluruh pompa</text>

        <rect x="0" y="234" width="544" height="42" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="16" y="260" fill="#cbd5e1" font-size="12">D. Menunggu air baku jernih kembali secara alami</text>
      </g>

      <!-- Navigator -->
      <g transform="translate(0, 360)">
        <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="600">NAVIGATOR 20 NOMOR SOAL:</text>
        <g transform="translate(0, 26)">
          <rect width="48" height="32" rx="4" fill="#059669" /><text x="24" y="21" fill="#fff" font-size="11" text-anchor="middle">1</text>
          <rect x="54" width="48" height="32" rx="4" fill="#059669" /><text x="78" y="21" fill="#fff" font-size="11" text-anchor="middle">2</text>
          <rect x="108" width="48" height="32" rx="4" fill="#059669" /><text x="132" y="21" fill="#fff" font-size="11" text-anchor="middle">3</text>
          <rect x="162" width="48" height="32" rx="4" fill="#059669" /><text x="186" y="21" fill="#fff" font-size="11" text-anchor="middle">4</text>
          <rect x="216" width="48" height="32" rx="4" fill="#059669" /><text x="240" y="21" fill="#fff" font-size="11" text-anchor="middle">5</text>
          <rect x="270" width="48" height="32" rx="4" fill="#059669" /><text x="294" y="21" fill="#fff" font-size="11" text-anchor="middle">6</text>
          <rect x="324" width="48" height="32" rx="4" fill="#059669" /><text x="348" y="21" fill="#fff" font-size="11" text-anchor="middle">7</text>
          <rect x="378" width="48" height="32" rx="4" fill="#059669" /><text x="402" y="21" fill="#fff" font-size="11" text-anchor="middle">8</text>
          <rect x="432" width="48" height="32" rx="4" fill="#059669" /><text x="456" y="21" fill="#fff" font-size="11" text-anchor="middle">9</text>
          <rect x="486" width="48" height="32" rx="4" fill="#059669" /><text x="510" y="21" fill="#fff" font-size="11" text-anchor="middle">10</text>
        </g>
        <g transform="translate(0, 66)">
          <rect width="48" height="32" rx="4" fill="#059669" /><text x="24" y="21" fill="#fff" font-size="11" text-anchor="middle">11</text>
          <rect x="54" width="48" height="32" rx="4" fill="#059669" /><text x="78" y="21" fill="#fff" font-size="11" text-anchor="middle">12</text>
          <rect x="108" width="48" height="32" rx="4" fill="#059669" /><text x="132" y="21" fill="#fff" font-size="11" text-anchor="middle">13</text>
          <rect x="162" width="48" height="32" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" /><text x="186" y="21" fill="#fff" font-size="11" text-anchor="middle">14</text>
          <rect x="216" width="48" height="32" rx="4" fill="#1e293b" /><text x="240" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">15</text>
          <rect x="270" width="48" height="32" rx="4" fill="#1e293b" /><text x="294" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">16</text>
          <rect x="324" width="48" height="32" rx="4" fill="#1e293b" /><text x="348" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">17</text>
          <rect x="378" width="48" height="32" rx="4" fill="#1e293b" /><text x="402" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">18</text>
          <rect x="432" width="48" height="32" rx="4" fill="#1e293b" /><text x="456" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">19</text>
          <rect x="486" width="48" height="32" rx="4" fill="#1e293b" /><text x="510" y="21" fill="#94a3b8" font-size="11" text-anchor="middle">20</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Right Card: Post-Test Final Outcome (Andi Kurniawan - peserta.lulus) -->
  <g transform="translate(1140, 285)">
    <rect width="428" height="660" rx="14" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
    
    <g transform="translate(24, 24)">
      <rect width="130" height="24" rx="6" fill="#059669" />
      <text x="65" y="16" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">PASCA PELATIHAN</text>
      
      <text x="0" y="55" fill="#ffffff" font-size="17" font-weight="700">Post-Test Kelulusan Jalur</text>
      <text x="0" y="74" fill="#34d399" font-size="11.5">Peserta: Andi Kurniawan (peserta.lulus)</text>

      <line x1="0" y1="90" x2="380" y2="90" stroke="#334155" stroke-width="1" />

      <!-- Post-Test Score Box (Andi Kurniawan: Skor 88) -->
      <g transform="translate(0, 105)">
        <rect width="380" height="90" rx="10" fill="#064e3b" opacity="0.4" stroke="#059669" stroke-width="1.5" />
        <text x="20" y="32" fill="#a7f3d0" font-size="12">Capaian Post-Test Akhir:</text>
        <text x="20" y="68" fill="#34d399" font-size="34" font-weight="800">88 <tspan font-size="16" fill="#a7f3d0">/ 100</tspan></text>
        <text x="360" y="60" fill="#a7f3d0" font-size="12" text-anchor="end">Status: Lulus (≥70)</text>
      </g>

      <!-- Metrik T1 Calculation Box for Andi Kurniawan (54 -> 88 = +63.0% > 25%) -->
      <g transform="translate(0, 215)">
        <rect width="380" height="150" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5" />
        <text x="16" y="24" fill="#c7d2fe" font-size="12" font-weight="700">HASIL METRIK T1 KENAIKAN KOMPETENSI:</text>
        
        <text x="16" y="52" fill="#ffffff" font-size="13">Pre-Test: <tspan font-weight="700" fill="#f59e0b">54</tspan> ➔ Post-Test: <tspan font-weight="700" fill="#34d399">88</tspan></text>
        <text x="16" y="76" fill="#ffffff" font-size="13">Kenaikan: <tspan font-weight="700" fill="#38bdf8">+34 Poin (+63,0%)</tspan></text>

        <rect x="16" y="94" width="348" height="38" rx="6" fill="#059669" />
        <text x="190" y="118" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓ MELEBIHI TARGET PRD T1 (+63% &gt; 25%)</text>
      </g>

      <!-- Piagam Issuance Check -->
      <g transform="translate(0, 390)">
        <rect width="380" height="210" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="26" fill="#f8fafc" font-size="12" font-weight="700">STATUS VERIFIKASI SYARAT PIAGAM:</text>
        
        <text x="16" y="56" fill="#34d399" font-size="11.5">✓ 17 Misi Jalur Terpadu: Selesai</text>
        <text x="16" y="80" fill="#34d399" font-size="11.5">✓ Misi Kelulusan TRP-02: Lulus (Skor 94 ≥ 80)</text>
        <text x="16" y="104" fill="#34d399" font-size="11.5">✓ Post-Test Akhir: 88 / 100 (Lulus ≥ 70)</text>
        <text x="16" y="128" fill="#34d399" font-size="11.5">✓ Piagam SSA/NUS/2026/0001: TERBIT (Operator Ahli)</text>

        <rect x="16" y="150" width="348" height="42" rx="8" fill="#0284c7" />
        <text x="190" y="176" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">LIHAT PIAGAM RESMI SAYA (L8) →</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L4a: PRE-TEST &amp; POST-TEST EVALUASI KOMPETENSI (SimSCADA-Air v1.0)")

print("Generating L3, L4, L4a...")
l3_svg = sanitize_xml(generate_l3())
l4_svg = sanitize_xml(generate_l4())
l4a_svg = sanitize_xml(generate_l4a())

with open(os.path.join(PUBLIC_DIR, "mockup_l3_track_select.svg"), "w", encoding="utf-8") as f:
    f.write(l3_svg)
with open(os.path.join(PUBLIC_DIR, "mockup_l4_module_quiz.svg"), "w", encoding="utf-8") as f:
    f.write(l4_svg)
with open(os.path.join(PUBLIC_DIR, "mockup_l4a_pre_post_test.svg"), "w", encoding="utf-8") as f:
    f.write(l4a_svg)

ET.parse(os.path.join(PUBLIC_DIR, "mockup_l3_track_select.svg"))
ET.parse(os.path.join(PUBLIC_DIR, "mockup_l4_module_quiz.svg"))
ET.parse(os.path.join(PUBLIC_DIR, "mockup_l4a_pre_post_test.svg"))
print("L3, L4, L4a successfully generated and validated in public/!")

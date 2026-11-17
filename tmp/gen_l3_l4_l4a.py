#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 2: L3, L4, L4a
"""
import os
import sys

OUTPUT_DIR = "public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

def generate_l3():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Pemilihan Jalur Pembelajaran Operator", "Pilih salah satu spesialisasi kompetensi air minum · 1 Jalur Aktif per Peserta (PRD §7)", 120)

    content = f"""{hdr}
{title}

  <!-- Notice Banner PRD §7 -->
  <g transform="translate(32, 195)">
    <rect width="1536" height="54" rx="8" fill="#0c4a6e" opacity="0.4" stroke="#0284c7" stroke-width="1.5" />
    <text x="24" y="24" fill="#38bdf8" font-size="13" font-weight="700">ℹ️ ATURAN JALUR BELAJAR (PRD SIMSCADA-AIR v1.0 §7):</text>
    <text x="24" y="42" fill="#e2e8f0" font-size="12">Satu jalur aktif per peserta. Tidak ada prasyarat untuk memilih Terpadu. Misi IPA atau Distribusi yang telah lulus dihitung otomatis bila pindah ke Terpadu. Jalur di luar paket lisensi tidak ditampilkan.</text>
  </g>

  <!-- 3 Track Cards Container (Widths: 485 each, spacing: 38) -->
  <g transform="translate(32, 275)">
    
    <!-- CARD 1: OPERATOR IPA (9 MISI) -->
    <g transform="translate(0, 0)" filter="url(#dropShadow)">
      <rect width="485" height="660" rx="16" fill="url(#cardGrad)" stroke="#0284c7" stroke-width="2.5" />
      
      <!-- Active Badge -->
      <rect x="345" y="20" width="120" height="26" rx="13" fill="#0284c7" />
      <text x="405" y="37" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">JALUR AKTIF ANDA</text>

      <g transform="translate(28, 28)">
        <!-- Icon -->
        <rect width="48" height="48" rx="12" fill="#0369a1" />
        <text x="24" y="32" fill="#ffffff" font-size="22" text-anchor="middle">💧</text>

        <text x="64" y="24" fill="#ffffff" font-size="18" font-weight="700">Operator IPA</text>
        <text x="64" y="42" fill="#38bdf8" font-size="12" font-weight="600">Instalasi Pengolahan Air · 9 Misi</text>

        <line x1="0" y1="65" x2="429" y2="65" stroke="#334155" stroke-width="1" />

        <text x="0" y="90" fill="#cbd5e1" font-size="12.5" line-height="1.5">Fokus pelatihan pengolahan air minum dari air baku</text>
        <text x="0" y="108" fill="#cbd5e1" font-size="12.5">hingga air olahan siap minum sesuai Permenkes 2/2023.</text>

        <!-- Mission Highlights -->
        <g transform="translate(0, 130)">
          <rect width="429" height="280" rx="10" fill="#0f172a" stroke="#1e293b" />
          <text x="16" y="26" fill="#94a3b8" font-size="11" font-weight="700">KATALOG 9 MISI BERJENJANG (IPA-01 s/d IPA-09):</text>
          
          <text x="16" y="52" fill="#34d399" font-size="11.5">✓ T1 Mudah: IPA-01 Kenali Ruang Kendali</text>
          <text x="16" y="74" fill="#34d399" font-size="11.5">✓ T2 Sedang: IPA-02 Menyalakan Intake</text>
          <text x="16" y="96" fill="#34d399" font-size="11.5">✓ T2 Sedang: IPA-03 Dosis Koagulan Normal</text>
          <text x="16" y="118" fill="#34d399" font-size="11.5">✓ T2 Sedang: IPA-04 Jaga Filter &amp; Backwash</text>
          <text x="16" y="140" fill="#34d399" font-size="11.5">✓ T2 Sedang: IPA-05 Klorinasi Tepat</text>
          <text x="16" y="162" fill="#38bdf8" font-size="11.5" font-weight="700">✓ T3 Sulit: IPA-06 Lonjakan Kekeruhan (Sesi Contoh)</text>
          <text x="16" y="184" fill="#34d399" font-size="11.5">✓ T3 Sulit: IPA-07 Gangguan Pompa Trip</text>
          <text x="16" y="206" fill="#f59e0b" font-size="11.5" font-weight="600">⏳ T3 Sulit: IPA-08 Dosis Klor Tidak Sesuai</text>
          <text x="16" y="228" fill="#818cf8" font-size="11.5" font-weight="600">🔒 T5 Ujian: IPA-09 Misi Kelulusan IPA (KKM ≥80)</text>

          <rect x="16" y="245" width="397" height="24" rx="4" fill="#1e293b" />
          <text x="214" y="261" fill="#94a3b8" font-size="10.5" text-anchor="middle">Progres Anda: 7 dari 9 Misi Selesai (14 Bintang)</text>
        </g>

        <!-- Target Level & Piagam -->
        <g transform="translate(0, 430)">
          <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="600">CAPAIAN AKHIR JALUR:</text>
          <text x="0" y="34" fill="#e2e8f0" font-size="12">Level Operator Madya · Piagam "Operator IPA"</text>
          
          <rect x="0" y="50" width="429" height="44" rx="8" fill="#0284c7" />
          <text x="214" y="77" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">LANJUTKAN BELAJAR IPA-08 →</text>
        </g>
      </g>
    </g>

    <!-- CARD 2: OPERATOR DISTRIBUSI (7 MISI) -->
    <g transform="translate(525, 0)" filter="url(#dropShadow)">
      <rect width="485" height="660" rx="16" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      
      <g transform="translate(28, 28)">
        <!-- Icon -->
        <rect width="48" height="48" rx="12" fill="#0d9488" />
        <text x="24" y="32" fill="#ffffff" font-size="22" text-anchor="middle">🚰</text>

        <text x="64" y="24" fill="#ffffff" font-size="18" font-weight="700">Operator Distribusi</text>
        <text x="64" y="42" fill="#2dd4bf" font-size="12" font-weight="600">Jaringan Perpipaan &amp; Pompa · 7 Misi</text>

        <line x1="0" y1="65" x2="429" y2="65" stroke="#334155" stroke-width="1" />

        <text x="0" y="90" fill="#cbd5e1" font-size="12.5">Fokus pelatihan hidrolika perpipaan, manajemen tekanan</text>
        <text x="0" y="108" fill="#cbd5e1" font-size="12.5">zona, kebocoran pipa, reservoir, dan sisa klor ujung jaringan.</text>

        <!-- Mission Highlights -->
        <g transform="translate(0, 130)">
          <rect width="429" height="280" rx="10" fill="#0f172a" stroke="#1e293b" />
          <text x="16" y="26" fill="#94a3b8" font-size="11" font-weight="700">KATALOG 7 MISI BERJENJANG (DST-01 s/d DST-07):</text>
          
          <text x="16" y="52" fill="#e2e8f0" font-size="11.5">• T1 Mudah: DST-01 Kenali Jaringan Distribusi</text>
          <text x="16" y="74" fill="#e2e8f0" font-size="11.5">• T2 Mudah: DST-02 Pompa Distribusi &amp; Reservoir</text>
          <text x="16" y="96" fill="#e2e8f0" font-size="11.5">• T2 Sedang: DST-03 Atur Tekanan Jam Puncak</text>
          <text x="16" y="118" fill="#e2e8f0" font-size="11.5">• T2 Sedang: DST-04 Sisa Klor di Ujung Jaringan</text>
          <text x="16" y="140" fill="#f59e0b" font-size="11.5">• T3 Sulit: DST-05 Gangguan: Kebocoran Pipa</text>
          <text x="16" y="162" fill="#f59e0b" font-size="11.5">• T3 Sulit: DST-06 Gangguan: Tekanan Jaringan Drop</text>
          <text x="16" y="184" fill="#818cf8" font-size="11.5">• T5 Ujian: DST-07 Misi Kelulusan Distribusi (≥80)</text>

          <rect x="16" y="245" width="397" height="24" rx="4" fill="#1e293b" />
          <text x="214" y="261" fill="#64748b" font-size="10.5" text-anchor="middle">Jalur Belum Dipilih · Siap Dimulai Kapan Saja</text>
        </g>

        <!-- Target Level & Piagam -->
        <g transform="translate(0, 430)">
          <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="600">CAPAIAN AKHIR JALUR:</text>
          <text x="0" y="34" fill="#e2e8f0" font-size="12">Level Operator Madya · Piagam "Operator Distribusi"</text>
          
          <rect x="0" y="50" width="429" height="44" rx="8" fill="#1e293b" stroke="#0d9488" stroke-width="1.5" />
          <text x="214" y="77" fill="#2dd4bf" font-size="13" font-weight="700" text-anchor="middle">PILIH JALUR INI</text>
        </g>
      </g>
    </g>

    <!-- CARD 3: OPERATOR AIR MINUM TERPADU (17 MISI) -->
    <g transform="translate(1050, 0)" filter="url(#dropShadow)">
      <rect width="485" height="660" rx="16" fill="url(#cardGrad)" stroke="#4338ca" stroke-width="2" />
      
      <!-- Recommended Badge -->
      <rect x="300" y="20" width="165" height="26" rx="13" fill="#4338ca" />
      <text x="382" y="37" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">KOMPETENSI LENGKAP</text>

      <g transform="translate(28, 28)">
        <!-- Icon -->
        <rect width="48" height="48" rx="12" fill="#312e81" />
        <text x="24" y="32" fill="#ffffff" font-size="22" text-anchor="middle">🌐</text>

        <text x="64" y="24" fill="#ffffff" font-size="18" font-weight="700">Air Minum Terpadu</text>
        <text x="64" y="42" fill="#818cf8" font-size="12" font-weight="600">Hulu ke Hilir (IPA + Distribusi) · 17 Misi</text>

        <line x1="0" y1="65" x2="429" y2="65" stroke="#334155" stroke-width="1" />

        <text x="0" y="90" fill="#cbd5e1" font-size="12.5">Satu-satunya jalur dengan tingkat Gangguan Berantai</text>
        <text x="0" y="108" fill="#cbd5e1" font-size="12.5">(TRP-01) dan Misi Kelulusan Terpadu Hulu-Hilir (TRP-02).</text>

        <!-- Mission Highlights -->
        <g transform="translate(0, 130)">
          <rect width="429" height="280" rx="10" fill="#0f172a" stroke="#1e293b" />
          <text x="16" y="26" fill="#c7d2fe" font-size="11" font-weight="700">17 MISI LENGKAP (TANPA PRASYARAT):</text>
          
          <text x="16" y="52" fill="#e2e8f0" font-size="11.5">• 8 Misi Pengolahan Air (IPA-01 s/d IPA-08)</text>
          <text x="16" y="74" fill="#e2e8f0" font-size="11.5">• 6 Misi Jaringan Distribusi (DST-01 s/d DST-06)</text>
          <text x="16" y="96" fill="#c084fc" font-size="11.5" font-weight="700">★ T4 Sangat Sulit: TRP-01 Hulu ke Hilir</text>
          <text x="16" y="118" fill="#c084fc" font-size="11.5">  (Kekeruhan drop IPA → reservoir turun → tekanan drop)</text>
          <text x="16" y="140" fill="#818cf8" font-size="11.5" font-weight="700">★ T5 Ujian: TRP-02 Misi Kelulusan Terpadu (≥80)</text>

          <rect x="16" y="180" width="397" height="88" rx="6" fill="#1e1b4b" stroke="#4338ca" />
          <text x="26" y="202" fill="#a5b4fc" font-size="11" font-weight="700">PENGAKUAN PROGRES OTOMATIS (PRD §7):</text>
          <text x="26" y="222" fill="#c7d2fe" font-size="10.5">Misi IPA-01 s/d 07 yang sudah Anda selesaikan akan</text>
          <text x="26" y="240" fill="#c7d2fe" font-size="10.5">langsung dihitung jika Anda beralih ke jalur Terpadu.</text>
        </g>

        <!-- Target Level & Piagam -->
        <g transform="translate(0, 430)">
          <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="600">CAPAIAN AKHIR JALUR:</text>
          <text x="0" y="34" fill="#e2e8f0" font-size="12">Level Tertinggi: Operator Ahli (3.500 XP) · Piagam Terpadu</text>
          
          <rect x="0" y="50" width="429" height="44" rx="8" fill="url(#primaryGrad)" />
          <text x="214" y="77" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">PINDAH KE JALUR TERPADU (17 MISI)</text>
        </g>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L3: PEMILIHAN JALUR PEMBELAJARAN (SimSCADA-Air v1.0)")

def generate_l4():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Modul Materi &amp; Kuis Pra-Misi", "Misi Contoh Konsisten: IPA-06 Gangguan Lonjakan Kekeruhan Air Baku (Tingkat 3 Sulit)", 120)

    content = f"""{hdr}
{title}

  <!-- Left Column: Module Theory & Senior Operator Briefing (Width: 880) -->
  <g transform="translate(32, 190)">
    <rect width="880" height="770" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(32, 28)">
      <!-- Mission Badge -->
      <rect width="130" height="26" rx="6" fill="#0284c7" />
      <text x="65" y="17" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">MISI: IPA-06</text>
      
      <rect x="140" width="130" height="26" rx="6" fill="#f59e0b" opacity="0.2" stroke="#f59e0b" />
      <text x="205" y="17" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">TINGKAT: 3 SULIT</text>

      <text x="0" y="60" fill="#ffffff" font-size="20" font-weight="700">Briefing Misi: Gangguan Lonjakan Kekeruhan Air Baku</text>
      <text x="0" y="80" fill="#38bdf8" font-size="12">Pengali XP: 2,0x · Waktu Target: 10 Menit · Standar Kualitas Permenkes No. 2/2023</text>

      <line x1="0" y1="98" x2="816" y2="98" stroke="#334155" stroke-width="1" />

      <!-- Story Briefing from Senior Operator Mentor PRD §9 & §10 -->
      <g transform="translate(0, 115)">
        <rect width="816" height="150" rx="10" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
        <circle cx="48" cy="48" r="28" fill="#0369a1" />
        <text x="48" y="55" fill="#ffffff" font-size="22" text-anchor="middle">👨‍🏫</text>
        
        <text x="92" y="32" fill="#38bdf8" font-size="13" font-weight="700">BRIEFING DARI TOKOH MENTOR: OPERATOR SENIOR (PAK SLAMET)</text>
        <text x="92" y="54" fill="#e2e8f0" font-size="12.5" font-weight="500">"Selamat pagi Dimas! Baru saja kami menerima peringatan dari pos pantau intake sungai:</text>
        <text x="92" y="74" fill="#e2e8f0" font-size="12.5" font-weight="500">hujan lebat di daerah tangkapan hulu membawa lumpur pekat. Kekeruhan air baku diprediksi melonjak</text>
        <text x="92" y="94" fill="#e2e8f0" font-size="12.5" font-weight="500">hingga &gt;180 NTU. Tugas Anda adalah mengendalikan pembubuhan koagulan &amp; flokulasi agar</text>
        <text x="92" y="114" fill="#e2e8f0" font-size="12.5" font-weight="500">kekeruhan air olahan tetap aman di bawah 3 NTU. Waspadai bahaya filter jenuh!"</text>
      </g>

      <!-- Key Learning Points PRD §9 & Permenkes No. 2/2023 -->
      <g transform="translate(0, 285)">
        <text x="0" y="16" fill="#f8fafc" font-size="14" font-weight="700">POIN SOP &amp; AMBANG BATAS OPERASIONAL KRITIS (PERMENKES NO. 2/2023):</text>
        
        <g transform="translate(0, 30)">
          <rect width="260" height="72" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Batas Kekeruhan Air Olahan</text>
          <text x="14" y="48" fill="#38bdf8" font-size="18" font-weight="700">&lt; 3,0 NTU</text>
          <text x="14" y="62" fill="#ef4444" font-size="9.5">≥3 NTU: Alarm Kritis Tinggi</text>

          <rect x="276" width="260" height="72" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Rentang Aman pH Koagulasi</text>
          <text x="14" y="48" fill="#10b981" font-size="18" font-weight="700">6,5 – 8,5</text>
          <text x="14" y="62" fill="#94a3b8" font-size="9.5">Koreksi dengan penyesuai pH</text>

          <rect x="552" width="264" height="72" rx="8" fill="#0f172a" stroke="#1e293b" />
          <text x="14" y="24" fill="#94a3b8" font-size="11">Target Waktu Tindakan Pertama</text>
          <text x="14" y="48" fill="#f59e0b" font-size="18" font-weight="700">&lt; 45 Detik</text>
          <text x="14" y="62" fill="#34d399" font-size="9.5">Penentu Komponen Respons (25%)</text>
        </g>

        <!-- Step-by-Step SOP -->
        <g transform="translate(0, 120)">
          <rect width="816" height="290" rx="10" fill="#0f172a" stroke="#1e293b" />
          <text x="20" y="28" fill="#38bdf8" font-size="12" font-weight="700">LANGKAH STANDAR OPERASIONAL PROSEDUR (SOP PENANGANAN LONJAKAN KEKERUHAN):</text>
          
          <text x="20" y="60" fill="#cbd5e1" font-size="12">1. <tspan font-weight="700" fill="#ffffff">Akui Alarm (ACK):</tspan> Segera tekan tombol Akui begitu alarm "Kekeruhan Air Baku Tinggi" muncul.</text>
          <text x="20" y="85" fill="#cbd5e1" font-size="12">2. <tspan font-weight="700" fill="#ffffff">Buka Panel Koagulasi:</tspan> Klik titik kontrol Flash Mixer Koagulasi di diagram HMI.</text>
          <text x="20" y="110" fill="#cbd5e1" font-size="12">3. <tspan font-weight="700" fill="#ffffff">Naikkan Dosis Koagulan:</tspan> Sesuaikan setpoint dosis PAC dari 20 mg/L ke 48 mg/L sesuai kurva jar-test.</text>
          <text x="20" y="135" fill="#cbd5e1" font-size="12">4. <tspan font-weight="700" fill="#ffffff">Koreksi pH Air:</tspan> Pastikan dosis penyesuai pH aktif agar pH bertahan di angka 7,20.</text>
          <text x="20" y="160" fill="#cbd5e1" font-size="12">5. <tspan font-weight="700" fill="#ffffff">Turunkan Debit Intake (Opsional):</tspan> Jika flok lambat mengendap, kurangi debit dari 100 L/s ke 75 L/s.</text>
          <text x="20" y="185" fill="#cbd5e1" font-size="12">6. <tspan font-weight="700" fill="#ffffff">Pantau Bak Sedimentasi &amp; Filtrasi:</tspan> Awasi kekeruhan keluar sedimentasi dan kenaikan headloss filter.</text>
          <text x="20" y="210" fill="#cbd5e1" font-size="12">7. <tspan font-weight="700" fill="#ffffff">Verifikasi Pemulihan:</tspan> Alarm akan clear otomatis saat kekeruhan air olahan &lt;2,7 NTU stabil 10 detik.</text>

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
    return svg_wrap(content, "MOCKUP L4: MODUL MATERI & KUIS PRA-MISI (SimSCADA-Air v1.0)")

def generate_l4a():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Pre-Test &amp; Post-Test Evaluasi Kompetensi", "Pengukuran Indikator Keberhasilan Metrik T1: Kenaikan Kompetensi ≥ 25% (PRD §3 & §11)", 120)

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

  <!-- Left Card: Pre-Test Diagnostic Baseline (Width: 460) -->
  <g transform="translate(32, 285)">
    <rect width="460" height="660" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    
    <g transform="translate(24, 24)">
      <rect width="120" height="24" rx="6" fill="#f59e0b" opacity="0.2" stroke="#f59e0b" />
      <text x="60" y="16" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">TAHAP AWAL</text>
      
      <text x="0" y="55" fill="#ffffff" font-size="17" font-weight="700">Pre-Test Diagnostik Awal</text>
      <text x="0" y="74" fill="#94a3b8" font-size="11.5">Dilaksanakan saat pertama kali mendaftar jalur</text>

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
      <!-- Test Header -->
      <text x="0" y="18" fill="#ffffff" font-size="16" font-weight="700">Lembar Uji Kompetensi Teori &amp; Studi Kasus</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">20 Soal Pilihan Ganda Berbobot · Batas Waktu 30 Menit</text>

      <rect x="440" y="2" width="130" height="34" rx="6" fill="#0f172a" stroke="#0284c7" />
      <text x="505" y="24" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">⏱️ 18:42 Tersisa</text>

      <line x1="0" y1="52" x2="544" y2="52" stroke="#334155" stroke-width="1" />

      <!-- Sample Question Container -->
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

      <!-- Question Palette Grid -->
      <g transform="translate(0, 360)">
        <text x="0" y="16" fill="#94a3b8" font-size="11" font-weight="600">NAVIGATOR 20 NOMOR SOAL:</text>
        
        <!-- Row 1 (1-10) -->
        <g transform="translate(0, 26)">
          <!-- Render 10 mini buttons -->
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

        <!-- Row 2 (11-20) -->
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

  <!-- Right Card: Post-Test Final Outcome (Width: 460) -->
  <g transform="translate(1140, 285)">
    <rect width="428" height="660" rx="14" fill="url(#cardGrad)" stroke="#059669" stroke-width="2" />
    
    <g transform="translate(24, 24)">
      <rect width="130" height="24" rx="6" fill="#059669" />
      <text x="65" y="16" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">PASCA PELATIHAN</text>
      
      <text x="0" y="55" fill="#ffffff" font-size="17" font-weight="700">Post-Test Kelulusan Jalur</text>
      <text x="0" y="74" fill="#34d399" font-size="11.5">Syarat Piagam: Skor Post-Test Wajib ≥ 70 (PRD §13)</text>

      <line x1="0" y1="90" x2="380" y2="90" stroke="#334155" stroke-width="1" />

      <!-- Projected Score Box -->
      <g transform="translate(0, 105)">
        <rect width="380" height="90" rx="10" fill="#064e3b" opacity="0.4" stroke="#059669" stroke-width="1.5" />
        <text x="20" y="32" fill="#a7f3d0" font-size="12">Capaian Post-Test Akhir:</text>
        <text x="20" y="68" fill="#34d399" font-size="34" font-weight="800">84 <tspan font-size="16" fill="#a7f3d0">/ 100</tspan></text>
        <text x="360" y="60" fill="#a7f3d0" font-size="12" text-anchor="end">Status: Lulus (≥70)</text>
      </g>

      <!-- Metrik T1 Calculation Box -->
      <g transform="translate(0, 215)">
        <rect width="380" height="150" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5" />
        <text x="16" y="24" fill="#c7d2fe" font-size="12" font-weight="700">HASIL METRIK T1 KENAIKAN KOMPETENSI:</text>
        
        <text x="16" y="52" fill="#ffffff" font-size="13">Pre-Test: <tspan font-weight="700" fill="#f59e0b">56</tspan> ➔ Post-Test: <tspan font-weight="700" fill="#34d399">84</tspan></text>
        <text x="16" y="76" fill="#ffffff" font-size="13">Kenaikan: <tspan font-weight="700" fill="#38bdf8">+28 Poin (+50.0%)</tspan></text>

        <rect x="16" y="94" width="348" height="38" rx="6" fill="#059669" />
        <text x="190" y="118" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓ MELEBIHI TARGET PRD T1 (+50% &gt; 25%)</text>
      </g>

      <!-- Piagam Issuance Check -->
      <g transform="translate(0, 390)">
        <rect width="380" height="210" rx="10" fill="#0f172a" stroke="#1e293b" />
        <text x="16" y="26" fill="#f8fafc" font-size="12" font-weight="700">STATUS VERIFIKASI SYARAT PIAGAM:</text>
        
        <text x="16" y="56" fill="#34d399" font-size="11.5">✓ 9 Misi Jalur IPA: Selesai</text>
        <text x="16" y="80" fill="#34d399" font-size="11.5">✓ Misi Kelulusan IPA-09: Lulus (Skor ≥80)</text>
        <text x="16" y="104" fill="#34d399" font-size="11.5">✓ Post-Test Akhir: 84 / 100 (Lulus ≥70)</text>
        <text x="16" y="128" fill="#38bdf8" font-size="11.5">✓ Persetujuan Instruktur: Diajukan ke Pak Budi</text>

        <rect x="16" y="150" width="348" height="42" rx="8" fill="#0284c7" />
        <text x="190" y="176" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">LIHAT PREVIEW PIAGAM SAYA (L8) →</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L4a: PRE-TEST & POST-TEST EVALUASI KOMPETENSI (SimSCADA-Air v1.0)")

print("Generating L3, L4, L4a...")
with open(os.path.join(OUTPUT_DIR, "mockup_l3_track_select.svg"), "w") as f:
    f.write(generate_l3())
with open(os.path.join(OUTPUT_DIR, "mockup_l4_module_quiz.svg"), "w") as f:
    f.write(generate_l4())
with open(os.path.join(OUTPUT_DIR, "mockup_l4a_pre_post_test.svg"), "w") as f:
    f.write(generate_l4a())
print("L3, L4, L4a generated successfully.")

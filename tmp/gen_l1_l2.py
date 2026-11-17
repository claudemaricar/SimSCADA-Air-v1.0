#!/usr/bin/env python3
"""
SimSCADA-Air Mockup Batch 1: L1, L2, L3, L4, L4a
"""
import os

OUTPUT_DIR = "/public"
os.makedirs(OUTPUT_DIR, exist_ok=True)

from generate_all_mockups import svg_wrap, header_tenant, page_title_block

def generate_l1():
    content = f"""  <!-- Main Card Container -->
  <g transform="translate(480, 75)" filter="url(#dropShadow)">
    <rect width="640" height="840" rx="20" fill="url(#cardGrad)" stroke="#334155" stroke-width="2" />

    <!-- Brand Header -->
    <g transform="translate(50, 36)">
      <rect width="52" height="52" rx="12" fill="url(#accentGrad)" />
      <path d="M 26 12 C 26 12, 16 26, 16 34 A 10 10 0 0 0 36 34 C 36 26, 26 12, 26 12 Z" fill="#ffffff" />
      <path d="M 22 36 A 4 4 0 0 0 30 36" stroke="#0284c7" stroke-width="2" fill="none" stroke-linecap="round" />
      <text x="68" y="26" fill="#ffffff" font-size="26" font-weight="700" letter-spacing="0.5">SimSCADA-Air</text>
      <text x="68" y="46" fill="#38bdf8" font-size="12" font-weight="600" letter-spacing="1.2">SIMULATOR SCADA OPERATOR AIR MINUM</text>
    </g>

    <!-- Tagline (PRD §5: Hapus kata Sertifikasi) -->
    <text x="50" y="125" fill="#94a3b8" font-size="13">Platform Pelatihan Berbasis Standar Permenkes No. 2/2023</text>
    <line x1="50" y1="145" x2="590" y2="145" stroke="#334155" stroke-width="1" />

    <!-- Form Element: Username (Auto-detects role & tenant) -->
    <text x="50" y="180" fill="#e2e8f0" font-size="13" font-weight="600">ID OPERATOR / USERNAME</text>
    <rect x="50" y="195" width="540" height="46" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5" />
    <text x="68" y="224" fill="#38bdf8" font-size="14" font-weight="500">peserta.ipa</text>
    <text x="570" y="224" fill="#64748b" font-size="12" text-anchor="end">🏢 Balai Diklat Air Minum Nusantara</text>

    <!-- Form Element: Password -->
    <text x="50" y="270" fill="#e2e8f0" font-size="13" font-weight="600">KATA SANDI</text>
    <rect x="50" y="285" width="540" height="46" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1" />
    <text x="68" y="316" fill="#94a3b8" font-size="18" letter-spacing="4">••••••••••••</text>
    <text x="50" y="348" fill="#64748b" font-size="11">Sandi Demo: <tspan fill="#f59e0b" font-weight="600">Demo#2026</tspan> (Khusus prototipe, otomatis terisi)</text>

    <!-- Auto-Detection Info Banner -->
    <g transform="translate(50, 365)">
      <rect width="540" height="48" rx="8" fill="#0c4a6e" opacity="0.4" stroke="#0284c7" stroke-width="1" />
      <text x="16" y="22" fill="#7dd3fc" font-size="12" font-weight="600">ℹ️ Sistem mengenali Lembaga &amp; Peran secara otomatis dari akun.</text>
      <text x="16" y="38" fill="#94a3b8" font-size="11">5 Peran: Super Admin, Admin Lembaga, Pimpinan Lembaga, Instruktur, Peserta Operator.</text>
    </g>

    <!-- Action Button: Masuk Workspace -->
    <g transform="translate(50, 428)">
      <rect width="540" height="48" rx="10" fill="url(#primaryGrad)" />
      <text x="270" y="30" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle" letter-spacing="0.5">MASUK WORKSPACE SIMULASI →</text>
    </g>

    <!-- 10 Quick Demo Logins Section PRD §5 -->
    <rect x="50" y="495" width="540" height="315" rx="10" fill="#090d16" stroke="#1e293b" />
    <text x="66" y="520" fill="#f59e0b" font-size="12" font-weight="700" letter-spacing="0.5">⚡ MASUK SEBAGAI… (10 AKUN DEMO RESMI PRD §5):</text>
    <text x="66" y="536" fill="#64748b" font-size="10">Klik salah satu akun untuk simulasi instan peran terkait:</text>

    <!-- Grid of 10 Demo Accounts (2 columns x 5 rows) -->
    <!-- Col 1: Nusantara & Superadmin -->
    <g transform="translate(66, 548)">
      <!-- 1. Super Admin -->
      <rect x="0" y="0" width="245" height="42" rx="6" fill="#1e1b4b" stroke="#4338ca" stroke-width="1" />
      <text x="10" y="18" fill="#c7d2fe" font-size="11" font-weight="700">👑 superadmin</text>
      <text x="10" y="32" fill="#818cf8" font-size="9.5">Platform SimSCADA-Air (2 Lembaga)</text>

      <!-- 2. Admin Nusantara -->
      <rect x="0" y="48" width="245" height="42" rx="6" fill="#064e3b" stroke="#059669" stroke-width="1" />
      <text x="10" y="66" fill="#a7f3d0" font-size="11" font-weight="700">🏢 admin.nusantara</text>
      <text x="10" y="80" fill="#34d399" font-size="9.5">Admin Balai Nusantara (50 Kursi)</text>

      <!-- 3. Pimpinan Nusantara -->
      <rect x="0" y="96" width="245" height="42" rx="6" fill="#3b0764" stroke="#9333ea" stroke-width="1" />
      <text x="10" y="114" fill="#f3e8ff" font-size="11" font-weight="700">👔 pimpinan.nusantara</text>
      <text x="10" y="128" fill="#c084fc" font-size="9.5">Pimpinan Lembaga (T1–T4 &amp; Piagam)</text>

      <!-- 4. Instruktur Nusantara -->
      <rect x="0" y="144" width="245" height="42" rx="6" fill="#451a03" stroke="#d97706" stroke-width="1" />
      <text x="10" y="162" fill="#fde68a" font-size="11" font-weight="700">🎓 instruktur.nusantara</text>
      <text x="10" y="176" fill="#fbbf24" font-size="9.5">Pak Budi (Membina Angkatan 1)</text>

      <!-- 5. Peserta Baru Nusantara -->
      <rect x="0" y="192" width="245" height="42" rx="6" fill="#082f49" stroke="#0284c7" stroke-width="1" />
      <text x="10" y="210" fill="#bae6fd" font-size="11" font-weight="700">👤 peserta.baru</text>
      <text x="10" y="224" fill="#38bdf8" font-size="9.5">Dimas (Terpadu · Pre-test &amp; Baru)</text>
    </g>

    <!-- Col 2: Peserta Nusantara & Tirta Mandiri -->
    <g transform="translate(325, 548)">
      <!-- 6. Peserta IPA Nusantara -->
      <rect x="0" y="0" width="245" height="42" rx="6" fill="#082f49" stroke="#0284c7" stroke-width="1" />
      <text x="10" y="18" fill="#bae6fd" font-size="11" font-weight="700">👤 peserta.ipa</text>
      <text x="10" y="32" fill="#38bdf8" font-size="9.5">Nusantara (Jalur IPA · 820 XP)</text>

      <!-- 7. Peserta Distribusi Nusantara -->
      <rect x="0" y="48" width="245" height="42" rx="6" fill="#082f49" stroke="#0284c7" stroke-width="1" />
      <text x="10" y="66" fill="#bae6fd" font-size="11" font-weight="700">👤 peserta.distribusi</text>
      <text x="10" y="80" fill="#38bdf8" font-size="9.5">Nusantara (Jalur Distribusi · Tengah)</text>

      <!-- 8. Peserta Lulus Nusantara -->
      <rect x="0" y="96" width="245" height="42" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1" />
      <text x="10" y="114" fill="#a7f3d0" font-size="11" font-weight="700">🎓 peserta.lulus</text>
      <text x="10" y="128" fill="#34d399" font-size="9.5">Nusantara (17 Misi · Piagam Terbit)</text>

      <!-- 9. Admin Tirta Mandiri -->
      <rect x="0" y="144" width="245" height="42" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1" />
      <text x="10" y="162" fill="#e2e8f0" font-size="11" font-weight="700">🏢 admin.tirta</text>
      <text x="10" y="176" fill="#94a3b8" font-size="9.5">Pusat Pelatihan Tirta Mandiri (50 K)</text>

      <!-- 10. Peserta Tirta Mandiri -->
      <rect x="0" y="192" width="245" height="42" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1" />
      <text x="10" y="210" fill="#e2e8f0" font-size="11" font-weight="700">👤 peserta.tirta</text>
      <text x="10" y="224" fill="#94a3b8" font-size="9.5">Tirta Mandiri (Uji Isolasi Multi-Tenant)</text>
    </g>

    <!-- Footer Note inside Card -->
    <text x="320" y="826" fill="#475569" font-size="11" text-anchor="middle">Isolasi Database Antar-Lembaga · Sesuai PRD SimSCADA-Air v1.0 §5</text>
  </g>

  <!-- Left Annotation: Auto Role & Multi-Tenant -->
  <g transform="translate(60, 240)">
    <rect width="360" height="150" rx="10" fill="#1e293b" opacity="0.95" stroke="#38bdf8" stroke-width="1.5" />
    <circle cx="24" cy="24" r="10" fill="#0284c7" />
    <text x="24" y="28" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">1</text>
    <text x="44" y="28" fill="#38bdf8" font-size="13" font-weight="700">Auto-Detect Peran &amp; Lembaga</text>
    <text x="20" y="55" fill="#cbd5e1" font-size="12">Pemilih peran manual dihapus sesuai PRD §5.</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">Sistem langsung mengarahkan pengguna ke</text>
    <text x="20" y="95" fill="#cbd5e1" font-size="12">dasbor peran masing-masing dengan isolasi</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="12">data penuh antar-lembaga (Nusantara vs Tirta).</text>
  </g>
  <path d="M 420 310 L 460 310 L 525 220" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="5,4" fill="none" marker-end="url(#dotBlue)" />

  <!-- Right Annotation: 10 Demo Accounts -->
  <g transform="translate(1180, 560)">
    <rect width="360" height="160" rx="10" fill="#1e293b" opacity="0.95" stroke="#10b981" stroke-width="1.5" />
    <circle cx="24" cy="24" r="10" fill="#10b981" />
    <text x="24" y="28" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">2</text>
    <text x="44" y="28" fill="#34d399" font-size="13" font-weight="700">10 Akun Demo Standar PRD §5</text>
    <text x="20" y="55" fill="#cbd5e1" font-size="12">Semua 10 akun demo PRD terdaftar dengan</text>
    <text x="20" y="75" fill="#cbd5e1" font-size="12">kata sandi seragam <tspan fill="#f59e0b" font-weight="700">Demo#2026</tspan>:</text>
    <text x="20" y="95" fill="#cbd5e1" font-size="12">• Super Admin, Pimpinan, Admin, Instruktur</text>
    <text x="20" y="115" fill="#cbd5e1" font-size="12">• 4 Peserta Nusantara (Baru, IPA, Dist, Lulus)</text>
    <text x="20" y="135" fill="#cbd5e1" font-size="12">• 2 Akun Tirta Mandiri untuk uji isolasi.</text>
  </g>
  <path d="M 1180 640 L 1120 640 L 1025 640" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5,4" fill="none" marker-end="url(#dotGreen)" />
"""
    return svg_wrap(content, "MOCKUP L1: PORTAL AUTENTIKASI MULTI-TENANT (SimSCADA-Air v1.0)")

def generate_l2():
    hdr = header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW")
    title = page_title_block("Beranda Peserta &amp; Peta Misi Jalur", "Jalur Aktif: Operator IPA (9 Misi) · Selesaikan misi secara berurutan untuk membuka Misi Kelulusan", 120)
    
    content = f"""{hdr}
{title}

  <!-- Left Column: Profile Card & Summary (Width: 380) -->
  <g transform="translate(32, 190)">
    <!-- Profile Card PRD §8 & §11 -->
    <rect width="380" height="360" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
    <g transform="translate(24, 24)">
      <circle cx="36" cy="36" r="32" fill="#0284c7" />
      <text x="36" y="44" fill="#ffffff" font-size="20" font-weight="700" text-anchor="middle">DW</text>
      <text x="84" y="28" fill="#f8fafc" font-size="17" font-weight="700">Dimas Wahyu Pratama</text>
      <text x="84" y="48" fill="#94a3b8" font-size="12">Balai Diklat Air Minum Nusantara</text>
      <text x="84" y="66" fill="#38bdf8" font-size="12" font-weight="600">Angkatan 1 · Jalur IPA</text>

      <line x1="0" y1="85" x2="332" y2="85" stroke="#334155" stroke-width="1" />

      <!-- Level & XP PRD §8 -->
      <text x="0" y="112" fill="#94a3b8" font-size="11" font-weight="600">LEVEL OPERATOR (PRD §8):</text>
      <rect x="0" y="122" width="160" height="30" rx="6" fill="#0284c7" opacity="0.2" stroke="#0284c7" />
      <text x="80" y="142" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Operator Muda</text>

      <!-- XP Bar -->
      <text x="180" y="112" fill="#94a3b8" font-size="11" font-weight="600">TOTAL XP: <tspan fill="#f59e0b">820 XP</tspan></text>
      <rect x="180" y="126" width="152" height="12" rx="6" fill="#0f172a" />
      <rect x="180" y="126" width="65" height="12" rx="6" fill="url(#goldGrad)" />
      <text x="180" y="152" fill="#64748b" font-size="10">820 / 1.200 XP ke Operator Madya</text>

      <!-- Stats Grid -->
      <g transform="translate(0, 175)">
        <rect width="102" height="65" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="51" y="24" fill="#94a3b8" font-size="10" text-anchor="middle">Misi Lulus</text>
        <text x="51" y="48" fill="#38bdf8" font-size="20" font-weight="700" text-anchor="middle">7 / 9</text>

        <rect x="115" width="102" height="65" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="166" y="24" fill="#94a3b8" font-size="10" text-anchor="middle">Bintang</text>
        <text x="166" y="48" fill="#f59e0b" font-size="20" font-weight="700" text-anchor="middle">14 ★</text>

        <rect x="230" width="102" height="65" rx="8" fill="#0f172a" stroke="#1e293b" />
        <text x="281" y="24" fill="#94a3b8" font-size="10" text-anchor="middle">Lencana</text>
        <text x="281" y="48" fill="#10b981" font-size="20" font-weight="700" text-anchor="middle">3 / 8</text>
      </g>

      <!-- Piagam Status Card PRD §11 -->
      <g transform="translate(0, 255)">
        <rect width="332" height="52" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1" />
        <text x="12" y="22" fill="#c7d2fe" font-size="11" font-weight="700">STATUS PIAGAM KELULUSAN:</text>
        <text x="12" y="38" fill="#a5b4fc" font-size="12">Belum Memenuhi (Sisa 2 Misi Jalur IPA)</text>
        <text x="318" y="32" fill="#818cf8" font-size="16" text-anchor="end">🔒</text>
      </g>
    </g>
  </g>

  <!-- Left Bottom: AI Smart Advisor & Pre-Test Box -->
  <g transform="translate(32, 570)">
    <!-- AI Advisor Box PRD §11 -->
    <rect width="380" height="190" rx="14" fill="#0c2538" stroke="#0284c7" stroke-width="1.5" />
    <g transform="translate(20, 20)">
      <text x="0" y="16" fill="#38bdf8" font-size="13" font-weight="700">💡 SARAN BELAJAR OTOMATIS (PRD §11)</text>
      <text x="0" y="42" fill="#e2e8f0" font-size="12" font-weight="600">"Waktu respons Anda pada misi gangguan rata-rata</text>
      <text x="0" y="60" fill="#e2e8f0" font-size="12" font-weight="600">2× target skenario. Ulangi latihan penanganan</text>
      <text x="0" y="78" fill="#e2e8f0" font-size="12" font-weight="600">pompa trip di IPA-07 sebelum Misi Kelulusan."</text>
      
      <rect x="0" y="98" width="340" height="42" rx="6" fill="#0369a1" />
      <text x="170" y="124" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">LATIHAN ULANG: IPA-07 POMPA TRIP →</text>
    </g>

    <!-- Pre-Test vs Post-Test Card PRD §3 & §11 -->
    <g transform="translate(0, 205)">
      <rect width="380" height="175" rx="14" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5" />
      <g transform="translate(20, 20)">
        <text x="0" y="16" fill="#f8fafc" font-size="13" font-weight="700">EVALUASI KOMPETENSI (METRIK T1)</text>
        
        <rect x="0" y="32" width="160" height="60" rx="8" fill="#0f172a" />
        <text x="12" y="52" fill="#94a3b8" font-size="11">Pre-Test Baseline</text>
        <text x="12" y="78" fill="#f59e0b" font-size="20" font-weight="700">56 <tspan font-size="12">/ 100</tspan></text>

        <rect x="180" y="32" width="160" height="60" rx="8" fill="#0f172a" />
        <text x="192" y="52" fill="#94a3b8" font-size="11">Post-Test Akhir</text>
        <text x="192" y="78" fill="#64748b" font-size="16" font-weight="600">Terkunci 🔒</text>
        <text x="0" y="112" fill="#64748b" font-size="10.5">Post-test terbuka setelah Misi Kelulusan IPA-09 lulus (≥80).</text>
        <text x="0" y="128" fill="#38bdf8" font-size="10.5">Target PRD T1: Kenaikan Kompetensi minimal +25%.</text>
      </g>
    </g>
  </g>

  <!-- Right Section: 5-Tier Mission Roadmap (PRD §7: 9 Misi Jalur IPA) -->
  <g transform="translate(436, 190)">
    <rect width="1132" height="770" rx="14" fill="url(#cardDark)" stroke="#334155" stroke-width="1.5" />
    
    <!-- Roadmap Header -->
    <g transform="translate(28, 22)">
      <text x="0" y="18" fill="#f8fafc" font-size="16" font-weight="700">PETA MISI JALUR OPERATOR IPA (9 MISI BERJENJANG)</text>
      <text x="0" y="38" fill="#94a3b8" font-size="12">Aturan Bintang: &lt;70 Belum Lulus · 70–84 (1★) · 85–94 (2★) · ≥95 (3★). Misi Kelulusan lulus jika skor ≥80.</text>
    </g>

    <!-- 5 Difficulty Tiers PRD §7 -->
    
    <!-- TIER 1: PENGENALAN (MUDAH) -->
    <g transform="translate(28, 75)">
      <rect width="1076" height="105" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="105" rx="4" fill="#0284c7" />
      <text x="24" y="24" fill="#38bdf8" font-size="12" font-weight="700">TINGKAT 1: PENGENALAN (MUDAH · TANPA GANGGUAN)</text>
      
      <!-- Card IPA-01 -->
      <g transform="translate(24, 36)">
        <rect width="320" height="56" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <circle cx="28" cy="28" r="14" fill="#059669" />
        <text x="28" y="33" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">✓</text>
        <text x="52" y="22" fill="#ffffff" font-size="12" font-weight="700">IPA-01: Kenali Ruang Kendali</text>
        <text x="52" y="38" fill="#34d399" font-size="11">Skor: 96 · 3 Bintang (★★★)</text>
        <text x="260" y="30" fill="#f59e0b" font-size="13">★★★</text>
      </g>
    </g>

    <!-- TIER 2: OPERASI NORMAL (SEDANG) -->
    <g transform="translate(28, 195)">
      <rect width="1076" height="120" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="120" rx="4" fill="#059669" />
      <text x="24" y="22" fill="#34d399" font-size="12" font-weight="700">TINGKAT 2: OPERASI NORMAL (MUDAH – SEDANG)</text>

      <!-- Card IPA-02 -->
      <g transform="translate(24, 34)">
        <rect width="250" height="70" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="22" fill="#ffffff" font-size="11.5" font-weight="700">IPA-02: Menyalakan Intake</text>
        <text x="14" y="38" fill="#94a3b8" font-size="10.5">Start pompa &amp; debit target</text>
        <text x="14" y="56" fill="#34d399" font-size="11" font-weight="600">Skor: 92 (★★☆)</text>
      </g>

      <!-- Card IPA-03 -->
      <g transform="translate(288, 34)">
        <rect width="250" height="70" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="22" fill="#ffffff" font-size="11.5" font-weight="700">IPA-03: Dosis Koagulan Normal</text>
        <text x="14" y="38" fill="#94a3b8" font-size="10.5">Kekeruhan air olahan &lt;3 NTU</text>
        <text x="14" y="56" fill="#34d399" font-size="11" font-weight="600">Skor: 88 (★★☆)</text>
      </g>

      <!-- Card IPA-04 -->
      <g transform="translate(552, 34)">
        <rect width="250" height="70" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="22" fill="#ffffff" font-size="11.5" font-weight="700">IPA-04: Jaga Filter &amp; Backwash</text>
        <text x="14" y="38" fill="#94a3b8" font-size="10.5">Headloss filter &amp; siklus cuci</text>
        <text x="14" y="56" fill="#34d399" font-size="11" font-weight="600">Skor: 85 (★★☆)</text>
      </g>

      <!-- Card IPA-05 -->
      <g transform="translate(816, 34)">
        <rect width="244" height="70" rx="8" fill="#1e293b" stroke="#059669" stroke-width="1.5" />
        <text x="14" y="22" fill="#ffffff" font-size="11.5" font-weight="700">IPA-05: Klorinasi Tepat</text>
        <text x="14" y="38" fill="#94a3b8" font-size="10.5">Sisa klor 0,2–0,5 mg/L</text>
        <text x="14" y="56" fill="#34d399" font-size="11" font-weight="600">Skor: 86 (★★☆)</text>
      </g>
    </g>

    <!-- TIER 3: GANGGUAN TUNGGAL (SULIT) -->
    <g transform="translate(28, 330)">
      <rect width="1076" height="150" rx="10" fill="#0f172a" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="150" rx="4" fill="#f59e0b" />
      <text x="24" y="22" fill="#fbbf24" font-size="12" font-weight="700">TINGKAT 3: GANGGUAN TUNGGAL (SULIT · 5 GANGGUAN UTAMA PRD §7)</text>

      <!-- Card IPA-06: Sesi Contoh Konsisten PRD -->
      <g transform="translate(24, 34)">
        <rect width="330" height="98" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <rect x="14" y="10" width="75" height="18" rx="4" fill="#0284c7" />
        <text x="51" y="23" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">SESI CONTOH</text>
        <text x="96" y="24" fill="#38bdf8" font-size="12" font-weight="700">IPA-06: Lonjakan Kekeruhan</text>
        <text x="14" y="46" fill="#cbd5e1" font-size="11">Air baku 185 NTU · Naikkan dosis &amp; pH</text>
        <text x="14" y="66" fill="#f59e0b" font-size="12" font-weight="700">Skor: 88 · 2★ · +176 XP</text>
        <text x="14" y="84" fill="#10b981" font-size="10.5">✓ Lulus dengan Baik (Durasi 08:30)</text>
      </g>

      <!-- Card IPA-07: Pompa Trip -->
      <g transform="translate(370, 34)">
        <rect width="330" height="98" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
        <text x="14" y="24" fill="#ffffff" font-size="12" font-weight="700">IPA-07: Gangguan Pompa Trip</text>
        <text x="14" y="46" fill="#cbd5e1" font-size="11">Alihkan ke pompa cadangan &amp; reset</text>
        <text x="14" y="66" fill="#f59e0b" font-size="12" font-weight="700">Skor: 76 · 1★ · +152 XP</text>
        <text x="14" y="84" fill="#fbbf24" font-size="10.5">⚠️ Perlu perbaikan waktu respons</text>
      </g>

      <!-- Card IPA-08: Dosis Klor Tidak Sesuai (Aktif Berikutnya) -->
      <g transform="translate(716, 34)">
        <rect width="344" height="98" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2" />
        <rect x="14" y="10" width="85" height="18" rx="4" fill="#38bdf8" />
        <text x="56" y="23" fill="#082f49" font-size="10" font-weight="700" text-anchor="middle">MISI BERIKUT</text>
        <text x="108" y="24" fill="#ffffff" font-size="12" font-weight="700">IPA-08: Dosis Klor Drop</text>
        <text x="14" y="46" fill="#bae6fd" font-size="11">Koreksi setpoint klor &amp; pantau reservoir</text>
        <text x="14" y="66" fill="#7dd3fc" font-size="11">Status: Siap Dikerjakan (Terbuka)</text>
        
        <rect x="14" y="74" width="160" height="18" rx="4" fill="#0284c7" />
        <text x="94" y="87" fill="#ffffff" font-size="10.5" font-weight="700" text-anchor="middle">MULAI MISI INI →</text>
      </g>
    </g>

    <!-- TIER 4: GANGGUAN BERANTAI (KHUSUS TERPADU) -->
    <g transform="translate(28, 495)">
      <rect width="1076" height="90" rx="10" fill="#090d16" stroke="#1e293b" />
      <rect x="0" y="0" width="8" height="90" rx="4" fill="#64748b" />
      <text x="24" y="22" fill="#94a3b8" font-size="12" font-weight="700">TINGKAT 4: GANGGUAN BERANTAI (SANGAT SULIT · KHUSUS JALUR TERPADU TRP-01)</text>
      <text x="24" y="48" fill="#64748b" font-size="12">Jalur Operator IPA melompat langsung dari Gangguan Tunggal ke Misi Kelulusan Ujian.</text>
      <text x="24" y="68" fill="#0284c7" font-size="11.5">Misi TRP-01 "Hulu ke Hilir" hanya tersedia di Jalur Air Minum Terpadu (17 Misi).</text>
    </g>

    <!-- TIER 5: MISI KELULUSAN (UJIAN) -->
    <g transform="translate(28, 600)">
      <rect width="1076" height="140" rx="10" fill="#1e1b4b" stroke="#4338ca" stroke-width="1.5" />
      <rect x="0" y="0" width="8" height="140" rx="4" fill="#818cf8" />
      <text x="24" y="26" fill="#c7d2fe" font-size="13" font-weight="700">TINGKAT 5: MISI KELULUSAN JALUR IPA (UJIAN AKHIR · BATAS WAKTU &amp; TANPA PETUNJUK)</text>
      
      <g transform="translate(24, 40)">
        <rect width="600" height="82" rx="8" fill="#0f172a" stroke="#334155" />
        <text x="18" y="26" fill="#ffffff" font-size="14" font-weight="700">IPA-09: Misi Kelulusan Operator IPA</text>
        <text x="18" y="46" fill="#94a3b8" font-size="11.5">Skenario: Lonjakan kekeruhan ekstrem disusul pompa trip serentak tanpa petunjuk.</text>
        <text x="18" y="66" fill="#fbbf24" font-size="11" font-weight="600">Ambang Kelulusan: Skor Minimal ≥ 80 (PRD §8) · Pengali XP: 3,0x (Ujian)</text>
        <text x="560" y="48" fill="#ef4444" font-size="20" text-anchor="middle">🔒</text>
      </g>

      <g transform="translate(640, 40)">
        <rect width="412" height="82" rx="8" fill="#0f172a" stroke="#334155" />
        <text x="16" y="24" fill="#38bdf8" font-size="12" font-weight="700">SYARAT BUKA KUNCI IPA-09:</text>
        <text x="16" y="44" fill="#34d399" font-size="11">✓ IPA-01 s/d IPA-07 Lulus</text>
        <text x="16" y="64" fill="#f59e0b" font-size="11">⏳ Selesaikan IPA-08 (Dosis Klor Drop)</text>
      </g>
    </g>
  </g>
"""
    return svg_wrap(content, "MOCKUP L2: BERANDA PESERTA & ROADMAP MISI (SimSCADA-Air v1.0)")

print("Generating L1 & L2...")
with open(os.path.join(OUTPUT_DIR, "mockup_l1_login.svg"), "w") as f:
    f.write(generate_l1())
with open(os.path.join(OUTPUT_DIR, "mockup_l2_trainee_dashboard.svg"), "w") as f:
    f.write(generate_l2())
print("L1 & L2 generated successfully.")

# PRD SimSCADA-Air — Simulator SCADA Gamifikasi untuk Pelatihan Operator Air Minum

Oct 27, 2026 · @Eltima Corner

## 1. Ringkasan Produk

SimSCADA-Air adalah simulator SCADA berbasis web dengan pola gamifikasi untuk melatih operator air minum, dari Instalasi Pengolahan Air (IPA) sampai jaringan distribusi, tanpa menyentuh instalasi nyata. Peserta menyelesaikan misi berjenjang dari paling mudah sampai paling sulit, mendapat skor dan lencana, lalu menerima piagam kelulusan. Produk dijual ke lembaga pelatihan IPA dan distribusi air; setiap lembaga pembeli tampil dengan namanya sendiri dan punya dashboard evaluasi.

| Item | Keterangan |
| --- | --- |
| Nama produk | SimSCADA-Air |
| Judul proyek | Pengembangan Sistem Pembelajaran Berbasis Simulator SCADA untuk Pelatihan Operator Air Minum dari IPA hingga Jaringan Distribusi |
| Jenis dokumen | Product Requirements Document (PRD), versi 1.1 |
| Konteks | Tugas proyek kelompok, Program S2, Pradita University |
| Dasar | Lembar Kerja Misi 01–05 (W1–W5) dan Peta Komponen Sistem (Misi 05) |
| Target rilis | Prototipe dan uji coba terbatas pada akhir semester 1 |
| Pengguna akhir | Peserta, Instruktur, Admin Lembaga, Pimpinan Lembaga, Super Admin platform |

**Revisi 1.1 (16 Nov 2026):** jumlah misi jalur Terpadu dikoreksi dari 17 menjadi 16 (bagian 7 dan 8) agar sesuai dengan katalog misi.

Prioritas di seluruh dokumen memakai skala W4: **W** = Wajib, **P** = Penting, **B** = Bagus bila ada, **N** = Nanti.

## 2. Latar Belakang dan Masalah

Operator baru belum terampil menangani kondisi abnormal karena tidak ada sarana latihan yang aman. Mereka belajar sambil mendampingi operator senior, sementara gangguan seperti lonjakan kekeruhan, pompa trip, kebocoran pipa, atau tekanan drop tidak boleh dicoba di instalasi yang beroperasi.

| Aspek | Temuan (Misi 01) |
| --- | --- |
| Siapa | Operator baru dan operator yang dirotasi ke unit IPA atau distribusi |
| Di mana | Perusahaan air minum, dari unit IPA hingga jaringan distribusi |
| Kapan | Masa orientasi, saat rotasi, dan saat terjadi gangguan operasional |
| Dampak | Salah tindak mengganggu kualitas air dan pasokan pelanggan serta merusak peralatan |
| Cara saat ini | Pendampingan senior, SOP tertulis, pelatihan kelas tanpa praktik simulasi |
| Celah tambahan | Materi IPA dan distribusi terpisah, sehingga operator kurang paham alur sistem utuh |

**Rumusan masalah:** Bagaimana sistem pembelajaran berbasis simulator SCADA dapat meningkatkan keterampilan operator air minum dalam mengoperasikan dan menangani gangguan proses dari IPA hingga jaringan distribusi secara aman sebelum bertugas di instalasi nyata?

**Dasar pustaka (Misi 03).** Simulator operator terbukti memberi efek pelatihan sekitar 4,5 kali pelatihan konvensional (Lee & Ma, 2023). Pendekatan *serious game* mempercepat respons krisis kontaminasi air (PLOS ONE, 2025). Temuan ini menjadi alasan memakai gamifikasi, bukan sekadar simulator. Produk pembanding: EPANET (hidrolika distribusi), Hydromantis SimuWorks (simulator operator berlisensi), Ignition Maker Edition (platform HMI web).

**Peluang produk.** Contoh yang ditemukan di Misi 03 hanya menutup sebagian kebutuhan: EPANET tanpa pelatihan operator, SimuWorks untuk air limbah, Ignition masih harus dibangun sendiri. Belum ada satu paket berbahasa Indonesia yang menggabungkan IPA dan distribusi, misi berjenjang, penilaian otomatis, dan laporan untuk lembaga pelatihan. Karena itu SimSCADA-Air dirancang sebagai produk yang dijual ke banyak lembaga, bukan alat internal satu instalasi.

## 3. Tujuan dan Metrik Keberhasilan

Produk berhasil bila, dalam 6 bulan setelah dipakai lembaga, nilai uji kompetensi operator baru naik minimal 25% dan 80% peserta lulus 5 skenario gangguan utama. Target ini dari piagam proyek (Misi 02); dashboard evaluasi lembaga (bagian 12) mengukurnya langsung.

| Kode | Metrik | Target | Cara ukur di sistem |
| --- | --- | --- | --- |
| T1 | Kenaikan rata-rata nilai uji kompetensi dibanding pelatihan konvensional | ≥ 25% | Pre-test saat pendaftaran vs post-test setelah misi kelulusan |
| T2 | Peserta yang menangani 5 skenario gangguan utama dengan benar | ≥ 80% | Misi gangguan lulus (≥ 1 bintang): kekeruhan, pompa trip, dosis klor, kebocoran, tekanan drop |
| T3 | Waktu orientasi operator baru sampai siap bertugas | dari ±3 bulan menjadi ±2 bulan | Selisih tanggal mulai jalur dan tanggal piagam terbit |
| T4 | Penyelesaian jalur oleh peserta yang terdaftar | ≥ 70% (usulan) | Piagam terbit ÷ peserta aktif per angkatan |
| T5 | Kemudahan pakai prototipe | SUS ≥ 70 (usulan) | Kuesioner kepada peserta uji coba (Misi 02: uji coba pengguna) |

T1–T3 berasal dari Misi 02. T4 dan T5 adalah usulan tambahan untuk produk komersial dan perlu disepakati kelompok.

**Tujuan bisnis.** Produk dapat dijual sebagai lisensi ke lebih dari satu lembaga pelatihan, dengan data tiap lembaga terpisah dan identitas lembaga tampil di layar, laporan, dan piagam.

## 4. Cakupan

Cakupan Misi 02 diperluas dengan lima hal: gamifikasi misi berjenjang, dashboard capaian, piagam kelulusan, model multi-lembaga dengan dashboard evaluasi pembeli, dan tiga jalur belajar. Batas keamanannya tetap: simulator tidak pernah terhubung ke SCADA/PLC nyata.

**Termasuk**

- Simulator SCADA web: intake, koagulasi, flokulasi, sedimentasi, filtrasi, desinfeksi, reservoir, dan jaringan distribusi (Misi 02).
- Skenario kondisi normal dan gangguan, modul materi, kuis, dan penilaian otomatis (Misi 02).
- Gamifikasi: misi dari mudah ke sulit, skor, bintang, XP, level operator, lencana, papan peringkat.
- Tiga jalur belajar: IPA saja, Distribusi saja, atau Terpadu IPA sampai Distribusi.
- Sistem alarm dengan akui (acknowledge), clear manual, dan clear otomatis setelah tindakan yang benar.
- Narasi pop-up untuk setiap titik kontrol simulasi.
- Dashboard capaian peserta, dashboard instruktur, dashboard evaluasi lembaga pembeli.
- Piagam kelulusan PDF dengan nama lembaga dan kode verifikasi.
- Multi-lembaga: nama, logo, pengguna, dan data tiap lembaga pembeli terpisah.
- Akun demo per peran untuk prototipe.
- Laporan hasil pelatihan PDF/Excel (Misi 04).

**Tidak termasuk**

- Koneksi ke SCADA/PLC instalasi yang beroperasi atau kendali nyata apa pun (Misi 02).
- Pengadaan sensor dan perangkat keras lapangan (Misi 02).
- Sertifikasi resmi operator; piagam hanya bukti selesai pelatihan, sertifikasi tetap oleh lembaga sertifikasi (Misi 02).
- Aplikasi mobile native (Misi 02).
- Pembayaran daring dan penagihan otomatis lisensi; pada prototipe lisensi diatur manual oleh Super Admin.
- Mode tim multi-pemain (Misi 04, prioritas N) ditunda ke rilis berikutnya.

## 5. Pengguna, Peran, dan Akun Prototipe

Sistem punya lima peran. Tiga berasal dari persona Misi 01; dua ditambahkan karena produk dijual ke banyak lembaga: Pimpinan Lembaga (pemilik dashboard evaluasi) dan Super Admin (pengelola platform).

| Peran | Persona / contoh | Tujuan utama | Hak akses inti |
| --- | --- | --- | --- |
| Peserta | Dimas, 23 th, operator baru lulusan SMK/D3 Teknik | Cepat mahir dan lulus uji kompetensi | Materi, kuis, misi pada jalurnya, dashboard capaian, unduh piagam |
| Instruktur | Pak Budi, 48 th, operator senior / pengawas produksi | Melatih dan menilai kesiapan secara objektif | Kelompok binaan: tugaskan misi, buat skenario, buka kunci misi, putar ulang log, setujui kelulusan |
| Admin Lembaga | Rina, 30 th, staf Diklat/SDM | Mengelola peserta, jadwal, skenario, laporan | Pengguna dan kelompok lembaganya, identitas lembaga (nama, logo, penanda tangan piagam), laporan |
| Pimpinan Lembaga | Kepala Diklat / Kepala Bagian Produksi & Distribusi di lembaga pembeli | Menilai efektivitas pelatihan dan nilai investasi | Dashboard evaluasi lembaga (baca saja), unduh laporan, tanda tangan digital piagam |
| Super Admin | Tim pengembang SimSCADA-Air | Mengelola lembaga pembeli dan lisensi | Daftar lembaga, kuota kursi, masa lisensi, pustaka misi dan narasi baku |

### Akun demo untuk prototipe

Setiap peran dan setiap jalur belajar punya akun sendiri agar semua use case bisa didemokan. Dua lembaga fiktif dipakai untuk menunjukkan bahwa data antar-lembaga terpisah.

| Username | Peran | Lembaga | Kondisi data awal |
| --- | --- | --- | --- |
| superadmin | Super Admin | Platform SimSCADA-Air | 2 lembaga aktif, lisensi masing-masing 50 kursi |
| admin.nusantara | Admin Lembaga | Balai Diklat Air Minum Nusantara (fiktif) | 2 kelompok, 1 instruktur, 4 peserta |
| pimpinan.nusantara | Pimpinan Lembaga | Balai Diklat Air Minum Nusantara | Dashboard evaluasi terisi data angkatan contoh |
| instruktur.nusantara | Instruktur | Balai Diklat Air Minum Nusantara | Membina kelompok "Angkatan 1" |
| peserta.baru | Peserta, jalur Terpadu | Balai Diklat Air Minum Nusantara | Belum mulai; menampilkan pre-test dan misi pertama |
| peserta.ipa | Peserta, jalur IPA | Balai Diklat Air Minum Nusantara | Di tengah jalur, beberapa misi berbintang |
| peserta.distribusi | Peserta, jalur Distribusi | Balai Diklat Air Minum Nusantara | Di tengah jalur |
| peserta.lulus | Peserta, jalur Terpadu | Balai Diklat Air Minum Nusantara | Semua misi lulus, piagam sudah terbit |
| admin.tirta | Admin Lembaga | Pusat Pelatihan Tirta Mandiri (fiktif) | 1 kelompok, data terpisah dari lembaga pertama |
| peserta.tirta | Peserta, jalur IPA | Pusat Pelatihan Tirta Mandiri | Untuk uji isolasi data |

Semua akun demo memakai kata sandi bersama `Demo#2026`, khusus lingkungan prototipe. Halaman login menampilkan tombol "Masuk sebagai…" per peran agar penguji tidak perlu mengetik. Pada rilis produksi, akun demo dihapus dan kata sandi wajib diganti saat login pertama.

### Matriks akses

| Fitur | Peserta | Instruktur | Admin Lembaga | Pimpinan Lembaga | Super Admin |
| --- | --- | --- | --- | --- | --- |
| Jalankan simulator dan misi | Ya | Ya (mode uji) | Tidak | Tidak | Ya (mode uji) |
| Dashboard capaian pribadi | Ya | Tidak | Tidak | Tidak | Tidak |
| Kelola skenario dan misi | Tidak | Ya | Ya | Tidak | Pustaka baku |
| Monitoring kelompok | Tidak | Kelompok binaan | Semua kelompok | Ringkasan | Tidak |
| Dashboard evaluasi lembaga | Tidak | Tidak | Ya | Ya | Semua lembaga |
| Kelola pengguna | Tidak | Tidak | Lembaganya | Tidak | Admin lembaga |
| Terbitkan / tanda tangan piagam | Unduh | Setujui | Atur templat | Tanda tangan | Tidak |
| Kelola lembaga dan lisensi | Tidak | Tidak | Tidak | Tidak | Ya |

## 6. Model Multi-Lembaga (Lembaga Pembeli)

Setiap lembaga pembeli adalah satu *tenant*: punya nama, logo, pengguna, kelompok, skenario tambahan, dan laporan sendiri yang tidak terlihat oleh lembaga lain. Nama lembaga tampil di semua tempat yang dilihat peserta maupun pihak luar.

**Tempat nama lembaga dimunculkan**

- Halaman login (setelah memilih lembaga atau lewat alamat khusus, misalnya `nusantara.simscada-air.id`).
- Header setiap layar: logo lembaga + nama lembaga, dengan teks kecil "Didukung oleh SimSCADA-Air".
- Briefing misi dan layar hasil ("Balai Diklat Air Minum Nusantara · Angkatan 1").
- Dashboard evaluasi, laporan PDF/Excel, dan piagam kelulusan.
- Halaman verifikasi piagam publik.

**Data per lembaga**

| Data | Keterangan |
| --- | --- |
| Profil | Nama resmi, singkatan, logo, alamat, kontak, jenis lembaga (diklat PDAM, balai pelatihan, lembaga swasta) |
| Lisensi | Paket jalur (IPA, Distribusi, Terpadu), kuota kursi peserta, tanggal mulai dan berakhir |
| Penanda tangan piagam | Nama dan jabatan pimpinan, tanda tangan digital, nama instruktur penilai |
| Konfigurasi belajar | Ambang kelulusan, leaderboard aktif/nonaktif, skenario tambahan milik lembaga |

**Aturan lisensi (prototipe)**

- Peserta baru tidak bisa didaftarkan bila kuota kursi habis; Admin Lembaga melihat sisa kursi.
- Lisensi berakhir: peserta masih bisa login dan mengunduh piagam, tetapi tidak bisa memulai misi baru.
- Jalur yang tidak termasuk paket tidak tampil di pilihan jalur.
- Pustaka misi baku dari Super Admin dipakai semua lembaga; lembaga hanya bisa menambah skenario sendiri, tidak mengubah misi baku.

## 7. Jalur Pembelajaran dan Katalog Misi

Peserta memilih satu dari tiga jalur: IPA saja (9 misi), Distribusi saja (7 misi), atau Terpadu IPA sampai Distribusi (16 misi). Di setiap jalur misi tersusun dari paling mudah sampai paling sulit dalam lima tingkat, dan setiap jalur ditutup satu Misi Kelulusan.

&#91;embedded content: jalur belajar · 3 jalur, 5 tingkat kesulitan\]

Jalur IPA dan Distribusi melompat dari gangguan tunggal langsung ke ujian; hanya jalur Terpadu yang punya tingkat gangguan berantai hulu ke hilir (TRP-01).

**Lima tingkat kesulitan**

1. **Pengenalan (Mudah):** mengenal layar HMI dan titik kontrol; tanpa gangguan.
2. **Operasi normal (Mudah–Sedang):** menjalankan unit sampai parameter stabil di rentang normal.
3. **Gangguan tunggal (Sulit):** satu gangguan muncul; peserta harus mengenali alarm dan bertindak sesuai SOP.
4. **Gangguan berantai (Sangat sulit):** dua gangguan beruntun atau dampak hulu ke hilir.
5. **Misi Kelulusan (Ujian):** gangguan berantai dengan batas waktu dan tanpa petunjuk.

**Katalog misi baku**

| Kode | Nama misi | Tingkat | Yang dilatih | Jalur |
| --- | --- | --- | --- | --- |
| IPA-01 | Kenali Ruang Kendali IPA | 1 Mudah | Membuka narasi semua titik kontrol IPA, membaca nilai proses | IPA, Terpadu |
| IPA-02 | Menyalakan Intake | 2 Mudah | Start pompa intake, mencapai debit target air baku | IPA, Terpadu |
| IPA-03 | Dosis Koagulan Kondisi Normal | 2 Sedang | Mengatur dosis koagulan dan pengadukan sampai kekeruhan air olahan < 3 NTU | IPA, Terpadu |
| IPA-04 | Jaga Filter, Lakukan Backwash | 2 Sedang | Membaca kenaikan *headloss*, menjalankan backwash tanpa mengganggu produksi | IPA, Terpadu |
| IPA-05 | Klorinasi Tepat | 2 Sedang | Mengatur dosis klor sampai sisa klor 0,2–0,5 mg/L | IPA, Terpadu |
| IPA-06 | Gangguan: Lonjakan Kekeruhan Air Baku | 3 Sulit | Menaikkan dosis koagulan, menurunkan debit bila perlu | IPA, Terpadu |
| IPA-07 | Gangguan: Pompa Trip | 3 Sulit | Mengalihkan ke pompa cadangan, reset pompa setelah penyebab ditangani | IPA, Terpadu |
| IPA-08 | Gangguan: Dosis Klor Tidak Sesuai | 3 Sulit | Mengoreksi dosis klor, memantau sisa klor di reservoir | IPA, Terpadu |
| IPA-09 | Misi Kelulusan IPA | 5 Ujian | Lonjakan kekeruhan disusul pompa trip, tanpa petunjuk, batas waktu | IPA |
| DST-01 | Kenali Jaringan Distribusi | 1 Mudah | Membuka narasi reservoir, pompa distribusi, valve zona, PRV, titik pantau tekanan | Distribusi, Terpadu |
| DST-02 | Pompa Distribusi dan Level Reservoir | 2 Mudah | Menjaga level reservoir sambil memenuhi kebutuhan zona | Distribusi, Terpadu |
| DST-03 | Atur Tekanan Jam Puncak | 2 Sedang | Mengatur pompa dan PRV agar tekanan zona tetap di rentang layanan | Distribusi, Terpadu |
| DST-04 | Sisa Klor di Ujung Jaringan | 2 Sedang | Memantau sisa klor di titik terjauh dan mengoreksinya | Distribusi, Terpadu |
| DST-05 | Gangguan: Kebocoran Pipa | 3 Sulit | Menemukan ruas bocor dari pola tekanan dan debit, menutup valve isolasi | Distribusi, Terpadu |
| DST-06 | Gangguan: Tekanan Jaringan Drop | 3 Sulit | Mencari penyebab (pompa, valve, kebutuhan), memulihkan tekanan | Distribusi, Terpadu |
| DST-07 | Misi Kelulusan Distribusi | 5 Ujian | Kebocoran saat jam puncak dengan level reservoir rendah | Distribusi |
| TRP-01 | Hulu ke Hilir | 4 Sangat sulit | Kekeruhan tinggi menurunkan produksi IPA, reservoir turun, tekanan distribusi drop | Terpadu |
| TRP-02 | Misi Kelulusan Terpadu | 5 Ujian | Gangguan IPA dan distribusi beruntun dalam satu sesi | Terpadu |

Jalur Terpadu memuat IPA-01 s.d. IPA-08, DST-01 s.d. DST-06, TRP-01, dan TRP-02, total 16 misi. IPA-09 dan DST-07 tidak termasuk karena keduanya Misi Kelulusan khusus jalur IPA dan Distribusi. Misi IPA atau Distribusi yang sudah lulus di jalur lain dihitung otomatis bila peserta pindah ke Terpadu. Lima gangguan utama Misi 02 tercakup di IPA-06, IPA-07, IPA-08, DST-05, dan DST-06.

**Aturan urutan.** Misi berikutnya terbuka setelah misi sebelumnya lulus (minimal 1 bintang). Instruktur dapat membuka kunci misi untuk peserta tertentu. Setiap misi diawali modul materi singkat dan kuis 5 soal; kuis ≥ 60 membuka simulator (Misi 04).

## 8. Gamifikasi: Skor, Bintang, XP, Level, Lencana

Setiap misi menghasilkan skor 0–100 dari empat komponen yang diukur otomatis dari log tindakan dan log alarm. Skor menentukan bintang; bintang menentukan kelulusan misi; XP dan lencana memberi motivasi jangka panjang.

**Komponen skor misi**

| Komponen | Bobot | Cara hitung |
| --- | --- | --- |
| Ketepatan tindakan | 40% | Tindakan benar sesuai SOP skenario ÷ tindakan yang diharapkan; tindakan salah mengurangi poin |
| Waktu respons | 25% | Waktu dari alarm muncul sampai tindakan benar pertama, dibanding waktu target skenario |
| Stabilitas parameter | 20% | Persentase waktu misi saat parameter kunci (kekeruhan, pH, sisa klor, tekanan, level) berada di rentang normal |
| Penanganan alarm | 15% | Alarm diakui, penyebab ditangani, alarm clear; alarm yang dibiarkan atau di-clear tanpa perbaikan mengurangi poin |

**Pengurang skor**

- Tindakan tidak aman (misalnya mematikan semua pompa distribusi, dosis klor jauh di atas batas): −15 poin per kejadian dan dicatat sebagai temuan di umpan balik.
- Memakai petunjuk (*hint*): −5 poin per petunjuk. Membuka narasi titik kontrol tidak mengurangi skor.
- Waktu habis pada Misi Kelulusan: misi dinilai gagal.

**Bintang dan kelulusan misi**

| Skor | Hasil |
| --- | --- |
| < 70 | Belum lulus, boleh mengulang tanpa batas |
| 70–84 | 1 bintang, lulus |
| 85–94 | 2 bintang |
| ≥ 95 | 3 bintang |

Misi Kelulusan memakai ambang lebih tinggi: skor ≥ 80. Yang dihitung adalah skor terbaik; semua percobaan tetap tersimpan untuk instruktur.

**XP dan level operator**

XP = skor × pengali tingkat (Mudah 1; Sedang 1,5; Sulit 2; Sangat sulit 2,5; Ujian 3), hanya untuk skor terbaik baru. Kuis materi memberi XP setara skor kuis. Level ditampilkan di header dan dashboard.

| Level | XP kumulatif |
| --- | --- |
| Operator Magang | 0 |
| Operator Muda | 400 |
| Operator Madya | 1.200 |
| Operator Utama | 2.500 |
| Operator Ahli | 3.500 |

Hitungan kasar: 16 misi Terpadu dengan skor rata-rata 90 plus kuis rata-rata 80 menghasilkan sekitar 3.700 XP, sehingga Operator Ahli tercapai menjelang akhir jalur Terpadu. Jalur IPA atau Distribusi saja berakhir di sekitar Operator Madya (±2.100 XP untuk IPA). Ambang ini disetel ulang setelah uji coba.

**Lencana**

| Lencana | Syarat |
| --- | --- |
| Penjelajah Titik Kontrol | Membuka narasi semua titik kontrol di satu jalur |
| Respons Kilat | Tindakan benar pertama < 50% waktu target pada misi gangguan |
| Tanpa Alarm Terlewat | Menyelesaikan misi gangguan dengan semua alarm diakui dan clear |
| Penjaga Mutu Air | Kekeruhan dan sisa klor di rentang normal sepanjang misi IPA |
| Penjaga Tekanan | Tekanan semua zona di rentang layanan sepanjang misi distribusi |
| Tiga Bintang IPA / Distribusi | Semua misi di jalur itu 3 bintang |
| Hulu ke Hilir | Lulus TRP-01 |
| Lulus Tanpa Petunjuk | Lulus jalur tanpa memakai petunjuk sama sekali |

**Papan peringkat.** Peringkat XP per kelompok dan per lembaga, mingguan dan sepanjang waktu. Admin Lembaga dapat menonaktifkannya. Peserta hanya melihat peringkat di lembaganya sendiri.

## 9. Simulator SCADA: Titik Kontrol dan Narasi Pop-up

Layar simulator menampilkan diagram proses intake → koagulasi → flokulasi → sedimentasi → filtrasi → desinfeksi → reservoir → jaringan distribusi (Misi 05). Setiap titik kontrol punya ikon "i" yang membuka narasi pop-up; narasi bisa dibuka kapan saja, termasuk saat misi berjalan, tanpa mengurangi skor.

**Tata letak layar simulator**

- **Header:** logo dan nama lembaga, nama misi, timer, skor sementara, tombol Petunjuk dan Selesai.
- **Panel proses (tengah):** diagram HMI dengan nilai proses langsung; pada jalur IPA hanya bagian IPA yang aktif, pada Distribusi dimulai dari reservoir, pada Terpadu semuanya.
- **Panel kendali (kanan):** kontrol titik yang sedang dipilih (start/stop pompa, setpoint dosis, buka/tutup valve, setpoint PRV).
- **Panel alarm (bawah):** banner alarm terbaru dan daftar alarm (bagian 10).
- **Panel tren (lipat):** grafik 10 menit terakhir parameter kunci.

**Titik kontrol**

| Titik kontrol | Nilai yang dipantau | Kontrol peserta | Gangguan terkait |
| --- | --- | --- | --- |
| Intake dan pompa air baku | Debit air baku, kekeruhan air baku, status pompa | Start/Stop pompa 1–2, pilih pompa duty/standby | Pompa trip, lonjakan kekeruhan |
| Koagulasi (pembubuhan + pengaduk cepat) | Dosis koagulan, pH | Setpoint dosis koagulan, dosis penyesuai pH | Lonjakan kekeruhan |
| Flokulasi | Status pengaduk lambat | On/Off pengaduk, kecepatan | Kualitas flok turun |
| Sedimentasi | Kekeruhan keluar bak, level lumpur | Buang lumpur (*blowdown*) | Kekeruhan lolos ke filter |
| Filtrasi | Kekeruhan air olahan, *headloss* filter | Mulai backwash per filter | Filter jenuh |
| Desinfeksi | Dosis klor, sisa klor | Setpoint dosis klor | Dosis klor tidak sesuai |
| Reservoir | Level reservoir, sisa klor | Valve masuk/keluar | Level rendah |
| Pompa distribusi | Debit, tekanan keluar, status pompa | Start/Stop, jumlah pompa jalan | Pompa trip, tekanan drop |
| Valve zona dan PRV | Posisi valve, setpoint PRV | Buka/tutup valve isolasi, setpoint PRV | Kebocoran, tekanan drop |
| Titik pantau jaringan | Tekanan, debit zona, sisa klor ujung | Hanya pantau | Kebocoran, sisa klor rendah |

**Rentang normal awal.** Kekeruhan air olahan < 3 NTU, pH 6,5–8,5, sisa klor bebas 0,2–0,5 mg/L, sesuai Permenkes No. 2 Tahun 2023 ([sumber](https://repository.upnjatim.ac.id/49237/3/22034010005.-bab2.pdf.pdf), [sumber](https://eprints.poltekkesjogja.ac.id/23934/3/2026_P07133222011_chapter1.pdf)). Rentang tekanan layanan, level reservoir, dan *headloss* filter ditetapkan per skenario dan divalidasi Kepala Bagian Produksi & Distribusi (Misi 02).

**Isi narasi pop-up (per titik kontrol)**

1. **Apa ini:** nama dan fungsi unit dalam 2–3 kalimat, dengan gambar skematik.
2. **Yang dipantau:** parameter, satuan, rentang normal, dan nilai saat ini.
3. **Yang bisa dikendalikan:** kontrol yang tersedia dan efeknya.
4. **Dampak ke hilir:** apa yang terjadi di unit berikutnya bila titik ini bermasalah (misalnya koagulasi kurang → kekeruhan lolos ke filter → filter cepat jenuh).
5. **Gangguan umum dan SOP singkat:** tanda-tanda, langkah penanganan, dan kesalahan yang sering terjadi.
6. **Pelajari lebih lanjut:** tautan ke modul materi terkait.

**Perilaku narasi**

- Muncul saat ikon "i" diklik, atau otomatis sekali saat titik itu pertama kali dibuka di misi tingkat Pengenalan.
- Arahkan kursor ke titik kontrol: *tooltip* singkat nama + nilai saat ini.
- Saat alarm aktif, narasi titik terkait menampilkan bagian "Gangguan umum" lebih dulu.
- Narasi baku disusun Super Admin; Admin Lembaga dan Instruktur dapat menambah catatan lokal (misalnya SOP lembaga) tanpa mengubah narasi baku.
- Setiap narasi yang dibuka dicatat untuk lencana Penjelajah Titik Kontrol.

**Narasi misi.** Selain narasi titik kontrol, setiap misi punya briefing (situasi, tujuan, batas waktu, kriteria lulus) dan debriefing di layar hasil, disampaikan oleh tokoh mentor "operator senior" agar alurnya terasa seperti cerita.

## 10. Sistem Alarm

Alarm muncul saat parameter keluar rentang atau peralatan gagal, dan hilang dengan dua cara: otomatis clear setelah tindakan yang benar memulihkan kondisi, atau di-clear manual oleh peserta setelah kondisi pulih. Alarm tidak bisa di-clear selama penyebabnya masih ada; ini inti pembelajarannya.

**Tampilan alarm**

- Banner di atas panel alarm menampilkan alarm terbaru dengan prioritas tertinggi.
- Daftar alarm: waktu, prioritas, titik kontrol, pesan, status, tombol Akui dan Clear.
- Simbol titik kontrol di diagram berkedip sesuai warna prioritas, dan menampilkan ikon bentuk (segitiga, lingkaran) agar tidak bergantung pada warna saja.
- Bunyi alarm berhenti setelah diakui; peserta dapat mematikan suara di pengaturan.
- Klik alarm → panel kendali melompat ke titik kontrol terkait, dengan tautan ke narasinya.

**Prioritas**

| Prioritas | Arti | Contoh |
| --- | --- | --- |
| Kritis | Mutu air atau pasokan langsung terancam | Sisa klor < 0,2 mg/L di reservoir, pompa distribusi trip |
| Tinggi | Akan menjadi kritis bila tidak ditangani | Kekeruhan air olahan ≥ 3 NTU, tekanan zona di bawah batas |
| Sedang | Perlu perhatian dalam waktu wajar | *Headloss* filter tinggi, level reservoir rendah |
| Info | Pemberitahuan, tanpa tindakan wajib | Backwash selesai, pompa cadangan berjalan |

**Status alarm**

| Status | Kondisi | Yang bisa dilakukan peserta |
| --- | --- | --- |
| Aktif, belum diakui | Kondisi abnormal, belum dilihat | Akui |
| Aktif, diakui | Kondisi abnormal, peserta sedang menangani | Bertindak di titik kontrol; Clear ditolak |
| Pulih, belum di-clear | Kondisi sudah normal kembali | Clear manual, atau tunggu clear otomatis |
| Clear | Alarm selesai, pindah ke riwayat | – |

**Aturan clear**

1. **Clear otomatis:** bila parameter kembali ke rentang normal (dengan *deadband*, misalnya kekeruhan ≤ 2,7 NTU untuk alarm 3 NTU) dan bertahan 10 detik waktu simulasi, alarm berpindah ke Clear dengan catatan "pulih otomatis setelah tindakan: \<tindakan peserta>".
2. **Clear manual:** tombol Clear aktif hanya bila kondisi sudah pulih. Bila ditekan saat kondisi masih abnormal, sistem menolak dengan pesan "Penyebab belum ditangani" dan mencatatnya sebagai kesalahan penanganan alarm.
3. **Alarm terkunci (*latched*):** alarm peralatan seperti pompa trip tidak clear otomatis. Peserta harus menangani penyebab, lalu Reset pompa, baru Clear. Ini melatih urutan SOP.
4. **Mode tanpa tindakan:** bila kondisi pulih sendiri tanpa tindakan peserta (misalnya gangguan sementara), alarm tetap clear otomatis tetapi tidak menambah skor.

**Alarm per gangguan utama**

| Gangguan | Alarm yang muncul | Tindakan yang benar | Cara clear |
| --- | --- | --- | --- |
| Lonjakan kekeruhan air baku | Kekeruhan air baku tinggi (Sedang), lalu kekeruhan air olahan ≥ 3 NTU (Tinggi) | Naikkan dosis koagulan; turunkan debit intake bila perlu; backwash filter jenuh | Otomatis saat kekeruhan air olahan normal |
| Pompa trip | Pompa intake/distribusi trip (Kritis) | Jalankan pompa cadangan; periksa penyebab; Reset pompa | Terkunci: Reset lalu Clear manual |
| Dosis klor tidak sesuai | Sisa klor rendah atau tinggi (Kritis/Tinggi) | Koreksi setpoint dosis klor; pantau sisa klor reservoir | Otomatis saat sisa klor 0,2–0,5 mg/L |
| Kebocoran pipa | Tekanan zona turun + debit zona naik tidak wajar (Tinggi) | Identifikasi ruas, tutup valve isolasi terdekat | Otomatis saat tekanan pulih setelah isolasi |
| Tekanan jaringan drop | Tekanan zona di bawah batas (Tinggi) | Tambah pompa jalan atau koreksi setpoint PRV/valve | Otomatis saat tekanan di rentang layanan |

**Pencatatan.** Setiap kejadian alarm menyimpan waktu muncul, waktu diakui, tindakan yang diambil, waktu clear, dan cara clear. Data ini dipakai untuk komponen skor "Penanganan alarm" dan "Waktu respons", serta ditampilkan di putar ulang (*replay*) untuk instruktur.

## 11. Dashboard Capaian Belajar (Peserta)

Dashboard peserta menjawab tiga pertanyaan: sejauh mana saya di jalur ini, di mana kelemahan saya, dan apa yang harus saya kerjakan berikutnya. Dashboard ini sekaligus Beranda Peserta (layar 2 Misi 05).

| Komponen | Isi |
| --- | --- |
| Kartu profil | Nama, lembaga, kelompok, jalur, level operator, XP dan sisa XP ke level berikutnya |
| Peta misi | Misi tersusun dari mudah ke sulit; status terkunci / terbuka / lulus dengan 1–3 bintang; tombol Lanjutkan misi berikutnya |
| Progres jalur | Persentase misi lulus, jumlah bintang dari maksimal, syarat piagam yang sudah dan belum terpenuhi |
| Peta kompetensi | Skor rata-rata per kompetensi: Operasi normal IPA, Mutu air (kekeruhan, klor), Respons gangguan, Penanganan alarm, Hidrolika distribusi |
| Tren skor | Grafik skor terbaik per misi dan tren percobaan |
| Riwayat percobaan | Tanggal, misi, skor, bintang, durasi; tautan ke layar hasil dan umpan balik |
| Lencana | Lencana yang sudah didapat dan yang belum (abu-abu, dengan syaratnya) |
| Peringkat | Posisi di kelompok dan lembaga (bila diaktifkan Admin Lembaga) |
| Pre-test vs post-test | Nilai awal dan nilai terakhir, ditampilkan setelah post-test |
| Status piagam | Belum memenuhi / menunggu persetujuan instruktur / terbit, dengan tombol Unduh |

**Saran belajar otomatis.** Dari komponen skor terendah, dashboard menyarankan satu tindakan, misalnya "Waktu respons Anda di misi gangguan rata-rata 2× target; ulangi IPA-07" atau "Buka narasi Desinfeksi sebelum mencoba IPA-08".

## 12. Dashboard Evaluasi Lembaga dan Dashboard Instruktur

Dashboard evaluasi lembaga menunjukkan kepada pembeli apakah pelatihan berhasil dan apakah lisensinya terpakai. Indikatornya langsung memetakan target T1–T4; nama dan logo lembaga tampil di header dan di setiap ekspor.

### Dashboard evaluasi lembaga (Pimpinan Lembaga, Admin Lembaga)

| Indikator | Definisi | Kaitan target |
| --- | --- | --- |
| Peningkatan kompetensi | Rata-rata (post-test − pre-test) ÷ pre-test, per angkatan | T1 (≥ 25%) |
| Penguasaan 5 gangguan utama | % peserta yang lulus IPA-06, IPA-07, IPA-08, DST-05, DST-06 | T2 (≥ 80%) |
| Waktu menuju lulus | Median hari dari mulai jalur sampai piagam terbit | T3 |
| Tingkat kelulusan | Piagam terbit ÷ peserta aktif, per jalur dan angkatan | T4 |
| Peserta aktif | Peserta yang login dalam 14 hari terakhir | – |
| Rata-rata skor dan bintang | Per misi, per jalur, per kelompok | – |
| Misi paling sulit | 5 misi dengan tingkat gagal percobaan pertama tertinggi | Bahan perbaikan materi |
| Kesalahan paling sering | Tindakan salah dan alarm salah tangani terbanyak | Bahan perbaikan SOP lembaga |
| Perbandingan kelompok | Skor dan kelulusan antar-kelompok/angkatan dan antar-instruktur | – |
| Pemakaian lisensi | Kursi terpakai / kuota, sisa masa lisensi, jam simulasi total | Nilai investasi |

**Filter:** periode, jalur, kelompok/angkatan, instruktur. **Ekspor:** PDF ringkasan eksekutif berkop lembaga dan Excel data rinci per peserta (Misi 04, prioritas B).

### Dashboard instruktur

- Daftar peserta binaan: misi saat ini, skor terakhir, bintang, hari sejak aktivitas terakhir, penanda "tertinggal" bila tidak lulus misi yang sama 3 kali.
- Matriks peserta × misi berwarna sesuai bintang.
- Putar ulang sesi: urutan tindakan, alarm, dan grafik parameter dengan garis waktu.
- Aksi: tugaskan misi atau skenario, buka kunci misi, beri catatan, setujui kelulusan.

### Dashboard Super Admin

- Daftar lembaga: status lisensi, kursi terpakai, peserta aktif, piagam terbit.
- Peringatan lisensi akan berakhir (30 hari) dan kuota hampir habis (≥ 90%).

## 13. Piagam Kelulusan

Piagam terbit otomatis dalam PDF begitu peserta memenuhi syarat jalurnya dan instruktur menyetujui. Piagam memuat nama lembaga pembeli dan bisa diverifikasi lewat kode QR, tetapi bukan sertifikat kompetensi resmi.

**Syarat kelulusan per jalur**

1. Semua misi wajib di jalur lulus (minimal 1 bintang).
2. Misi Kelulusan jalur (IPA-09, DST-07, atau TRP-02) dengan skor ≥ 80.
3. Post-test ≥ 70.
4. Persetujuan instruktur (dapat dinonaktifkan Admin Lembaga agar piagam terbit langsung).

**Predikat**

| Rata-rata skor terbaik semua misi jalur | Predikat |
| --- | --- |
| 70–84 | Lulus |
| 85–94 | Lulus dengan Baik |
| ≥ 95 | Lulus dengan Pujian |

**Isi piagam**

- Logo dan nama lembaga pembeli; teks kecil "Simulator: SimSCADA-Air".
- Judul "Piagam Kelulusan" dan nama jalur: Operator IPA, Operator Distribusi, atau Operator Air Minum Terpadu (IPA–Distribusi).
- Nama peserta, kelompok/angkatan, tanggal lulus, predikat, level operator, jumlah bintang.
- Nomor piagam unik (format usulan: `SSA/<kode lembaga>/<tahun>/<nomor urut>`).
- Tanda tangan digital Pimpinan Lembaga dan instruktur penilai.
- Kode QR menuju halaman verifikasi publik.
- Catatan kaki: "Piagam ini menyatakan penyelesaian pelatihan berbasis simulator dan bukan sertifikat kompetensi resmi."

**Halaman verifikasi publik.** Memasukkan nomor piagam atau memindai QR menampilkan nama peserta, lembaga, jalur, tanggal, predikat, dan status (sah / dicabut). Admin Lembaga dapat mencabut piagam yang salah terbit dengan alasan tercatat.

**Templat.** Satu templat baku A4 mendatar; Admin Lembaga mengatur logo, nama dan jabatan penanda tangan, serta warna aksen.

## 14. Kebutuhan Fungsional

Tiga puluh satu kebutuhan fungsional mencakup sepuluh user story Misi 04 ditambah sembilan kebutuhan baru dari tugas ini. Kolom Sumber menunjuk user story Misi 04 (US-1 sampai US-10, sesuai urutan di lembar kerja) atau poin tambahan (Baru).

| Kode | Kebutuhan | Prioritas | Sumber |
| --- | --- | --- | --- |
| FR-01 | Login dengan username dan kata sandi; sistem mengenali peran dan lembaga | W | Misi 05 layar 1 |
| FR-02 | Tombol "Masuk sebagai…" per akun demo di lingkungan prototipe | W | Baru (poin 6) |
| FR-03 | Pemisahan data per lembaga; nama dan logo lembaga tampil di header, laporan, piagam | W | Baru (poin 4) |
| FR-04 | Super Admin mengelola lembaga, paket jalur, kuota kursi, masa lisensi | P | Baru (poin 4) |
| FR-05 | Admin Lembaga mengelola akun peserta, instruktur, dan kelompok | P | US-8 |
| FR-06 | Peserta memilih jalur IPA, Distribusi, atau Terpadu sesuai paket lembaga | W | Baru (poin 5) |
| FR-07 | Peta misi dari mudah ke sulit dengan kunci berurutan | W | Baru (poin 1) |
| FR-08 | Modul materi singkat dan kuis sebelum misi | P | US-6 |
| FR-09 | Pre-test saat mulai jalur dan post-test sebelum piagam | W | Target T1 |
| FR-10 | Simulasi proses IPA intake sampai reservoir secara real-time | W | US-1 |
| FR-11 | Simulasi jaringan distribusi: tekanan, debit, kebocoran | W | US-5 (dinaikkan dari P) |
| FR-12 | Mode Terpadu: keluaran IPA memengaruhi reservoir dan distribusi | W | Baru (poin 5) |
| FR-13 | Pemicu gangguan sesuai skenario: 5 gangguan utama | W | US-2 |
| FR-14 | Kontrol peserta: start/stop pompa, setpoint dosis, valve, PRV, backwash, reset | W | Misi 05 layar 3 |
| FR-15 | Alarm dengan prioritas, akui, clear manual bersyarat, clear otomatis, alarm terkunci | W | Baru (poin 8) |
| FR-16 | Narasi pop-up untuk setiap titik kontrol | W | Baru (poin 9) |
| FR-17 | Briefing dan debriefing misi | P | Baru (poin 9) |
| FR-18 | Petunjuk (hint) berbayar skor | B | Baru (poin 1) |
| FR-19 | Penilaian otomatis 4 komponen, bintang, dan umpan balik tindakan benar/salah | W | US-3 |
| FR-20 | XP, level operator, dan lencana | W | Baru (poin 1) |
| FR-21 | Papan peringkat per kelompok dan lembaga, bisa dinonaktifkan | B | Baru (poin 1) |
| FR-22 | Dashboard capaian peserta | W | Baru (poin 2) |
| FR-23 | Instruktur membuat, mengatur, dan menugaskan skenario | W | US-4 |
| FR-24 | Dashboard instruktur: progres, nilai, matriks peserta × misi | P | US-7 |
| FR-25 | Putar ulang sesi simulasi | B | US-7 |
| FR-26 | Dashboard evaluasi lembaga dengan indikator T1–T4 dan pemakaian lisensi | W | Baru (poin 4) |
| FR-27 | Ekspor laporan PDF/Excel berkop lembaga | B | US-9 |
| FR-28 | Piagam kelulusan PDF dengan predikat, tanda tangan digital, nomor, QR | W | Baru (poin 3) |
| FR-29 | Halaman verifikasi piagam publik dan pencabutan piagam | P | Baru (poin 3) |
| FR-30 | Catatan SOP lokal lembaga pada narasi titik kontrol | B | Baru (poin 9) |
| FR-31 | Mode tim: operator ruang kontrol dan operator lapangan | N | US-10 |

## 15. Kebutuhan Non-Fungsional

Yang paling menentukan adalah keamanan isolasi (tidak ada jalur ke kendali nyata) dan respons simulasi di bawah 1 detik, karena tanpa keduanya latihan tidak aman atau tidak terasa nyata.

| Kode | Kategori | Kebutuhan |
| --- | --- | --- |
| NFR-01 | Keamanan isolasi | Server simulator tidak punya koneksi jaringan ke SCADA/PLC instalasi nyata; tidak ada driver protokol industri (Modbus, OPC UA) di aplikasi |
| NFR-02 | Kinerja | Langkah simulasi 1 detik; perubahan nilai dan alarm tampil di layar ≤ 1 detik setelah terjadi |
| NFR-03 | Kapasitas prototipe | 30 sesi simulasi bersamaan per server tanpa penurunan kinerja |
| NFR-04 | Platform | Berjalan di browser Chrome/Edge versi terbaru di PC/laptop ruang diklat, resolusi minimal 1366×768, tanpa instalasi |
| NFR-05 | Isolasi data lembaga | Setiap kueri disaring per lembaga di sisi server; pengguna satu lembaga tidak dapat membaca data lembaga lain |
| NFR-06 | Keamanan akun | HTTPS, kata sandi di-hash, kendali akses berbasis peran, sesi berakhir setelah 30 menit tidak aktif |
| NFR-07 | Jejak audit | Perubahan pengguna, skenario, lisensi, dan pencabutan piagam tercatat dengan pelaku dan waktu |
| NFR-08 | Ketersediaan data | Simulasi yang terputus dapat dilanjutkan; log tindakan disimpan per langkah, bukan di akhir misi |
| NFR-09 | Aksesibilitas | Status alarm tidak hanya ditandai warna; kontras teks memadai; suara alarm dapat dimatikan |
| NFR-10 | Bahasa | Antarmuka, narasi, dan piagam berbahasa Indonesia; istilah teknis mengikuti istilah PDAM |
| NFR-11 | Pencadangan | Basis data dicadangkan harian, disimpan 14 hari |
| NFR-12 | Keterpeliharaan | Skenario, misi, narasi, dan ambang alarm adalah data yang bisa diubah tanpa mengubah kode |
| NFR-13 | Privasi | Data pribadi peserta minimum (nama, email, lembaga, kelompok); mengikuti UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi |

## 16. Arsitektur dan Model Data

Arsitektur mengikuti peta komponen Misi 05, ditambah lapisan lembaga (tenant), gamifikasi, dan piagam di backend, serta logika alarm di mesin simulasi.

&#91;embedded content: arsitektur SimSCADA-Air · 4 komponen server, 5 peran\]

Pengguna mengakses frontend lewat HTTPS; frontend menerima nilai proses dan alarm dari mesin simulasi secara real-time, sedangkan mesin simulasi mengirim skenario dan log tindakan ke backend untuk dinilai dan disimpan.

**Usulan teknologi prototipe**

| Lapisan | Usulan | Alasan |
| --- | --- | --- |
| Frontend | React + diagram HMI berbasis SVG, WebSocket | Diagram proses interaktif dan pembaruan nilai real-time di browser |
| Backend API | Node.js (NestJS) atau Laravel | Sesuaikan dengan kemampuan pengembang kelompok |
| Mesin simulasi | Proses terpisah dengan langkah 1 detik; model keseimbangan massa sederhana untuk IPA dan model hidrolika sederhana untuk distribusi | Cukup realistis untuk latihan, mudah disetel |
| Database | PostgreSQL (atau MySQL, sesuai Misi 05) | Relasional, mendukung penyaringan per lembaga |
| PDF | Pembuat PDF di server dari templat HTML | Piagam dan laporan berkop lembaga |
| Hosting | Kontainer Docker di server lokal atau VPS | Mudah dipasang ulang di lembaga pembeli |

**Model data inti**

| Entitas | Atribut utama | Relasi |
| --- | --- | --- |
| Lembaga | nama, singkatan, logo, kode, penanda tangan | punya banyak Lisensi, Pengguna, Kelompok |
| Lisensi | paket jalur, kuota kursi, mulai, berakhir | milik satu Lembaga |
| Pengguna | nama, email, peran, status | milik satu Lembaga; peserta masuk satu Kelompok |
| Kelompok | nama angkatan, instruktur, jalur | milik satu Lembaga |
| Jalur | IPA / Distribusi / Terpadu | berisi urutan Misi |
| Misi | kode, nama, tingkat, kriteria lulus, batas waktu | memakai satu Skenario; urutan per Jalur |
| Skenario | kondisi awal, gangguan, waktu muncul, tindakan benar | dipakai Misi; bisa milik Lembaga |
| Titik kontrol | nama, unit proses, parameter, rentang normal | punya Narasi dan Definisi alarm |
| Narasi | enam bagian isi, catatan lokal lembaga | milik Titik kontrol |
| Definisi alarm | parameter, ambang, deadband, prioritas, terkunci ya/tidak | milik Titik kontrol |
| Sesi simulasi | peserta, misi, mulai, selesai, status | punya Log tindakan dan Log alarm |
| Log tindakan | waktu, titik kontrol, tindakan, nilai | milik Sesi |
| Log alarm | waktu muncul, diakui, clear, cara clear | milik Sesi |
| Hasil misi | skor 4 komponen, total, bintang, XP | milik Sesi |
| Lencana peserta | lencana, tanggal didapat | milik Pengguna |
| Hasil kuis | jenis (materi, pre-test, post-test), nilai | milik Pengguna |
| Piagam | nomor, jalur, predikat, tanggal, status sah/dicabut | milik Pengguna dan Lembaga |

## 17. Daftar Layar Prototipe

Prototipe terdiri dari 16 layar: lima layar sketsa Misi 05 (L1, L2, L5, L6, L10) yang diperluas, ditambah sebelas layar untuk gamifikasi, piagam, dan multi-lembaga.

| No | Layar | Peran | Isi utama | Tombol penting |
| --- | --- | --- | --- | --- |
| L1 | Login | Semua | Logo lembaga, username, kata sandi, tombol akun demo | Masuk, Masuk sebagai… |
| L2 | Beranda Peserta / Dashboard Capaian | Peserta | Profil, level, XP, peta misi, progres, lencana, status piagam | Lanjutkan misi, Buka materi |
| L3 | Pilih Jalur | Peserta | Kartu IPA, Distribusi, Terpadu dengan jumlah misi dan perkiraan durasi | Pilih jalur |
| L4 | Materi, Kuis, Briefing Misi | Peserta | Modul singkat, kuis 5 soal, briefing misi | Mulai kuis, Mulai simulasi |
| L5 | Simulator SCADA | Peserta, Instruktur | Diagram HMI, nilai proses, panel kendali, panel alarm, tren, narasi pop-up | Start/Stop, Setpoint, Valve, Reset, Akui, Clear, Petunjuk, Selesai |
| L6 | Hasil dan Umpan Balik | Peserta | Skor, komponen skor, bintang, XP, lencana baru, tindakan benar/salah, debriefing | Ulangi, Misi berikutnya, Kembali |
| L7 | Lencana dan Peringkat | Peserta | Koleksi lencana, papan peringkat | – |
| L8 | Piagam Saya | Peserta | Pratinjau piagam, syarat yang terpenuhi | Unduh PDF |
| L9 | Dashboard Instruktur | Instruktur | Daftar peserta binaan, matriks peserta × misi, penanda tertinggal | Tugaskan, Buka kunci, Setujui kelulusan |
| L10 | Kelola Skenario | Instruktur, Admin Lembaga | Daftar skenario; form jenis gangguan, waktu muncul, tingkat, peserta tujuan | Buat skenario, Simpan & tugaskan |
| L11 | Putar Ulang Sesi | Instruktur | Garis waktu tindakan, alarm, grafik parameter | Putar, Lompat ke alarm |
| L12 | Kelola Pengguna dan Kelompok | Admin Lembaga | Daftar akun, kelompok, sisa kursi lisensi | Tambah, Impor CSV, Nonaktifkan |
| L13 | Pengaturan Lembaga | Admin Lembaga | Nama, logo, penanda tangan piagam, ambang kelulusan, leaderboard | Simpan |
| L14 | Dashboard Evaluasi Lembaga | Pimpinan, Admin Lembaga | Indikator T1–T4, pemakaian lisensi, misi tersulit, perbandingan kelompok | Filter, Ekspor PDF/Excel |
| L15 | Kelola Lembaga dan Lisensi | Super Admin | Daftar lembaga, paket, kuota, masa berlaku | Tambah lembaga, Ubah lisensi |
| L16 | Verifikasi Piagam (publik) | Tanpa login | Kolom nomor piagam, hasil verifikasi | Verifikasi |

**Alur demo yang disarankan (±15 menit):** login `peserta.baru` → pilih jalur Terpadu → IPA-01 dengan narasi pop-up → `peserta.ipa` menjalankan IPA-06 (alarm kekeruhan, clear otomatis) dan IPA-07 (pompa trip, reset lalu clear manual) → layar hasil → `peserta.lulus` mengunduh piagam dan memverifikasinya di L16 → `instruktur.nusantara` memutar ulang sesi → `pimpinan.nusantara` membuka dashboard evaluasi → `admin.tirta` membuktikan data lembaga pertama tidak terlihat.

## 18. Rencana Rilis dan Kriteria Penerimaan

Prototipe akhir semester 1 memuat semua kebutuhan berprioritas W; P dan B dikerjakan bila waktu cukup, N ditunda. Uji coba terbatas dilakukan dengan peserta dan instruktur sesuai rencana pelibatan Misi 02.

1. **Fase 1 — Prototipe (akhir semester 1):** FR berprioritas W, 2 lembaga demo, 10 akun demo, minimal misi tingkat 1–3 di jalur IPA dan Distribusi, TRP-01, dan ketiga Misi Kelulusan.
2. **Fase 2 — Uji coba terbatas:** satu kelompok peserta dan instruktur; kuesioner kemudahan pakai; penyetelan ambang skor, XP, dan alarm; validasi skenario oleh Kepala Bagian Produksi & Distribusi.
3. **Fase 3 — Siap jual:** FR prioritas P dan B, templat piagam final, ekspor laporan, panduan Admin Lembaga.
4. **Fase berikutnya:** mode tim (FR-31) dan skenario tambahan.

**Kriteria penerimaan prototipe**

- [ ] Setiap akun demo dapat login dan hanya melihat menu sesuai peran (matriks akses bagian 5).
- [ ] `admin.tirta` dan `peserta.tirta` tidak dapat melihat data Balai Diklat Air Minum Nusantara.
- [ ] Nama dan logo lembaga tampil di header, dashboard evaluasi, laporan, dan piagam.
- [ ] Peserta dapat memilih jalur IPA, Distribusi, atau Terpadu, dan peta misinya sesuai katalog bagian 7.
- [ ] Misi berikutnya terkunci sampai misi sebelumnya lulus; instruktur dapat membuka kunci.
- [ ] Kelima gangguan utama dapat dipicu dan memunculkan alarm sesuai tabel bagian 10.
- [ ] Alarm kekeruhan clear otomatis setelah dosis koagulan dinaikkan dan kekeruhan kembali normal 10 detik.
- [ ] Tombol Clear ditolak selama kondisi abnormal; alarm pompa trip baru dapat di-clear setelah Reset.
- [ ] Setiap titik kontrol membuka narasi pop-up berisi enam bagian narasi.
- [ ] Layar hasil menampilkan skor 4 komponen, bintang, XP, dan daftar tindakan benar/salah.
- [ ] Dashboard capaian menampilkan level, XP, progres jalur, lencana, dan status piagam.
- [ ] Dashboard evaluasi lembaga menampilkan indikator T1–T4 dan pemakaian lisensi.
- [ ] Piagam PDF terbit untuk `peserta.lulus` dengan nomor unik dan QR yang lolos verifikasi di L16.
- [ ] Simulator tidak memiliki konfigurasi koneksi ke perangkat lapangan (NFR-01).

## 19. Risiko, Asumsi, dan Pertanyaan Terbuka

Risiko terbesar adalah model proses yang terlalu sederhana sehingga instruktur tidak percaya hasil penilaiannya; mitigasinya adalah validasi skenario oleh praktisi sejak Fase 1.

| Risiko | Dampak | Mitigasi |
| --- | --- | --- |
| Model proses tidak realistis | Instruktur menolak penilaian otomatis | Model sederhana tetapi divalidasi praktisi; ambang dan respons proses dapat disetel tanpa ubah kode |
| Cakupan prototipe terlalu luas untuk satu semester | Tenggat terlewat | Kerjakan prioritas W dulu; misi tambahan berupa data, bukan fitur baru |
| Gamifikasi mendorong "mengejar poin" | Peserta menghafal urutan, bukan memahami | Variasi waktu dan besar gangguan antar-percobaan; skor stabilitas dan alarm, bukan hanya kecepatan |
| Papan peringkat menurunkan motivasi peserta peringkat bawah | Peserta berhenti | Bisa dinonaktifkan; tampilkan kemajuan pribadi lebih dulu |
| Piagam disalahartikan sebagai sertifikat resmi | Masalah hukum dan reputasi | Catatan kaki eksplisit; halaman verifikasi menyebut jenis piagam |
| Kebocoran data antar-lembaga | Kehilangan kepercayaan pembeli | Penyaringan per lembaga di server; uji isolasi di kriteria penerimaan |

**Asumsi**

- Lembaga pembeli menyediakan PC/laptop dan jaringan di ruang diklat.
- Rentang mutu air memakai Permenkes No. 2 Tahun 2023; rentang hidrolika ditetapkan per skenario.
- Satu peserta menempuh satu jalur aktif dalam satu waktu.
- Nama lembaga di akun demo bersifat fiktif.

**Pertanyaan terbuka untuk kelompok**

- Bobot skor (40/25/20/15) dan ambang bintang perlu disepakati atau divalidasi praktisi?
- Persetujuan instruktur untuk piagam wajib atau opsional secara baku?
- Model harga lisensi: per kursi per tahun, per paket jalur, atau kombinasi?
- Teknologi yang dipilih untuk prototipe (lihat usulan di bagian 16) sesuai kemampuan tim pengembang?
- Perlu kuesioner kepuasan sebagai bagian dari laporan lembaga?

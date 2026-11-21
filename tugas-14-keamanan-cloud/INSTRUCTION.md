# INSTRUCTION.md — Tugas 14: Keamanan Cloud

**Tujuan:** Memindai seluruh riwayat repository dengan Gitleaks, mempraktikkan GitHub Actions Secrets tanpa membocorkan nilainya, serta menganalisis Shared Responsibility Model dan IAM Least Privilege.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Koordinasi pemindaian Gitleaks, verifikasi command dan cakupan riwayat commit, serta analisis hasil scan. |
| Farrellino Ulung Satya Amando | Menyiapkan GitHub Secret dummy dan menguji penggunaan secret sebagai environment variable pada workflow. |
| Haniel Juanta Sembiring | Melengkapi dan menguji workflow GitHub Actions pada `.github/workflows/` di root repository; memastikan nilai secret tidak dicetak. |
| Rohmatul Choirul Anam | Analisis Shared Responsibility, `.gitignore`, `.env.example`, IAM Least Privilege, dan dokumentasi bukti. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota memasang/menjalankan Gitleaks secara lokal dan memindai riwayat repository sendiri.
2. Bandingkan hasil scan. Jangan menganggap temuan otomatis sebagai kredensial aktif; klasifikasikan dan dokumentasikan dengan aman.
3. Setiap anggota membaca workflow dan menjelaskan bagaimana secret diteruskan ke proses tanpa mencetak nilainya.
4. Semua anggota ikut memeriksa hasil run GitHub Actions dan memastikan nilai secret tidak muncul di log.
5. Setiap anggota memahami mengapa secret dummy digunakan, mengapa secret asli tidak boleh dimasukkan ke repository, serta batasan masking log.

## Langkah pengerjaan

1. Pastikan Gitleaks tersedia dan jalankan perintah scan sesuai README tugas dari root repository.
2. Simpan laporan ke `tugas-14-keamanan-cloud/bukti/gitleaks-report.json`.
3. Dokumentasikan temuan, termasuk false positive atau contoh secret dummy dari latihan sebelumnya. Jangan menampilkan atau menyebarkan nilai sensitif.
4. Buat GitHub Secret bernama `DUMMY_API_KEY` dengan nilai dummy, bukan kredensial layanan asli.
5. Lengkapi workflow contoh pada `.github/workflows/tugas-14-ci-example.yml` di root repo. Perhatikan trigger `paths` sesuai instruksi tugas.
6. Jalankan workflow dan periksa log. Jangan pernah menambahkan perintah yang mencetak isi secret.
7. Ambil screenshot halaman Secrets yang hanya memperlihatkan nama secret, bukan nilainya, dan screenshot log Actions.
8. Analisis pembagian tanggung jawab penyedia cloud dan pengguna/developer dalam kebocoran access key.
9. Jelaskan peran `.gitignore`, `.env.example`, dan mengapa `.env` asli tidak boleh di-commit.
10. Jelaskan least privilege dan contoh pembatasan izin key.
11. Jelaskan mekanisme masking GitHub Actions serta keterbatasannya, sesuai instruksi README.

## Berkas submission

- `README.md`
- `JURNAL.md`
- `.gitignore`
- `.env.example` — hanya template tanpa rahasia asli.
- `bukti/gitleaks-report.json`
- Bukti screenshot GitHub Secrets dan log workflow.
- `.github/workflows/tugas-14-ci-example.yml` — berada di root repository.

## Kriteria selesai

Seluruh riwayat repository dipindai, secret dummy dipakai melalui workflow, nilai secret tidak tampil di log, bukti disimpan aman, dan semua anggota menjalankan scan serta memahami hasilnya.

## Aturan kerja wajib untuk seluruh anggota

1. Baca README tugas terkait, `HANDBOOK.md`, dan `RUBRIK-UMUM.md` sebelum mulai.
2. PIC adalah penanggung jawab koordinasi dan pemeriksaan, bukan satu-satunya orang yang mengerjakan.
3. Setiap anggota wajib melakukan praktik langsung pada laptop masing-masing jika memungkinkan. Jika keterbatasan perangkat mengharuskan praktik bergantian, setiap orang tetap harus menjalankan ulang langkah inti dan menjelaskan hasilnya.
4. Setiap anggota wajib menghasilkan kontribusi nyata yang dapat ditelusuri melalui commit GitHub atas nama sendiri. Jangan melakukan commit atas nama anggota lain.
5. Setiap anggota wajib memahami hasil kerja tiga anggota lainnya. Lakukan sesi saling menjelaskan dan tanya jawab sebelum tugas dinyatakan selesai.
6. Catat progres, kendala, percobaan yang gagal, solusi, dan pembagian kontribusi pada `JURNAL.md`.
7. Simpan bukti asli berupa screenshot terminal/browser, log, diagram, atau video pada folder `bukti/` sesuai instruksi tugas.
8. Ikuti kebijakan AI Level 2 pada repositori: AI hanya untuk brainstorming dan penyusunan kerangka. Jangan meminta AI menghasilkan kode, analisis akhir, diagram final, atau README siap salin. Catat penggunaan AI pada `JURNAL.md`.
9. Jangan mengubah skeleton atau file yang diminta tetap menjadi bukti kondisi awal kecuali README tugas secara eksplisit mengizinkan.
10. Setelah semua anggota menyetujui hasil, lakukan commit dan push bertahap. Buat tag `tugas-XX-submit` sesuai Handbook, lalu kumpulkan permalink folder pada tag tersebut ke LMS.

## Identitas anggota

| Nama | NIM |
|---|---|
| Nuevalen Refitra Alswanado | 103072430008 |
| Farrellino Ulung Satya Amando | 103072400005 |
| Haniel Juanta Sembiring | 103072400145 |
| Rohmatul Choirul Anam | 103072400024 |

## Bukti kontribusi minimum per anggota

- Minimal satu commit bermakna atas nama sendiri pada tugas ini.
- Ada hasil praktik/analisis yang jelas dan dapat ditunjukkan.
- Mampu menjelaskan bagian sendiri dan menjawab pertanyaan tentang bagian anggota lain.
- Nama, NIM, dan kontribusi dicantumkan secara jujur pada tabel kontribusi di README submission.

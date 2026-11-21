# INSTRUCTION.md — Tugas 12: Implementasi PaaS

**Tujuan:** Menjalankan aplikasi Flask secara lokal dan melakukan deployment pada PaaS free tier yang tidak meminta kartu kredit, lalu memahami pembagian tanggung jawab developer dan platform.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Audit skeleton Flask, identifikasi konfigurasi aplikasi, dan koordinasi persiapan repository untuk deployment. |
| Farrellino Ulung Satya Amando | Pengujian lokal: virtual environment, dependency, menjalankan aplikasi, endpoint utama dan `/health`. |
| Haniel Juanta Sembiring | Persiapan konfigurasi deployment berbasis dokumentasi resmi PaaS, build/start command, dan pemeriksaan log deployment. |
| Rohmatul Choirul Anam | Verifikasi akses URL publik, screenshot, tabel shared responsibility, dan analisis keterbatasan PaaS. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota membuat virtual environment sendiri, memasang dependency, dan menjalankan aplikasi secara lokal.
2. Setiap anggota menguji endpoint utama dan `/health` melalui browser atau HTTP client.
3. Setiap anggota membaca dokumentasi platform PaaS yang dipilih dan menjelaskan apa yang dikelola platform.
4. Deployment publik dapat dikoordinasikan oleh satu PIC, tetapi semua anggota harus ikut menyaksikan proses build, membaca log, menguji URL publik, dan mampu menjelaskan prosesnya.
5. Jika memungkinkan, setiap anggota melakukan deployment ulang pada akun/repo uji sendiri tanpa membuat layanan berbayar. Jangan membuat banyak service yang tidak diperlukan.
6. Gunakan hanya free tier. Jangan memasukkan kartu pembayaran atau mengaktifkan fitur berbayar.

## Langkah pengerjaan

1. Pilih Render atau PythonAnywhere sesuai README tugas dan kebijakan free tier saat pengerjaan.
2. Lengkapi skeleton Flask agar menampilkan identitas kelompok, waktu server, dan endpoint `/health`.
3. Jalankan lokal terlebih dahulu dan pastikan tidak ada error.
4. Pastikan dependency dicatat pada file yang sesuai.
5. Hubungkan repository GitHub ke PaaS dan ikuti dokumentasi resmi untuk build/start command.
6. Setelah deployment, uji URL publik dari browser dan endpoint health.
7. Catat URL aplikasi, tanggal pengujian, status, dan bukti screenshot.
8. Buat tabel perbandingan tanggung jawab developer vs platform, termasuk OS patching, runtime, web server, TLS/HTTPS, aplikasi, dan data.
9. Jelaskan kapan keterbatasan library sistem operasi membuat IaaS/container lebih tepat daripada PaaS.
10. Periksa kembali batas free tier agar tidak memicu biaya.

## Berkas submission

- `app/app.py`
- `requirements.txt` sesuai skeleton
- `README.md` — URL aktif, screenshot, tabel tanggung jawab, dan analisis.
- `JURNAL.md`
- `bukti/` — bukti aplikasi lokal dan publik.

## Kriteria selesai

Aplikasi berjalan lokal dan dapat diakses melalui URL publik, endpoint health diuji, tidak ada biaya berbayar yang diaktifkan, serta seluruh anggota dapat menjelaskan proses deployment dan shared responsibility.

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

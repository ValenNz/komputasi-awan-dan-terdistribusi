# INSTRUCTION.md — Tugas 13: SaaS & Twelve-Factor App

**Tujuan:** Mengaudit aplikasi `bad_app.py` terhadap Factor I (Codebase), Factor II (Dependencies), dan Factor III (Config), lalu membuat versi perbaikan `fixed_app.py`.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Audit Factor I — Codebase dan keterlacakan satu codebase untuk banyak deployment. |
| Farrellino Ulung Satya Amando | Audit Factor II — Dependencies, inventarisasi dependency, dan strategi penguncian versi. |
| Haniel Juanta Sembiring | Audit Factor III — Config, identifikasi nilai hardcoded, environment variable, dan konfigurasi runtime. |
| Rohmatul Choirul Anam | Integrasi perbaikan pada `fixed_app.py`, pengujian sebelum/sesudah, dan konsistensi laporan audit. |

## Praktik bersama — wajib dilakukan semua anggota

1. Semua anggota membaca `bad_app.py` dan mencatat temuan secara mandiri sebelum berdiskusi.
2. Setiap anggota menunjukkan minimal satu bukti lokasi pelanggaran dari file asli.
3. Semua anggota ikut menguji aplikasi versi awal dan versi perbaikan.
4. Semua anggota memeriksa bahwa `bad_app.py` tetap tidak diubah.
5. Setiap anggota menjelaskan tiga faktor dan alasan konfigurasi/dependency tidak boleh bergantung pada asumsi laptop developer.

## Langkah pengerjaan

1. Baca `AUDIT-TEMPLATE.md` dan `bad_app.py`.
2. Identifikasi pelanggaran Factor I, II, dan III berdasarkan bukti di source.
3. Catat setiap temuan: lokasi, risiko, prinsip yang dilanggar, dan usulan perbaikan.
4. Buat `fixed_app.py` sebagai versi perbaikan; jangan mengubah `bad_app.py`.
5. Pastikan konfigurasi sensitif dan endpoint berasal dari environment variable, bukan nilai hardcoded.
6. Buat `requirements.txt` dengan versi dependency yang terkunci sesuai environment yang diuji.
7. Hilangkan asumsi path lokal yang hanya berlaku pada laptop tertentu.
8. Jalankan versi perbaikan pada environment bersih/virtual environment dan uji bahwa aplikasi dapat berjalan dengan konfigurasi yang disediakan.
9. Isi template audit dan ringkas hasilnya di README.
10. Lakukan review silang: tiap anggota memeriksa satu faktor yang bukan tanggung jawab utamanya.

## Berkas submission

- `README.md`
- `AUDIT-TEMPLATE.md` yang sudah diisi sebagai laporan audit sesuai ketentuan repositori.
- `JURNAL.md`
- `app/bad_app.py` — tetap sebagai bukti before, jangan diubah.
- `app/fixed_app.py`
- `app/requirements.txt`
- `bukti/`

## Kriteria selesai

Tiga faktor diaudit dengan bukti spesifik, `bad_app.py` tetap utuh, `fixed_app.py` berjalan, dependency terkunci, konfigurasi menggunakan environment variable, dan semua anggota memahami seluruh temuan.

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

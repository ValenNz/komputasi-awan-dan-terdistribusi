# INSTRUCTION.md — Tugas 10: Arsitektur Cloud yang Skalabel

**Tujuan:** Menjalankan arsitektur Nginx Load Balancer dengan beberapa instance aplikasi menggunakan Docker Compose, melakukan load test, scale-up horizontal, perbandingan vertical scaling, dan uji kegagalan instance.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Integrasi `docker-compose.yml`, konfigurasi layanan dan port; koordinasi skenario horizontal 3–4 instance. |
| Galang Herjuo Mulya | Implementasi dan pengujian `app/app.py`, identitas instance melalui environment variable, dan pemeriksaan response. |
| Haniel Juanta Sembiring | Konfigurasi Nginx `nginx/nginx.conf`, upstream backend, proxy, dan verifikasi distribusi request. |
| Rohmatul Choirul Anam | `load_test.py`, pengumpulan metrik jumlah request, latency/kegagalan, serta dokumentasi perbandingan. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota menjalankan `docker compose up --build` dan mengakses endpoint melalui `http://localhost:8080/`.
2. Setiap anggota mengirim request dan mengidentifikasi instance yang merespons.
3. Semua anggota ikut menjalankan load test; minimal satu kali setiap orang menjalankan skenario 3 instance dan membaca hasilnya.
4. Bersama-sama tambahkan `app4`, restart layanan, dan ulangi load test.
5. Jalankan skenario satu instance dengan resource lebih besar untuk perbandingan vertical scaling.
6. Matikan satu instance saat pengujian berjalan. Amati apakah request gagal, dialihkan, atau tetap berhasil; catat hasil nyata.
7. Setiap anggota menjelaskan perbedaan horizontal scaling, vertical scaling, load balancing, dan auto-scaling.

## Langkah pengerjaan

1. Periksa skeleton yang disediakan sebelum mengubah file.
2. Lengkapi `INSTANCE_ID` pada aplikasi dan konfigurasi upstream Nginx.
3. Pastikan tiga instance dapat dijangkau melalui load balancer.
4. Jalankan load test dengan parameter yang konsisten (misalnya 300 request dan 30 thread).
5. Catat jumlah request per instance, total request berhasil/gagal, dan latency yang dapat diukur.
6. Tambahkan instance keempat dan ulangi pengujian dengan parameter yang sama.
7. Jalankan skenario vertical scaling satu instance dengan batas resource yang lebih besar. Catat konfigurasi resource yang benar-benar digunakan.
8. Matikan satu backend dan lakukan pengujian ulang. Catat perilaku aktual dan keterbatasan konfigurasi health check/failover.
9. Bandingkan hasil horizontal vs vertical scaling menggunakan tabel berdasarkan data eksperimen.
10. Jelaskan keterbatasan penambahan instance manual dibanding autoscaling cloud sungguhan.

## Berkas submission

- `app/app.py`
- `nginx/nginx.conf`
- `docker-compose.yml`
- `load_test.py`
- `README.md`
- `JURNAL.md`
- `bukti/` — hasil load test, `docker compose ps`, dan skenario instance mati.

## Kriteria selesai

Distribusi request terbukti melalui angka, 3–4 instance berjalan, horizontal dan vertical scaling dibandingkan dengan data aktual, skenario instance mati dicatat, serta seluruh anggota menjalankan dan memahami praktik.

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
| Galang Herjuo Mulya | 103072430006 |
| Haniel Juanta Sembiring | 103072400145 |
| Rohmatul Choirul Anam | 103072400024 |

## Bukti kontribusi minimum per anggota

- Minimal satu commit bermakna atas nama sendiri pada tugas ini.
- Ada hasil praktik/analisis yang jelas dan dapat ditunjukkan.
- Mampu menjelaskan bagian sendiri dan menjawab pertanyaan tentang bagian anggota lain.
- Nama, NIM, dan kontribusi dicantumkan secara jujur pada tabel kontribusi di README submission.

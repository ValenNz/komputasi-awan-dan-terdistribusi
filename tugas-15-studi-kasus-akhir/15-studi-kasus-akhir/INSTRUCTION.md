# INSTRUCTION.md — Tugas 15: Studi Kasus Akhir Smart City

**Tujuan:** Mengintegrasikan simulasi sensor, message queue, processor, dan object storage MinIO menjadi sistem end-to-end. Sistem harus membuktikan satu konsep sistem terdistribusi benar-benar bekerja melalui skenario gangguan.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Integrasi Docker Compose dan infrastruktur RabbitMQ + MinIO; koordinasi konfigurasi service, jaringan, volume, dan akses dashboard. |
| Farrellino Ulung Satya Amando | Implementasi/pengujian `sensors/sensor_publisher.py`: beberapa sensor, data terstruktur, pengiriman berkala, dan identitas sensor. |
| Haniel Juanta Sembiring | Implementasi/pengujian `processor/consumer_to_storage.py`: consume pesan, validasi/pemrosesan, dan penyimpanan object JSON ke MinIO. |
| Rohmatul Choirul Anam | Integrasi end-to-end, pengujian skenario gangguan, bukti, diagram arsitektur, dan konsolidasi laporan/refleksi. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota menjalankan Docker Compose dan memverifikasi dashboard RabbitMQ serta MinIO.
2. Setiap anggota menjalankan publisher dan consumer secara langsung, bukan hanya melihat rekaman anggota lain.
3. Setiap anggota memverifikasi bahwa pesan sensor masuk ke antrean dan object JSON tersimpan di MinIO.
4. Semua anggota ikut melakukan skenario gangguan: hentikan consumer sementara sensor tetap mengirim, kemudian hidupkan kembali consumer dan amati apakah pesan tertahan diproses.
5. Setiap anggota menjelaskan alur data dari sensor sampai object storage serta peran broker.
6. Semua anggota ikut menguji setidaknya satu variasi data sensor atau jumlah sensor.
7. Sebelum final, lakukan demo kelompok end-to-end dan sesi tanya jawab silang.

## Langkah pengerjaan

1. Baca seluruh README tugas dan pahami skeleton yang disediakan.
2. Tentukan konsep sistem terdistribusi yang akan ditampilkan. Default yang disarankan adalah Message Queue dari Tugas 4. Jika memilih Bully, DHT, atau Consistency, implementasikan sampai terlihat bekerja dan jelaskan alasannya.
3. Jalankan RabbitMQ dan MinIO melalui `docker compose up -d`.
4. Siapkan virtual environment dan dependency.
5. Lengkapi publisher agar beberapa sensor mengirim data periodik dengan ID sensor, jenis sensor, nilai, dan timestamp yang relevan.
6. Lengkapi processor agar menerima pesan dan menyimpan tiap data sensor sebagai object JSON ke bucket MinIO.
7. Uji alur normal dan pastikan object benar-benar muncul pada MinIO.
8. Jalankan skenario gangguan: hentikan consumer saat publisher tetap mengirim; catat kondisi antrean; nyalakan consumer kembali; buktikan pesan tertunda diproses. Jangan mengklaim pesan tidak hilang sebelum memverifikasinya.
9. Buat diagram arsitektur Mermaid yang sesuai dengan implementasi aktual.
10. Tulis refleksi: tantangan utama, keputusan arsitektur, trade-off, dan hubungan konsep dari tugas-tugas sebelumnya.
11. Rekam video demo utuh sesuai README: sistem berjalan end-to-end lalu skenario gangguan dilakukan dalam rekaman yang sama.
12. Pastikan seluruh anggota memiliki commit bermakna pada bagian yang dikerjakan dan tabel kontribusi mencerminkan kenyataan.

## Berkas submission

- `README.md` — laporan akhir, diagram arsitektur, integrasi konsep, refleksi.
- `JURNAL.md`
- `docker-compose.yml`
- `requirements.txt`
- `sensors/sensor_publisher.py`
- `processor/consumer_to_storage.py`
- `bukti/` — screenshot dashboard/log dan video demo.

## Kriteria selesai

Data dari beberapa sensor berhasil masuk melalui broker dan tersimpan di MinIO, skenario consumer mati lalu hidup kembali diuji, konsep sistem terdistribusi terlihat bekerja, video demo memenuhi ketentuan, dan semua anggota dapat menjelaskan keseluruhan sistem.

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

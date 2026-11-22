# INSTRUCTION.md — Tugas 11: Implementasi IaaS

**Tujuan:** Membuat simulasi server Linux kustom menggunakan Dockerfile, menjalankan otomasi perusahaan melalui Bash, dan membuktikan otomasi benar-benar berjalan di container.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Desain Dockerfile berbasis base image OS penuh, instalasi paket, dan konfigurasi startup container. |
| Galang Herjuo Mulya | Implementasi serta pengujian `provision.sh` untuk skenario backup otomatis. |
| Haniel Juanta Sembiring | Implementasi serta pengujian alternatif otomasi log rotation/cleanup atau health check; pilih satu skenario yang berbeda dari anggota kedua. |
| Rohmatul Choirul Anam | Integrasi Dockerfile dan script, uji end-to-end, kumpulkan bukti, serta analisis IaaS dan perbedaan container vs VM. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota membangun image Docker dari source kelompok.
2. Setiap anggota menjalankan container dan mengamati proses startup.
3. Semua anggota menguji script otomasi dengan data uji: file contoh untuk backup, log lama untuk cleanup, atau service hidup/mati untuk health check.
4. Setiap anggota mengubah satu kondisi uji dan mengamati hasilnya.
5. Semua anggota menjelaskan bagian yang dikelola pengguna pada IaaS dan keterbatasan container dibanding VM penuh.

## Langkah pengerjaan

1. Pilih satu skenario otomasi utama dan satu skenario tambahan bila beban memungkinkan.
2. Buat Dockerfile dengan base image OS penuh, bukan image `-slim` atau `-alpine`, sesuai ketentuan tugas.
3. Instal tool yang dibutuhkan seperti `cron`, `rsync`, atau `curl`.
4. Buat `provision.sh` yang benar-benar melakukan pekerjaan, bukan hanya mencetak pesan.
5. Pastikan script memiliki permission yang sesuai dan dijalankan saat container startup.
6. Build dan jalankan container sesuai instruksi README tugas.
7. Buktikan hasil otomasi melalui file hasil backup, log, atau keluaran health check.
8. Uji kondisi normal dan kondisi kegagalan yang relevan.
9. Tulis analisis mengapa rancangan ini merupakan simulasi IaaS serta perbedaan kernel, isolasi, overhead, dan fleksibilitas container vs VM.
10. Jangan mengklaim container setara sepenuhnya dengan VM sungguhan.

## Berkas submission

- `Dockerfile`
- `provision.sh`
- `README.md`
- `JURNAL.md`
- `bukti/` — screenshot/log bukti otomasi.

## Kriteria selesai

Image berhasil dibangun, container berjalan, otomasi terbukti menghasilkan efek, seluruh anggota menjalankan pengujian, dan analisis menjelaskan batas simulasi Docker secara tepat.

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

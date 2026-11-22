# INSTRUCTION.md — Tugas 09: Cloud Delivery & Deployment Model

**Tujuan:** Menganalisis rancangan Sistem Data Kependudukan dan menentukan deployment model serta service model yang sesuai. Tugas ini analisis/desain, bukan deployment cloud sungguhan.

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Analisis karakteristik esensial NIST dan kebutuhan kerahasiaan, skalabilitas, serta akses lintas instansi. |
| Galang Herjuo Mulya | Evaluasi deployment model Public, Private, Hybrid, dan Community Cloud; susun alasan pemilihan dan penolakan alternatif. |
| Haniel Juanta Sembiring | Pemetaan komponen sistem ke IaaS, PaaS, dan SaaS; jelaskan batas tanggung jawab tiap model. |
| Rohmatul Choirul Anam | Identifikasi minimal dua risiko spesifik beserta mitigasi; integrasikan argumen dan buat diagram arsitektur konseptual. |

## Praktik bersama — wajib dilakukan semua anggota

1. Setiap anggota membaca studi kasus dan membuat keputusan awal deployment/service model secara mandiri.
2. Diskusikan perbedaan keputusan. Jangan langsung menerima rekomendasi PIC tanpa argumen.
3. Buat diagram rancangan bersama yang menunjukkan data inti, portal akses, instansi pengguna, batas private/public segment jika dipilih, serta aliran data.
4. Setiap anggota wajib mempresentasikan satu risiko dan mitigasinya, serta menjelaskan satu karakteristik NIST.
5. Lakukan peer review: tiap anggota memeriksa satu bagian analisis anggota lain dan memberi masukan berbasis kebutuhan kasus.

## Langkah pengerjaan

1. Uraikan kebutuhan: data sangat rahasia, ribuan instansi, beban tidak merata, skalabilitas, dan kendali infrastruktur.
2. Nilai pilihan deployment berdasarkan karakteristik NIST: on-demand self-service, broad network access, resource pooling, rapid elasticity, dan measured service.
3. Tentukan deployment model yang paling masuk akal dan jelaskan trade-off-nya. Hindari alasan generik seperti “private lebih aman” tanpa penjelasan.
4. Petakan komponen berbeda ke service model IaaS/PaaS/SaaS sesuai kebutuhan kontrol dan operasional.
5. Analisis minimal dua risiko spesifik dan mitigasinya.
6. Bandingkan dengan satu alternatif yang ditolak.
7. Satukan hasil menjadi `README.md`, tambahkan diagram bila membantu, dan isi `JURNAL.md`.

## Berkas submission

- `README.md` — jawaban empat poin sesuai README tugas.
- `JURNAL.md` — proses, keputusan, kendala, dan log AI.
- `bukti/` — diagram pendukung bila digunakan.

## Kriteria selesai

Semua empat pertanyaan pada README tugas terjawab, argumen terikat pada studi kasus, setiap anggota dapat mempertahankan keputusan kelompok, dan semua anggota memiliki commit sendiri.

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

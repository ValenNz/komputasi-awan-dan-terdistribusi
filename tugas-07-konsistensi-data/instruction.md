# INSTRUCTION.md — Tugas 07: Konsistensi Data

**Tujuan:** Menyelesaikan dan memvalidasi studi kasus replikasi saldo e-wallet FoodGo, model konsistensi, diagram, serta simulasi Read-Your-Writes (RYW).

## Pembagian tanggung jawab utama

| Anggota | Fokus utama / deliverable |
|---|---|
| Nuevalen Refitra Alswanado | Audit dan pematangan analisis Sequential vs Eventual, dampak bisnis, serta skenario tambahan. Periksa ketepatan argumen dan istilah konsistensi. |
| Galang Herjuo Mulya | Audit sequence diagram Mermaid untuk skenario bug dan fix; verifikasi urutan pesan, aktor, dan kondisi replikasi. |
| Haniel Juanta Sembiring | Verifikasi simulasi `src/replica_simulation.py`, jalankan ulang, telusuri output, dan dokumentasikan hasil aktual. |
| Rohmatul Choirul Anam | Review teknis dan integrasi: uji kasus batas, cek kesesuaian diagram dengan simulasi, lengkapi matriks pengujian serta review `JURNAL.md` dan bukti. |

## Praktik bersama — wajib dilakukan semua anggota

1. Buka dan baca studi kasus FoodGo pada README tugas 07.
2. Setiap anggota jalankan sendiri `python src/replica_simulation.py` (jika skeleton tersedia). Catat output yang benar-benar diperoleh.
3. Setiap anggota jelaskan perbedaan `stale read` pada skenario naif dan hasil yang dijamin RYW.
4. Bersama-sama telusuri alur: top-up di Jakarta, replikasi tertunda, pembacaan di Bandung, pemeriksaan `version_number`, dan timeout/fallback.
5. Lakukan review silang: setiap anggota harus dapat menjelaskan satu bagian yang bukan deliverable utamanya.

## Langkah pengerjaan

1. Audit file dan status yang sudah ada. Jangan menghapus hasil yang sudah benar; perbaiki hanya jika ditemukan ketidaksesuaian.
2. Pastikan analisis membahas mengapa data finansial tidak cukup memakai eventual consistency, trade-off sequential consistency, dan alasan pemilihan RYW.
3. Pastikan diagram menunjukkan kondisi bug dan fix secara konsisten dengan mekanisme pada kode.
4. Jalankan simulasi minimal dua kali dan simpan output aktual ke `bukti/`.
5. Tambahkan pengujian untuk kondisi versi replika tertinggal, versi sudah sama, serta timeout/fallback bila skeleton mendukungnya.
6. Cocokkan angka saldo dan versi pada narasi, diagram, kode, dan output. Jangan menuliskan hasil yang tidak pernah diuji.
7. Perbarui tabel kontribusi dengan keempat anggota dan kontribusi yang benar-benar dilakukan.

## Berkas yang perlu diperiksa/dikumpulkan

- `README.md` — analisis dan diagram.
- `src/replica_simulation.py` — simulasi.
- `JURNAL.md` — proses dan log AI.
- `bukti/` — output eksekusi dan bukti pengujian.

## Kriteria selesai

- Semua anggota berhasil menjalankan dan menjelaskan simulasi.
- Diagram bug/fix sesuai perilaku program.
- Hasil pengujian aktual terdokumentasi.
- Keempat anggota memiliki commit sendiri dan kontribusi nyata.

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

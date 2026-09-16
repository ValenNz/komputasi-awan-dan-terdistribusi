### 📋 Pembagian Tugas Anggota Kelompok

| Nama | NIM | Peran & Tanggung Jawab Utama | Pitfall yang Dianalisis |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswando** (Ketua) | 10203072430008 | **Koordinator & Integrator.** Menganalisis Pitfall 1, memimpin diskusi, mengumpulkan hasil, memastikan format `README.md` & `JURNAL.md` sesuai template, serta melakukan `git tag` dan submission ke Moodle. | **Pitfall 1: "Latency is zero" (Asumsi Latensi Nol / Tidak Ada Timeout)** <br>*Fokus:* Dampak tidak adanya timeout pada pemanggilan antar-service. |
| **Farrelino Ulung Satya Amando** | 103072400005 | **Analis Arsitektur.** Menganalisis Pitfall 2, melakukan review silang terhadap tulisan Nuevalen & Haniel, mendokumentasikan perbedaan pendapat di `JURNAL.md`. | **Pitfall 2: Arsitektur Monolitik & "Bandwidth is infinite"** <br>*Fokus:* Satu server menangani semua modul (pesanan, bayar, notifikasi) hingga kewalahan saat trafik naik. |
| **Haniel Juanta Sembiring** | 103072400145 | **Analis Fault Tolerance.** Menganalisis Pitfall 3, melakukan review silang terhadap tulisan Nuevalen & Farrelino, memastikan log AI di `JURNAL.md` terisi dengan benar. | **Pitfall 3: "The network is reliable" (Kurangnya Mekanisme Retry & Fault Tolerance)** <br>*Fokus:* Komentar kode `# network is always reliable, no need for retry` dan crash total yang membutuhkan restart manual. |

---

### 🚀 Langkah Kerja yang Disarankan (SOP Kelompok)

Agar memenuhi rubrik "Proses & kontribusi kelompok (20%)" dan aturan commit individu, ikuti alur ini:

#### 1. Diskusi Awal (Wajib didokumentasikan)
- Lakukan panggilan/meeting singkat (15-30 menit).
- **Penting:** Ambil screenshot layar meeting (menampilkan nama peserta) atau foto whiteboard/catatan diskusi. Simpan di folder `tugas-01-identifikasi-masalah-pitfall/bukti/`.
- Catat poin diskusi langsung ke `JURNAL.md` (jangan ditulis ulang nanti, tulis saat itu juga).

#### 2. Pengerjaan Individual (Commit dari Laptop Masing-Masing)
- Setiap anggota membuat branch atau langsung edit di `main` (sesuai kesepakatan), tapi **wajib commit dari akun GitHub masing-masing**.
- Contoh commit Farrelino: `git commit -m "Tugas 1: Menambahkan analisis Pitfall 2 (Monolitik) oleh Farrelino"`
- Isi bagian kalian di `README.md` menggunakan template yang sudah disediakan.

#### 3. Review Silang (Wajib untuk nilai maksimal)
- Setelah semua bagian terisi, setiap anggota membaca tulisan anggota lain.
- Berikan 1-2 kalimat saran/koreksi di `JURNAL.md` bagian "Review Silang". 
  *Contoh: "Nuevalen mengomentari analisis Farrelino: Solusi microservice-nya sudah tepat, tapi tambahkan catatan bahwa ini akan meningkatkan kompleksitas deployment."*

#### 4. Finalisasi oleh Ketua (Nuevalen)
- Nuevalen melengkapi bagian "Kesimpulan Kelompok" di `README.md`.
- Nuevalen memastikan `JURNAL.md` sudah terisi lengkap (termasuk Log AI).
- Nuevalen melakukan:
  ```bash
  git add .
  git commit -m "Tugas 1: Finalisasi README, Jurnal, dan review silang lengkap"
  git push origin main
  git tag tugas-01-submit
  git push origin tugas-01-submit
  ```
- Nuevalen menyalin link permalink tag tersebut ke Moodle.

---

### 📝 Draft Awal `JURNAL.md` (Bisa Langsung Di-copy & Dilanjutkan)

Gunakan ini sebagai starting point di file `tugas-01-identifikasi-masalah-pitfall/JURNAL.md` kalian:

```markdown
# Jurnal Proses — Tugas 1

## [Tanggal Hari Ini, misal: 16 September 2026]
- **Peserta:** Nuevalen, Farrelino, Haniel (via Discord/Zoom/Offline)
- **Poin diskusi:** 
  - Membaca studi kasus FoodGo bersama. 
  - Sepakat membagi 3 pitfall utama: (1) Tidak ada timeout, (2) Beban monolitik, (3) Asumsi network reliable tanpa retry.
  - Farrelino mengingatkan bahwa solusi "pindah ke cloud" bukan jawaban, harus ada perubahan desain arsitektur (misal: pemisahan service).
- **Perbedaan pendapat:** Haniel awalnya mengusulkan solusi "tambah server", tapi didiskusikan ulang bahwa jika kodenya tetap monolitik dan tanpa timeout, tambah server hanya akan memindahkan masalah. Disepakati solusinya adalah *Circuit Breaker* dan *Decoupling*.

## Review Silang
- **Nuevalen** mengomentari analisis **Farrelino**: "Penjelasan tentang bottleneck I/O di arsitektur monolitik sudah jelas. Saran: tambahkan istilah 'Single Point of Failure' agar lebih teknis."
- **Haniel** mengomentari analisis **Nuevalen**: "Trade-off pada solusi timeout sudah tepat, perlu ditekankan bahwa user experience bisa terdampak jika timeout terlalu pendek."
- **Farrelino** mengomentari analisis **Haniel**: "Kaitan antara komentar kode `# network is always reliable` dengan cascading failure sudah sangat relevan dengan skenario."

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan sendiri |
|---|---|---|---|---|
| 16 Sep 2026 | Qwen (AI Assistant) | "Apa saja 3 fallacies of distributed computing yang paling relevan dengan aplikasi food delivery yang mengalami timeout dan crash saat trafik tinggi?" | AI menyebutkan: Latency is zero, Network is reliable, dan Bandwidth is infinite. | Kami menggunakan daftar ini hanya sebagai *brainstorming* awal. Kami kemudian mencocokkannya secara manual dengan kalimat spesifik di skenario FoodGo dan merumuskan dampak serta solusinya sendiri tanpa menyalin teks AI. |
```

# 📋 Instruksi Pembagian Tugas 1: Identifikasi Pitfall FoodGo (Asumsi)

**Kelompok:** [Isi Nama Kelompok, misal: Kelompok FoodGo Dev]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]

### 👥 Anggota & Pembagian Peran Utama
Sesuai aturan, **tiap anggota wajib menganalisis 1 pitfall utama secara mendalam** dan melakukan *commit* dari laptop masing-masing.

| Nama | NIM | Peran Utama (Pitfall yang Dianalisis) | Fokus Analisis |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Pitfall 1:** *"The network is reliable"* | Fokus pada ketiadaan mekanisme *timeout* dan *retry* pada panggilan antar-service. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Pitfall 2:** *"Latency is zero"* | Fokus pada asumsi pemanggilan *synchronous* yang memblokir *thread* (menunggu tanpa batas) antar modul (pesanan & pembayaran). |
| **Haniel Juanta Sembiring** | 103072400145 | **Pitfall 3:** *Single Point of Failure* (Arsitektur Monolitik) | Fokus pada gejala "satu server menangani semua modul" yang *crash* dan butuh *restart manual* (mengacu pada slide: *Centralized solutions have a single point of failure*). |

> **Catatan:** Meskipun punya peran utama, **semua anggota wajib** membaca, mengoreksi, dan memberikan komentar pada analisis anggota lain (*Cross-Review*) sebelum di-*submit*.

---

## 🔄 Alur Kerja (Workflow) Kelompok

Ikuti langkah ini agar proses rapi dan sesuai rubrik:

### Langkah 1: Kerja Individu (Durasi: 1-2 Hari)
Setiap anggota mengerjakan bagian masing-masing di `README.md` (bisa pakai *branch* masing-masing atau langsung di `main` dengan koordinasi). Pastikan 5 poin ini terjawab untuk pitfall kalian:
1. **Bukti di skenario:** Kutip kalimat asli dari deskripsi FoodGo.
2. **Kenapa ini keliru:** Jelaskan menggunakan teori dari slide (misal: jaringan nyata punya latensi dan bisa putus).
3. **Dampak ke FoodGo:** Jelaskan mekanisme teknisnya (misal: "Thread menumpuk, memori habis, server *crash*").
4. **Solusi desain awal:** Usulkan konsep (misal: *Circuit Breaker*, *Asynchronous Messaging*).
5. **Trade-off:** Apa kerugian dari solusi tersebut (misal: "Data mungkin tidak konsisten sementara waktu").

### Langkah 2: Diskusi Kelompok (Durasi: 30-45 Menit)
Lakukan panggilan (Zoom/Discord/Meet). **Jangan hanya chat teks.**
- Bahas apakah solusi yang diusulkan saling bertabrakan atau justru saling melengkapi.
- Rumuskan **Kesimpulan Kelompok** bersama (bagian paling bawah `README.md`).
- **Wajib:** Catat poin diskusi, perbedaan pendapat, dan keputusan di `JURNAL.md`.

### Langkah 3: Review Silang & Finalisasi (Durasi: 1 Hari)
- Baca analisis teman sekelompok.
- Berikan komentar konstruktif (misal: *"Menurutku trade-off di bagian Nuevalen bisa ditambahin soal beban jaringan saat retry"*).
- Catat aktivitas *review* ini di bagian **Review Silang** pada `JURNAL.md`.
- Pastikan format penulisan sudah sesuai `ANALISIS-TEMPLATE.md`.

### Langkah 4: Git Commit & Push (Wajib dari Laptop Masing-Masing)
Jangan biarkan 1 orang meng-*commit* semua pekerjaan. Contoh alur Git yang benar:
```bash
# Nuevalen mengerjakan bagiannya
git pull origin main
git add tugas-01-identifikasi-masalah-pitfall/README.md
git commit -m "Tugas 1: Nuevalen - Analisis Pitfall 'The network is reliable' & update jurnal"
git push origin main

# Farrellino mengerjakan bagiannya
git pull origin main
git add tugas-01-identifikasi-masalah-pitfall/README.md tugas-01-identifikasi-masalah-pitfall/JURNAL.md
git commit -m "Tugas 1: Farrellino - Analisis Pitfall 'Latency is zero' & catatan diskusi"
git push origin main

# Haniel mengerjakan bagiannya & merapikan kesimpulan
git pull origin main
git add tugas-01-identifikasi-masalah-pitfall/
git commit -m "Tugas 1: Haniel - Analisis SPOF, Kesimpulan Kelompok, & finalisasi jurnal"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Dilarang Copy-Paste AI:** AI hanya boleh dipakai untuk *brainstorming* (Level 2). Dilarang meminta AI menuliskan paragraf analisis utuh. Jika ketahuan generik, nilai "Kedalaman Analisis" (30%) akan anjlok.
2. **Isi Log AI di JURNAL.md:** Jika ada yang pakai AI untuk cari ide, **WAJIB** isi tabel "Log Penggunaan AI" di `JURNAL.md`. Jika tidak pakai, tulis "Tidak memakai AI".
3. **Kaitkan dengan Skenario:** Jawaban yang bisa dipakai untuk kasus apa saja (generik) akan mendapat nilai rendah. Selalu sebut "FoodGo", "modul pesanan", "modul pembayaran".

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Diskusi Awal - [Tanggal]
- Peserta: Nuevalen, Farrellino, Haniel
- Pembagian tugas: Nuevalen ambil "Network reliable", Farrellino ambil "Latency zero", Haniel ambil "Monolithic SPOF".
- Kebuntuan: Sempat bingung membedakan "Network reliable" dan "Latency zero". 
- Solusi: Kita sepakat "Network reliable" fokus pada ketiadaan retry/timeout, sedangkan "Latency zero" fokus pada asumsi respons instan yang memblokir thread.

## Review Silang - [Tanggal]
- Nuevalen mengomentari analisis Farrellino: Menyarankan untuk menambahkan solusi "Message Queue" agar tidak blocking.
- Farrellino mengomentari analisis Haniel: Menyetujui solusi pemisahan service, tapi mengingatkan trade-off-nya adalah kompleksitas deployment bertambah.

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran AI | Bagaimana diolah sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Apa trade-off dari penggunaan circuit breaker?" | Menjelaskan tentang delay deteksi failure dan kompleksitas konfigurasi. | Saya (Haniel) menulis ulang dengan bahasa sendiri dan mengaitkannya spesifik dengan kasus FoodGo. |
```
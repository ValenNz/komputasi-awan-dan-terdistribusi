# 📋 Instruksi Pembagian Tugas 3: Efisiensi Proses & Kontainer FoodGo (Asumsi)

**Kelompok:** [Isi Nama Kelompok]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]  
**Fokus Utama:** Mengganti pemrosesan pesanan yang berat (OS process) menjadi ringan (*multithreading*), membuktikan pemahaman *race condition* & *Lock*, serta mengemasnya dalam *Docker container*.

### 👥 Anggota & Pembagian Peran Utama

| Nama | NIM | Peran Utama & Fokus Analisis | Output yang Diharapkan |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Logika Multithreading & Analisis Race Condition**<br>Fokus: Mengisi `# TODO` di `order_simulator.py` (membuat worker konkuren, simulasi race condition, dan perbaikan pakai `threading.Lock()`). Menulis analisis di `README.md` kenapa *thread* lebih efisien daripada *process* (merujuk biaya *context switching* di Bab 3). | File `src/order_simulator.py` yang berfungsi & paragraf analisis di `README.md`. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Containerization (Docker) & Bukti Eksekusi**<br>Fokus: Melengkapi `# TODO` di `Dockerfile` (base image, install, CMD), memastikan `requirements.txt` rapi, dan mengumpulkan semua bukti eksekusi (screenshot/video) di folder `bukti/`. | File `Dockerfile` yang berhasil di-build, folder `bukti/` berisi 3+ screenshot/video valid. |
| **Haniel Juanta Sembiring** | 103072400145 | **Dokumentasi, Jurnal, & Integrasi Akhir**<br>Fokus: Mengelola `JURNAL.md` (mencatat log sebelum/sesudah lock, error Docker), menyatukan tulisan anggota ke `README.md`, dan memastikan kepatuhan terhadap aturan AI Level 2. | File `JURNAL.md` yang lengkap, `README.md` final yang terstruktur rapi, dan review silang. |

> **Catatan Penting:** Meskipun ada pembagian peran, **semua anggota WAJIB** me-review hasil kerja teman sebelum di-*push* untuk memastikan konsistensi (misal: nama variabel di Python cocok dengan penjelasan di README).

---

## 🔄 Alur Kerja (Workflow) Kelompok

Ikuti langkah ini agar proses rapi dan sesuai rubrik:

### Langkah 1: Kerja Individu (Durasi: 1-2 Hari)
- **Nuevalen**: Kerjakan `order_simulator.py`. Pastikan ada 2 mode atau 2 bagian kode yang bisa dijalankan/ditunjukkan: satu yang sengaja *tanpa lock* (untuk menunjukkan angka counter yang salah/berkurang), dan satu *dengan lock* (angka counter akurat). 
- **Farrellino**: Lengkapi `Dockerfile`. Pastikan image bisa di-build (`docker build -t foodgo-order-sim .`) dan di-run (`docker run --rm foodgo-order-sim`) tanpa error. Ambil screenshot terminal yang menunjukkan prompt laptop kalian.
- **Haniel**: Siapkan kerangka `JURNAL.md` dan `README.md`. Mulai catat setiap kendala yang dihadapi teman-teman (misal: "Awalnya lupa `COPY requirements.txt`, jadi error di Docker").

### Langkah 2: Diskusi Kelompok & Validasi Bukti (Durasi: 30 Menit)
Lakukan panggilan singkat.
- Validasi bukti: Apakah screenshot *race condition* sudah jelas menunjukkan angka yang meleset? Apakah screenshot Docker sudah menunjukkan output yang sama dengan versi lokal?
- Pastikan tidak ada kode yang di-*copy paste* mentah dari AI pada bagian `# TODO`. Jika pakai AI, pastikan sudah ditulis ulang dan dimodifikasi.

### Langkah 3: Git Commit & Push (Wajib dari Laptop Masing-Masing)
Jangan biarkan 1 orang meng-*commit* semua pekerjaan. Contoh alur Git yang benar:

```bash
# 1. Nuevalen push logika threading
git pull origin main
git add tugas-03-multithreading-container/src/order_simulator.py tugas-03-multithreading-container/README.md
git commit -m "Tugas 3: Nuevalen - Implementasi multithreading, simulasi race condition & perbaikan Lock"
git push origin main

# 2. Farrellino push Dockerfile & bukti
git pull origin main
git add tugas-03-multithreading-container/Dockerfile tugas-03-multithreading-container/requirements.txt tugas-03-multithreading-container/bukti/
git commit -m "Tugas 3: Farrellino - Lengkapkan Dockerfile skeleton & tambahkan bukti eksekusi container"
git push origin main

# 3. Haniel push jurnal, integrasi README, & finalisasi
git pull origin main
git add tugas-03-multithreading-container/JURNAL.md tugas-03-multithreading-container/README.md
git commit -m "Tugas 3: Haniel - Update JURNAL.md (log before/after lock), rapikan struktur README, & log AI"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Wajib Ada Bukti "Sebelum" dan "Sesudah"**: Rubrik memberi 25% bobot pada bukti *race condition* & perbaikan. Jika hanya ada klaim teks tanpa screenshot/log perbandingan angka counter, nilai akan anjlok.
2. **Kaitkan dengan Teori Bab 3**: Di `README.md`, Nuevalen/Haniel harus menyebutkan bahwa *thread context switching* lebih murah daripada *process context switching* karena thread berbagi *address space* yang sama (tidak perlu trap ke kernel untuk ganti memori), sehingga mengatasi masalah "server boros resource" pada FoodGo.
3. **Aturan AI (Level 2)**: DILARANG meminta AI mengisi bagian `# TODO` di `order_simulator.py` atau `Dockerfile`. AI hanya boleh dipakai untuk brainstorming (misal: "Jelaskan konsep race condition di Python"). Wajib isi tabel Log AI di `JURNAL.md`.
4. **Hindari `time.sleep` yang Menipu**: Pastikan multithreading benar-benar konkuren (gunakan `concurrent.futures.ThreadPoolExecutor` atau `threading.Thread` dengan `.start()` dan `.join()`), bukan sekadar loop sekuensial yang disamarkan.

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: [Misal: 874 dari 1000 pesanan]
- Kenapa bisa meleset: [Jelaskan dengan kata sendiri: Karena thread berbagi address space, saat dua thread membaca nilai counter yang sama secara bersamaan, lalu keduanya menambah dan menulis kembali, satu update akan tertimpa (lost update). Ini sesuai materi Bab 3 tentang thread yang tidak memiliki proteksi memori otomatis dari OS.]

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: [Misal: 1000 dari 1000 pesanan]
- Mekanisme perbaikan: [Menambahkan `threading.Lock()` di sekitar bagian kritis (critical section) increment counter, sehingga hanya satu thread yang bisa mengakses variabel tersebut pada satu waktu.]

## Kendala Docker
- Error yang ditemui: [Misal: "python: can't open file '/app/src/order_simulator.py': [Errno 2] No such file or directory"]
- Cara memperbaiki: [Misal: "Menambahkan perintah `COPY src/ ./src/` di Dockerfile sebelum CMD, dan memastikan WORKDIR sudah benar."]

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Apa perbedaan biaya context switch antara thread dan process di OS?" | Menjelaskan bahwa process switch butuh pergantian page table (MMU), sedangkan thread switch hanya pergantian register dalam address space yang sama. | Saya (Nuevalen) menggunakan poin ini untuk memperkuat argumen di README.md kenapa FoodGo harus beralih dari fork() process ke multithreading. |
```
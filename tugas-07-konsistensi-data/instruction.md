# 📋 Instruksi Pembagian Tugas 7: Konsistensi Data (FoodGo)

**Kelompok:** [Isi Nama Kelompok]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]  
**Fokus Utama:** Menganalisis masalah inkonsistensi saldo *e-wallet* FoodGo akibat replikasi lambat, memilih model konsistensi yang tepat, memvisualisasikannya dengan *Sequence Diagram*, dan (opsional) mensimulasikannya dalam kode.

### 👥 Anggota & Pembagian Peran Utama

| Nama | NIM | Peran Utama & Fokus Analisis | Output yang Diharapkan |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Analisis Teoritis & Skenario Tambahan**<br>Fokus: Menentukan model konsistensi (Sequential vs Eventual), mengusulkan solusi *Client-Centric* (misal: *Read-Your-Writes*), dan **membuat 1 skenario tambahan** di luar FoodGo (misal: ojek online) untuk membuktikan pemahaman. | Paragraf analisis mendalam, usulan solusi konkret, dan skenario tambahan di `README.md`. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Visualisasi Diagram & Simulasi Kode**<br>Fokus: Membuat *Sequence Diagram* (Mermaid) untuk skenario "Bug" dan "Fix". Melengkapi kode `src/replica_simulation.py` (TODO) untuk mensimulasikan *inconsistent read* dan *Read-Your-Writes*. | Kode Mermaid yang valid di `README.md`, dan file `src/replica_simulation.py` yang berjalan tanpa error. |
| **Haniel Juanta Sembiring** | 103072400145 | **Testing, Bukti Eksekusi & Dokumentasi**<br>Fokus: Menjalankan simulasi Farrellino, mengambil screenshot/output terminal ke folder `bukti/`, merapikan `README.md` akhir, dan menyusun `JURNAL.md` yang komprehensif. | Folder `bukti/` berisi output simulasi, `README.md` final yang terintegrasi, dan `JURNAL.md`. |

> **Catatan Penting:** Meskipun ada pembagian peran, **semua anggota WAJIB** me-review hasil kerja teman sebelum di-*push*. Pastikan alur di *Sequence Diagram* Farrellino sinkron dengan penjelasan teoritis Nuevalen.

---

## 🔄 Alur Kerja (Workflow) Kelompok

### Langkah 1: Kerja Individu (Durasi: 1-2 Hari)
- **Nuevalen**: Tulis analisis di `README.md`. 
  - *Tips:* Jelaskan kenapa *Eventual Consistency* berbahaya untuk saldo *e-wallet* (dampak bisnis: komplain pelanggan, kerugian finansial), tapi mungkin oke untuk "jumlah like". Usulkan *Read-Your-Writes* (sesuai materi Bab 7 slide 24) di mana server Bandung harus "menarik" (pull) update dari Jakarta sebelum memproses read dari pelanggan tersebut.
  - *Wajib:* Buat skenario tambahan (misal: "Aplikasi Booking Hotel: User membatalkan kamar di Server A, lalu cek status di Server B. Harus pakai *Read-Your-Writes* atau *Monotonic Reads*").
- **Farrellino**: 
  - Buat *Sequence Diagram* di `README.md` menggunakan `sequenceDiagram`. Aktor: `Pelanggan`, `Server Jakarta`, `Server Bandung`, `Proses Replikasi`. Buat 2 diagram: (1) Tanpa Consistency Guarantee (Gagal), (2) Dengan Read-Your-Writes (Sukses).
  - Lengkapi `src/replica_simulation.py`. Pastikan ada logika *timestamp* atau *version* sederhana untuk mengimplementasikan *Read-Your-Writes*.
- **Haniel**: Siapkan folder `bukti/` dan kerangka `JURNAL.md`. Pelajari materi Bab 7 tentang *Client-Centric Consistency* (Monotonic Reads, Monotonic Writes, Read-Your-Writes, Writes-Follow-Reads).

### Langkah 2: Integrasi & Pengujian Skenario (Durasi: 30-45 Menit)
Lakukan sesi *live testing* bersama (via screen share):
1. **Farrellino** menjalankan `python3 src/replica_simulation.py`.
2. **Haniel** merekam/mengambil screenshot terminal yang menunjukkan output "Inconsistent Read" (saldo lama terbaca) dan "Consistent Read" (saldo baru terbaca berkat Read-Your-Writes). Simpan di `bukti/`.
3. **Nuevalen** dan **Haniel** me-review *Sequence Diagram* Farrellino. Pastikan notasi panah dan pesan (misal: `TopUp`, `CheckBalance`, `ReplicateData`) sesuai dengan narasi di `README.md`.

### Langkah 3: Git Commit & Push (Wajib dari Laptop Masing-Masing)

```bash
# 1. Nuevalen push analisis teoritis & skenario tambahan
git pull origin main
git add tugas-07-konsistensi-data/README.md
git commit -m "Tugas 7: Nuevalen - Analisis Sequential vs Eventual, usulan Read-Your-Writes, & skenario tambahan"
git push origin main

# 2. Farrellino push sequence diagram & kode simulasi
git pull origin main
git add tugas-07-konsistensi-data/README.md tugas-07-konsistensi-data/src/replica_simulation.py
git commit -m "Tugas 7: Farrellino - Sequence diagram Mermaid (bug & fix) & implementasi simulasi replikasi"
git push origin main

# 3. Haniel push bukti, finalisasi README, dan JURNAL
git pull origin main
git add tugas-07-konsistensi-data/bukti/ tugas-07-konsistensi-data/README.md tugas-07-konsistensi-data/JURNAL.md
git commit -m "Tugas 7: Haniel - Bukti output simulasi, finalisasi README, & update JURNAL"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Skenario Tambahan WAJIB (Bukti Pemahaman):** Rubrik dan instruksi secara eksplisit meminta **1 skenario tambahan** buatan sendiri (bukan FoodGo) di `README.md`. Jika tidak ada, nilai komponen analisis akan dipotong karena dianggap hanya "hafalan skenario".
2. **Kualitas Sequence Diagram (30% Bobot):** Diagram harus jelas menunjukkan **titik kegagalan** (misal: `Server Bandung -> Pelanggan: Return Saldo Lama`) dan **titik perbaikan** (misal: `Server Bandung -> Server Jakarta: Pull Update Saldo`). Gunakan fitur Mermaid `note right of ...` untuk memberi penjelasan pada langkah kritis.
3. **Simulasi adalah Nilai Tambah (Bonus):** Meskipun opsional, mengerjakan Bagian 2 sangat disarankan untuk mendongkrak nilai dan membuktikan bahwa konsep *Client-Centric* benar-benar diimplementasikan, bukan hanya wacana.
4. **Aturan AI (Level 2):** DILARANG meminta AI menuliskan analisis akhir, membuat kode Mermaid utuh, atau mengisi `# TODO` di `src/replica_simulation.py`. AI hanya boleh dipakai untuk brainstorming (misal: "Beri contoh skenario client-centric consistency di aplikasi travel"). Wajib isi tabel Log AI di `JURNAL.md`.

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Analisis Konsistensi
- Keputusan: Kami memilih Eventual Consistency TIDAK cukup untuk saldo e-wallet, karena...
- Solusi Client-Centric: Kami mengusulkan Read-Your-Writes. Mekanismenya adalah... (jelaskan dengan bahasa sendiri, misal: server mencatat versi data terakhir yang dibaca user X, jika versi di server lokal lebih tua, server akan block read dan pull dari server utama dulu).

## Skenario Tambahan
- Skenario: [Misal: Aplikasi E-Commerce, User menambah barang ke keranjang di Server A, lalu klik checkout di Server B].
- Model yang tepat: [Misal: Monotonic Writes atau Read-Your-Writes].

## Revisi Sequence Diagram
- Versi 1: Diagram masih terlalu sederhana, hanya ada Pelanggan dan Server.
- Versi 2: Menambahkan aktor "Proses Replikasi" dan "Server Bandung" secara eksplisit, serta menambahkan `note` pada langkah di mana inkonsistensi terjadi.

## Log Simulasi (Jika mengerjakan Bagian 2)
- Output Inconsistent Read: [Salin snippet output terminal di mana saldo Bandung = 50.000 padahal di Jakarta sudah 150.000]
- Output Read-Your-Writes: [Salin snippet output terminal di mana Server Bandung melakukan 'pull' dan saldo menjadi 150.000]

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Berikan contoh kasus read-your-writes consistency di luar aplikasi keuangan" | Memberikan contoh aplikasi manajemen tugas (task manager) di mana user membuat task baru dan langsung melihatnya di dashboard. | Saya (Nuevalen) menggunakan konsep ini untuk menyusun skenario tambahan di README.md, namun saya menulis ulang narasinya agar spesifik ke konteks aplikasi ojek online. |
```
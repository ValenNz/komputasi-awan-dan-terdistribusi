# 📋 Instruksi Pembagian Tugas 5: Koordinasi & Konsensus (FoodGo)

**Kelompok:** [Isi Nama Kelompok]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]  
**Fokus Utama:** Mengimplementasikan **Bully Algorithm** untuk memilih *Node Leader* secara dinamis di antara 5 proses Python, serta membuktikan mekanisme *re-election* saat leader mati.

### 👥 Anggota & Pembagian Peran Utama

| Nama | NIM | Peran Utama & Fokus Implementasi | Output yang Diharapkan |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Logika Inti Election (TODO 1 & 2)**<br>Fokus: Menangani pesan `ELECTION` dan `OK` di `on_message`, serta mengimplementasikan mekanisme *timeout* menggunakan `threading.Event()` di `start_election` untuk menunggu balasan dari node ber-ID lebih tinggi. | File `src/node.py` (bagian TODO 1 & 2) yang berfungsi dengan mekanisme *timeout* yang akurat dan non-blocking. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Logika Leader & Monitoring (TODO 3 & 4)**<br>Fokus: Mengimplementasikan `declare_leader` (broadcast `COORDINATOR` ke semua peer) dan loop `monitor_leader` untuk secara periodik mengecek ketersediaan leader dan memicu election baru jika leader *crash*. | File `src/node.py` (bagian TODO 3 & 4) yang berfungsi, memastikan *state* `leader_id` tersinkronisasi di semua node. |
| **Haniel Juanta Sembiring** | 103072400145 | **Testing, Bukti Eksekusi & Analisis Dokumen**<br>Fokus: Menjalankan 5 terminal, mensimulasikan skenario (start normal & leader mati), mengumpulkan screenshot/log ke folder `bukti/`, serta menyusun `README.md` (analisis trade-off Bully vs Raft) dan `JURNAL.md`. | Folder `bukti/` lengkap, `README.md` dengan analisis mendalam, dan `JURNAL.md` yang terdokumentasi dengan baik. |

> **Catatan Penting:** Meskipun ada pembagian peran, **semua anggota WAJIB** me-review hasil kerja teman sebelum di-*push* untuk memastikan konsistensi (misal: nama pesan `ELECTION`, `OK`, `COORDINATOR` harus persis sama di semua bagian kode).

---

## 🔄 Alur Kerja (Workflow) Kelompok

### Langkah 1: Kerja Individu (Durasi: 1-2 Hari)
- **Nuevalen**: Lengkapi `on_message` dan `start_election`. 
  - *Tips:* Tambahkan `self.ok_received = threading.Event()` di `__init__`. Di `on_message`, jika dapat "OK", panggil `self.ok_received.set()`. Di `start_election`, gunakan `self.ok_received.wait(timeout=ELECTION_TIMEOUT)`.
- **Farrellino**: Lengkapi `declare_leader` dan `monitor_leader`.
  - *Tips:* Di `monitor_leader`, gunakan `self.send_message` ke port leader. Jika return `False`, reset `self.ok_received` (jika ada) dan panggil `start_election()`.
- **Haniel**: Siapkan folder `bukti/` dan kerangka `README.md`/`JURNAL.md`. Pelajari materi Bab 5 tentang kelemahan Bully Algorithm (banyak pesan, *single point of failure* sementara) vs Raft (heartbeat, term number).

### Langkah 2: Integrasi & Pengujian Skenario (Durasi: 45-60 Menit)
Lakukan sesi *live testing* bersama (via screen share atau langsung di satu ruangan):
1. **Skenario 1 (Start Normal):** Buka 5 terminal, jalankan node 1 s/d 5 hampir bersamaan. Amati log. Node 5 harusnya menjadi leader. Haniel mengambil screenshot/log.
2. **Skenario 2 (Leader Mati):** Tekan `Ctrl+C` pada terminal Node 5. Amati terminal Node 1-4. Node 4 harusnya mendeteksi kegagalan, memulai election, dan akhirnya mendeklarasikan diri sebagai leader baru. Haniel merekam/mengambil screenshot log ini.

### Langkah 3: Git Commit & Push (Wajib dari Laptop Masing-Masing)
Jangan biarkan 1 orang meng-*commit* semua pekerjaan. Contoh alur Git yang benar:

```bash
# 1. Nuevalen push logika election
git pull origin main
git add tugas-05-koordinasi-konsensus/src/node.py
git commit -m "Tugas 5: Nuevalen - Implementasi on_message & start_election dengan threading.Event timeout"
git push origin main

# 2. Farrellino push logika monitoring & declare
git pull origin main
git add tugas-05-koordinasi-konsensus/src/node.py
git commit -m "Tugas 5: Farrellino - Implementasi declare_leader & monitor_leader untuk deteksi kegagalan"
git push origin main

# 3. Haniel push bukti, README, dan JURNAL
git pull origin main
git add tugas-05-koordinasi-konsensus/bukti/ tugas-05-koordinasi-konsensus/README.md tugas-05-koordinasi-konsensus/JURNAL.md
git commit -m "Tugas 5: Haniel - Dokumentasi skenario testing, analisis Bully vs Raft, & update JURNAL"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Bukti Skenario adalah Kunci (30% bobot):** Rubrik sangat menekankan pada bukti *re-election*. Screenshot/log harus jelas menunjukkan: (a) Node 5 jadi leader awal, (b) Node 5 dimatikan, (c) Node lain mendeteksi, (d) Node 4 (atau tertinggi yang tersisa) menjadi leader baru.
2. **Mekanisme Timeout di Python:** Gunakan `threading.Event().wait(timeout=...)` untuk TODO 2. **Jangan gunakan `time.sleep()` biasa** karena akan memblokir thread dan mencegah `on_message` menerima pesan "OK" secara bersamaan.
3. **Analisis Harus Spesifik ke FoodGo:** Di `README.md`, jelaskan bahwa *Leader* dibutuhkan untuk mengurutkan pesanan (misal: memberikan *Logical Clock* atau *Sequence ID* terpusat) agar tidak ada pesanan yang diproses ganda. Bandingkan: Bully cepat tapi *message-heavy* (O(N²) saat election), sedangkan Raft lebih stabil dengan *heartbeat* tapi lebih kompleks diimplementasikan.
4. **Aturan AI (Level 2):** DILARANG meminta AI mengisi bagian `# TODO` di `node.py`. AI hanya boleh dipakai untuk brainstorming (misal: "Jelaskan perbedaan message complexity antara Bully dan Raft"). Wajib isi tabel Log AI di `JURNAL.md`.

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Implementasi Bully
- Kendala saat mengisi TODO 1-4: [Misal: Awalnya `start_election` menggunakan `time.sleep()`, sehingga thread utama terkunci dan tidak bisa menerima pesan "OK" dari node lain di `on_message`. Solusi: Mengganti dengan `threading.Event().wait(timeout=ELECTION_TIMEOUT)` sesuai saran materi konkurensi.]

## Skenario 1: Start normal
- Leader yang terpilih: Node 5
- Log/observasi: [Misal: Node 1, 2, 3, 4 mengirim ELECTION ke node di atasnya. Node 5 membalas OK ke semua, lalu karena tidak ada node di atasnya, Node 5 langsung broadcast COORDINATOR. Semua node mengupdate leader_id menjadi 5.]

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: Node 4
- Berapa lama waktu sampai leader baru terdeteksi: [Misal: Sekitar 3-4 detik, sesuai dengan interval `time.sleep(3)` di `monitor_leader` ditambah `ELECTION_TIMEOUT` 2 detik.]
- Log/observasi: [Misal: Node 4 gagal mengirim pesan ke port 5005. Node 4 memicu start_election(), mengirim ke node di atasnya (tidak ada), lalu mendeklarasikan diri sebagai COORDINATOR baru.]

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Bagaimana cara implementasi timeout non-blocking di Python threading untuk menunggu event?" | Menjelaskan penggunaan `threading.Event().wait(timeout=detik)` yang mengembalikan True jika diset, False jika timeout. | Saya (Nuevalen) mengadopsi konsep ini untuk mengganti `time.sleep()` di TODO 2, agar thread server tetap bisa menerima pesan "OK" secara asinkron. |
```
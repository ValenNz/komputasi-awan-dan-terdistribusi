# 📋 Instruksi Pembagian Tugas 4: Komunikasi Antar Komponen FoodGo (Asumsi)

**Kelompok:** [Isi Nama Kelompok]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]  
**Fokus Utama:** Mengimplementasikan komunikasi **sinkron (RPC)** atau **asinkron (Message Queue)** antara modul Pembayaran dan modul Pesanan/Kurir FoodGo, serta membuktikan konsep *decoupling*.

> ⚠️ **KEPUTUSAN AWAL:** Kelompok harus memilih **minimal 1 jalur** (A atau B). Disarankan mengerjakan **keduanya** untuk pemahaman lebih dalam dan nilai eksplorasi tambahan.

---

## 👥 Anggota & Pembagian Peran Utama

### **REKOMENDASI: Mengerjakan Kedua Jalur (A + B)**

| Nama | NIM | Peran Utama & Fokus Implementasi | Output yang Diharapkan |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Jalur A: RPC (Sinkron)**<br>Fokus: Melengkapi `rpc/server.py` & `rpc/client.py`, membuktikan komunikasi blocking (client menunggu response), dan menganalisis dampak jika server down. | Folder `rpc/` berfungsi penuh, screenshot 2 terminal (server & client), paragraf analisis sinkron di `README.md`. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Jalur B: Message Queue (Asinkron) - Infrastructure & Publisher**<br>Fokus: Setup Docker RabbitMQ, melengkapi `mq/publisher.py`, dan memastikan event bisa dipublish ke antrean. | `docker-compose.yml` jalan, `mq/publisher.py` berhasil kirim pesan, screenshot dashboard RabbitMQ di `bukti/`. |
| **Haniel Juanta Sembiring** | 103072400145 | **Jalur B: Message Queue - Consumer & Bukti Decoupling**<br>Fokus: Melengkapi `mq/consumer.py`, **membuktikan pesan tidak hilang** saat consumer mati (uji asynchronous decoupling), dan menulis analisis di `README.md`. | `mq/consumer.py` berfungsi, video/screenshot uji "consumer mati-nyala", paragraf analisis asinkron di `README.md`, koordinasi `JURNAL.md`. |

> **Catatan Penting:** Meskipun ada pembagian peran, **semua anggota WAJIB** me-review hasil kerja teman sebelum di-*push* untuk memastikan konsistensi.

---

## 🔄 Alur Kerja (Workflow) Kelompok

### **Langkah 1: Setup & Kerja Individu (Durasi: 1-2 Hari)**

#### **Nuevalen (RPC):**
1. Lengkapi `rpc/server.py`:
   - Implementasi fungsi `cek_saldo(user_id)` → return saldo dari dict.
   - Implementasi `proses_pembayaran(user_id, jumlah)` → validasi saldo, kurangi, return status.
   - Setup `SimpleXMLRPCServer` di port 8000.
2. Lengkapi `rpc/client.py`:
   - Buat `ServerProxy` ke `http://localhost:8000`.
   - Panggil kedua fungsi RPC dan ukur waktu respons (buktikan blocking).
3. Uji: Jalankan server di terminal 1, client di terminal 2. Ambil screenshot.

#### **Farrellino (MQ - Publisher & Infra):**
1. Jalankan `docker compose up -d` di folder `mq/`.
2. Verifikasi dashboard RabbitMQ di `http://localhost:15672` (login: guest/guest).
3. Lengkapi `mq/publisher.py`:
   - Koneksi ke RabbitMQ localhost via `pika.BlockingConnection`.
   - Deklarasi queue `pembayaran_berhasil` dengan `durable=True`.
   - Publish 3 event pembayaran dalam loop.
4. Ambil screenshot dashboard RabbitMQ yang menunjukkan queue terbentuk.

#### **Haniel (MQ - Consumer & Uji Decoupling):**
1. Lengkapi `mq/consumer.py`:
   - Koneksi & deklarasi queue yang sama (`durable=True`).
   - Daftarkan `callback` dengan `basic_consume`.
   - Implementasi `callback`: parse JSON, cetak notifikasi, kirim `basic_ack`.
2. **Uji Kritis (Wajib untuk rubrik 25%):**
   - **Skenario A:** Jalankan consumer → jalankan publisher → lihat pesan masuk.
   - **Skenario B (Decoupling):** Matikan consumer → jalankan publisher 3x → nyalakan consumer → **buktikan 3 pesan tetap diproses** (tidak hilang).
3. Rekam video atau ambil screenshot terminal yang menunjukkan bukti ini.

---

### **Langkah 2: Diskusi Kelompok & Analisis (Durasi: 30 Menit)**
Lakukan panggilan singkat untuk menyimpulkan:
- **Kapan pakai RPC?** → Untuk operasi yang butuh respons seketika (cek saldo, validasi pembayaran).
- **Kapan pakai MQ?** → Untuk notifikasi yang tidak kritis (kirim email, update kurir) agar modul pembayaran tidak terhambat.
- **Apa trade-off-nya?** → RPC sederhana tapi coupling tinggi; MQ kompleks tapi resilient.

---

### **Langkah 3: Git Commit & Push (Wajib dari Laptop Masing-Masing)**

```bash
# 1. Nuevalen push RPC implementation
git pull origin main
git add tugas-04-rpc-message-queue/rpc/ tugas-04-rpc-message-queue/README.md
git commit -m "Tugas 4: Nuevalen - Implementasi RPC sinkron (server & client) + bukti blocking"
git push origin main

# 2. Farrellino push MQ infrastructure & publisher
git pull origin main
git add tugas-04-rpc-message-queue/mq/docker-compose.yml tugas-04-rpc-message-queue/mq/publisher.py tugas-04-rpc-message-queue/bukti/
git commit -m "Tugas 4: Farrellino - Setup RabbitMQ Docker & publisher event pembayaran"
git push origin main

# 3. Haniel push consumer, uji decoupling, & finalisasi
git pull origin main
git add tugas-04-rpc-message-queue/mq/consumer.py tugas-04-rpc-message-queue/mq/requirements.txt tugas-04-rpc-message-queue/JURNAL.md tugas-04-rpc-message-queue/README.md
git commit -m "Tugas 4: Haniel - Consumer MQ, bukti async decoupling (pesan tidak hilang), analisis README & JURNAL"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Bukti "Pesan Tidak Hilang" adalah Kunci (25% bobot):** Untuk Jalur B, **WAJIB** menunjukkan screenshot/video saat consumer mati, publisher kirim pesan, lalu consumer nyala dan pesan tetap diproses. Ini inti dari *asynchronous decoupling*.
2. **Durable Queue:** Pastikan `channel.queue_declare(queue=QUEUE_NAME, durable=True)` di kedua sisi (publisher & consumer). Tanpa ini, pesan hilang saat RabbitMQ restart.
3. **Acknowledgement:** Consumer **WAJIB** kirim `ch.basic_ack(delivery_tag=method.delivery_tag)` setelah pesan diproses. Tanpa ack, pesan akan di-redeliver terus-menerus.
4. **Analisis Harus Spesifik:** Jangan tulis "RPC itu sinkron". Tulis: "RPC cocok untuk cek saldo karena modul Pesanan butuh keputusan instan apakah pembayaran berhasil. Jika pakai MQ untuk ini, user harus menunggu tanpa kepastian."
5. **Aturan AI (Level 2):** DILARANG meminta AI mengisi bagian `# TODO`. AI hanya boleh dipakai untuk brainstorming (misal: "Jelaskan perbedaan blocking vs non-blocking I/O"). Wajib isi tabel Log AI di `JURNAL.md`.

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Jalur yang Dipilih
- Jalur A (RPC) dan Jalur B (Message Queue)
- Alasan: Kami ingin memahami kedua paradigma komunikasi untuk kasus FoodGo yang berbeda kebutuhannya.

## Kendala Teknis
- Farrellino: Docker RabbitMQ gagal start karena port 5672 sudah dipakai aplikasi lain. Solusi: matikan proses lama dengan `lsof -i :5672` dan `kill -9 <PID>`.
- Haniel: Consumer error "Connection refused" saat publisher jalan. Solusi: pastikan `docker compose up -d` sudah jalan SEBELUM jalankan publisher/consumer.

## Uji "Pesan Tidak Hilang" (Jalur B)
- Langkah uji:
  1. Matikan consumer.py (Ctrl+C)
  2. Jalankan publisher.py → kirim 3 event
  3. Cek dashboard RabbitMQ → terlihat 3 pesan di antrean "pembayaran_berhasil" (ready: 3)
  4. Nyalakan consumer.py → otomatis memproses 3 pesan sekaligus
- Hasil: Ketiga pesan berhasil diproses dengan urutan yang sama. Ini membuktikan RabbitMQ menyimpan pesan di antrean (persistent) walau consumer offline.

## Analisis Pemilihan Pola
- RPC (Nuevalen): Cocok untuk operasi cek saldo karena client butuh jawaban instan. Kelemahan: jika server Pembayaran down, client Pesanan ikut error (tight coupling).
- MQ (Haniel): Cocok untuk notifikasi kurir karena modul Pembayaran tidak perlu menunggu kurir siap. Jika modul Kurir down, pesan tetap tersimpan dan diproses nanti (loose coupling).

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran AI | Bagaimana diolah jadi tulisan sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Apa perbedaan durable queue dan transient queue di RabbitMQ?" | Menjelaskan durable queue disimpan ke disk, transient hanya di RAM. | Saya (Farrellino) menggunakan konsep ini untuk memastikan `durable=True` di semua deklarasi queue tugas kami. |
```

---

## 🎯 Checklist Submission (Sebelum Tag & Submit)

- [ ] **RPC (Jalur A):** Server & client berjalan, screenshot 2 terminal berdampingan.
- [ ] **MQ (Jalur B):** Docker RabbitMQ jalan, publisher & consumer berfungsi.
- [ ] **Bukti Decoupling:** Screenshot/video pesan tetap diproses walau consumer sempat mati.
- [ ] **Dashboard RabbitMQ:** Screenshot `http://localhost:15672` menunjukkan queue & messages ready.
- [ ] **README.md:** Analisis lengkap kenapa RPC/MQ cocok untuk skenario tertentu.
- [ ] **JURNAL.md:** Log kendala, hasil uji decoupling, dan Log Penggunaan AI.
- [ ] **Commit History:** Ketiga anggota terlihat kontribusinya di `git log`.
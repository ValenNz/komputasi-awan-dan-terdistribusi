# 📋 Instruksi Pembagian Tugas 2: Perancangan Arsitektur FoodGo (Asumsi)

**Kelompok:** [Isi Nama Kelompok]  
**Target Selesai:** [Isi Tanggal, misal: H-2 sebelum deadline]  
**Fokus Utama:** Mengubah arsitektur monolitik FoodGo menjadi terdesentralisasi (*decoupled*) menggunakan **SOA** dan/atau **Publish-Subscribe**.

### 👥 Anggota & Pembagian Peran Utama

| Nama | NIM | Peran Utama & Fokus Analisis | Output yang Diharapkan |
| :--- | :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | **Pemilihan Gaya Arsitektur & Core Services**<br>Fokus: Justifikasi pemilihan SOA/Pub-Sub, dan merancang alur komunikasi antara modul **Pesanan** dan **Pembayaran** (Sinkron vs Asinkron). | Paragraf justifikasi arsitektur & deskripsi interaksi Order-Payment di `README.md`. |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | **Visualisasi Diagram & Skenario End-to-End**<br>Fokus: Membuat diagram (Mermaid/draw.io) yang memuat 4+ komponen, dan menulis narasi langkah demi langkah skenario (Pelanggan → Bayar → Resto → Kurir). | Kode Mermaid / File `.png` diagram, dan teks alur skenario di `README.md`. |
| **Haniel Juanta Sembiring** | 103072400145 | **Analisis Trade-off & Integrasi Peripheral**<br>Fokus: Merancang interaksi modul **Kurir/Notifikasi** & **Katalog Resto** (via Message Broker), serta menganalisis trade-off (misal: kompleksitas debugging, *eventual consistency*). | Paragraf analisis trade-off yang mendalam & koordinasi pengisian `JURNAL.md`. |

> **Catatan Penting:** Meskipun ada pembagian peran, **semua anggota WAJIB** me-review hasil kerja teman sebelum di-*push* untuk memastikan konsistensi antar bagian.

---

## 🔄 Alur Kerja (Workflow) Kelompok

Ikuti langkah ini agar proses rapi dan sesuai rubrik:

### Langkah 1: Brainstorming & Kerja Individu (Durasi: 1-2 Hari)
Setiap anggota mengerjakan bagiannya di `README.md`. 
- **Nuevalen:** Tentukan apakah kita pakai SOA murni, Pub-Sub murni, atau Hybrid (misal: SOA untuk Payment, Pub-Sub untuk Notifikasi). Tulis alasannya berdasarkan materi Bab 2 (misal: menghindari *temporal coupling*).
- **Farrellino:** Buat draft diagram. Pastikan ada panah yang jelas bertuliskan jenis komunikasi (misal: "HTTP Request/Response" atau "Publish Event: OrderCreated").
- **Haniel:** Tulis analisis trade-off. Jangan hanya tulis "lebih scalable". Tulis spesifik, misal: "Pub-Sub menghilangkan *blocking* pada modul pesanan, TAPI menambah kompleksitas debugging karena alur eksekusi tidak lagi linear (*eventual consistency*)."

### Langkah 2: Diskusi Kelompok & Revisi Diagram (Durasi: 30-45 Menit)
Lakukan panggilan singkat.
- Validasi diagram Farrellino: Apakah semua komponen (Pesanan, Pembayaran, Kurir, Katalog, Broker) sudah terhubung dengan benar sesuai alur yang dijelaskan Nuevalen dan Haniel?
- Diskusikan revisi. **Wajib** mencatat perubahan ini di `JURNAL.md` (misal: "Versi 1 diagram terlalu generik, Versi 2 ditambahi Message Broker eksplisit untuk decoupling").

### Langkah 3: Git Commit & Push (Wajib dari Laptop Masing-Masing)
Jangan biarkan 1 orang meng-*commit* semua pekerjaan. Contoh alur Git yang benar:

```bash
# 1. Nuevalen push bagian justifikasi & core service
git pull origin main
git add tugas-02-perancangan-arsitektur/README.md
git commit -m "Tugas 2: Nuevalen - Justifikasi arsitektur Hybrid (SOA+PubSub) & alur Order-Payment"
git push origin main

# 2. Farrellino push diagram & skenario
git pull origin main
git add tugas-02-perancangan-arsitektur/README.md tugas-02-perancangan-arsitektur/diagram/
git commit -m "Tugas 2: Farrellino - Penambahan diagram Mermaid & skenario end-to-end FoodGo"
git push origin main

# 3. Haniel push analisis trade-off & finalisasi jurnal
git pull origin main
git add tugas-02-perancangan-arsitektur/
git commit -m "Tugas 2: Haniel - Analisis trade-off decoupling, integrasi Notifikasi, & update JURNAL.md"
git push origin main
```

---

## ⚠️ Pengingat Penting (Berdasarkan Handbook & Rubrik)

1. **Diagram TIDAK BOLEH Generik:** Diagram yang terlihat seperti *copy-paste* dari tutorial internet tanpa penyesuaian konteks "FoodGo" (misal: nama komponen masih "Service A", "Service B") akan mendapat nilai rendah pada rubrik "Kelengkapan & Kejelasan Diagram" (30%).
2. **Tunjukkan Jenis Komunikasi:** Di diagram, wajib diberi label apakah itu *Synchronous (Request-Response)* atau *Asynchronous (Publish/Subscribe)*. Ini poin kunci dari materi Bab 2.
3. **Aturan AI (Level 2):** Boleh tanya AI: *"Apa trade-off umum dari arsitektur publish-subscribe dibanding RPC?"*. **DILARANG** meminta AI: *"Buatkan analisis trade-off untuk tugas FoodGo saya"*. Semua teks analisis harus ditulis ulang dengan bahasa sendiri dan dikaitkan spesifik ke skenario FoodGo.
4. **Isi Log AI:** Jika memakai AI untuk brainstorming, wajib isi tabel di `JURNAL.md`.

---

## 📝 Template Cepat untuk JURNAL.md (Silakan Diisi)

```markdown
## Diskusi Awal & Pembagian Tugas - [Tanggal]
- Peserta: Nuevalen, Farrellino, Haniel
- Keputusan Arsitektur: Kami memilih kombinasi SOA (untuk Pesanan-Pembayaran agar konsisten) dan Publish-Subscribe (untuk Notifikasi Kurir agar tidak blocking).
- Pembagian: Nuevalen (Justifikasi & Core), Farrellino (Diagram & Skenario), Haniel (Trade-off & Peripheral).

## Revisi Diagram (Versi 1 → Versi 2) - [Tanggal]
- Versi 1: Diagram hanya menampilkan koneksi langsung antar service (masih terlalu coupled).
- Versi 2: Menambahkan komponen eksplisit "Message Broker (RabbitMQ/Kafka)" di tengah. Alur notifikasi ke Kurir dan Resto diubah menjadi "Subscribe Event", bukan direct HTTP call.
- Alasan: Sesuai materi Bab 2, ini mengurangi *temporal coupling* dan *referential coupling*.

## Review Silang - [Tanggal]
- Farrellino mengomentari analisis Haniel: Menyarankan untuk menambahkan contoh konkret trade-off, misal: "Jika broker down, event OrderCreated hilang, perlu mekanisme Dead Letter Queue".
- Haniel mengomentari diagram Farrellino: Memastikan label panah sudah jelas membedakan "HTTP POST" (sinkron) dan "Publish Event" (asinkron).

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran AI | Bagaimana diolah jadi tulisan sendiri |
|---|---|---|---|---|
| [Tgl] | ChatGPT | "Jelaskan perbedaan temporal coupling dan referential coupling dalam konteks message queue" | Menjelaskan bahwa temporal coupling berarti pengirim dan penerima harus aktif di waktu yang sama. | Saya (Haniel) menggunakan konsep ini untuk memperkuat argumen kenapa FoodGo butuh Pub-Sub pada modul notifikasi kurir. |
```
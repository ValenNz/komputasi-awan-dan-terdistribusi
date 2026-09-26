# Jurnal Proses — Tugas 2

## 24 September 2026
**Kontribusi: Nuevalen Refitra Alswanfo (103072430008)**
- **Fokus Tugas**: Pemilihan Gaya Arsitektur & Core Services (Justifikasi SOA/Pub-Sub dan alur Order-Payment).
- **Analisis Awal**: Menganalisis masalah *coupling* pada sistem monolitik FoodGo menggunakan kerangka pikir Bab 2 (Temporal & Referential Coupling). Menyimpulkan bahwa *pure Pub-Sub* tidak cocok untuk pembayaran karena risiko *eventual consistency* pada transaksi finansial.
- **Keputusan Desain**: Merumuskan justifikasi mengapa kombinasi SOA (untuk transaksi kritis/sinkron) dan Pub-Sub (untuk notifikasi/asinkron) adalah solusi optimal untuk mencapai *decoupling* tanpa mengorbankan integritas data pembayaran.
- **Penulisan**: Menyusun paragraf justifikasi arsitektur dan deskripsi mendetail mengenai interaksi *blocking request-response* antara Order Service dan Payment Service di `README.md`.

## 26 September 2026
**Kontribusi: Haniel Juanta Sembiring (103072400145)**
- **Analisis Trade-Off**: menulikasan dan merumuskan analisis mendalam terkait trade-off dari arsitektur yang dipili oleh kami, seperti kompleksitas debugging, pelacakan eror yang tidak liner, dan masalah konsitensi data(eventual consitency).
- **Integrasi Peripheral**: Merancang dan menjelaskan bagaimana interaksi antara modul Kurir/Notifikasi dan Katalog Resto dilakukan secara asinkron menggunakan Message Broker.
- **Manajemen Administrasi Tugas**: Bertanggung jawab penuh atas koordinasi dan pengisian log kegiatan di dalam file.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

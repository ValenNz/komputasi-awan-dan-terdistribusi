### **Bagian 1: Penjelasan Mendetail Materi (Bab 2: Architectures)**
Berdasarkan PDF *Distributed Systems Chapter 02*, berikut adalah konsep kunci yang **sangat relevan** dengan tugas Anda:

1. **Architectural Styles (Gaya Arsitektur)**  
   Didefinisikan oleh komponen yang dapat diganti, cara komponen terhubung (connector), data yang dipertukarkan, dan konfigurasinya. Tujuannya adalah mengatur kompleksitas sistem.

2. **Service-Oriented Architecture (SOA) / RESTful**  
   - **Esensi**: Sistem dilihat sebagai kumpulan *resources* (sumber daya) yang dikelola oleh komponen terpisah.  
   - **Operasi**: Menggunakan operasi standar seperti `GET` (ambil data), `POST` (modifikasi), `PUT` (buat baru), `DELETE` (hapus).  
   - **Kaitan**: Memecah aplikasi monolitik menjadi layanan-layanan (services) kecil yang berdiri sendiri (misal: Service Pesanan, Service Pembayaran), sehingga bisa di-deploy secara independen.

3. **Coordination & Coupling (Kaitan & Ketergantungan)**  
   Ini adalah **jantung dari masalah FoodGo**. PDF membagi coupling menjadi dua dimensi:
   - **Referential Coupling**: Apakah pengirim pesan perlu tahu *siapa* penerimanya secara eksplisit?  
   - **Temporal Coupling**: Apakah pengirim dan penerima harus *aktif pada waktu yang sama*?  
   - **Publish-Subscribe (Event-based)** berada di kategori **Referentially Decoupled** (penerbit event tidak perlu tahu siapa yang berlangganan) dan bisa **Temporally Decoupled** (jika menggunakan Message Broker, pesan disimpan sampai penerima siap).

4. **Publish-Subscribe Architectures**  
   - **Esensi**: Komponen mem-*publish* event ke *message broker*, dan komponen lain yang *subscribe* (berlangganan) ke topik tertentu akan menerima event tersebut.  
   - **Contoh di PDF**: Linda tuple space, di mana proses menulis (`out`) dan membaca (`rd`/`in`) data dari ruang bersama tanpa perlu tahu proses mana yang menulis/membaca.

5. **Middleware & Broker**  
   Menggunakan broker (seperti Message Broker) mengurangi kompleksitas integrasi dari $O(N^2)$ (jika semua saling terhubung langsung) menjadi $O(N)$ (semua terhubung ke satu broker).

---

### **Bagian 2: Kaitan Materi dengan Tugas 2 (FoodGo)**
**Masalah di Tugas 1**: FoodGo saat ini **monolitik**. Artinya, semua modul (pesanan, pembayaran, notifikasi, katalog) terikat erat (*tightly coupled*). Jika tim kurir ingin update modulnya, seluruh aplikasi harus restart → *downtime* total. Ini adalah contoh ekstrem dari **Temporal & Referential Coupling**.

**Maksud Tugas 2**: Dosen ingin Anda mendesain ulang sistem ini agar menjadi **decoupled** (terlepas) menggunakan gaya arsitektur yang dipelajari di Bab 2.  
- Jika memilih **SOA**, Anda memisahkan modul menjadi layanan mandiri yang berkomunikasi via API (misal: REST/HTTP).  
- Jika memilih **Publish-Subscribe**, Anda memisahkan modul menggunakan *event* (misal: "PesananDibuat"), sehingga modul Kurir dan Resto bisa bereaksi tanpa saling menunggu atau tahu keberadaan satu sama lain.  
- **Kombinasi (Sangat Direkomendasikan)**: Gunakan SOA untuk proses yang butuh kepastian langsung (sinkron, seperti Pembayaran), dan Pub-Sub untuk proses yang bisa berjalan di latar belakang (asinkron, seperti Notifikasi Kurir & Resto).

---

### **Bagian 3: Panduan Mengerjakan Tugas 2 (Langkah demi Langkah)**

#### **Langkah 1: Pemilihan Gaya Arsitektur & Justifikasi**
Pilih **Kombinasi SOA + Publish-Subscribe**.  
**Justifikasi**:  
- Sistem FoodGo membutuhkan *decoupling* agar tim bisa deploy secara independen (mengatasi masalah monolitik).  
- **SOA (RESTful)** digunakan untuk interaksi *request-response* yang membutuhkan kepastian langsung (sinkron), misalnya: Pelanggan meminta pembayaran → Service Pembayaran memproses dan langsung mengembalikan status "Sukses/Gagal".  
- **Publish-Subscribe** digunakan untuk alur kerja yang tidak perlu menunggu (asinkron). Ketika pesanan sukses dibuat, Service Pesanan hanya perlu *publish* event `OrderCreated`. Service Katalog Resto dan Service Notifikasi Kurir akan *subscribe* ke event ini. Mereka tidak perlu tahu satu sama lain (*referentially decoupled*) dan tidak harus aktif di detik yang sama jika ada antrian (*temporally decoupled* berkat Message Broker).

#### **Langkah 2: Diagram Arsitektur (Mermaid)**
*Catatan: Diagram ini dibuat spesifik untuk FoodGo, bukan contoh generik, untuk memenuhi kriteria rubrik.*

```mermaid
graph TD
    %% Aktor
    Customer((Pelanggan))
    Courier((Kurir))
    Restaurant((Resto))

    %% Komponen Utama (Services)
    OrderSvc[Service Pesanan<br/>(Order Service)]
    PaymentSvc[Service Pembayaran<br/>(Payment Service)]
    CatalogSvc[Service Katalog Resto<br/>(Catalog Service)]
    CourierNotifSvc[Service Notifikasi Kurir<br/>(Courier Service)]

    %% Middleware
    Broker[(Message Broker<br/>RabbitMQ/Kafka)]
    APIGW[API Gateway]

    %% Interaksi Pelanggan (Sinkron / SOA)
    Customer -->|1. HTTP POST /orders| APIGW
    APIGW -->|2. Forward Request| OrderSvc
    OrderSvc -->|3. HTTP POST /charge (Sinkron)| PaymentSvc
    PaymentSvc -->|4. Response: Payment Success| OrderSvc

    %% Interaksi Event-Driven (Asinkron / Pub-Sub)
    OrderSvc -->|5. Publish Event: 'OrderCreated'| Broker
    
    %% Subscriber 1: Resto
    Broker -->|6. Subscribe Topik: 'Order.Created'| CatalogSvc
    CatalogSvc -->|7. Update status pesanan di dashboard| Restaurant
    
    %% Subscriber 2: Kurir
    Broker -->|8. Subscribe Topik: 'Order.Created'| CourierNotifSvc
    CourierNotifSvc -->|9. Push notification ke aplikasi| Courier

    %% Styling agar rapi
    classDef service fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef broker fill:#fff3e0,stroke:#e65100,stroke-width:2px,stroke-dasharray: 5 5;
    classDef actor fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    
    class OrderSvc,PaymentSvc,CatalogSvc,CourierNotifSvc,APIGW service;
    class Broker broker;
    class Customer,Courier,Restaurant actor;
```

#### **Langkah 3: Alur Skenario End-to-End**
Jelaskan diagram di atas dengan narasi berikut di `README.md`:
1. **Pelanggan membuat pesanan**: Pelanggan mengirim *HTTP Request* (sinkron) ke API Gateway, yang meneruskannya ke **Service Pesanan**.
2. **Proses Pembayaran**: Service Pesanan memanggil **Service Pembayaran** melalui *RPC/HTTP Request* (sinkron). Service Pembayaran memvalidasi dan mengembalikan respons "Sukses".
3. **Penerbitan Event**: Setelah pembayaran sukses, Service Pesanan tidak langsung memanggil Resto/Kurir. Sebaliknya, ia *publish* sebuah event `OrderCreated` (berisi ID pesanan, detail resto, lokasi) ke **Message Broker** (asinkron).
4. **Notifikasi Resto**: **Service Katalog Resto** yang *subscribe* ke topik `Order.Created` menerima event tersebut, lalu memperbarui dashboard resto dan mengirim notifikasi ke pemilik resto.
5. **Penugasan Kurir**: Secara paralel, **Service Notifikasi Kurir** yang juga *subscribe* ke topik yang sama menerima event, lalu mencari kurir terdekat dan mengirim *push notification* ke aplikasi kurir.

#### **Langkah 4: Analisis Trade-off (Poin Kritis untuk Nilai 30%)**
Jangan hanya memuji arsitektur ini. Sebutkan kekurangannya secara teknis berdasarkan materi:
- **Kelebihan (Mengatasi Coupling)**: 
  - *Referential Decoupling*: Service Pesanan tidak perlu tahu alamat IP atau keberadaan Service Kurir/Resto.
  - *Temporal Decoupling*: Jika Service Kurir sedang *down* atau di-*deploy* ulang, event `OrderCreated` tetap aman diantrekan di Message Broker dan akan diproses saat Service Kurir hidup kembali. Tidak ada *downtime* total.
- **Kekurangan / Trade-off**:
  1. **Kompleksitas Debugging**: Alur tidak lagi linear. Jika pesanan tidak sampai ke kurir, developer harus melacak log di Service Pesanan, lalu ke Message Broker, lalu ke Service Kurir (distributed tracing menjadi wajib).
  2. **Eventual Consistency**: Karena asinkron, ada jeda waktu (milidetik hingga detik) antara pembayaran sukses dan notifikasi muncul di resto. Sistem harus menangani kasus di mana pengguna menyegarkan halaman sebelum event diproses.
  3. **Single Point of Failure (SPOF)**: Message Broker menjadi komponen kritis. Jika broker mati, seluruh komunikasi asinkron terhenti (perlu solusi seperti cluster/high availability).

---

### **Bagian 4: Tips Mendapatkan Nilai Maksimal (Sesuai Rubrik)**

1. **Ketepatan Pemilihan (20%)**: Pastikan kata kunci dari PDF seperti *"decoupling"*, *"temporal"*, *"referential"*, dan *"asinkron"* muncul di justifikasi Anda.
2. **Kelengkapan Diagram (30%)**: Gunakan diagram Mermaid di atas (atau buat ulang di draw.io dengan gaya yang mirip). Pastikan panah memiliki label yang jelas menyebutkan **jenis komunikasi** (misal: "Sinkron: HTTP POST" atau "Asinkron: Publish Event"). *Hindari diagram kotak-kotak generik tanpa label spesifik FoodGo.*
3. **Analisis Trade-off (30%)**: Poin tentang "Eventual Consistency" dan "Distributed Tracing Complexity" akan menunjukkan bahwa Anda benar-benar memahami konsekuensi dari arsitektur terdistribusi, bukan hanya menyalin teori.
4. **Proses & JURNAL.md (20%)**: Buat file `JURNAL.md` yang berisi log pembagian tugas. Contoh:
   ```markdown
   ## Jurnal Kegiatan Kelompok
   - [Tanggal] - Anggota A: Riset materi Bab 2 (SOA & Pub-Sub) dan penyusunan justifikasi.
   - [Tanggal] - Anggota B: Pembuatan diagram Mermaid dan penyesuaian alur end-to-end.
   - [Tanggal] - Anggota C: Penulisan analisis trade-off dan review akhir README.md.
   ```
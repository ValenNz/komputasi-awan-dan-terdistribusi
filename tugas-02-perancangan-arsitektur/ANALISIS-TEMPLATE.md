# Tugas 1 — Analisis ***** FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 | - **Fokus Tugas**: Pemilihan Gaya Arsitektur & Core Services (Justifikasi SOA/Pub-Sub dan alur Order-Payment).
- **Analisis Awal**: Menganalisis masalah *coupling* pada sistem monolitik FoodGo menggunakan kerangka pikir Bab 2 (Temporal & Referential Coupling). Menyimpulkan bahwa *pure Pub-Sub* tidak cocok untuk pembayaran karena risiko *eventual consistency* pada transaksi finansial.
- **Keputusan Desain**: Merumuskan justifikasi mengapa kombinasi SOA (untuk transaksi kritis/sinkron) dan Pub-Sub (untuk notifikasi/asinkron) adalah solusi optimal untuk mencapai *decoupling* tanpa mengorbankan integritas data pembayaran.
- **Penulisan**: Menyusun paragraf justifikasi arsitektur dan deskripsi mendetail mengenai interaksi *blocking request-response* antara Order Service dan Payment Service di `README.md`.  |


| Haniel Juanta Sembiring | 103072400145 | - **Analisis Trade-Off**: menulikasan dan merumuskan analisis mendalam terkait trade-off dari arsitektur yang dipili oleh kami, seperti kompleksitas debugging, pelacakan eror yang tidak liner, dan masalah konsitensi data(eventual consitency).
- **Integrasi Peripheral**: Merancang dan menjelaskan bagaimana interaksi antara modul Kurir/Notifikasi dan Katalog Resto dilakukan secara asinkron menggunakan Message Broker.
- **Manajemen Administrasi Tugas**: Bertanggung jawab penuh atas koordinasi dan pengisian log kegiatan di dalam file. |


| Farrellino Ulung Satya Amando | 103072400005 | - **Visualisasi Diagram**: Merancang dan memfinalisasi diagram arsitektur terdesentralisasi FoodGo yang merepresentasikan transisi dari sistem monolitik ke hibrida (SOA & Pub-Sub). Diagram ini mencakup komponen Client, Order Service, Payment Service, Message Broker, Catalog Service (Resto), dan Notification Service (Kurir) dengan pelabelan komunikasi sinkron dan asinkron yang jelas.
- **Skenario End-to-End**: Menyusun narasi alur transaksi lengkap langkah demi langkah mulai dari permintaan pemesanan awal oleh pelanggan, validasi pembayaran sinkron, hingga publikasi event asinkron melalui Message Broker ke layanan restoran dan kurir.|


## 1. Pemilihan Gaya Arsitektur dan Justifikasi

Kami memilih **kombinasi Service-Oriented Architecture (SOA) dan Publish-Subscribe** untuk mengatasi *tight coupling* pada sistem monolitik FoodGo. **SOA** digunakan pada proses utama yang membutuhkan respons langsung dan konsistensi data, seperti komunikasi antara **Order Service** dan **Payment Service**. Sementara itu, **Publish-Subscribe** digunakan untuk proses asinkron seperti notifikasi kepada Resto dan Kurir. Penggunaan *Message Broker* membuat komunikasi lebih *decoupled* karena antarmodul tidak perlu saling mengetahui alamat maupun harus aktif secara bersamaan.

## 2. Skenario end-to-end Sistem dengan Arsiteltur Ini 

1. **Inisiasi Pesanan (Pelanggan → Order Service)**
* Pelanggan melakukan pemesanan melalui aplikasi, yang mengirimkan **1. Pesan (HTTP Request)** secara sinkron ke **Order Service (SOA/Sinkron)** untuk mencatat transaksi awal.


2. **Pemrosesan Pembayaran dan Validasi Pembayaran (Order Service ⇄ Payment Service)**
* Untuk memastikan integritas finansial dan menghindari masalah eventual consistency, Order Service mengirimkan **2. Request Pembayaran (Sinkron)** ke **Payment Service (SOA/Sinkron)**.
* Setelah pembayaran divalidasi, Payment Service mengembalikan respons **3. Status: Berhasil (Sinkron)** ke Order Service.


3. **Distribusi Event Asinkron (Order Service → Message Broker)**
* Setelah pembayaran sukses, Order Service melakukan publish event dengan mengirimkan **4. Publish Event: 'OrderCreated'** secara asinkron ke **Message Broker (Pub-Sub/Asinkron)** supaya tidak terjadi blocking pada main service.


4. **Konsumsi Event oleh Periferal (Message Broker → Catalog & Notification Service)**
* **Catalog Service (Resto)** akan menerima event dengan melakukan **5. Subscribe 'OrderCreated'** untuk memproses pembuatan makanan di sisi restoran.
* Di saat yang bersamaan, **Notification Service (Kurir)** juga melakukan **6. Subscribe 'OrderCreated'** untuk mempersiapkan tugas penjemputan dan pengiriman bagi kurir secara asinkron.

## 3. Alur Skenario *End-to-End*: Order-Payment

Kami menggunakan komunikasi **sinkron (*Request-Response*)** antara **Order Service** dan **Payment Service**. Pelanggan melakukan pemesanan → Order Service mengirim permintaan pembayaran → Payment Service memproses dan mengembalikan status pembayaran → jika berhasil, Order Service menerbitkan *event* `OrderCreated` ke *Message Broker* untuk diproses oleh layanan lain.

## 4. Solusi Coupling dan Analisis Trade Off 

Gaya yang menggunakan Publish Subscribe yang melalui message broker digunakan pada modul notifikasi kurir dan katalog resto. Gaya ini efektif mengatasi masalah tight coupling dari aplikasi monolitik seperto FoodGo karena menciptakan Decoupling pada dua dimensi utama:
    
    1. Referential Decoupling: sesuai dengan diagram Order Service hanya bertugas melempar sebuah event ke broker, tanpa perlu mengetahui ip addres, end point sehingga tidak terlalu mempedulikan lokasi dari layanan kurir benar-benar ada disana atau tidak. Broker bertanggu jawab untuk proses pengiriman.

    2. Temporal Decoupling: Pengirim event yaitu Order Service dan penerima event seperti kurir atau resto tidak harus aktif di waktu yang sama. jadi mungkin ketika service kurir down berarti pesanan langganan tidak masuk, tetapi dengan ada nya temporal decoupling, maka event pesanan yang terkirim hanya tertunda. ketika layanan menjadi normal, maka pesanan akan terkirim jadi tidak hilang begitu saja. pessanan tersebut menjadi antrean message broker, dan kemudian ditarik subscribe ketika layanan normal.

**Trade off** 

Meskipun arsitektur ini mempermudah skalabilitas dan kemadirian tiap modul, ada beberapa kelemahan baru yang muncul, yakni:

    1. Kompleksitas Debugging dan Tracing yang Tinggi: Alur sistem tidak berjalan secara linear seperti modul monolitik. Jika misal pelanggan mengeluh kalau kurir tidak datang, penelusuran eror sangat menyusahkan karena developer harus mengecek log pesanan terpisah seperti di Order Service, kemudian Message Broker, dan selanjutnya Notification Service. Hal di atas mewajibkan implementasi Distributed Tracing, seperti penambahan ID unik di setiap header event.

    2. Eventual Consistency: Sistem Pub-Sub tidak berfungsi penuh dalam transaksi sinkron. Pub-Sub memiliki kelebihan sifat asynchronous yang dapat dipastika kalau ini memiliki latensi, berbeda dengan modul monolitik, contoh ketika modul pembayaran yang muncul di HP pelanggan dan tablet restoran. Tantangan yang muncul sekarang bagaimana cara mengatasi masalah data belum sinkron seutuhnya di momen tertentu.

    3. Ancama Single Point of Failure(SPOF) pada Broker: arsitektur yang sebelumnya kita rancang dapat menjadi mandiri namun, ia menempatkan beban kritis pada Message Broker. Apabila software broker lumpuh total, seluruh backbone dari komunikasi asynchronous yang menjadi kelebihan akan hancur bahkan aplikasi tidak bisa dijalankan. tim dituntut menjamin keandalan broker.




### Alasan Menggunakan Komunikasi Sinkron

Kami memilih komunikasi sinkron karena pembayaran membutuhkan **respons dan kepastian status secara langsung**. Jika menggunakan komunikasi asinkron, status pesanan dan pembayaran berpotensi tidak konsisten karena pembayaran dapat belum selesai ketika pesanan sudah tercatat. Oleh karena itu, **SOA digunakan untuk transaksi kritis**, sedangkan **Publish-Subscribe digunakan untuk proses lanjutan yang tidak membutuhkan respons langsung**.

---

## Kesimpulan Kelompok
Perancangan arsitektur hibrida yang memadukan Service-Oriented Architecture (SOA) dan Publish-Subscribe pada sistem FoodGo memberikan nilai tambah yang signifikan dalam hal fleksibilitas operasional dan ketahanan sistem. Pendekatan ini merupakan solusi untuk menangani  tight coupling melalui temporal dan referential decoupling, di mana modul perifer seperti restoran dan kurir dapat berjalan secara mandiri dan asinkron tanpa membebani layanan utama. 

Selain itu, integritas finansial juga akan tetap terjaga secara optimal melalui komunikasi sinkron yang ketat antara layanan Order dan Payment. Arsitektur ini mempunyai sedikit kelemahan yaitu peningkatan kompleksitas debugging karena alur eksekusi yang tidak lagi linier dan juga ketergantungan operasional pada Message Broker. Walaupun begit, manfaat skalabilitas dan konsistensi data yang didapatkan tetap jauh lebih unggul yang membuat model hybrid ini solusi yang efektif untuk masalah dari sistem FoodGo.
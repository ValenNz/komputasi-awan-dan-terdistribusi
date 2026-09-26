# Tugas 1 — Analisis ***** FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 |  |
| Farrellino Ulung Satya Amando | 103072400005 |  |
| Haniel Juanta Sembiring | 103072400145 |  |

## 1. Pemilihan Gaya Arsitektur dan Justifikasi

Kami memilih **kombinasi Service-Oriented Architecture (SOA) dan Publish-Subscribe** untuk mengatasi *tight coupling* pada sistem monolitik FoodGo. **SOA** digunakan pada proses utama yang membutuhkan respons langsung dan konsistensi data, seperti komunikasi antara **Order Service** dan **Payment Service**. Sementara itu, **Publish-Subscribe** digunakan untuk proses asinkron seperti notifikasi kepada Resto dan Kurir. Penggunaan *Message Broker* membuat komunikasi lebih *decoupled* karena antarmodul tidak perlu saling mengetahui alamat maupun harus aktif secara bersamaan.

## 2.

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
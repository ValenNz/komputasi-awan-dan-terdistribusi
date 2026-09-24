# Tugas 1 — Analisis ***** FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 |  |
| Farrellino Ulung Satya Amando | 103072400005 |  |
| Haniel Juanta Sembiring | 103072400145 |  |

## 1. Pemilihan Gaya Arsitektur & Justifikasi (Oleh: Nuevalen Refitra Alswanfo)
Berdasarkan materi Bab 2 (*Distributed Systems*), sistem monolitik FoodGo saat ini mengalami *tight coupling* yang parah, baik secara **temporal** (seluruh modul harus aktif bersamaan) maupun **referential** (modul harus tahu alamat internal satu sama lain). Untuk mengatasinya, kami memilih **Kombinasi Service-Oriented Architecture (SOA) dan Publish-Subscribe**.

**Justifikasi Pemilihan:**
1. **SOA (RESTful/Request-Response)** dipilih khusus untuk menangani *core services* yang membutuhkan kepastian state secara langsung (*strong consistency*), seperti interaksi antara modul Pesanan dan Pembayaran.
2. **Publish-Subscribe (Event-Driven)** dipilih untuk menangani proses latar belakang (*background tasks*) seperti notifikasi ke Resto dan Kurir. Dengan adanya *Message Broker* sebagai *middleware*, modul Pesanan menjadi:
   - *Referentially Decoupled*: Tidak perlu tahu alamat IP atau keberadaan Service Kurir/Resto.
   - *Temporally Decoupled*: Service Kurir/Resto tidak harus sedang *online* saat event dipublikasikan. Jika sedang di-*deploy* ulang, pesan akan aman diantrekan di broker, sehingga **menghilangkan risiko downtime total** seperti pada sistem monolitik.

## 3. Alur Skenario End-to-End: Fokus Interaksi Order-Payment (Oleh: Nuevalen Refitra Alswanfo)
Interaksi antara **Modul Pesanan (Order Service)** dan **Modul Pembayaran (Payment Service)** dirancang secara ketat menggunakan pola komunikasi **Sinkron (Request-Response)** berbasis SOA (misalnya, HTTP POST/REST atau gRPC).

- **Mekanisme Alur**: 
  1. Pelanggan mengonfirmasi pesanan di *frontend*.
  2. **Order Service** mengirimkan permintaan pembayaran secara langsung (*direct call*) ke **Payment Service**.
  3. **Order Service** memasuki keadaan *blocking* (menunggu) hingga **Payment Service** mengembalikan respons eksplisit (misalnya: `HTTP 200 OK` dengan status "LUNAS" atau `HTTP 402` jika dana tidak cukup).
  4. Hanya jika responsnya "Sukses", Order Service akan melanjutkan ke langkah berikutnya, yaitu mem-*publish* event `OrderCreated` ke Message Broker (Asinkron).

- **Mengapa Harus Sinkron (Bukan Asinkron/Pub-Sub)?**: 
   Proses pembayaran adalah transaksi bisnis kritis yang membutuhkan *immediate feedback*. Jika kita menggunakan Pub-Sub (asinkron) untuk pembayaran, sistem akan mengalami *eventual consistency* yang berisiko tinggi: pesanan bisa saja tercatat "dibuat" di database padahal pembayaran sebenarnya gagal, atau pelanggan terjebak dalam ketidakpastian tanpa status transaksi yang *real-time*. Oleh karena itu, *temporal coupling* pada bagian inti ini justru **diperlukan dan tepat** diselesaikan dengan pola SOA, sementara *decoupling* hanya diterapkan pada tahap notifikasi selanjutnya.

---

## Kesimpulan Kelompok
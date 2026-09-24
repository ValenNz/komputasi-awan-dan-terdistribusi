# Tugas 1 — Analisis ***** FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 |  |
| Farrellino Ulung Satya Amando | 103072400005 |  |
| Haniel Juanta Sembiring | 103072400145 |  |

## 1. Pemilihan Gaya Arsitektur dan Justifikasi

Kami memilih **kombinasi Service-Oriented Architecture (SOA) dan Publish-Subscribe** untuk mengatasi *tight coupling* pada sistem monolitik FoodGo. **SOA** digunakan pada proses utama yang membutuhkan respons langsung dan konsistensi data, seperti komunikasi antara **Order Service** dan **Payment Service**. Sementara itu, **Publish-Subscribe** digunakan untuk proses asinkron seperti notifikasi kepada Resto dan Kurir. Penggunaan *Message Broker* membuat komunikasi lebih *decoupled* karena antarmodul tidak perlu saling mengetahui alamat maupun harus aktif secara bersamaan.

## 3. Alur Skenario *End-to-End*: Order-Payment

Kami menggunakan komunikasi **sinkron (*Request-Response*)** antara **Order Service** dan **Payment Service**. Pelanggan melakukan pemesanan → Order Service mengirim permintaan pembayaran → Payment Service memproses dan mengembalikan status pembayaran → jika berhasil, Order Service menerbitkan *event* `OrderCreated` ke *Message Broker* untuk diproses oleh layanan lain.

### Alasan Menggunakan Komunikasi Sinkron

Kami memilih komunikasi sinkron karena pembayaran membutuhkan **respons dan kepastian status secara langsung**. Jika menggunakan komunikasi asinkron, status pesanan dan pembayaran berpotensi tidak konsisten karena pembayaran dapat belum selesai ketika pesanan sudah tercatat. Oleh karena itu, **SOA digunakan untuk transaksi kritis**, sedangkan **Publish-Subscribe digunakan untuk proses lanjutan yang tidak membutuhkan respons langsung**.

---

## Kesimpulan Kelompok
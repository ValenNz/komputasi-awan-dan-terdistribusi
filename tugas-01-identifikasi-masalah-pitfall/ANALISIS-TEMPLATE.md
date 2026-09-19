# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 | Pitfall 1: "The network is reliable" |
| Farrellino Ulung Satya Amando | 103072400005 | Pitfall 2: "Latency is zero" |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: *“The network is reliable”*

### Analisis Kami

Berdasarkan skenario FoodGo, kami menemukan adanya asumsi bahwa **jaringan antar-service selalu dapat diandalkan**. Hal ini terlihat dari kode yang menggunakan komentar:

> *“network is always reliable, no need for retry”*

Selain itu, pada pemanggilan antara **modul pesanan dan modul pembayaran** tidak terdapat timeout, sehingga modul pesanan dapat menunggu respons dari modul pembayaran tanpa batas waktu.

Menurut analisis kami, kondisi tersebut merupakan bentuk **fallacy “The network is reliable”** karena sistem menganggap komunikasi antar-service akan selalu berhasil, padahal dalam sistem terdistribusi kegagalan komunikasi dapat terjadi sewaktu-waktu.

### Mengapa Menjadi Masalah?

Kami melihat bahwa masalah utamanya bukan hanya ketika jaringan gagal, tetapi **bagaimana FoodGo menangani kegagalan tersebut**.

Misalnya, ketika modul pembayaran mengalami overload pada saat promo atau jam makan siang, respons pembayaran dapat menjadi sangat lambat. Karena tidak terdapat timeout, modul pesanan akan terus menunggu respons tersebut.

Kondisi tersebut dapat menyebabkan:

**Modul Pembayaran lambat → Modul Pesanan ikut menunggu → banyak request menumpuk → resource/thread habis → request baru ikut lambat atau gagal**

Dengan demikian, menurut analisis kami, **satu masalah pada modul pembayaran dapat berdampak ke modul lain**. Hal ini sesuai dengan gejala pada skenario, yaitu aplikasi menjadi sangat lambat dan beberapa permintaan mengalami timeout.

Kami juga melihat bahwa ketiadaan retry membuat kegagalan sementara berpotensi langsung dianggap sebagai kegagalan transaksi. Padahal, gangguan jaringan atau service bisa saja hanya terjadi sesaat.

### Dampak pada FoodGo

Dari skenario tersebut, kami menganalisis beberapa dampak:

1. **Request dapat menggantung terlalu lama**
   Modul pesanan tidak memiliki batas waktu ketika menunggu respons pembayaran.

2. **Resource modul pesanan dapat terkuras**
   Semakin banyak request yang menunggu, semakin banyak resource yang digunakan sehingga request lainnya ikut terdampak.

3. **Terjadi efek berantai (*cascading failure*)**
   Gangguan pada modul pembayaran dapat menyebabkan modul pesanan ikut mengalami penurunan performa.

4. **Pengguna mengalami kegagalan atau keterlambatan transaksi**
   Pengguna dapat melihat proses checkout sangat lambat atau gagal meskipun gangguan awal hanya terjadi pada komunikasi antar-service.

5. **Beban service pembayaran dapat semakin meningkat**
   Jika sistem terus mengirim request ketika service pembayaran sedang bermasalah, proses pemulihan dapat menjadi semakin sulit.

### Solusi yang Kami Usulkan

Berdasarkan analisis tersebut, kami mengusulkan beberapa mekanisme:

**1. Timeout**

Setiap komunikasi antara modul pesanan dan pembayaran perlu memiliki batas waktu. Misalnya, setelah beberapa detik tidak mendapatkan respons, request dihentikan sehingga resource tidak terus terpakai.

**2. Retry dengan Exponential Backoff dan Jitter**

Untuk kegagalan yang bersifat sementara (*transient failure*), sistem dapat mencoba kembali request secara terbatas. Jarak antar percobaan dibuat semakin panjang dan diberi *jitter* agar banyak request tidak melakukan retry secara bersamaan.

**3. Circuit Breaker**

Jika modul pembayaran terus mengalami kegagalan, modul pesanan dapat menghentikan sementara pemanggilan ke modul tersebut. Dengan begitu, service pembayaran memiliki kesempatan untuk pulih dan sistem tidak terus memberikan beban tambahan.

**4. Idempotency**

Karena retry pada proses pembayaran memiliki risiko request yang sama diproses lebih dari sekali, kami juga menilai perlu adanya **idempotency key**. Mekanisme ini membantu memastikan satu transaksi tidak diproses atau ditagihkan berulang kali ketika terjadi retry.

### Trade-off yang Kami Pertimbangkan

Kami juga menemukan bahwa solusi tersebut tidak bisa diterapkan tanpa mempertimbangkan konsekuensinya.

* **Timeout terlalu pendek** dapat membuat transaksi yang sebenarnya masih diproses dianggap gagal.
* **Retry** dapat menambah beban service jika dilakukan terlalu sering atau tanpa *backoff*.
* **Circuit breaker** dapat membuat sementara waktu pengguna tidak dapat melakukan pembayaran ketika circuit dalam kondisi *open*.
* **Idempotency** menambah kompleksitas pada desain dan implementasi modul pembayaran.

Karena itu, menurut analisis kami, solusi yang tepat bukan sekadar **menambahkan retry**, tetapi membuat komunikasi antar-service memiliki mekanisme **timeout, retry yang terkontrol, circuit breaker, dan idempotency** sesuai karakteristik proses pembayaran.

---

## Pitfall 2: "Latency is Zero"

### Analisis Kami
Berdasarkan skenario FoodGo, kami menemukan adanya asumsi bahwa pemanggilan antar-service berjalan secara instan. Hal ini terlihat jelas dari :

"...tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)."

Padahal, terdapat beberapa permintaan timeout di saat waktu pesanan melonjak. Menurut analisis kami, ini termasuk ke bentuk fallacy “Latency is zero” karena menganggap pengiriman data ke layanan lain dan responsenya tidak membutuhkan waktu sehingga modul dibiarkan menunggu tanpa batas waktu.

### Mengapa Menjadi Masalah?
Kami melihat bahwa masalah utamanya terletak pada konsep komunikasi selalu membutuhkan waktu (latensi), apalagi jika melibatkan pihak ketiga seperti payment gateway, diabaikan begitu saja. 

Misalnya, ketika modul pembayaran melambat akibat lonjakan trafik saat promo, latensi responsnya meningkat drastis. Karena modul pesanan tidak memiliki timeout, setiap proses yang bertugas melayani pelanggan akan tertahan saat memanggil layanan pembayaran.

Kondisi tersebut dapat menyebabkan:

Modul pembayaran lambat yang tentunya diikuti dengan respons memakan waktu lama (latensi tinggi). Ini akan menyebabkan thread modul pesanan tertahan sehingga request baru terus berdatangan dan menumpuk. Thread pool akan habis dan server crash. 

### Dampak pada FoodGo
Dari skenario tersebut, kami menganalisis beberapa dampak spesifik:

1. **Thread server terkuras habis (Thread Exhaustion)**
Modul pesanan yang memanggil modul pembayaran dibiarkan menunggu tanpa batas waktu, sehingga resource memori/proses pada server tertahan dan terkuras habis saat trafik naik.

2. **Aplikasi menjadi sangat lambat**
Karena antrean request menumpuk di server yang resource-nya hampir habis, pengguna merasakan loading aplikasi yang sangat lama.

3. **Beberapa permintaan mengalami timeout di sisi pengguna**
Meskipun kode internal tidak memiliki timeout, koneksi dari aplikasi (device pengguna) ke server FoodGo pada akhirnya akan terputus karena terlalu lama menunggu respons dari server yang macet.

4. **Server backend crash total**
Habisnya resource akibat tumpukan request yang menggantung menyebabkan server tidak bisa lagi beroperasi sehingga mati dan operasional down hingga dilakukan restart manual.

### Solusi yang Kami Usulkan
Karena permasalahan yang telah dijelaskan sebelumnya, kami mengusulkan sistem diperbaiki dengan:

1. Timeout yang Ketat

Setiap komunikasi antar-modul (terutama ke modul pembayaran) wajib memiliki batas waktu yang spesifik, misalnya 5 hingga 7 detik. Jika tidak ada respons, koneksi diputus secara paksa agar thread server terbebas dan bisa melayani request lain.

2. Komunikasi Asinkron

Sebagai alternatif jangka panjang, daripada menunggu respons pembayaran secara sinkron, modul pesanan dapat menaruh pesan ke Message Broker (seperti RabbitMQ/Kafka). Sistem tidak perlu saling menunggu, dan proses pembayaran dikerjakan di latar belakang. Modul pesanan langsung bebas melayani pelanggan lain, sementara modul pembayaran mengambil pesan dari antrean tersebut dan memprosesnya di latar belakang sesuai kapasitasnya.

3. Webhooks untuk Komunikasi Asinkron Pihak Bank ke Server

Karena pemrosesan di pihak bank/e-wallet memerlukan waktu (latensi > 0), modul pembayaran tidak perlu menggantung koneksi ke bank. Setelah transaksi dikirim, koneksi diputus. Ketika bank selesai memproses pembayaran di sistem mereka, payment gateway akan mengirimkan notifikasi otomatis secara asinkron via Webhook kembali ke server FoodGo.

### Trade-off yang Kami Pertimbangkan
trade-off teknis dan operasional yang harus ditangani oleh sistem dari masing-masing solusi:

1. Konsekuensi dari Timeout yang Ketat

Inkonsistensi Status Data: 
Jika koneksi diputus paksa pada detik ke-7, modul pesanan berada dalam ketidakpastian. Sistem tidak tahu apakah pemotongan saldo di bank sebenarnya sudah berhasil namun responsnya terlambat, atau memang transaksinya gagal.

Kewajiban Membangun Sistem Rekonsiliasi: 
Untuk mengatasi inkonsistensi di atas, tim harus membangun program tambahan (background job) yang bertugas mengecek ulang ke pihak bank secara berkala untuk mencocokkan status akhir transaksi yang terkena timeout, guna mencegah pelanggan dirugikan (misalnya: saldo terpotong tetapi pesanan telanjur digagalkan oleh sistem).

2. Konsekuensi dari Komunikasi Asinkron (Message Broker)

Perubahan Pengalaman Pengguna: 
Karena pemrosesan diletakkan di latar belakang, pelanggan tidak bisa lagi mendapatkan layar "Sukses" secara instan. Tim frontend harus mengubah antarmuka aplikasi untuk menangani status transisi ("Pesanan Anda Sedang Diproses"), yang bisa menurunkan kenyamanan pengguna yang terbiasa dengan respons seketika.

Risiko Pemrosesan Ganda: 
Sistem Message Broker umumnya menjamin pengiriman pesan minimal satu kali (at-least-once delivery), sehingga ada risiko pesan yang sama tersalurkan dua kali akibat fluktuasi jaringan. Modul pembayaran wajib mengimplementasikan Idempotency (kunci unik per transaksi) agar pelanggan tidak tertagih dua kali untuk pesanan yang sama.

3. Konsekuensi dari Penggunaan Webhooks Bank
Risiko Notifikasi Hilang:
Jika bank mengirimkan Webhook tepat ketika server FoodGo sedang mengalami downtime atau restart singkat, notifikasi tersebut akan gagal diterima. Akibatnya, status transaksi pelanggan akan menggantung selamanya. Sistem tetap memerlukan mekanisme fallback (seperti melakukan polling otomatis setiap 10 menit) khusus untuk mengambil data transaksi yang Webhook-nya gagal masuk.


---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]



**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]

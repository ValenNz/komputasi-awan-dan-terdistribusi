# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 | Pitfall 1: "The network is reliable" |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
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

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]



**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]

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

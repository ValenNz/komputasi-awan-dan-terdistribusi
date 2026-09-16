# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Nuevalen Refitra Alswanado | 103072430008 | Pitfall 1: "The network is reliable" |
| [nama 2] | [nim] | [pitfall/bagian yang dikerjakan] |
| [nama 3] | [nim] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: [nama pitfall] — ditulis oleh [nama]

## Pitfall 1: *"The network is reliable"* — ditulis oleh Nuevalen Refitra Alswanado

**Bukti di skENARIO:**
Pada deskripsi FoodGo tertulis secara eksplisit:
> *"Tim menemukan bahwa kode mereka menulis asumsi seperti `# network is always reliable, no need for retry` dan tidak ada timeout sama sekali pada pemanggilan antar service (modul pesanan memanggil modul pembayaran dan menunggu tanpa batas waktu)."*

Komentar `no need for retry` dan ketiadaan timeout adalah manifestasi langsung dari fallacy pertama Peter Deutsch: mengasumsikan jaringan antar-service (dalam hal ini antara modul pesanan dan modul pembayaran di FoodGo) selalu bisa diandalkan untuk menghantarkan request dan response.

**Kenapa ini keliru:**
Dalam sistem terdistribusi nyata, jaringan **tidak pernah** 100% reliable. Ada banyak penyebab kegagalan yang berada di luar kendali aplikasi:
- *Packet loss* karena kongesti di router/switch antar-rack atau antar-datacenter.
- *Transient failure*: server pembayaran sedang GC pause, restart, atau overload sesaat.
- *TCP connection reset* oleh load balancer atau firewall karena idle terlalu lama.
- *DNS resolution failure* sesaat saat service discovery refresh.
- *Partial failure*: hanya satu replica dari service pembayaran yang bermasalah, bukan semuanya.

Mengasumsikan jaringan selalu reliable berarti mengabaikan kenyataan bahwa kegagalan itu **normal dan pasti terjadi**, terutama saat trafik FoodGo melonjak (jam makan siang / promo besar) — persis skenario yang dilaporkan.

**Dampak ke FoodGo:**
Karena tidak ada timeout dan tidak ada retry, yang terjadi di FoodGo adalah mekanisme kegagalan berantai (*cascading failure*) seperti ini:
1. Modul pesanan memanggil modul pembayaran secara *synchronous* untuk memvalidasi transaksi.
2. Ketika modul pembayaran lambat (misal karena DB-nya overload saat promo), request dari modul pesanan **menggantung tanpa batas** — tidak ada batas waktu tunggu.
3. Setiap request yang menggantung ini mengikat satu *thread* di thread pool modul pesanan. Karena thread pool terbatas (misal 200 thread di Tomcat/Undertow), dalam hitungan detik semua thread terpakai.
4. Akibatnya, modul pesanan **tidak bisa melayani request baru sama sekali** — bahkan untuk operasi yang sebenarnya tidak butuh pembayaran (misal lihat menu). User melihat aplikasi "sangat lambat, beberapa permintaan timeout" (sesuai gejala yang dilaporkan).
5. Karena tidak ada retry, satu kegagalan jaringan sesaat (misal 1 detik packet loss) langsung jadi kegagalan permanen bagi user — pesanan gagal bayar, user harus ulang dari awal, beban malah bertambah.
6. Di sisi lain, karena tidak ada mekanisme deteksi dini, modul pesanan terus mencoba memanggil modul pembayaran yang sedang sakit, memperparah beban modul pembayaran → *death spiral*.

Jadi ironinya: asumsi "jaringan reliable" justru bikin sistem FoodGo **lebih tidak reliable** saat dibutuhkan.

**Solusi desain awal:**
Saya mengusulkan kombinasi tiga mekanisme yang saling melengkapi untuk modul pesanan ↔ modul pembayaran di FoodGo:

1. **Timeout agresif di setiap pemanggilan antar-service.** Misalnya timeout 3 detik untuk panggilan pembayaran. Jika tidak ada respons dalam 3 detik, anggap gagal dan lepaskan thread — jangan biarkan menggantung.
2. **Retry dengan *exponential backoff* + *jitter*.** Jika panggilan gagal karena *transient error* (timeout, 5xx, connection reset), coba ulang maksimal 3 kali dengan delay yang semakin panjang (100ms → 200ms → 400ms) ditambah *random jitter* agar retry dari banyak client tidak serentak (*thundering herd*).
3. **Circuit Breaker** di modul pesanan. Jika dalam 10 detik terakhir lebih dari 50% panggilan ke pembayaran gagal, circuit breaker "trip" ke posisi OPEN — semua panggilan berikutnya langsung gagal cepat (*fast fail*) tanpa benar-barar memanggil pembayaran, selama misal 30 detik. Ini memberi waktu modul pembayaran untuk recover tanpa dihujani request lagi.

Ketiga mekanisme ini bisa diimplementasikan dengan library seperti Resilience4j (Java) atau Polly (.NET) tanpa harus menulis dari nol — realistis untuk tim kecil FoodGo.

**Trade-off:**
- **Timeout yang terlalu pendek** bisa menyebabkan kegagalan palsu (*false positive*): pembayaran sebenarnya sedang diproses tapi belum selesai, kita sudah anggap gagal → risiko *double charge* jika user retry. Perlu desain *idempotency key* di modul pembayaran untuk mengatasinya, yang menambah kompleksitas.
- **Retry** memperparah beban saat service target sedang overload — kalau tidak pakai backoff + jitter, kita justru ikut menumbang *thundering herd* yang membuat modul pembayaran makin lama recover.
- **Circuit Breaker** berarti ada periode di mana user FoodGo **pasti** gagal bayar (selama circuit OPEN), meskipun modul pembayaran sebenarnya sudah mulai pulih. User experience jadi "tiba-tiba tidak bisa checkout" selama beberapa puluh detik. Perlu mekanisme *half-open* dan fallback UI yang jelas ("Pembayaran sedang gangguan, coba beberapa saat lagi").
- Secara keseluruhan, menambah timeout + retry + circuit breaker = menambah **konfigurasi yang 

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

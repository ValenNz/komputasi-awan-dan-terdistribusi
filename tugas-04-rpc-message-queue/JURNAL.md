# Jurnal Proses — Tugas 4

### Analisis Pemilihan Pola Komunikasi (Oleh: Nuevalen - Jalur A)

**Mengapa RPC cocok untuk skenario "Cek Saldo" & "Proses Pembayaran"?**
RPC (Remote Procedure Call) bersifat **sinkron dan blocking**. Ini sangat cocok untuk operasi kritis seperti validasi saldo karena modul Pesanan *harus* mendapatkan kepastian instan sebelum melanjutkan ke tahap berikutnya (misalnya, membuat invoice). Jika menggunakan MQ untuk cek saldo, modul Pesanan harus menunggu event balasan yang tidak pasti waktunya, yang akan merusak pengalaman pengguna (UX).

**Apa yang terjadi jika dipakai untuk skenario yang salah?**
Jika RPC dipaksa digunakan untuk "Kirim notifikasi ke modul Kurir", maka modul Pembayaran akan **terblokir (hang)** menunggu modul Kurir merespons. Jika modul Kurir sedang down atau lambat, modul Pembayaran ikut menjadi tidak responsif, antrean pembayaran menumpuk, dan sistem mengalami *cascading failure* (kegagalan berantai) akibat *tight coupling*.

**Apa yang terjadi pada request RPC jika server mati di tengah proses?**
Berdasarkan pengujian kami, jika `server.py` dimatikan (Ctrl+C) saat `client.py` sedang berjalan atau akan memanggil fungsi, client akan langsung melempar error `ConnectionRefusedError` atau `socket.error` setelah mencapai *timeout*. Client tidak memiliki mekanisme *retry* otomatis (kecuali kita memprogramnya secara manual dengan `try-except` dan loop). Ini membuktikan kelemahan utama RPC: **tidak ada fault tolerance bawaan** untuk kegagalan server.

## Jalur yang dipilih
- [RPC / MQ / keduanya], alasan: ...

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok): ...

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

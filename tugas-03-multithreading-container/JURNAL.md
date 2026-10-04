# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: 84 dari 100 pesanan (lokal), dan 69 dari 100 pesanan (di Docker)
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): Karena thread-thread tersebut berbagi memori yang sama, terjadi tumpang tindih isntruksi saat membaca dan menulis data ke variabel counter. Thread satu belum sempat menyimpan, tapi thread yang lain sudah membaca data yang lama. Akibatnya, banyak  hitungan pesanan yang saling tertimpa atau lost update sehingga hasil akhirnya di bawah 100.

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: 100 dari 100 pesanan yang berarti selalu akurat baik docker maupun di lokal.

## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: Proses pembuatan image dan eksekusi container berjalan lancar tanpa eror fatal, semua konfigurasi `COPY` dan `WORKDIR` di Dockerfile langsung dieksekusi.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | NO AI | ... | ... | ... |

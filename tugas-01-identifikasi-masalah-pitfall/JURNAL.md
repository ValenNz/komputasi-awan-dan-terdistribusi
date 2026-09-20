# Jurnal Proses — Tugas 1

## 17 September 2026
- Peserta: 
Haniel Juanta Sembiring
Farrellino Ulung Satya Amando
Nuevalen Refitra Alswando

- Poin diskusi:
Sudah terlihat jelas bahwa masalahnya ada di rancangan sistemnya. Asumsinya juga kurang lebih menjelaskan apa yang salah dan perlu diperbaiki. Ada 3 pitfall:
1. The network is reliable
2. Latency is zero
3. Single point of failure

Komunikasi antar service tidak selalu berhasil. Bisa saja error sewaktu-waktu. Kalau misalkan tidak ada timeout sehingga:
Modul Pembayaran lambat, Modul Pesanan ikut menunggu,  banyak request menumpuk, resource/thread habis, request baru ikut lambat atau gagal.

Tidak ada juga server cadangan dan semua modul bergantung pada satu. Satu modul crash, yang lainnya ikutan terdampak dan sistem tentunya akan crash. Seharusnya ada back up server, karena setiap proses berebut resource yang sangat terbatas dari hanya 1 server.

Solusinya:
Buat agar sistem bsia restart otomatis jika terjadi crash. Belum memperbaiki masalah utama, namun bisa jadi langkah penanganan setelah server crash.

Perbaikan sistem agar tidak crash:
- Ubah arsitektur ke microservice supaya lebih ringan
- Pakai webhooks untuk modul pembayaran atau message broker pada sistem
- Pakai timeout dan circuit breaker supaya tidak memakan banyak resource yang membuat server crash
- Jika proses hanya gagal untuk sementara saja, sistem bisa dirancang supaya bisa melakukan request namun secara terbatas



## Review Silang
- Haniel menambahkan ide dasar dari Nuevalen mengenai timeout dan circuit breaker. Timeout yang terlalu singkat bisa membatalkan proses yang saat itu sedang diproses dan circuit breaker berkemungkinan menyulitkan user saat melakukan pembayaran. Karena itu, perlu diset agar waktu timeout dan penggunaan circuit breaker diset dengan tepat.

- Farrellino merasa saran dari Haniel mengenai transisi menjadi arsitektur microservice dapat membuat operasional sistem memiliki kompleksitas yang lebih tinggi. Namun, ide ini tetap bisa diterapkan jika tim siap menangani operasionalnya.

- Nuevalen menyebutkan bahwa ide penggunaan message broker dari Farrellino berkemungkinan dapat menimbulkan masalah bagi user, karena notifikasi yang sama dapat muncul 2 kali yang tentunya dapat membuat user bingung, namun juga dapat bekerja dengan efektif jika bisa diterapkan dengan baik supaya sistem tidak perlu saling menunggu. 

## Log Penggunaan AI (Level 2)
| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 17 September 2026 | Tidak memakai AI | - | - | - |

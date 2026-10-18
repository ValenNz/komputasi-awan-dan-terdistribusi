# Jurnal Proses — Tugas 5

# Jurnal Proses — Tugas 5

## Implementasi Bully
- **Kendala saat mengisi TODO 1-4:** 
  Awalnya kami mencoba menggunakan `time.sleep()` di dalam `start_election()` untuk menunggu balasan `OK`. Namun, hal ini menyebabkan *deadlock* karena thread utama terkunci dan tidak bisa menjalankan `start_server()` untuk menerima pesan `OK` dari node lain di `on_message`. 
  **Solusi:** Kami mengganti mekanisme tunggu dengan `threading.Event()`. Di `__init__` kami membuat `self.ok_event = threading.Event()`. Saat `on_message` menerima `OK`, ia memanggil `self.ok_event.set()`. Di `start_election`, kami menggunakan `self.ok_event.wait(timeout=ELECTION_TIMEOUT)`. Ini membuat thread bisa menunggu secara non-blocking dan langsung lanjut jika ada `OK` atau timeout tercapai.
- **Kendala Jaringan:** Awalnya `handle_connection` tidak mengetahui port pengirim untuk membalas pesan `OK`. Kami menyelesaikannya dengan asumsi konvensi port `5000 + sender_id` sesuai dengan argumen CLI.

## Skenario 1: Start normal
- **Leader yang terpilih:** Node 5
- **Log/observasi:** Saat 5 node dijalankan hampir bersamaan dalam waktu singkat, Node 1, 2, 3, dan 4 mendeteksi bahwa variabel leader_id masih kosong (tidak ada leader). Kondisi ini memicu mereka untuk secara otomatis memanggil start_election().
Mereka mengirim pesan ELECTION ke semua node yang memiliki ID lebih besar dari dirinya.
Node 5, yang memiliki ID tertinggi, menerima pesan ELECTION dari Node 1, 2, 3, dan 4.
Sesuai aturan Bully, Node 5 membalas pesan OK ke keempat node tersebut. Penerimaan OK ini membuat Node 1-4 berhenti mencalonkan diri (karena ok_event mereka di-set menjadi true).
Karena Node 5 tidak memiliki peer dengan ID di atasnya, ia tidak menunggu OK dari siapa pun. Ia langsung menganggap diri pemenang, memanggil declare_leader(), dan melakukan broadcast pesan COORDINATOR ke seluruh jaringan untuk memberi tahu bahwa ia adalah leader sah.


## Skenario 2: Leader dimatikan
- **Leader baru yang terpilih:** Node 4
- **Berapa lama waktu sampai leader baru terdeteksi:** Sekitar **3 detik**.
- **Log/observasi:** Waktu deteksi kegagalan (failure detection) sangat bergantung pada durasi time.sleep(3) yang ada di dalam loop fungsi monitor_leader().
Setelah proses Node 5 ditekan Ctrl+C untuk dimatikan paksa, Node 4 (dan node lain seperti 1, 2, 3) yang sedang berada dalam fase sleep akan terbangun pada siklus berikutnya.
Mereka mencoba mengirim pesan heartbeat berupa PING ke port 5005, yaitu port milik Node 5.
Karena proses Node 5 sudah mati, koneksi ditolak oleh sistem operasi (ConnectionRefusedError), sehingga fungsi send_message mengembalikan nilai False.
Node 4, yang memiliki ID tertinggi kedua setelah Node 5, mereset variabel leader_id menjadi None dan segera memicu start_election().
Node 4 mengirim ELECTION ke node di atasnya (Node 5), namun tidak ada balasan. Setelah timeout, Node 4 mendeklarasikan diri sebagai COORDINATOR baru.
Node 1, 2, dan 3 menerima broadcast COORDINATOR dari Node 4 dan memperbarui state leader_id mereka secara otomatis.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 16 Okt 2026 | Gemini | "kenapa sistem butuh leader buat nanganin konflik urutan pesanan?" | AI menyarankan untuk fokus membahas masalah jam fisik yang tidak sinkron dan peran leader sebagai pengatur antrean utama (single source of truth). | Kami menggunakan konsep pengatur antrean tunggal tersebut sebagai kerangka jawaban awal, lalu menuliskannya ulang sesuai pemahaman kelompok kami. |
| 18 Okt 2026 | Gemini | "bantu jelaskan bedanya algoritma bully sama raft pakai bahasa gampang" | AI memberi poin perbandingan: Bully menang berdasarkan ID tapi boros pesan, Raft pakai voting dan lebih aman untuk data. | Kami membaca ide tersebut untuk bahan diskusi kelompok, lalu mengetik ulang perbandingannya menggunakan bahasa kami sendiri di README. |
| 18 Okt 2026 | Gemini | "apa aja kelemahan bully algorithm buat kasus kayak foodgo?" | AI memberikan 3 poin utama: masalah jaringan penuh (message storm), jeda tanpa leader saat proses pemilihan, dan sistem tidak stabil jika koneksi memburuk. | Kami mengambil 3 kerangka poin tersebut, menuliskan penjelasannya, dan mencocokkannya dengan hasil log pengujian skenario 2 yang kami jalankan malam harinya. |
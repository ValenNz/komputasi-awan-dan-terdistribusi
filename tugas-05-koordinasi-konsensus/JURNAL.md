# Jurnal Proses — Tugas 5

# Jurnal Proses — Tugas 5

## Implementasi Bully
- **Kendala saat mengisi TODO 1-4:** 
  Awalnya kami mencoba menggunakan `time.sleep()` di dalam `start_election()` untuk menunggu balasan `OK`. Namun, hal ini menyebabkan *deadlock* karena thread utama terkunci dan tidak bisa menjalankan `start_server()` untuk menerima pesan `OK` dari node lain di `on_message`. 
  **Solusi:** Kami mengganti mekanisme tunggu dengan `threading.Event()`. Di `__init__` kami membuat `self.ok_event = threading.Event()`. Saat `on_message` menerima `OK`, ia memanggil `self.ok_event.set()`. Di `start_election`, kami menggunakan `self.ok_event.wait(timeout=ELECTION_TIMEOUT)`. Ini membuat thread bisa menunggu secara non-blocking dan langsung lanjut jika ada `OK` atau timeout tercapai.
- **Kendala Jaringan:** Awalnya `handle_connection` tidak mengetahui port pengirim untuk membalas pesan `OK`. Kami menyelesaikannya dengan asumsi konvensi port `5000 + sender_id` sesuai dengan argumen CLI.

## Skenario 1: Start normal
- **Leader yang terpilih:** Node 5
- **Log/observasi:** Saat 5 node dijalankan hampir bersamaan, Node 1, 2, 3, dan 4 mendeteksi tidak ada leader, sehingga memicu `start_election()`. Mereka mengirim `ELECTION` ke node di atasnya. Node 5 menerima `ELECTION` dari 1, 2, 3, dan 4. Node 5 membalas `OK` ke mereka, yang membuat Node 1-4 berhenti mencalonkan diri (karena `ok_event` di-set). Karena Node 5 tidak memiliki peer di atasnya, ia langsung memanggil `declare_leader()` dan broadcast `COORDINATOR`.

## Skenario 2: Leader dimatikan
- **Leader baru yang terpilih:** Node 4
- **Berapa lama waktu sampai leader baru terdeteksi:** Sekitar **3 detik**.
- **Log/observasi:** Waktu deteksi bergantung pada `time.sleep(3)` di dalam loop `monitor_leader()`. Setelah Node 5 ditekan `Ctrl+C`, Node 4 (dan node lain) yang sedang melakukan `sleep` terbangun, mencoba mengirim `PING` ke port 5005. Karena koneksi ditolak (`ConnectionRefusedError`), `send_message` mengembalikan `False`. Node 4 mereset `leader_id` menjadi `None` dan memicu `start_election()`. Node 4 mengirim `ELECTION` ke node di atasnya (tidak ada), lalu mendeklarasikan diri sebagai `COORDINATOR` baru. Node 1, 2, dan 3 menerima `COORDINATOR` dan memperbarui state mereka.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

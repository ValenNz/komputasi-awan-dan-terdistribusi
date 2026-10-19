# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): ...
- Cara memperbaikinya: ...

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: ...
- Hasil sebelum & sesudah node keluar: ...

## Implementasi register_kurir & lookup (Nuevalen)
- **Kesalahan pertama:** Awalnya bingung bagaimana cara menyimpan data agar tahu node mana yang memegangnya, karena `self.data` hanya mapping `hash -> (kurir_id, ip)`.
- **Cara memperbaiki:** Menyadari bahwa di simulasi ini, `self.data` bersifat global untuk kemudahan visualisasi. Yang penting adalah memanggil `find_successor(key_hash)` sebelum menyimpan/mengambil, untuk mensimulasikan bahwa operasi tersebut "didelegasikan" ke node yang benar. Menambahkan `print` log agar perpindahan tanggung jawab terlihat jelas di terminal.

## Skenario Leave (Pengujian)
- **Node keluar:** `node-jakarta-1` (hash=XX)
- **Successor yang ambil alih:** `node-bandung-1` (hash=XX) *(Sesuaikan dengan hasil run programmu)*
- **Hasil:** Saat `node-jakarta-1` dihapus dari `self.nodes`, pemanggilan `lookup` untuk kurir yang sebelumnya dipegang node tersebut berhasil diarahkan ke successor barunya. Data tidak hilan

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

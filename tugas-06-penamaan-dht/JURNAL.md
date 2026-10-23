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

## Implementasi find_successor (Haniel)
- **Kesalahan pertama:** Saat menyaring node dengan kondisi `nid >= key_hash`, sempat lupa menangani kondisi ketika nilai `key_hash` lebih besar daripada semua ID node yang ada di ring, sehingga list kandidat menjadi kosong dan pemanggilan `min()` menyebabkan error.
- **Cara memperbaiki:** Menyimpan daftar node yang memenuhi `nid >= key_hash` ke dalam list `candidates`, lalu mengecek terlebih dahulu apakah `candidates` ada isinya. Jika ada, fungsi mengembalikan `min(candidates)`, sedangkan jika kosong, fungsi melakukan wrap-around ke node paling awal di ring dengan mengembalikan `min(self.nodes.keys())`.

## Skenario Awal (Pengujian)
- **Hash node:** `node-jakarta-1` (hash=177), `node-jakarta-2` (hash=102), `node-bandung-1` (hash=40), `node-surabaya-1` (hash=136)
- **Hash kurir:** `kurir-001` (hash=50), `kurir-002` (hash=28), `kurir-003` (hash=132)
- **Hasil:** Keempat node awal berhasil masuk ke dalam ring dan ketiga kurir berhasil didaftarkan ke node successor masing-masing. Saat dilakukan pengujian `lookup` sebelum perubahan topologi, `kurir-001` dan `kurir-002` berhasil ditemukan pada successor yang sesuai dan mengembalikan alamat IP `192.168.1.10` serta `192.168.1.11`.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
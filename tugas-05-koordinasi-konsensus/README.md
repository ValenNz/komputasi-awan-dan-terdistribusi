# Tugas 5 (Pekan 5) — Koordinasi & Konsensus

**Materi terkait:** Physical/Logical Clock, Election Algorithm (Bully/Raft).

## Studi Kasus

Terjadi konflik urutan waktu pada pesanan FoodGo (dua server mencatat urutan pesanan berbeda karena jam tidak sinkron), dan sistem membutuhkan satu **"Node Leader"** untuk mengelola antrean pesanan pusat agar tidak terjadi konflik pemrosesan ganda.

## Tugas Kelompok

Implementasikan simulasi **Bully Algorithm** untuk memilih leader di antara **5 node virtual** yang berjalan sebagai 5 proses Python terpisah di laptop yang sama (tiap node = satu proses di port berbeda, komunikasi lewat TCP socket di `localhost`).

Skeleton yang disediakan (`src/node.py`) sudah menangani bagian **infrastruktur jaringan** (membuka socket, menerima & mengirim pesan antar node) — bagian **algoritma Bully sendiri sengaja dikosongkan** (`# TODO`), karena itu inti pembelajaran tugas ini.

### Aturan Bully Algorithm yang harus diimplementasikan

1. Node yang mendeteksi leader tidak merespons (atau saat start pertama kali) mengirim pesan `ELECTION` ke semua node dengan ID **lebih besar** darinya.
2. Jika ada node ber-ID lebih besar yang merespons `OK`, node yang memulai election **berhenti mencalonkan diri** dan menunggu pesan `COORDINATOR`.
3. Jika **tidak ada** node ber-ID lebih besar yang merespons dalam batas waktu tertentu, node tersebut menjadi leader dan mem-broadcast `COORDINATOR` ke semua node lain.
4. Semua node mencatat siapa leader saat ini.

### Cara Menjalankan

Buka 5 terminal terpisah (satu per node):
```bash
python3 src/node.py --id 1 --port 5001 --peers 5002,5003,5004,5005
python3 src/node.py --id 2 --port 5002 --peers 5001,5003,5004,5005
python3 src/node.py --id 3 --port 5003 --peers 5001,5002,5004,5005
python3 src/node.py --id 4 --port 5004 --peers 5001,5002,5003,5005
python3 src/node.py --id 5 --port 5005 --peers 5001,5002,5003,5004
```

### Skenario Wajib Diuji & Dicatat

1. **Start normal**: nyalakan node 1–5 hampir bersamaan, catat siapa yang terpilih jadi leader (harusnya node ber-ID tertinggi, yaitu node 5).
2. **Leader mati**: matikan (Ctrl+C) proses node leader (node 5), amati node lain mendeteksi leader hilang dan memicu election baru. Catat leader baru yang terpilih (harusnya node 4).
3. Simpan log terminal (screenshot atau `> log_nodeX.txt` redirect) dari kedua skenario ke folder `bukti/`.

## Struktur Submission

```
tugas-05-koordinasi-konsensus/
├── README.md      # Analisis: kenapa perlu leader, kenapa Bully (vs Raft), hasil 2 skenario
├── JURNAL.md
├── src/
│   └── node.py
└── bukti/          # Log/screenshot skenario start normal & leader mati
```

## Rubrik Penilaian (Tugas 5)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi Bully Algorithm benar | 35% | Election, OK, COORDINATOR message bekerja sesuai aturan algoritma |
| Bukti skenario leader mati → re-election | 30% | Log jelas menunjukkan leader baru terpilih otomatis |
| Analisis (kenapa perlu leader, trade-off Bully vs Raft) | 20% | Dikaitkan ke masalah urutan pesanan di skenario FoodGo |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI tentang gambaran umum algoritma election; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/node.py` (logika `on_message`, `start_election`, `declare_leader`, `monitor_leader`). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menjelaskan kenapa Bully Algorithm selalu memilih node ber-ID tertinggi yang masih hidup, dan apa kelemahannya dibanding algoritma lain (mis. jumlah pesan yang dikirim saat election, single point of failure sebelum leader baru terpilih) — bukan sekadar definisi generik.

---

## Laporan Analisis Kelompok

**Anggota Kelompok:**
1. Nuevalen Refitra Alswanfo (103072430008)
2. Haniel Juanta Sembiring (103072400145)
3. FARRELLINO ULUNG SATYA AMANDO (103072400005)

### 1. Kenapa Sistem Membutuhkan Leader? (Studi Kasus FoodGo)
Dalam arsitektur terdistribusi seperti aplikasi FoodGo, ketiadaan sinkronisasi waktu fisik (*physical clock drift*) antar server menyebabkan masalah inkonsistensi data yang fatal. Jika ada dua server yang menerima pesanan pada saat yang bersamaan, ketidaksinkronan jam internal server dapat membuat urutan pesanan menjadi kacau dan tercatat berbeda di masing-masing server. Hal ini memicu *double processing* (pemrosesan ganda, di mana dua server mencoba memproses/mengurangi stok untuk pesanan yang sama secara bersamaan).

Untuk menyelesaikannya, sistem membutuhkan satu **Node Leader** yang bertindak sebagai *Single Source of Truth*. Dengan terpilihnya leader:
- **Sentralisasi Antrean:** Seluruh pesanan dari berbagai server diteruskan ke Node Leader untuk dimasukkan ke dalam satu antrean utama.
- **Urutan Mutlak:** Nomor urut pesanan ditentukan secara mutlak oleh leader, tidak lagi bergantung pada *timestamp* fisik server lokal.
- **Pencegahan Konflik:** Karena instruksi pemrosesan hanya keluar dari satu pintu (leader), mustahil ada dua server yang memproses pesanan yang sama, sehingga pemrosesan ganda dapat dicegah.

### 2. Trade-off: Bully Algorithm vs Raft
- **Pendekatan Pemilihan:** Bully bersifat deterministik; node dengan ID tertinggi otomatis menang tanpa *voting*. Raft berbasis konsensus mayoritas (kuorum), di mana *leader* dipilih melalui pemungutan suara dari node yang hidup.
- **Kompleksitas Jaringan:** Bully sangat boros lalu lintas jaringan dengan kompleksitas $O(n^2)$ saat *election* karena saling mengirim pesan secara serentak. Raft lebih efisien ($O(n)$) karena menggunakan *randomized timeout* untuk mencegah bentrokan pencalonan.
- **Kekinian Data (*State Liveness*):** Bully memilih leader murni dari ID, sehingga berisiko memilih node yang data antrean pesanannya sudah tertinggal (*outdated*). Raft menjamin leader terpilih memiliki *log* data paling mutakhir.

### 3. Cara Kerja dan Kelemahan Bully Algorithm
**Kenapa memilih node ber-ID tertinggi?**
Pemilihan berdasarkan ID tertinggi memberikan determinisme mutlak. Dalam sistem terdistribusi, aturan statis ini memastikan semua node secara independen akan konvergen dan mengakui satu pemenang yang sama tanpa prosedur *voting* yang rumit, asalkan semua node mengikuti aturan bahwa pesan dari ID yang lebih rendah harus diabaikan/di-bully.

**Kelemahan Algoritma Bully:**
1. **Traffic Jaringan Membeludak:** Saat *election*, setiap node mengirim pesan `ELECTION` ke semua node ber-ID lebih tinggi. Hal ini dapat menciptakan *message storm* yang membuat jaringan macet jika node sangat banyak.
2. **Single Point of Failure (Jeda Tanpa Leader):** Selama proses *election* (sejak leader lama mati hingga `COORDINATOR` baru diterima), sistem berada dalam status "tanpa leader". Pada jeda ini, FoodGo sama sekali tidak bisa memproses pesanan baru.
3. **Flapping (Ketidakstabilan):** Jika node ber-ID tertinggi memiliki koneksi yang tidak stabil (sering mati-nyala), ia akan terus-menerus memicu *election* baru, merusak stabilitas sistem.

### 4. Hasil Pengujian Skenario
- **Skenario 1 (Start Normal):** Kelima node dijalankan secara bersamaan. Beberapa node ber-ID rendah pada awalnya memicu *election*. Namun, Node 5 yang memiliki ID tertinggi (5005) pada akhirnya menang, mendeklarasikan dirinya sebagai leader, dan mem-broadcast pesan `COORDINATOR`. Node 1, 2, 3, dan 4 sepakat dan mencatat Node 5 sebagai *leader* baru.
- **Skenario 2 (Leader Mati):** Proses Node 5 dimatikan paksa (menggunakan `KeyboardInterrupt` / `Ctrl+C`). Fungsi *monitoring* pada Node 1, 2, 3, dan 4 mendeteksi bahwa pesan PING ke Node 5 gagal dan mencetak log `Leader 5 terdeteksi mati! Memulai election...`. Karena Node 5 mati, Node 4 memenangkan *election* (sebagai ID tertinggi yang tersisa), lalu mencetak `*** MENJADI LEADER! Broadcasting COORDINATOR... ***`. Node 1, 2, dan 3 kemudian memperbarui catatan mereka dengan Node 4 sebagai *leader* baru.
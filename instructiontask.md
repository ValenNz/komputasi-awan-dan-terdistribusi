# 📚 Repositori Tugas: Sistem Terdistribusi & Komputasi Awan

Repositori ini digunakan oleh kelompok kami untuk mengerjakan seluruh tugas (Tugas 1–15) sepanjang semester. **Baca panduan ini dengan saksama sebelum mulai mengerjakan tugas** agar alur kerja kita rapi, kontribusi tercatat, dan sesuai dengan rubrik penilaian dosen.

## 👥 Anggota Kelompok

| Nama | NIM | Peran / Fokus (Opsional, bisa disesuaikan per tugas) |
| :--- | :--- | :--- |
| **Nuevalen Refitra Alswanfo** | 103072430008 | - |
| **FARRELLINO ULUNG SATYA AMANDO** | 103072400005 | - |
| **Haniel Juanta Sembiring** | 103072400145 | - |

> ⚠️ **PENTING:** Sesuai aturan handbook, **setiap anggota WAJIB melakukan `commit` dan `push` dari laptop masing-masing**. Dilarang keras satu orang mengerjakan semua lalu di-commit atas nama sendiri. History commit adalah bukti kontribusi nyata.

---

## 🚀 1. Setup Awal (Lakukan SEKALI di awal semester)

Pastikan semua anggota sudah menginstal dan mengonfigurasi ini di laptop masing-masing:

1. **Git & GitHub**: 
   ```bash
   git config --global user.name "Nama Lengkap Sesuai Absen"
   git config --global user.email "email@mahasiswa.telkomuniversity.ac.id"
   ```
2. **Docker Desktop**: Pastikan berjalan dan verifikasi dengan `docker --version` serta `docker compose version`.
3. **Python 3 & Virtual Environment**: Selalu aktifkan venv per tugas agar dependensi tidak bentrok.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

---

## 🔄 2. Alur Kerja Harian (Cara Pull & Push)

Ikuti langkah ini **setiap kali** kalian mulai dan selesai mengerjakan bagian tugas.

### Langkah 1: Sebelum Mulai Mengerjakan (WAJIB)
Selalu tarik perubahan terbaru dari GitHub agar tidak terjadi konflik:
```bash
git pull origin main
```

### Langkah 2: Saat Mengerjakan
- Kerjakan bagian yang sudah dibagi.
- Simpan progres secara bertahap (jangan menunggu 100% selesai baru commit).
- **Update `JURNAL.md` secara real-time** (catat kendala, solusi, dan log penggunaan AI jika ada). Jangan merapikan jurnal di akhir, biarkan apa adanya sebagai bukti kerja asli.

### Langkah 3: Setelah Selesai Sebagian (Commit & Push)
Lakukan ini dari laptop masing-masing anggota:
```bash
# 1. Cek file yang berubah
git status

# 2. Tambahkan file yang dikerjakan (spesifik, jangan git add . jika tidak perlu)
git add tugas-XX-nama-tugas/

# 3. Commit dengan pesan yang JELAS dan mencantumkan nama/nim (opsional tapi disarankan)
git commit -m "Tugas XX: [Deskripsi singkat pekerjaan, misal: implementasi worker thread] - oleh [Nama]"

# 4. Push ke GitHub
git push origin main
```

> 💡 **Tips Branching (Opsional tapi Rapi):**  
> Jika ingin lebih aman, buat branch atas nama sendiri:  
> `git checkout -b fitur-nuevalen` → kerjakan → `git push origin fitur-nuevalen` → gabungkan ke `main` via Pull Request di GitHub repo kita sendiri.

---

## 📦 3. Struktur Folder Tugas (Wajib Diikuti)

Setiap folder tugas (`tugas-XX-.../`) harus mengikuti format ini:
```text
tugas-XX-nama-tugas/
├── README.md        # Analisis studi kasus & jawaban soal
├── JURNAL.md        # Log proses berpikir, debugging, & log penggunaan AI (Level 2)
├── src/             # Kode sumber (jika ada)
├── bukti/           # Screenshot terminal (terlihat prompt user) atau link video demo
└── (file lain)      # Misal: docker-compose.yml, diagram, dll.
```

---

## 🏁 4. Cara Submit Tugas (DEADLINE)

**JANGAN gunakan Pull Request ke repo dosen!** Kita menggunakan **Git Tag** untuk menandai submission.

Lakukan langkah ini saat tugas sudah 100% selesai dan siap dikumpulkan (bisa dilakukan oleh salah satu anggota, tapi pastikan semua perubahan sudah di-push):

1. Pastikan semua sudah di-commit dan di-push ke `main`:
   ```bash
   git pull origin main
   git push origin main
   ```
2. Buat tag submission (ganti `XX` dengan nomor tugas, misal `03`):
   ```bash
   git tag tugas-XX-submit
   git push origin tugas-XX-submit
   ```
3. **Ambil Link untuk Moodle**:  
   Buka GitHub, masuk ke folder tugas tersebut, lalu **klik dropdown branch/tag di kiri atas** dan pilih `tugas-XX-submit`.  
   Salin URL dari browser. Contoh format:  
   `https://github.com/<username-kelompok>/<nama-repo>/tree/tugas-03-submit/tugas-03-multithreading-container`
4. Tempel link tersebut ke kolom submission di **Moodle**.

> ⚠️ **Jika ada revisi sebelum deadline:**  
> Pindahkan tag ke commit terbaru:  
> `git tag -f tugas-XX-submit`  
> `git push origin tugas-XX-submit --force`  
> Link Moodle tidak perlu diganti, otomatis mengikuti tag terbaru.

---

## 🤖 5. Aturan Penggunaan AI

- **Diperbolehkan**: Level 2 (AI Assisted Idea Generation & Structuring). Boleh pakai AI untuk brainstorming ide awal atau menyusun outline.
- **DILARANG**: Meminta AI menulis kode akhir, analisis README, atau diagram secara utuh lalu tinggal copy-paste.
- **WAJIB**: Mencatat sesi penggunaan AI di bagian **"Log Penggunaan AI"** dalam `JURNAL.md` (apa yang ditanyakan, apa outputnya, dan bagaimana kita memodifikasinya).

---

## 🛠️ 6. Troubleshooting Singkat

| Masalah | Solusi |
| :--- | :--- |
| `git push` ditolak (`rejected`) | Jalankan `git pull origin main` dulu, selesaikan konflik jika ada, lalu `git push` lagi. |
| Port sudah dipakai (`address already in use`) | Ganti port di kode/`docker-compose.yml`, atau matikan proses lama (`lsof -i :PORT`). |
| Docker error / container langsung exit | Cek log dengan `docker logs <container-id>` atau `docker compose logs`. |
| Lupa update `JURNAL.md` | Sempatkan waktu 5 menit di akhir sesi coding untuk mencatat progres di jurnal. |

---

**Mari kita kerjakan dengan disiplin, jujur, dan kolaboratif!**  
Jika ada yang bingung dengan langkah Git atau Docker, diskusikan di grup chat sebelum asal commit agar history tetap bersih.

---
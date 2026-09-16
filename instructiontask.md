# Komputasi Awan dan Terdistribusi — Panduan Kelompok

Repository ini digunakan untuk mengerjakan tugas mata kuliah **Komputasi Awan dan Terdistribusi**.

Repository utama:
https://github.com/aldonesia/komputasi-awan-dan-terdistribusi

Repository kelompok:
https://github.com/ValenNz/komputasi-awan-dan-terdistribusi

---

## 👥 Anggota Kelompok

| No | Nama | NIM | Tugas/Peran |
|---|---|---|---|
| 1 | Farrelino Ulung Satya Amando | 103072400005 | Koordinator / Analisis |
| 2 | Haniel Juanta Sembiring | 103072400145 | Implementasi |
| 3 | Nuevalen Refitra Alswando | 103072430008 | Testing & Dokumentasi |

> Pembagian tugas dapat berubah sesuai kebutuhan masing-masing tugas.

---

# 📚 Struktur Repository

Setiap tugas sudah disediakan di dalam folder masing-masing.

Contoh:

```text
komputasi-awan-dan-terdistribusi/
│
├── tugas-01-identifikasi-masalah-pitfall/
├── tugas-02-...
├── tugas-03-...
├── tugas-04-...
├── ...
└── tugas-15-...
```

**Jangan membuat folder tugas baru di root repository.**

Jika dosen memberikan Tugas 1, maka fokus pada:

```text
tugas-01-identifikasi-masalah-pitfall/
```

Jika dosen memberikan Tugas 2, maka fokus pada folder:

```text
tugas-02-...
```

---

# 🚀 Cara Memulai

## 1. Clone Repository

Clone repository kelompok ke laptop masing-masing:

```bash
git clone https://github.com/ValenNz/komputasi-awan-dan-terdistribusi.git
```

Masuk ke folder:

```bash
cd komputasi-awan-dan-terdistribusi
```

Cek status Git:

```bash
git status
```

---

# 📖 2. Baca README Tugas

Sebelum mengerjakan tugas, **WAJIB membaca README.md yang terdapat di folder tugas tersebut.**

Contoh:

```text
tugas-01-identifikasi-masalah-pitfall/
└── README.md
```

README tugas berisi:
* Tujuan tugas
* Permasalahan yang harus diselesaikan
* Instruksi pengerjaan
* File yang harus dibuat/diedit
* Ketentuan tugas
* Rubrik penilaian

Jangan langsung mengerjakan sebelum memahami instruksinya.

---

# 📝 3. Alur Pengerjaan

Setiap tugas dikerjakan dengan alur:

```text
Baca README
     ↓
Pahami tugas
     ↓
Diskusi kelompok
     ↓
Bagi pekerjaan
     ↓
Kerjakan bagian masing-masing
     ↓
Review hasil
     ↓
Commit
     ↓
Push
     ↓
Testing / pengecekan akhir
     ↓
Finalisasi
     ↓
Buat Git Tag
```

---

# 👨‍💻 4. Pembagian Pekerjaan

Contoh pembagian untuk **3 anggota**:

### Anggota 1 — Koordinator / Analisis
**Tugas:**
* Memahami instruksi tugas secara menyeluruh
* Membantu menentukan pendekatan solusi
* Membagi pekerjaan secara adil
* Menggabungkan hasil pekerjaan anggota lain
* Melakukan final review sebelum pengumpulan

### Anggota 2 — Implementasi
**Tugas:**
* Mengerjakan bagian inti/coding implementasi
* Membuat atau mengubah file sesuai instruksi tugas
* Melakukan testing dasar pada bagian yang dikerjakan

### Anggota 3 — Testing & Dokumentasi
**Tugas:**
* Menguji hasil implementasi secara menyeluruh
* Mencari error dan mencatat hasil pengujian
* Membuat dokumentasi, menyusun laporan/jurnal
* Menambahkan screenshot/bukti jika diperlukan

> Pembagian di atas hanya contoh. Untuk setiap tugas, pembagian dapat disesuaikan dengan kebutuhan dan kesepakatan kelompok.

---

# 🌿 5. Aturan Git

## Sebelum mulai mengerjakan
Selalu ambil perubahan terbaru:
```bash
git pull origin main
```
Kemudian cek:
```bash
git status
```

## Setelah selesai mengerjakan
Lihat perubahan:
```bash
git status
```
Tambahkan perubahan:
```bash
git add .
```
Commit:
```bash
git commit -m "feat(tugas-01): mengerjakan bagian analisis"
```
Push:
```bash
git push origin main
```

---

# 💬 6. Format Commit

Gunakan commit message yang jelas dan menjelaskan apa yang dikerjakan.

Contoh:
```bash
git commit -m "feat(tugas-01): menambahkan analisis masalah"
git commit -m "feat(tugas-01): menambahkan implementasi"
git commit -m "test(tugas-01): melakukan pengujian"
git commit -m "docs(tugas-01): memperbaiki dokumentasi"
```

Hindari commit seperti:
```text
update
fix
coba
test
aaa
final
fix lagi
```
Karena commit history dapat digunakan untuk melihat kontribusi masing-masing anggota.

---

# ⚠️ 7. Penting: Jangan Saling Menimpa Pekerjaan

Sebelum mengubah file yang sedang dikerjakan anggota lain, **komunikasikan terlebih dahulu di grup.**

Contoh:
> "Aku mau edit README tugas-01 ya."

atau:
> "Aku sudah selesai bagian implementasi, selanjutnya Valen yang mau testing dan dokumentasi?"

Tujuannya agar tidak terjadi konflik Git atau pekerjaan yang tertimpa.

---

# 🤖 8. Aturan Penggunaan AI

Penggunaan AI harus mengikuti ketentuan yang diberikan pada repository/tugas oleh dosen.

AI dapat digunakan untuk:
* Brainstorming
* Memahami konsep
* Membantu membuat outline
* Menjelaskan error secara umum
* Membantu memahami dokumentasi

Namun, **jangan langsung menyalin hasil AI sebagai hasil akhir tugas jika tidak diperbolehkan oleh instruksi tugas.**

Setiap penggunaan AI yang diwajibkan untuk dicatat harus dituliskan pada:
```text
JURNAL.md
```

Contoh:
```markdown
## Penggunaan AI

AI digunakan untuk membantu memahami konsep dan menyusun
outline pengerjaan tugas.

AI tidak digunakan untuk menghasilkan hasil akhir yang
langsung disalin ke dalam tugas.
```
Selalu ikuti aturan AI yang terdapat pada README tugas.

---

# 🔍 9. Sebelum Push

Sebelum melakukan push, pastikan:
* [ ] Sudah membaca README tugas
* [ ] Pekerjaan sesuai instruksi
* [ ] Tidak ada file yang tidak diperlukan
* [ ] Tidak ada password/API key/token
* [ ] Program dapat dijalankan jika terdapat program
* [ ] Dokumentasi sudah diperbarui
* [ ] Sudah melakukan testing
* [ ] Commit message sudah jelas

---

# 🏁 10. Finalisasi Tugas

Jika tugas sudah selesai dan sudah direview semua anggota:

```bash
git status
```
Pastikan tidak ada perubahan yang belum di-commit.

Kemudian buat tag:
```bash
git tag tugas-01-submit
```
Push tag:
```bash
git push origin tugas-01-submit
```
Tag digunakan untuk menandai versi final tugas yang dikumpulkan.

---

# 📌 Aturan Utama Kelompok

1. **Baca README tugas sebelum mengerjakan.**
2. **Kerjakan hanya folder tugas yang diberikan dosen.**
3. **Jangan mengubah folder tugas lain tanpa alasan.**
4. **Setiap anggota harus memiliki kontribusi yang jelas.**
5. **Commit dilakukan secara berkala, bukan hanya sekali di akhir.**
6. **Gunakan commit message yang jelas.**
7. **Saling komunikasi sebelum mengubah file yang sedang dikerjakan anggota lain.**
8. **Lakukan review dan testing sebelum finalisasi.**
9. **Ikuti aturan penggunaan AI dari dosen.**
10. **Jangan menunggu satu orang mengerjakan semuanya.**

---

# 🗣️ Contoh Alur Kerja Tugas 01

Misalnya dosen memberikan:
> Tugas 01 — Identifikasi Masalah & Pitfall

Maka:

### 1. Semua anggota
Membaca:
```text
tugas-01-identifikasi-masalah-pitfall/README.md
```

### 2. Diskusi
Tentukan:
```text
Apa masalahnya?
Apa yang harus dianalisis?
File apa yang harus dibuat?
Siapa mengerjakan bagian apa?
```

### 3. Pembagian
```text
Anggota 1 (Farrelino) → Analisis masalah & Koordinasi
Anggota 2 (Haniel)    → Implementasi/contoh
Anggota 3 (Valen)     → Testing & Dokumentasi
```

### 4. Masing-masing mengerjakan bagian
Setelah selesai:
```bash
git add .
git commit -m "feat(tugas-01): mengerjakan bagian ..."
git push origin main
```

### 5. Review bersama
Cek apakah hasil sudah sesuai README.

### 6. Finalisasi
```bash
git tag tugas-01-submit
git push origin tugas-01-submit
```

---

# 📞 Komunikasi Kelompok

Gunakan grup untuk memberitahukan:
* Bagian yang sedang dikerjakan
* Bagian yang sudah selesai
* Perubahan file
* Error yang ditemukan
* Hasil testing
* Status finalisasi

Contoh:
> **Farrelino:** Aku kerjakan bagian analisis dan koordinasi tugas-01.

> **Haniel:** Oke, aku lanjut bagian implementasi setelah analisis fix.

> **Valen:** Siap, aku akan menunggu hasil implementasi untuk testing dan penyusunan JURNAL.md.

Dengan begitu semua anggota tahu progress masing-masing.

---

## 🎯 Target Kita

**Bukan hanya tugas selesai, tetapi semua anggota memahami apa yang dikerjakan dan memiliki kontribusi yang terlihat di GitHub.**
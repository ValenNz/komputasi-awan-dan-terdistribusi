# Jurnal Proses — Tugas 9: Cloud Delivery & Deployment Model

**Kelompok:** [Nama Kelompok]
**Tanggal Mulai:** [isi]
**Sifat:** Analisis di atas kertas, tanpa implementasi cloud

---

## 👥 Kontribusi Anggota

| Nama | NIM | Porsi Analisis | Status |
|---|---|---|---|
| Nuevalen Refitra Alswanfo | 103072430008 | Deployment model + 5 karakteristik NIST + tolak Public murni | ⏳ |
| Farrellino Ulung Satya Amando | 103072400005 | Service model per komponen + diagram + tolak Private murni | ⏳ |
| Haniel Juanta Sembiring | 103072400145 | Risiko spesifik + matriks risiko + mitigasi + UU PDP | ⏳ |

---

## 🗓️ Log Kegiatan

| Tanggal | Kegiatan | Peserta | Hasil |
|---|---|---|---|
| ... | Kick-off & pembagian tugas | Semua | Pembagian terlampir di `PEMBAGIAN_TUGAS.md` |
| ... | Kerja individu | Masing-masing | ... |
| ... | Review silang | Semua | ... |
| ... | Finalisasi & push | Semua | ... |

---

## 1️⃣ Diskusi Deployment Model
> **PIC: Nuevalen** — wajib diisi setelah sesi diskusi

### Opsi yang Dipertimbangkan

| Opsi | Kelebihan untuk Kasus Ini | Kekurangan | Keputusan |
|---|---|---|---|
| **Public Cloud** | Elastisitas nyaris tak terbatas saat lonjakan pemilu | Kendali infrastruktur di tangan penyedia; isu kedaulatan data & yurisdiksi | ❌ Ditolak |
| **Private Cloud** | Kendali penuh negara, cocok untuk NIK & biometrik | Elastisitas terbatas kapasitas fisik; risiko downtime saat lonjakan | ⚠️ ... |
| **Hybrid Cloud** | Core sensitif di private, beban lonjakan non-sensitif di public | Kompleksitas batas segmen & sinkronisasi | ⚠️ ... |
| **Community Cloud** | Dibagi antar instansi pemerintah (Dukcapil, Polri), tata kelola bersama | Perlu kesepakatan antar lembaga; kapasitas tetap terbatas | ⚠️ ... |

### Alasan Pemilihan (diisi Nuevalen)
- Kebutuhan kerahasiaan yang jadi *hard constraint*: ...
- Kebutuhan skalabilitas yang jadi *soft constraint*: ...
- Bagaimana 5 karakteristik NIST tetap terpenuhi: ...

### Kesimpulan Akhir
> **Deployment model yang dipilih:** [...]
> **Alasan utama:** [...]

---

## 2️⃣ Diskusi Service Model per Komponen
> **PIC: Farrellino**

### Komponen yang Teridentifikasi
1. Database inti (NIK, alamat, biometrik)
2. API verifikasi KYC
3. Portal publik cek status
4. Notifikasi / antrian
5. Dashboard analytics
6. Backup & DR

### Perdebatan yang Muncul
- Komponen mana yang **tidak boleh** pakai SaaS sama sekali? Kenapa? → ...
- Apakah API KYC lebih tepat IaaS atau PaaS? Alasan: → ...
- Apakah portal publik boleh SaaS penuh? Batasan datanya apa? → ...

### Kesimpulan Pemetaan
| Komponen | Service Model | Segmen | Alasan |
|---|---|---|---|
| ... | ... | ... | ... |

---

## 3️⃣ Diskusi Risiko & Mitigasi
> **PIC: Haniel**

### Risiko yang Diangkat dalam Diskusi
| ID | Risiko Spesifik | Likelihood (1-5) | Impact (1-5) | Skor | Mitigasi |
|---|---|---|---|---|---|
| R1 | ... | ... | ... | ... | ... |
| R2 | ... | ... | ... | ... | ... |
| R3 | ... | ... | ... | ... | ... |

### Risiko yang Sempat Diusulkan tapi Ditolak (karena terlalu generik)
- ... → alasan: tidak spesifik ke konteks data kependudukan

### Catatan Kepatuhan UU PDP No. 27/2022
- Data biometrik tergolong data pribadi **spesifik** → konsekuensi: ...
- Kewajiban audit trail & hak subjek data: ...

---

## 4️⃣ Diskusi Alternatif yang Ditolak

### 4a. Public Cloud Murni — ditolak oleh Nuevalen
- Alasan 1: ...
- Alasan 2: ...
- Alasan 3: ...

### 4b. Private Cloud Murni / IaaS-only — ditolak oleh Farrellino
- Alasan 1 (elastisitas): ...
- Alasan 2 (beban operasional): ...

---

## 🔍 Hasil Review Silang

| Reviewer | Bagian yang Direview | Temuan / Koreksi | Sudah Diperbaiki? |
|---|---|---|---|
| Nuevalen | Service model Farrellino | ... | ⏳ |
| Farrellino | Risiko Haniel | ... | ⏳ |
| Haniel | Argumen NIST Nuevalen | ... | ⏳ |

---

## 🎯 Refleksi Kelompok
*(diisi bersama setelah finalisasi)*

1. Trade-off paling sulit dalam tugas ini: **kerahasiaan vs skalabilitas** — bagaimana kami menyelesaikannya: ...
2. Hal baru yang dipahami tentang karakteristik NIST: ...
3. Kenapa satu sistem bisa punya **service model berbeda per komponen**: ...
4. Yang akan kami lakukan berbeda kalau mengulang: ...

---

## ✅ Checklist Akhir
- [ ] §1 Deployment model + tabel 5 NIST (Nuevalen)
- [ ] §2 Tabel service model ≥5 komponen + diagram Mermaid (Farrellino)
- [ ] §3 ≥3 risiko spesifik + matriks + mitigasi + UU PDP (Haniel)
- [ ] §4a Penolakan Public murni (Nuevalen)
- [ ] §4b Penolakan Private murni/IaaS-only (Farrellino)
- [ ] Review silang selesai oleh ketiga anggota
- [ ] 3 commit terpisah atas nama masing-masing anggota

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

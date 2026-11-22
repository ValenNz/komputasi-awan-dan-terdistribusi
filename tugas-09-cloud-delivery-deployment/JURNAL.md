# Jurnal Proses — Tugas 9: Cloud Delivery & Deployment Model

**Kelompok:** [Nama Kelompok]
**Tanggal Mulai:** [isi]
**Sifat:** Analisis di atas kertas, tanpa implementasi cloud

---

## 👥 Kontribusi Anggota

| Nama | NIM | Porsi Analisis | Status |
|---|---|---|---|
| Nuevalen Refitra Alswanfo | 103072430008 | Deployment model + 5 karakteristik NIST + tolak Public murni | ⏳ |
| Galang Herjuo Mulya | 103072430006 | Service model per komponen + diagram + tolak Private murni | ⏳ |
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
> **PIC: Nuevalen** — analisis karakteristik NIST dan pemilihan deployment model

### Opsi yang Dipertimbangkan

| Opsi | Kelebihan untuk Kasus Ini | Kekurangan | Keputusan |
|---|---|---|---|
| **Public Cloud** | Elastisitas nyaris tak terbatas saat lonjakan pemilu; biaya operasional rendah (OPEX) | Kendali infrastruktur di tangan penyedia asing; isu kedaulatan data; yurisdiksi CLOUD Act AS; tidak patuh UU PDP untuk data biometrik spesifik | ❌ **Ditolak** |
| **Private Cloud** | Kendali penuh negara, cocok untuk NIK & biometrik; kepatuhan UU PDP terjamin; audit trail internal | Elastisitas terbatas kapasitas fisik; CAPEX besar; risiko downtime saat lonjakan; butuh waktu lama untuk scale-up | ⚠️ Dipertimbangkan, tapi ditolak sebagai solusi tunggal |
| **Hybrid Cloud** | Core sensitif di private (kontrol negara), beban lonjakan non-sensitif di public (elastisitas); memadukan kerahasiaan + skalabilitas | Kompleksitas batas segmen & sinkronisasi; butuh API gateway & orkestrasi; biaya integrasi tinggi | ✅ **Dipilih** |
| **Community Cloud** | Dibagi antar instansi pemerintah (Dukcapil, Polri, Kemenkeu), tata kelola bersama, biaya dibagi | Perlu kesepakatan antar lembaga yang lama; kapasitas tetap terbatas; tidak menyelesaikan masalah lonjakan publik | ⚠️ Dapat jadi pelengkap, tapi bukan solusi utama |

### Alasan Pemilihan

**Kebutuhan kerahasiaan sebagai *hard constraint*:**
Data biometrik (sidik jari, wajah, iris) dan NIK adalah data pribadi spesifik menurut UU PDP No. 27/2022 Pasal 4. Pemrosesannya **wajib** dilakukan di bawah kendali penuh pengendali data (negara). Ini bukan preferensi, melainkan kewajiban hukum. Oleh karena itu, **core database kependudukan TIDAK BOLEH berada di public cloud**.

**Kebutuhan skalabilitas sebagai *soft constraint*:**
Pola akses tidak rata (lonjakan pemilu, pendaftaran sekolah, KYC perbankan) membutuhkan elastisitas. Namun skalabilitas ini **hanya diperlukan untuk komponen non-sensitif** (portal publik, cache, antrian, CDN, load balancer). Komponen ini tidak boleh berisi data biometrik mentah, hanya token/hash verifikasi.

**Solusi: Hybrid Cloud dengan segmentasi berbasis klasifikasi data.**
- Segmen private: data biometrik, NIK, alamat lengkap, core database.
- Segmen public: portal publik, cache, CDN, antrian, load balancer, API gateway (DMZ).
- Segmen terkontrol (gateway): token verifikasi, hash KYC, metadata transaksi.

### Bagaimana 5 Karakteristik NIST Tetap Terpenuhi

| Karakteristik NIST | Pemenuhan di Hybrid Cloud |
|---|---|
| **On-demand self-service** | Instansi pemerintah provision resource di private cloud via portal terkontrol; admin provision resource public cloud untuk beban non-sensitif |
| **Broad network access** | Instansi internal via intranet pemerintah; bank/KYC via API gateway; warga via portal publik (CDN) |
| **Resource pooling** | Pooling ganda: private pool antar instansi pemerintah (multi-tenancy terawasi), public pool komersial untuk beban non-sensitif |
| **Rapid elasticity** | Baseline di private cloud; burst ke public cloud saat lonjakan (auto-scaling hanya di public segment) |
| **Measured service** | Metering terpisah per segmen; chargeback internal untuk private; billing penyedia untuk public; audit trail terpusat untuk kepatuhan UU PDP |

### Kesimpulan Akhir

> **Deployment model yang dipilih:** **Hybrid Cloud** dengan segmentasi berbasis klasifikasi data.
>
> **Alasan utama:** Hybrid cloud adalah satu-satunya model yang memenuhi **hard constraint** kerahasiaan data biometrik (UU PDP, kedaulatan data) sekaligus **soft constraint** skalabilitas saat lonjakan akses. Private cloud murni gagal di elastisitas; public cloud murni gagal di kerahasiaan; community cloud tidak menyelesaikan masalah lonjakan publik. Hybrid memadukan keunggulan keduanya dengan trade-off kompleksitas operasional yang dapat dikelola.

---

## 4️⃣ Diskusi Alternatif yang Ditolak

### 4a. Public Cloud Murni — ditolak oleh Nuevalen

**Alasan 1: Pelanggaran kedaulatan data dan risiko yurisdiksi asing**
Data biometrik 280 juta warga negara adalah aset kedaulatan. Jika disimpan di public cloud penyedia asing (AWS, GCP, Azure), data tunduk pada hukum negara penyedia. **CLOUD Act AS** memungkinkan penegak hukum AS memaksa penyedia membuka data warga asing, meskipun server fisik berada di luar AS. Ini adalah risiko geopolitik yang tidak dapat diterima untuk infrastruktur kritis negara.

**Alasan 2: Ketidakpatuhan terhadap UU PDP No. 27/2022**
UU PDP mengklasifikasikan data biometrik sebagai **data pribadi spesifik** (Pasal 4) yang memerlukan perlindungan khusus. Public cloud murni membuat pemerintah kehilangan kendali atas:
- Lokasi fisik server (dapat berpindah tanpa pemberitahuan).
- Akses internal karyawan penyedia ke data.
- Audit trail yang dapat diverifikasi otoritas Indonesia.

Pelanggaran UU PDP berisiko sanksi administratif (denda hingga 2% pendapatan tahunan) dan pidana bagi pejabat pengendali data.

**Alasan 3: Vendor lock-in pada infrastruktur kritis nasional**
Sistem data kependudukan adalah critical national infrastructure. Ketergantungan pada satu penyedia public cloud menciptakan:
- Risiko pemutusan layanan akibat sanksi internasional atau kebangkrutan penyedia.
- Biaya migrasi keluar yang hampir mustahil untuk data sebesar ini.
- Ketidakpastian anggaran jangka panjang karena harga dapat berubah sepihak.

Prinsip **digital sovereignty** mengharuskan negara mempertahankan kendali penuh atas infrastruktur data kritisnya.

**Keputusan final:** Public cloud murni **ditolak total**. Namun, public cloud **dapat digunakan sebagai segmen pelengkap** dalam arsitektur hybrid, khusus untuk komponen non-sensitif (portal publik, cache, CDN) dengan batas data yang ketat (hanya token/hash, tidak ada data biometrik mentah).

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

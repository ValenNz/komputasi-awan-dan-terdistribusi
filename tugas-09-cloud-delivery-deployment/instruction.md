# 📋 Pembagian Tugas 9 — Cloud Delivery & Deployment Model
## Studi Kasus: Sistem Data Kependudukan Nasional

**Kelompok:** [Isi Nama Kelompok]
**Sifat Tugas:** Murni analisis & desain di atas kertas (TIDAK ada implementasi cloud / biaya apa pun)
**Target Selesai:** H-2 sebelum deadline

---

## 👥 Anggota & Porsi Kerja (Semua Dapat Bagian Analisis)

| Nama | NIM | Fokus Analisis | Bobot Rubrik yang Diampu |
|---|---|---|---|
| **Nuevalen Refitra Alswanfo** | 103072430008 | Deployment Model + Pemetaan 5 Karakteristik NIST | **30%** + 10% |
| **Farrellino Ulung Satya Amando** | 103072400005 | Service Model per Komponen + Diagram Arsitektur | **25%** + 10% |
| **Haniel Juanta Sembiring** | 103072400145 | Analisis Risiko & Mitigasi + Compliance UU PDP | **25%** |

> **Prinsip:** Tidak ada anggota yang tugasnya hanya "merapikan README". Integrasi dokumen adalah tugas **bersama**, dan setiap orang menulis sendiri bagian analisisnya langsung ke `README.md`.

---

## 🔵 NUEVALEN — Deployment Model & Karakteristik NIST

### Deliverable Wajib (tulis langsung di `README.md` §1 dan §4a)

**1. Rekomendasi Deployment Model (bobot 30%)**
- Pilih SATU: Public / Private / Hybrid / Community Cloud.
- Argumen **wajib berbasis kebutuhan kasus**, bukan hafalan definisi:
  - Kerahasiaan NIK + biometrik ( UU PDP No. 27/2022 )
  - Kedaulatan data (*data sovereignty*) — negara haruskendali penuh infrastruktur
  - Pola akses tidak rata (lonjakan pemilu / pendaftaran sekolah)
- Jelaskan **segmen mana yang masuk private, segmen mana yang boleh keluar**, kalau memilih Hybrid.

**2. Tabel Pemetaan 5 Karakteristik Esensial NIST SP 800-145**

Wajib isi kolom "Bagaimana model pilihan kami memenuhinya" untuk kelima baris:

| Karakteristik NIST | Terpenuhi? | Penjelasan Konkret di Sistem Kependudukan |
|---|---|---|
| On-demand self-service | ... | mis. Dukcapil daerah provisioning akun via portal mandiri |
| Broad network access | ... | ... |
| Resource pooling | ... | ... |
| Rapid elasticity | ... | ... |
| Measured service | ... | ... |

**3. Alternatif yang Ditolak #1 — Public Cloud Murni (bobot 10%)**
- Minimal 3 alasan penolakan yang spesifik ke data kependudukan (bukan "tidak aman" saja).
- Kaitkan dengan konsekuensi hukum & kedaulatan data.

### Definition of Done
- [ ] Rekomendasi deployment model + minimal 4 paragraf argumen
- [ ] Tabel 5 karakteristik NIST terisi semua (tidak ada "...")
- [ ] Penolakan Public Cloud murni dengan ≥3 alasan konkret
- [ ] Commit atas nama sendiri

---

## 🟢 FARRELLINO — Service Model per Komponen & Diagram

### Deliverable Wajib (tulis langsung di `README.md` §2 dan §4b)

**1. Dekomposisi Sistem Jadi Komponen (bobot 25%)**

Minimal **5 komponen**, contoh yang wajib dipertimbangkan:
- Database inti kependudukan (NIK, alamat, biometrik)
- API verifikasi KYC untuk bank/kepolisian
- Portal publik cek status permohonan (tanpa data sensitif)
- Sistem antrian / notifikasi
- Dashboard analytics untuk pembuat kebijakan
- Backup & disaster recovery

**2. Tabel Pemetaan Komponen → Service Model + Alasan**

| Komponen | Service Model (IaaS/PaaS/SaaS) | Segmen (Private/Public) | Alasan Teknis & Keamanan |
|---|---|---|---|
| Database inti + biometrik | ... | ... | ... |
| API KYC | ... | ... | ... |
| Portal cek status | ... | ... | ... |
| Notifikasi / email | ... | ... | ... |
| Dashboard analytics | ... | ... | ... |

> Aturan: **tidak boleh semua komponen diberi label yang sama**. Harus ada diferensiasi dan alasan kenapa berbeda.

**3. Diagram Arsitektur (Mermaid) → simpan juga di `bukti/`**
- Tunjukkan batas tegas **private segment ↔ public segment**.
- Tandai komponen mana yang boleh menyentuh data sensitif, mana yang hanya data ter-*anonimize*.
- Gunakan `flowchart` atau `graph TD` dengan `subgraph`.

**4. Alternatif yang Ditolak #2 — Private Cloud Murni / IaaS-only (bobot 10%)**
- Kenapa kurang tepat dari sisi skalabilitas saat lonjakan pemilu?
- Kenapa beban operasional (SDM, patching, capacity planning) jadi masalah?

### Definition of Done
- [ ] Tabel ≥5 komponen dengan service model berbeda-beda + alasan
- [ ] Diagram Mermaid valid (dirender, tidak error)
- [ ] Penolakan Private murni/IaaS-only dengan argumen elastisitas
- [ ] Commit atas nama sendiri

---

## 🟠 HANIEL — Analisis Risiko, Mitigasi & Kepatuhan Regulasi

### Deliverable Wajib (tulis langsung di `README.md` §3)

**1. Minimal 3 Risiko Spesifik + Mitigasi (bobot 25%)**

⚠️ **Risiko generik seperti "server bisa down" atau "data bisa dicuri" TIDAK diterima.** Harus spesifik ke konteks data kependudukan + model yang dipilih. Contoh arah yang benar:

| No | Risiko Spesifik | Dampak ke Warga Negara | Mitigasi Konkret |
|---|---|---|---|
| R1 | Kebocoran NIK/biometrik lewat segmen public yang salah konfigurasi | ... | ... |
| R2 | Gagal sinkronisasi data private ↔ public saat lonjakan pemilu | ... | ... |
| R3 | *Vendor lock-in* / yurisdiksi hukum penyedia cloud asing | ... | ... |
| R4 | *Insider threat* operator Dukcapil daerah | ... | ... |

**2. Matriks Risiko (Likelihood × Impact)**
- Beri skor 1–5 untuk tiap risiko, hitung prioritas.
- Tentukan risiko mana yang harus ditangani lebih dulu.

**3. Checklist Kepatuhan Regulasi**
- UU PDP No. 27/2022 (pasal tentang data spesifik/biometrik & pemrosesan)
- Kewajiban *data localization* untuk data strategis pemerintah
- Audit trail & hak subjek data (akses, koreksi, penghapusan)

**4. Verifikasi Silang (quality gate)**
- Cek apakah risiko yang ditulis benar-benar **nyambung** dengan deployment model Nuevalen dan komponen Farrellino.
- Kalau ada yang tidak sinkron, angkat di grup sebelum push.

### Definition of Done
- [ ] ≥3 risiko spesifik konteks kependudukan + mitigasi konkret
- [ ] Matriks likelihood × impact terisi
- [ ] Checklist kepatuhan UU PDP
- [ ] Commit atas nama sendiri

---

## 🤝 TUGAS BERSAMA (bukan dilempar ke satu orang)

| Aktivitas | Peserta | Durasi |
|---|---|---|
| Kick-off: sepakati hipotesis awal deployment model | Semua | 30 menit |
| Kerja individu sesuai porsi | Masing-masing | 1–2 hari |
| Sesi review silang (baca bagian teman, kasih koreksi) | Semua | 45 menit |
| Finalisasi `README.md` + isi `JURNAL.md` bagian masing-masing | Semua | 30 menit |
| Commit & push dari laptop sendiri | Semua | 10 menit |

### Aturan Review Silang
- Nuevalen → review tabel service model Farrellino (apakah segmen private/public konsisten?)
- Farrellino → review risiko Haniel (apakah komponennya ada di diagram?)
- Haniel → review argumen NIST Nuevalen (apakah 5 karakteristik benar-benar terjawab, bukan tempelan?)

---

## 🧭 Hipotesis Awal untuk Didiskusikan (belum final!)

> Ini **titik berangkat diskusi**, bukan jawaban jadi. Setiap anggota wajib menguji/membantah hipotesis ini di bagiannya masing-masing.

- **Deployment:** Hybrid — private untuk database inti & biometrik, public untuk portal cek status/antrian yang tidak memuat data sensitif.
- **Service:** IaaS/PaaS di private untuk core, PaaS/SaaS di public untuk komponen non-sensitif.
- **Risiko utama:** kebocoran di batas segmen + gagal sinkronisasi saat lonjakan.

Kalau ada anggota yang punya argumen lebih kuat untuk **Community Cloud** (cloud khusus antar-instansi pemerintah) atau **Private + CDN**, silakan bawa ke sesi kick-off — keputusan final dicatat di `JURNAL.md`.

---

## 📁 Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md              # §1 Nuevalen | §2 Farrellino | §3 Haniel | §4a Nuevalen | §4b Farrellino
├── JURNAL.md              # diisi masing-masing anggota
├── PEMBAGIAN_TUGAS.md     # dokumen ini
└── bukti/
    ├── arsitektur.mmd     # Farrellino
    └── matriks-risiko.md  # Haniel (opsional)
```

### Kerangka `README.md` (biar tidak tabrakan saat merge)

```
# Tugas 9 — Cloud Delivery & Deployment Model
## Studi Kasus                        [bersama]
## 1. Rekomendasi Deployment Model    [NUEVALEN]
## 2. Rekomendasi Service Model       [FARRELLINO]
## 3. Risiko & Mitigasi               [HANIEL]
## 4. Perbandingan Alternatif Ditolak
### 4a. Public Cloud Murni            [NUEVALEN]
### 4b. Private Murni / IaaS-only     [FARRELLINO]
## Ringkasan Kontribusi               [bersama]
```

> 💡 Karena satu file diedit 3 orang, **kerjakan berurutan atau pakai branch terpisah** lalu merge. Jangan edit section orang lain.

---

## 🚀 Git Commit (wajib dari laptop masing-masing)

```bash
# NUEVALEN
git pull origin main
git add tugas-09-cloud-delivery-deployment/README.md
git commit -m "Tugas 9: Nuevalen - Rekomendasi deployment model, pemetaan 5 karakteristik NIST, & penolakan public cloud murni"
git push origin main

# FARRELLINO
git pull origin main
git add tugas-09-cloud-delivery-deployment/README.md tugas-09-cloud-delivery-deployment/bukti/
git commit -m "Tugas 9: Farrellino - Pemetaan service model per komponen, diagram arsitektur, & penolakan private murni"
git push origin main

# HANIEL
git pull origin main
git add tugas-09-cloud-delivery-deployment/README.md tugas-09-cloud-delivery-deployment/JURNAL.md
git commit -m "Tugas 9: Haniel - Analisis risiko spesifik kependudukan, matriks risiko, mitigasi, & checklist UU PDP"
git push origin main
```

---

## 📊 Peta Rubrik → Penanggung Jawab

| Komponen Rubrik | Bobot | Penanggung Jawab |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | **Nuevalen** |
| Ketepatan rekomendasi service model | 25% | **Farrellino** |
| Analisis risiko & mitigasi | 25% | **Haniel** |
| Perbandingan alternatif ditolak | 20% | **Nuevalen (10%) + Farrellino (10%)** |
| Proses & kontribusi (JURNAL + commit) | — | **Semua** |

**Total:** setiap anggota memegang porsi analisis yang dinilai, tidak ada yang hanya jadi "editor".
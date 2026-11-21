# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.


## Bagian 1 — Rekomendasi Deployment Model (Nuevalen)

### 1.1 Rekomendasi: Hybrid Cloud dengan Segmentasi Berbasis Klasifikasi Data

Setelah menganalisis keempat opsi deployment model terhadap studi kasus Sistem Data Kependudukan, kelompok merekomendasikan **Hybrid Cloud** dengan segmentasi ketat berbasis klasifikasi data.

**Arsitektur segmentasi:**

| Segmen | Lokasi | Jenis Data | Tujuan |
|---|---|---|---|
| **Private Cloud (Government Cloud)** | Data center milik negara / pemerintah | NIK, data biometrik, alamat lengkap, data sensitif lainnya | Core database kependudukan, otoritas data primer |
| **Public Cloud** | Penyedia cloud komersial (dengan DC di wilayah Indonesia) | Data non-sensitif, cache, CDN, portal publik, antrian, load balancer | Menangani lonjakan akses, portal cek status, distribusi konten statis |
| **Secure Gateway / API Gateway** | Private segment (DMZ terkontrol) | Token verifikasi, hash KYC, metadata transaksi | Titik integrasi dengan instansi eksternal (bank, kepolisian) |

### 1.2 Justifikasi Berbasis Karakteristik Esensial NIST (SP 800-145)

Rekomendasi ini dievaluasi terhadap lima karakteristik esensial cloud computing menurut NIST:

#### 1. On-Demand Self-Service
Instansi pemerintah (dukcapil daerah, kepolisian) dapat memprovision resource komputasi untuk kebutuhan operasionalnya sendiri melalui portal terkontrol di **private cloud**, tanpa harus menunggu intervensi manual dari operator pusat. Untuk beban non-sensitif (misalnya portal publik saat musim pendaftaran sekolah), admin dapat menambah kapasitas di **public cloud** secara mandiri melalui dashboard penyedia.

#### 2. Broad Network Access
Layanan harus dapat diakses dari ribuan instansi di seluruh Indonesia melalui jaringan standar (internet/API). Hybrid cloud memungkinkan:
- Instansi internal mengakses core data via **jaringan pemerintah tertutup (Intranet Gov/Leased Line)**.
- Bank dan mitra KYC mengakses via **API Gateway** yang berada di segmen terkontrol dengan autentikasi ketat (mTLS, API key, rate limiting).
- Warga mengakses portal publik via **public cloud** yang di-front-end dengan CDN.

#### 3. Resource Pooling
- **Private cloud**: resource pooling antar instansi pemerintah dalam satu kluster terkelola, dengan multi-tenancy yang diawasi oleh otoritas pusat (Kemendagri/BSSN).
- **Public cloud**: resource pooling komersial untuk beban non-sensitif, dengan isolasi tenant yang disediakan penyedia.

Model hybrid memungkinkan pooling ganda: negara tetap punya kendali atas pool sumber daya data sensitif, sementara pool publik digunakan untuk skala.

#### 4. Rapid Elasticity (Karakteristik Penentu)
Ini adalah alasan utama hybrid dipilih. Studi kasus menyebutkan **pola akses tidak rata** dengan lonjakan saat:
- Musim pemilu (verifikasi DPT oleh KPU, partai, pengawas)
- Pendaftaran sekolah baru (verifikasi KK dan NIK orang tua)
- Lonjakan KYC perbankan di akhir tahun

**Private cloud murni tidak dapat memenuhi rapid elasticity** tanpa over-provisioning mahal yang menganggur di hari biasa. **Public cloud murni tidak dapat diterima** karena data biometrik. Hybrid adalah satu-satunya model yang memenuhi keduanya:
- Beban dasar (baseline) ditangani private cloud dengan kapasitas tetap.
- Lonjakan (burst) di-*spill over* ke public cloud untuk komponen non-sensitif (portal, cache, antrian, CDN).
- Auto-scaling hanya berlaku di public segment; private segment tetap pada kapasitas terencana.

#### 5. Measured Service
Penggunaan resource dapat diukur dan diaudit per segmen:
- Private cloud: metering internal untuk chargeback antar instansi pemerintah.
- Public cloud: metering dari penyedia, dengan tag per proyek/instansi.
- Audit trail terpusat memungkinkan verifikasi kepatuhan terhadap UU PDP.

### 1.3 Pemenuhan Kebutuhan Studi Kasus

| Kebutuhan Studi Kasus | Bagaimana Hybrid Cloud Memenuhi |
|---|---|
| Data sangat rahasia (UU PDP) | Core data di private cloud, kendali penuh negara, tidak keluar yurisdiksi |
| Ribuan instansi dengan akses tidak rata | Public cloud menyerap lonjakan; private cloud melayani akses terkontrol |
| Skalabilitas tanpa downtime | Burst ke public cloud saat pemilu/pendaftaran sekolah |
| Infrastruktur terkendali negara | Data biometrik & NIK tidak pernah menyentuh public cloud |

### 1.4 Trade-off yang Diterima

Hybrid cloud bukan solusi sempurna. Trade-off yang diterima:
- **Kompleksitas operasional tinggi**: dua lingkungan, dua model keamanan, dua set alat monitoring.
- **Sinkronisasi data**: data yang perlu diakses dari kedua segmen (misalnya token verifikasi KYC) harus disinkronkan dengan hati-hati.
- **Biaya integrasi**: API gateway, VPN, dan orkestrasi antar segmen menambah biaya.

Namun trade-off ini **lebih dapat diterima** daripada risiko melanggar UU PDP (jika memilih public cloud) atau risiko downtime massal saat pemilu (jika memilih private cloud murni).

---

## Bagian 4 — Alternatif yang Ditolak: Public Cloud Murni (Nuevalen)

Kelompok menolak **Public Cloud Murni** sebagai deployment model untuk Sistem Data Kependudukan. Berikut tiga alasan utama penolakan:

### Alasan 1: Kedaulatan Data dan Yurisdiksi Hukum

Data kependudukan (NIK, biometrik, alamat) adalah **aset kedaulatan negara**, bukan data komersial biasa. Jika disimpan di public cloud milik penyedia asing (AWS, GCP, Azure yang data centernya tersebar global), data tersebut tunduk pada yurisdiksi negara tempat penyedia beroperasi.

- **CLOUD Act (Amerika Serikat)** memungkinkan penegak hukum AS memaksa penyedia cloud AS membuka data warga negara asing, meskipun data tersebut disimpan di luar AS.
- **Data biometrik** (sidik jari, wajah, iris) tergolong **data pribadi spesifik** menurut UU PDP No. 27/2022 Pasal 4, yang pemrosesannya memerlukan perlindungan khusus.
- Menyerahkan data biometrik 280 juta warga negara ke entitas yang tunduk pada hukum asing adalah **risiko kedaulatan yang tidak dapat diterima**.

### Alasan 2: Ketidakpatuhan terhadap UU PDP No. 27/2022

UU Perlindungan Data Pribadi Indonesia menetapkan kewajiban ketat bagi pengendali data:

- **Pasal 35**: Pengendali data wajib menjaga keamanan data pribadi.
- **Pasal 56**: Larangan transfer data pribadi ke negara lain yang tidak memiliki tingkat perlindungan setara, kecuali ada perjanjian bilateral.
- **Pasal 4**: Data biometrik adalah data spesifik yang pemrosesannya memerlukan dasar hukum eksplisit dan tujuan spesifik.

Public cloud murni membuat pemerintah **kehilangan kendali operasional** atas:
- Lokasi fisik server (bisa berpindah tanpa pemberitahuan).
- Akses internal karyawan penyedia cloud ke data.
- Audit trail yang dapat diverifikasi oleh otoritas Indonesia.

Sanksi pelanggaran UU PDP mencapai **2% dari pendapatan tahunan** (untuk pengendali data sektor publik, dapat berupa sanksi administratif dan pidana bagi pejabat).

### Alasan 3: Vendor Lock-In pada Infrastruktur Kritis Negara

Sistem data kependudukan adalah **infrastruktur kritis nasional** (critical national infrastructure). Jika dibangun di atas public cloud murni:

- **Ketergantungan pada satu penyedia** menciptakan risiko geopolitik (sanksi, embargo, pemutusan layanan).
- **Migrasi keluar** dari public cloud untuk data sebesar ini hampir mustahil dalam waktu singkat.
- **Harga dapat berubah sepihak** oleh penyedia, menciptakan ketidakpastian anggaran negara jangka panjang.
- **Kegagalan penyedia** (bangkrut, terkena sanksi internasional) dapat melumpuhkan layanan kependudukan nasional.

Prinsip **digital sovereignty** mengharuskan negara mempertahankan kendali penuh atas infrastruktur data kritisnya, bukan menyerahkannya pada entitas komersial asing.

### Kesimpulan Penolakan

Public cloud murni **ditolak** karena:
1. Melanggar kedaulatan data dan membuka risiko yurisdiksi asing.
2. Tidak memenuhi kewajiban UU PDP untuk data biometrik spesifik.
3. Menciptakan vendor lock-in yang tidak dapat diterima untuk infrastruktur kritis negara.

Oleh karena itu, **Hybrid Cloud** dipilih sebagai kompromi: data sensitif tetap di private cloud (kendali negara penuh), sementara beban lonjakan non-sensitif dapat memanfaatkan elastisitas public cloud tanpa membahayakan kerahasiaan data inti.
##  **STRUKTUR MATERI CHAPTER 1**

### **1. DISTRIBUTED VS DECENTRALIZED SYSTEMS**

**Konsep Dasar:**
- **Centralized**: Sistem dengan kontrol terpusat (satu titik kendali)
- **Decentralized**: Proses dan sumber daya tersebar di banyak komputer, tapi tidak harus terkoordinasi
- **Distributed**: Proses dan sumber daya **cukup tersebar** di banyak komputer dan saling berkoordinasi

**Pertanyaan Kritis:**
Kapan sistem decentralized menjadi distributed? Apakah dengan menambah 1 link, 2 link, atau k links? Ini menunjukkan bahwa perbedaannya bukan sekadar jumlah koneksi, tapi **tingkat koordinasi dan integrasi**.

**Two Views on Realizing Distributed Systems:**
1. **Integrative View**: Menghubungkan sistem jaringan yang sudah ada menjadi sistem yang lebih besar
2. **Expansive View**: Memperluas sistem jaringan yang ada dengan komputer tambahan

**Definisi Formal:**
- **Decentralized System**: Sistem jaringan di mana proses dan sumber daya **necessarily** (harus) tersebar di banyak komputer
- **Distributed System**: Sistem jaringan di mana proses dan sumber daya **sufficiently** (cukup) tersebar di banyak komputer

---

### **2. MISKONSEPSI UMUM**

**a. "Centralized solutions do not scale" / " solusi yang terpusat tidak dapat berkembang atau menangani beban yang semakin besar"**
- **Definisi**
   "Solusi terpusat tidak dapat ditingkatkan skalanya dengan mudah (tidak scalable)."
- **Fakta**: Perlu bedakan antara **logically centralized** vs **physically centralized**
- **Contoh DNS Root**: 
  - Logically centralized (satu namespace)
  - Physically massively distributed (banyak server root di seluruh dunia)
  - Decentralized across organizations (dikelola berbagai organisasi)

**b. "Centralized solutions have a single point of failure" / "Solusi terpusat memiliki satu titik kegagalan tunggal"**
- **Definisi**
  - Centralized solutions (Solusi terpusat): Sebuah sistem di mana seluruh data, proses, atau kendali diatur dan disimpan di satu tempat atau satu server utama.
  - Single point of failure (Titik kegagalan tunggal): Satu bagian dari sistem yang jika bagian tersebut rusak, macet, atau mati, maka seluruh sistem akan ikut mati total.
- **Fakta**: Tidak selalu benar (contoh: DNS root)
- Single point of failure justru seringkali:
  - Lebih mudah dikelola
  - Lebih mudah dibuat robust (tahan kegagalan)
- **Contoh**
  Server Bank Down: Jika sebuah bank hanya menggunakan satu server pusat untuk memproses semua transaksi, dan server tersebut mati, maka seluruh nasabah di seluruh dunia tidak akan bisa mengambil uang atau menggunakan aplikasi mobile banking.

**Pelajaran Penting**: Banyak miskonsepsi tentang scalability, fault tolerance, security yang poorly founded. Kita perlu mengembangkan skill untuk menilai miskonsepsi tersebut.

---

## **3. PERSPECTIVES ON DISTRIBUTED SYSTEMS**

Distributed systems itu **kompleks** — untuk memahaminya secara menyeluruh, kita perlu melihat dari **berbagai perspektif**. Bayangkan seperti melihat gajah dari berbagai sudut: arsitekturnya, prosesnya, cara komunikasinya, dll. Tidak ada satu perspektif yang bisa menjelaskan semuanya.

Berikut penjelasan mendetail untuk setiap perspektif:

---

### **ARCHITECTURE (Arsitektur)**

**Definisi:**
Cara komponen-komponen sistem terdistribusi **diorganisir** dan **dihubungkan** satu sama lain. Ini mencakup pola struktur, pembagian tanggung jawab, dan hierarki komponen.

**Pertanyaan Kunci:**
- Bagaimana sistem dibagi menjadi komponen-komponen?
- Apa hubungan antara komponen-komponen tersebut?
- Apakah ada hierarki atau peer-to-peer?

**Common Architectural Patterns:**

**a. Client-Server Architecture:**
```
[Client 1] ──┐
[Client 2] ──┼──> [Server]
[Client 3] ──┘
```
- Client meminta layanan, server menyediakan layanan
- Contoh: Web browser (client) ↔ Web server
- **Kelebihan**: Kontrol terpusat, mudah dikelola
- **Kekurangan**: Server jadi bottleneck dan single point of failure

**b. Peer-to-Peer (P2P) Architecture:**
```
[Peer 1] ←──> [Peer 2]
   ↑    ↖       ↗   ↓
   │      ↘   ↙     │
[Peer 3] ←──> [Peer 4]
```
- Semua node setara, bisa jadi client dan server sekaligus
- Contoh: BitTorrent, early Skype
- **Kelebihan**: Scalable, tidak ada single point of failure
- **Kekurangan**: Sulit dikelola, kualitas tidak terjamin

**c. Multi-tier Architecture:**
```
[Tier 1: Presentation] ──> [Tier 2: Logic] ──> [Tier 3: Data]
```
- Sistem dibagi menjadi layer-layer (presentation, business logic, data)
- Contoh: Web app (frontend → backend API → database)
- **Kelebihan**: Separation of concerns, mudah di-scale per layer
- **Kekurangan**: Latency bertambah karena banyak hop

**d. Microservices Architecture:**
```
[Service A] ←──> [Service B]
      ↓              ↓
[Service C] ←──> [Service D]
```
- Sistem dibagi jadi service-service kecil yang independen
- Contoh: Netflix, Uber (modul pembayaran, notifikasi, dll terpisah)
- **Kelebihan**: Independen deployment, scalable per service
- **Kekurangan**: Kompleksitas operasional tinggi, distributed tracing sulit

**Mengapa Penting:**
Arsitektur menentukan **scalability**, **fault tolerance**, dan **maintainability** sistem. Pilihan arsitektur yang salah di awal bisa jadi bencana di kemudian hari.

---

### **PROCESS (Proses)**

**Definisi:**
Jenis-jenis **proses** yang berjalan di sistem terdistribusi dan **hubungan** antara proses-proses tersebut.

**Pertanyaan Kunci:**
- Apa saja proses yang berjalan?
- Apakah proses-proses ini cooperating atau competing?
- Bagaimana mereka berinteraksi?

**Types of Processes:**

**a. Client Processes:**
- Meminta layanan dari server
- Biasanya short-lived (hidup sebentar, selesai request)
- Contoh: Browser yang request halaman web

**b. Server Processes:**
- Menyediakan layanan ke client
- Biasanya long-lived (berjalan terus-menerus)
- Contoh: Web server, database server

**c. Peer Processes:**
- Bisa jadi client dan server sekaligus
- Contoh: Node BitTorrent yang download dan upload bersamaan

**d. Daemon/Background Processes:**
- Berjalan di background, tidak berinteraksi langsung dengan user
- Contoh: Cron job, monitoring agent

**Process Relationships:**

**a. Cooperating Processes:**
- Bekerja sama untuk mencapai tujuan bersama
- Contoh: Proses di MapReduce yang sama-sama hitung hasil
- **Tantangan**: Butuh koordinasi dan sinkronisasi

**b. Competing Processes:**
- Berebut resource yang sama
- Contoh: Banyak user yang sama-sama akses database
- **Tantangan**: Butuh mekanisme locking, concurrency control

**c. Independent Processes:**
- Tidak saling berinteraksi
- Contoh: User yang berbeda browsing web
- **Tantangan**: Minimal, tapi tetap butuh resource management

**Mengapa Penting:**
Memahami proses membantu kita mendesain **scheduling**, **load balancing**, dan **resource allocation** yang efisien.

---

### **COMMUNICATION (Komunikasi)**

**Definisi:**
Fasilitas dan mekanisme untuk **bertukar data** antar komponen dalam sistem terdistribusi.

**Pertanyaan Kunci:**
- Bagaimana data ditransfer?
- Apa protokol yang digunakan?
- Apakah komunikasi synchronous atau asynchronous?

**Communication Models:**

**a. Synchronous Communication (RPC - Remote Procedure Call):**
```
Client ──request──> Server
Client <──response── Server
(Client menunggu sampai response datang)
```
- Client kirim request dan **menunggu** response
- Contoh: REST API, gRPC
- **Kelebihan**: Sederhana, mudah di-debug
- **Kekurangan**: Blocking, latency tinggi kalau server lambat

**b. Asynchronous Communication (Message Passing):**
```
Client ──message──> [Message Queue] ──> Server
(Client tidak menunggu, langsung lanjut)
```
- Client kirim message dan **tidak menunggu** response
- Contoh: RabbitMQ, Kafka
- **Kelebihan**: Non-blocking, decoupling, scalable
- **Kekurangan**: Kompleks, sulit track message flow

**c. Multicast/Broadcast:**
```
Client ──message──> [Semua subscribers]
```
- Satu message dikirim ke banyak penerima sekaligus
- Contoh: Pub/Sub systems, chat rooms
- **Kelebihan**: Efisien untuk one-to-many
- **Kekurangan**: Overhead kalau banyak subscriber

**Communication Protocols:**

**a. TCP (Transmission Control Protocol):**
- Reliable, ordered delivery
- Ada handshake, acknowledgment, retransmission
- Contoh: HTTP, FTP
- **Use case**: Data yang harus sampai utuh dan berurutan

**b. UDP (User Datagram Protocol):**
- Unreliable, unordered delivery
- Tidak ada handshake, lebih cepat
- Contoh: Video streaming, DNS
- **Use case**: Performance lebih penting daripada reliability

**c. HTTP/HTTPS:**
- Application layer protocol untuk web
- Stateless (tidak simpan state antar request)
- HTTPS = HTTP + TLS (encrypted)

**Mengapa Penting:**
Pilihan komunikasi mempengaruhi **latency**, **throughput**, dan **fault tolerance**. Salah pilih bisa bikin sistem lambat atau tidak reliable.

---

### **COORDINATION (Koordinasi)**

**Definisi:**
Algoritma-algoritma **independen dari aplikasi** yang digunakan untuk **mengkoordinasi** aktivitas proses-proses dalam sistem terdistribusi.

**Pertanyaan Kunci:**
- Bagaimana proses-proses sinkronisasi?
- Bagaimana menghindari konflik?
- Bagaimana mencapai consensus?

**Coordination Problems:**

**a. Mutual Exclusion (Mutex):**
- Hanya satu proses yang boleh akses resource tertentu pada satu waktu
- Contoh: Dua user tidak boleh edit file yang sama bersamaan
- **Solusi**: Distributed locks (Zookeeper, etcd)

**b. Leader Election:**
- Memilih satu proses sebagai "leader" dari sekelompok proses
- Contoh: Database replica yang jadi master
- **Algoritma**: Bully algorithm, Raft consensus

**c. Distributed Consensus:**
- Semua proses harus setuju pada satu nilai
- Contoh: Blockchain, distributed database
- **Algoritma**: Paxos, Raft
- **Tantangan**: Byzantine fault tolerance (kalau ada node yang malicious)

**d. Clock Synchronization:**
- Menyamakan waktu antar node
- Contoh: Timestamp untuk event ordering
- **Algoritma**: NTP (Network Time Protocol), Lamport logical clocks

**e. Deadlock Detection:**
- Mendeteksi situasi di mana proses-proses saling menunggu
- Contoh: Transaction A tunggu lock dari B, B tunggu lock dari A
- **Solusi**: Timeout, deadlock detection algorithm

**Mengapa Penting:**
Tanpa koordinasi yang baik, sistem terdistribusi bisa mengalami **race conditions**, **deadlocks**, dan **inconsistencies**.

---

### **NAMING (Penamaan)**

**Definisi:**
Cara **mengidentifikasi** dan **mengakses** resource dalam sistem terdistribusi.

**Pertanyaan Kunci:**
- Bagaimana kita identifikasi resource?
- Bagaimana kita cari lokasi resource?
- Bagaimana kita handle perubahan lokasi?

**Naming Concepts:**

**a. Name vs Identifier vs Address:**
- **Name**: String yang mudah dibaca manusia (contoh: "www.google.com")
- **Identifier**: Unique key untuk resource (contoh: UUID)
- **Address**: Lokasi fisik resource (contoh: IP address 142.250.195.4)

**b. Name Resolution:**
- Proses menerjemahkan name jadi address
- Contoh: DNS (Domain Name System)
  ```
  www.google.com → 142.250.195.4
  ```

**c. Naming Services:**
- Layanan yang manage mapping name ↔ address
- Contoh: DNS, LDAP, Service Discovery (Consul, etcd)

**Naming Challenges:**

**a. Mobility:**
- Resource bisa pindah lokasi (mobile devices, VM migration)
- Solusi: Location-independent identifiers + location service

**b. Scalability:**
- Sistem naming harus handle jutaan resource
- Solusi: Hierarchical naming (DNS), distributed hash tables (DHT)

**c. Consistency:**
- Mapping name ↔ address bisa berubah
- Solusi: TTL (Time To Live), caching strategies

**Mengapa Penting:**
Naming yang buruk bikin sistem sulit digunakan dan di-maintain. User tidak mau ingat IP address, mereka mau pakai nama yang mudah.

---

### **CONSISTENCY AND REPLICATION (Konsistensi dan Replikasi)**

**Definisi:**
Menjaga **konsistensi data** yang **direplikasi** di banyak node, sambil tetap menjaga **performance**.

**Pertanyaan Kunci:**
- Bagaimana kita replikasi data?
- Bagaimana kita jaga konsistensi antar replica?
- Apa trade-off antara consistency dan performance?

**Replication Strategies:**

**a. Active Replication (Eager/Write-all):**
```
Write ──> [Replica 1] ──> [Replica 2] ──> [Replica 3]
(Semua replica di-update sebelum response ke client)
```
- Semua replica di-update bersamaan
- **Kelebihan**: Strong consistency, high availability
- **Kekurangan**: Latency tinggi (tunggu semua replica)

**b. Passive Replication (Lazy/Write-one):**
```
Write ──> [Primary] ──> [Backup 1]
                     └─> [Backup 2]
(Update backup secara asynchronous)
```
- Hanya primary yang di-update, backup di-update belakangan
- **Kelebihan**: Latency rendah
- **Kekurangan**: Weak consistency, risiko data loss kalau primary crash sebelum replicate

**c. Quorum-based Replication:**
- Write: Update W replica
- Read: Baca dari R replica
- Constraint: W + R > N (total replica)
- Contoh: DynamoDB, Cassandra

**Consistency Models:**

**a. Strong Consistency:**
- Semua client lihat data yang sama pada waktu yang sama
- Contoh: Traditional RDBMS
- **Trade-off**: Performance rendah, availability rendah

**b. Eventual Consistency:**
- Kalau tidak ada update, semua replica akhirnya akan sama
- Contoh: DNS, Cassandra
- **Trade-off**: Performance tinggi, tapi client bisa lihat data lama

**c. Causal Consistency:**
- Operasi yang causal related dilihat dalam urutan yang sama oleh semua client
- Contoh: Social media feeds
- **Trade-off**: Lebih kompleks dari eventual consistency

**CAP Theorem:**
Dalam sistem terdistribusi, kamu hanya bisa pilih **2 dari 3**:
- **C**onsistency: Semua node lihat data yang sama
- **A**vailability: Setiap request dapat response
- **P**artition tolerance: Sistem tetap jalan meski ada network partition

**Mengapa Penting:**
Replikasi dan konsistensi adalah **trade-off** antara performance, availability, dan correctness. Salah pilih bisa bikin sistem lambat atau data corrupt.

---

### **FAULT TOLERANCE (Toleransi Kesalahan)**

**Definisi:**
Kemampuan sistem untuk **tetap berjalan** meskipun ada **partial failures** (kegagalan sebagian komponen).

**Pertanyaan Kunci:**
- Bagaimana kita deteksi kegagalan?
- Bagaimana kita recover dari kegagalan?
- Bagaimana kita cegah kegagalan jadi catastrophic?

**Types of Failures:**

**a. Crash Failure:**
- Node berhenti bekerja tiba-tiba
- Contoh: Server crash, power outage
- **Solusi**: Redundancy, failover

**b. Omission Failure:**
- Node tidak kirim message atau tidak process request
- Contoh: Network timeout, message lost
- **Solusi**: Retries, acknowledgments

**c. Timing Failure:**
- Response datang terlalu lambat atau terlalu cepat
- Contoh: Real-time system yang miss deadline
- **Solusi**: Timeout mechanisms, QoS guarantees

**d. Response Failure:**
- Node kasih response yang salah
- Contoh: Bug di software, corrupted data
- **Solusi**: Validation, checksums

**e. Byzantine Failure:**
- Node berperilaku malicious atau unpredictable
- Contoh: Hacker, faulty hardware
- **Solusi**: Byzantine fault tolerance (BFT) algorithms

**Fault Tolerance Techniques:**

**a. Redundancy:**
- Punya backup komponen
- Contoh: RAID untuk storage, replica untuk database

**b. Checkpointing:**
- Simpan state secara periodik
- Kalau crash, recover dari checkpoint terakhir
- Contoh: Database transaction logs

**c. Recovery:**
- **Backward recovery**: Rollback ke state sebelumnya
- **Forward recovery**: Lanjut dari state sekarang, fix error
- Contoh: Transaction rollback, retry mechanisms

**d. Graceful Degradation:**
- Sistem tetap berfungsi (meski dengan fitur terbatas) meski ada failure
- Contoh: Website tetap bisa browse meski checkout error

**Mengapa Penting:**
Di sistem terdistribusi, **failure adalah normal**, bukan exception. Sistem harus dirancang untuk handle failures tanpa downtime.

---

### **SECURITY (Keamanan)**

**Definisi:**
Memastikan **akses yang terotorisasi** ke resource dan **melindungi** sistem dari ancaman.

**Pertanyaan Kunci:**
- Siapa yang boleh akses resource?
- Bagaimana kita verifikasi identitas?
- Bagaimana kita proteksi data dari eavesdropping?

**Security Threats:**

**a. Eavesdropping:**
- Attacker baca data yang ditransfer
- Contoh: Sniffing network traffic
- **Solusi**: Encryption (TLS/SSL)

**b. Masquerading/Spoofing:**
- Attacker pura-pura jadi entity lain
- Contoh: Phishing, IP spoofing
- **Solusi**: Authentication (passwords, certificates)

**c. Tampering:**
- Attacker ubah data di tengah jalan
- Contoh: Man-in-the-middle attack
- **Solusi**: Digital signatures, HMAC

**d. Replay:**
- Attacker capture message dan kirim ulang
- Contoh: Replay authentication token
- **Solusi**: Timestamps, nonces

**e. Denial of Service (DoS):**
- Attacker banjiri sistem dengan request
- Contoh: DDoS attack
- **Solusi**: Rate limiting, firewalls, load balancing

**Security Mechanisms:**

**a. Authentication:**
- Verifikasi identitas user/system
- Contoh: Password, 2FA, biometrics, certificates

**b. Authorization:**
- Tentukan apa yang boleh dilakukan authenticated user
- Contoh: ACL (Access Control List), RBAC (Role-Based Access Control)

**c. Encryption:**
- **Symmetric**: Key yang sama untuk encrypt & decrypt (AES)
- **Asymmetric**: Public key untuk encrypt, private key untuk decrypt (RSA)

**d. Digital Signatures:**
- Verifikasi authenticity dan integrity message
- Contoh: Tanda tangan digital di dokumen

**e. Firewalls & IDS:**
- **Firewall**: Filter network traffic
- **IDS (Intrusion Detection System)**: Deteksi suspicious activity

**Mengapa Penting:**
Sistem terdistribusi **exposed** ke banyak ancaman karena banyak titik akses. Security bukan afterthought, tapi harus didesain dari awal.

---

### **4. DESIGN GOALS (TUJUAN DESAIN)**

#### **a. Resource Sharing (Berbagi Sumber Daya)**

**Contoh Nyata :**
- Cloud-based shared storage: (Contoh: Google Drive, Dropbox) Pengguna menyimpan dan mengakses file di server jarak jauh seolah-olah file tersebut ada di hard disk pribadi.
- Peer-to-peer (P2P) assisted streaming: (Contoh: BitTorrent) Pengguna saling berbagi bandwidth dan penyimpanan untuk mendistribusikan konten multimedia, sehingga mengurangi beban pada server pusat.
- Shared mail services: (Contoh: Gmail, Outlook) Layanan email yang di-outsource ke penyedia cloud. Pengguna tidak perlu mengelola server email fisik sendiri, cukup akses via jaringan.
- Shared Web hosting (CDN): (Contoh: Cloudflare, Akamai) Konten web diduplikasi (di-cache) di berbagai server di seluruh dunia, sehingga pengguna mengakses data dari server yang secara geografis paling dekat (lebih cepat dan efisien).

**Filosofi**: *"The network is the computer"* (John Gage, Sun Microsystems)

#### **b. Distribution Transparency**

**Definisi**: Fenomena di mana sistem terdistribusi mencoba menyembunyikan fakta bahwa proses dan sumber dayanya tersebar secara fisik di banyak komputer.

**Types of Transparency:**

| **Transparency** | **Description** |
|------------------|-----------------|
| **Access** | Menyembunyikan perbedaan representasi data dan cara akses objek |
| **Location** | Menyembunyikan di mana objek berada |
| **Relocation** | Menyembunyikan bahwa objek bisa dipindah saat digunakan |
| **Migration** | Menyembunyikan bahwa objek bisa berpindah lokasi |
| **Replication** | Menyembunyikan bahwa objek direplikasi |
| **Concurrency** | Menyembunyikan bahwa objek dipakai banyak user |
| **Failure** | Menyembunyikan kegagalan dan recovery objek |

**Degree of Transparency - Mengapa Full Transparency Tidak Selalu Baik?**

**Alasan Teknis:**
1. **Communication latencies tidak bisa disembunyikan** - ada batasan fisika
2. **Completely hiding failures is impossible** (teoretis & praktis):
   - Tidak bisa membedakan komputer lambat vs gagal
   - Tidak bisa yakin server sudah perform operasi sebelum crash
3. **Full transparency mengurangi performa**:
   - Menjaga replica tetap sinkron butuh waktu
   - Flushing write operations ke disk untuk fault tolerance itu mahal

**Kapan Exposing Distribution Itu Baik?**
- Location-based services (mencari teman terdekat)
- User di different time zones
- Membuat user paham apa yang terjadi (misal: server tidak respond lama, laporkan sebagai failing)

**Kesimpulan**: Distribution transparency adalah tujuan yang bagus, tapi mencapainya berbeda cerita, dan seringkali **tidak perlu** diarahkan ke full transparency.

#### **c. Openness (Keterbukaan)**

**Definisi**: Sistem yang menawarkan komponen yang mudah digunakan atau diintegrasikan ke sistem lain.

**Karakteristik Open Distributed System:**
- Conform to well-defined interfaces
- Mudah berinteroperasi
- Support portability aplikasi
- Mudah di-extend

**Policies vs Mechanisms:**

| **Policies** (Apa yang diatur) | **Mechanisms** (Cara mengatur) |
|--------------------------------|----------------------------------|
| Level consistency untuk client-cached data | Allow dynamic setting of caching policies |
| Operasi yang diizinkan untuk downloaded code | Support different levels of trust untuk mobile code |
| QoS requirements yang disesuaikan | Provide adjustable QoS parameters per data stream |
| Level secrecy untuk komunikasi | Offer different encryption algorithms |

**On Strict Separation:**
- Semakin strict pemisahan policy & mechanism → semakin banyak konfigurasi parameter → semakin kompleks management
- **Finding a balance**: Hard-coding policies menyederhanakan management, tapi mengurangi fleksibilitas. **Tidak ada solusi obvious**.

---

### **4. DEPENDABILITY (Keandalan)**

**Basic Concept**: 
Komponen C depends on C* jika correctness behavior C bergantung pada correctness behavior C*. (Komponen bisa berupa processes atau channels).

**Requirements:**

| **Requirement** | **Description** |
|-----------------|-----------------|
| **Availability** | Kesiapan untuk digunakan (readiness for usage) |
| **Reliability** | Kontinuitas delivery service |
| **Safety** | Probabilitas sangat rendah untuk catastrophe |
| **Maintainability** | Seberapa mudah sistem yang gagal bisa diperbaiki |

**Reliability vs Availability:**

**Reliability R(t)**: Probabilitas kondisional bahwa komponen C telah berfungsi dengan benar selama [0, t) diberikan C berfungsi dengan benar pada T=0.

**Traditional Metrics:**
- **MTTF (Mean Time To Failure)**: Rata-rata waktu sampai komponen gagal
- **MTTR (Mean Time To Repair)**: Rata-rata waktu yang dibutuhkan untuk memperbaiki
- **MTBF (Mean Time Between Failures)**: MTTF + MTTR

**Terminologi - Failure, Error, Fault:**

| **Term** | **Description** | **Example** |
|----------|-----------------|-------------|
| **Failure** | Komponen tidak memenuhi spesifikasi | Program crash |
| **Error** | Bagian dari komponen yang bisa lead to failure | Programming bug |
| **Fault** | Penyebab dari error | Sloppy programmer |

**Handling Faults:**

| **Strategy** | **Description** | **Example** |
|--------------|-----------------|-------------|
| **Fault prevention** | Mencegah occurrence of fault | Don't hire sloppy programmers |
| **Fault tolerance** | Build komponen untuk mask fault | Build oleh 2 programmer independen |
| **Fault removal** | Reduce presence/number/seriousness of fault | Get rid of sloppy programmers |
| **Fault forecasting** | Estimate presence/incidence/consequences | Estimate kinerja recruiter |

---

### **5. SECURITY**

**Observation Penting**: *A distributed system that is not secure, is not dependable*

**What We Need:**

1. **Confidentiality**: Informasi hanya diungkapkan ke authorized parties
2. **Integrity**: Memastikan alterations to assets hanya bisa dilakukan secara authorized

**Key Concepts:**
- **Authentication**: Verifying correctness of claimed identity
- **Authorization**: Apakah identified entity punya access rights yang proper?
- **Trust**: Satu entity bisa assured bahwa entity lain akan perform actions sesuai expectation

**Security Mechanisms:**

**a. Symmetric Cryptosystem:**
- Encryption key EK(data) dan decryption key DK(data)
- Jika data = DK(EK(data)), maka DK = EK
- **Encryption dan decryption key SAMA** dan harus dirahasiakan

**b. Asymmetric Cryptosystem:**
- Public key PK(data) 
- Private (secret) key SK(data)

**c. Secure Hashing:**
- H(data) returns fixed-length string
- **Properties**:
  - Perubahan kecil dari data → data* menghasilkan H(data*) yang completely different
  - Given hash value, computationally impossible untuk find data dengan h = H(data)

**Practical Digital Signatures:**
Sign message untuk Bob oleh Alice menggunakan kombinasi private key dan hash.

---

### **6. SCALABILITY**

**Observation**: Banyak developer mudah menggunakan kata "scalable" tanpa menjelaskan **mengapa** sistem mereka benar-benar scale.

**Three Components of Scale:**

1. **Size Scalability**: Jumlah users atau processes
2. **Geographical Scalability**: Maximum distance antara nodes
3. **Administrative Scalability**: Jumlah administrative domains

**Fakta**: 
- Most systems hanya account untuk size scalability (sampai batas tertentu)
- Solusi umum: multiple powerful servers operating independently in parallel
- **Challenge masih ada** di geographical dan administrative scalability

**Size Scalability - Root Causes for Problems:**

1. Computational capacity (limited by CPUs)
2. Storage capacity (termasuk transfer rate antara CPUs dan disks)
3. Network antara user dan centralized service

**Formal Analysis - Queuing System:**

**Asumsi:**
- Queue infinite capacity → arrival rate tidak dipengaruhi queue length
- λ = arrival rate requests
- µ = processing capacity service (requests per second)

**Key Metrics:**
- **Utilization U** = fraction of time service busy
- **Average number of requests** dalam sistem
- **Average throughput**
- **Response time**: Total time untuk process request

**Observation Penting:**
- Jika U kecil → response-to-service time ≈ 1 (request langsung diproses)
- Jika U → 1 → sistem **grinding halt** (macet total)
- **Solusi**: Decrease S (service time)

**Problems dengan Geographical Scalability:**

1. **Cannot simply go from LAN to WAN**:
   - Banyak sistem asumsikan synchronous client-server interactions
   - Client kirim request dan wait for answer
   - **Latency** bisa prohibit skema ini

2. **WAN links inherently unreliable**:
   - Streaming video dari LAN ke WAN pasti fail

3. **Lack of multipoint communication**:
   - Simple search broadcast tidak bisa di-deploy
   - **Solusi**: Develop separate naming dan directory services (yang punya scalability problems sendiri)

**Problems dengan Administrative Scalability:**

**Essence**: Conflicting policies tentang:
- Usage (dan payment)
- Management
- Security

**Examples:**
- Computational grids: share expensive resources beda domains
- Shared equipment: kontrol, manage, use shared radio telescope

**Exception - Beberapa P2P Networks:**
- File-sharing (BitTorrent)
- P2P telephony (Skype versi awal)
- Peer-assisted audio streaming (Spotify)

**Note**: End users collaborate, **bukan** administrative entities.

**Techniques for Scaling:**

**a. Hide Communication Latencies:**
- Gunakan asynchronous communication
- Separate handler untuk incoming response
- **Problem**: Tidak semua aplikasi fit model ini

**b. Move Computations to Client:**
- Java applets dan scripts

**c. Partition Data and Computations:**
- Decentralized naming services (DNS)
- Decentralized information systems (WWW)

**d. Replication and Caching:**
- Replicated file servers dan databases
- Mirrored websites
- Web caches (di browsers dan proxies)
- File caching (di server dan client)

**The Problem with Replication:**

**Easy part**: Applying replication itu mudah

**Hard part**:
1. **Multiple copies → inconsistencies**: Modifikasi satu copy → berbeda dari yang lain
2. **Keeping copies consistent** butuh **global synchronization** pada setiap modification
3. **Global synchronization → precludes large-scale solutions**

**Observation Penting**: 
- Jika kita bisa **tolerate inconsistencies** → reduce need for global synchronization
- Tapi tolerating inconsistencies itu **application dependent**

---

### **7. CLASSIFICATION OF DISTRIBUTED SYSTEMS**

#### **A. High-Performance Distributed Computing**

**a. Parallel Computing:**
- **Multiprocessor/Multicore vs Multicomputer**
- Multiprocessor: shared memory, easier to program
- Multicomputer: message passing, harder tapi lebih scalable

**b. Distributed Shared Memory (DSM) Systems:**
- **Idea**: Implement shared-memory model di atas multicomputer
- **Example**: Map semua main-memory pages dari different processors ke satu virtual address space
- Jika processor A akses page P di processor B → OS di A traps dan fetch P dari B (seperti ambil dari disk)
- **Problem**: Performa tidak bisa compete dengan multiprocessors
- **Status**: Widely abandoned

**c. Cluster Computing:**
- Group of high-end systems connected via LAN
- **Characteristics**:
  - Homogeneous (same OS, near-identical hardware)
  - Single atau tightly coupled managing node(s)

**d. Grid Computing:**
- Plenty of nodes dari everywhere
- **Characteristics**:
  - Heterogeneous
  - Dispersed across several organizations
  - Bisa span wide-area network (WAN)
  
**Virtual Organizations**: 
- Grouping of users (atau their IDs)
- Allows authorization pada resource allocation

**Layers in Grid Computing:**

| **Layer** | **Function** |
|-----------|--------------|
| **Fabric** | Interfaces ke local resources (query state, capabilities, locking) |
| **Connectivity** | Communication/transaction protocols, authentication |
| **Resource** | Manage single resource (create processes, read data) |
| **Collective** | Access ke multiple resources (discovery, scheduling, replication) |
| **Application** | Actual grid applications dalam single organization |

---

#### **B. Distributed Information Systems**

**Problem**: Organizations punya banyak networked applications, tapi **interoperability painful**.

**Basic Approach:**
- Networked application = runs on server, services tersedia untuk remote clients
- Simple integration: clients combine requests → send off → collect responses → present coherent result

**Next Step**: 
- Direct application-to-application communication
- **Enterprise Application Integration (EAI)**

**Transactions - ACID Properties:**

| **Primitive** | **Description** |
|---------------|-----------------|
| BEGIN TRANSACTION | Mark start of transaction |
| END TRANSACTION | Terminate dan try to commit |
| ABORT TRANSACTION | Kill dan restore old values |
| READ | Read data dari file/table |
| WRITE | Write data ke file/table |

**ACID (All-or-Nothing):**
- **Atomic**: Happens indivisibly (seemingly)
- **Consistent**: Does not violate system invariants
- **Isolated**: Not mutual interference
- **Durable**: Commit berarti changes permanent

**TPM (Transaction Processing Monitor):**
- **Problem**: Data involved in transaction distributed across several servers
- **Solution**: TP Monitor coordinate execution of transaction

**Middleware dan EAI:**

**a. Remote Procedure Call (RPC):**
- Requests dikirim via local procedure call
- Packaged as message → processed → responded via message
- Result returned sebagai return from call

**b. Message Oriented Middleware (MOM):**
- Messages dikirim ke logical contact point (published)
- Forwarded ke subscribed applications

**How to Integrate Applications:**

| **Method** | **Pros & Cons** |
|------------|-----------------|
| **File transfer** | ✅ Technically simple<br> Not flexible (figure out file format, management, update propagation) |
| **Shared database** | ✅ Much more flexible<br>❌ Butuh common data scheme + risk bottleneck |
| **Remote Procedure Call** | ✅ Efektif untuk execution series of actions<br>❌ Caller dan callee harus up & running bersamaan |
| **Messaging** | ✅ Decoupling in time dan space<br>❌ Lebih kompleks |

---

#### **C. Distributed Pervasive Systems**

**Observation**: Next-generation distributed systems di mana nodes:
- Small, mobile
- Often embedded in larger system
- System **naturally blends** into user's environment

**Three (Overlapping) Subtypes:**

**1. Ubiquitous Computing Systems:**
- Pervasive dan continuously present
- Continuous interaction antara system dan user

**Core Elements:**
1. **Distribution**: Devices networked, distributed, accessible transparently
2. **Interaction**: Highly unobtrusive
3. **Context awareness**: System aware of user's context untuk optimize interaction
4. **Autonomy**: Devices operate autonomously tanpa human intervention (highly self-managed)
5. **Intelligence**: System bisa handle wide range of dynamic actions dan interactions

**2. Mobile Computing Systems:**
- Pervasive, tapi emphasis pada **devices inherently mobile**

**Distinctive Features:**
- Myriad of different mobile devices (smartphones, tablets, GPS, remote controls, active badges)
- **Mobile** = location expected to change over time → change of local services, reachability
- **Keyword**: Discovery
- **Problem**: Maintaining stable communication bisa serious problems
- **Historical note**: Research fokus pada direct resource sharing antar mobile devices → **never became popular** → dianggap fruitless path

**Bottom Line**: 
Mobile devices setup connections ke stationary servers → essentially jadi **clients of cloud-based services**

**Mobile Cloud Computing vs Mobile Edge Computing:**
- **Cloud Computing**: Processing di data center yang jauh
- **Edge Computing**: Processing di edge network (lebih dekat ke user)

**3. Sensor (and Actuator) Networks:**
- Pervasive, emphasis pada **collaborative sensing dan actuation**

**Characteristics:**
- **Many**: 10s - 1000s nodes
- **Simple**: Small memory/compute/communication capacity
- **Often battery-powered** (atau bahkan battery-less)

**Sensor Networks as Distributed Databases:**
- Dua extremes dalam pendekatan query dan data management

**The Cloud-Edge Continuum:**
- Spectrum dari cloud (jauh, powerful) ke edge (dekat, limited resources)

---

## **8. PITFALLS (JEBAKAN) DALAM DEVELOPING DISTRIBUTED SYSTEMS**

### **Observasi Penting**

> *"Many distributed systems are needlessly complex, caused by mistakes that required patching later on. Many false assumptions are often made."*

Banyak sistem terdistribusi yang **sebenarnya tidak perlu kompleks** — kompleksitas itu muncul karena developer membuat **asumsi keliru** di awal, lalu harus "menambal" (patching) masalahnya di kemudian hari. Asumsi-asumsi ini sering kali **tersembunyi** (implicit) dalam kode atau arsitektur, sehingga sulit dideteksi sampai sistem gagal di production.

Kedelapan asumsi keliru ini dikenal sebagai **"Fallacies of Distributed Computing"** — dirumuskan oleh **Peter Deutsch** dan rekan-rekannya di Sun Microsystems pada tahun 1990-an. Ini adalah pelajaran mahal yang dipelajari industri selama puluhan tahun.

---

## **1. "The network is reliable" ❌**
*(Jaringan itu andal)*

**Apa artinya asumsi ini:**
Developer menulis kode seolah-olah setiap request yang dikirim pasti sampai ke tujuan, dan setiap response pasti kembali. Tidak ada mekanisme untuk handle kegagalan jaringan.

**Kenapa keliru:**
Jaringan **tidak pernah** 100% reliable. Ada banyak penyebab kegagalan di luar kendala aplikasi:
- **Packet loss** karena kongesti router/switch
- **Transient failure**: server target sedang GC pause, restart, atau overload sesaat
- **TCP connection reset** oleh load balancer atau firewall karena idle terlalu lama
- **DNS resolution failure** sesaat saat service discovery refresh
- **Partial failure**: hanya satu replica dari service yang bermasalah, bukan semuanya
- **Cable cut, power outage, hardware failure** di datacenter

**Contoh kegagalan nyata:**
- **FoodGo**: Modul pesanan memanggil modul pembayaran tanpa timeout → saat pembayaran lambat, thread pesanan menggantung tanpa batas → thread pool habis → seluruh sistem crash.
- **Knight Capital Group (2012)**: Bug di deployment + asumsi jaringan reliable → kehilangan $440 juta dalam 45 menit.
- **AWS Outage (2017)**: Satu typo di S3 menyebabkan outage besar karena asumsi jaringan internal selalu reliable.

**Solusi mitigasi:**
- **Timeout** di setiap pemanggilan antar-service
- **Retry dengan exponential backoff + jitter** untuk transient errors
- **Circuit Breaker** untuk mencegah cascading failure
- **Idempotency key** agar retry tidak menyebabkan duplikasi operasi
- **Health check** dan **service discovery** yang robust

---

## **2. "The network is secure" ❌**
*(Jaringan itu aman)*

**Apa artinya asumsi ini:**
Data yang ditransfer lewat jaringan aman dari intersepsi, modifikasi, atau pemalsuan. Developer tidak meng-encrypt data atau tidak memverifikasi identitas.

**Kenapa keliru:**
Jaringan **selalu** bisa disadap, terutama:
- **Public WiFi** di kafe, bandara, hotel
- **ISP** yang bisa log traffic
- **Man-in-the-Middle (MitM) attack** di jaringan korporat
- **Insider threat** dari karyawan sendiri
- **State-level surveillance**

**Contoh kegagalan nyata:**
- **FireSheep (2010)**: Tool yang menunjukkan betapa mudahnya session cookie dicuri di WiFi publik.
- **Equifax Breach (2017)**: Data 147 juta orang bocor karena komunikasi tidak di-encrypt dengan benar.
- **Credential stuffing**: Attacker pakai credential yang bocor dari satu layanan untuk login ke layanan lain.

**Solusi mitigasi:**
- **TLS/SSL** untuk semua komunikasi (HTTPS, bukan HTTP)
- **Certificate pinning** di mobile apps
- **Mutual TLS (mTLS)** untuk komunikasi antar-service
- **Zero Trust Architecture**: "never trust, always verify"
- **Secret management** yang proper (Vault, AWS Secrets Manager)
- **Audit logging** untuk deteksi anomali

---

## **3. "The network is homogeneous" ❌**
*(Jaringan itu seragam)*

**Apa artinya asumsi ini:**
Semua node di jaringan punya hardware, OS, protokol, dan representasi data yang sama. Developer bisa asumsikan environment yang konsisten.

**Kenapa keliru:**
Dalam sistem terdistribusi nyata:
- **Hardware berbeda**: ARM (mobile), x86 (server), GPU (ML)
- **OS berbeda**: Linux, Windows, macOS, iOS, Android
- **Protokol berbeda**: HTTP/1.1, HTTP/2, HTTP/3, gRPC, WebSocket
- **Data representation berbeda**: Little-endian vs big-endian, UTF-8 vs UTF-16, JSON vs Protobuf vs XML
- **Timezone berbeda**: Server di US, client di Indonesia
- **Language/locale berbeda**: Format tanggal, angka, mata uang

**Contoh kegagalan nyata:**
- **Y2K Bug**: Asumsi tahun 2 digit → sistem gagal di tahun 2000.
- **Mars Climate Orbiter (1999)**: NASA kehilangan $125 juta karena satu tim pakai **metric** (Newton), tim lain pakai **imperial** (pound-force).
- **Gangnam Style YouTube bug**: Counter view overflow karena asumsi 32-bit integer cukup (2 miliar view).

**Solusi mitigasi:**
- **Standardized protocols**: HTTP/REST, gRPC, GraphQL
- **Serialization format** yang portable: JSON, Protobuf, Avro
- **Unicode (UTF-8)** untuk semua teks
- **ISO 8601** untuk timestamp (UTC)
- **API versioning** untuk backward compatibility
- **Feature flags** untuk handle perbedaan capability

---

## **4. "The topology does not change" ❌**
*(Topologi jaringan tidak berubah)*

**Apa artinya asumsi ini:**
Struktur jaringan stabil — node yang ada sekarang akan tetap ada di masa depan, dengan alamat yang sama.

**Kenapa keliru:**
Dalam sistem terdistribusi modern:
- **Nodes join/leave** terus-menerus (auto-scaling, spot instances)
- **IP address berubah** (DHCP, NAT, mobile networks)
- **Container/pod restart** dengan IP baru (Kubernetes)
- **Mobile devices** berpindah dari WiFi ke 4G ke WiFi lagi
- **Server migration** antar datacenter
- **DNS TTL** menyebabkan alamat lama masih di-cache

**Contoh kegagalan nyata:**
- **Hardcoded IP addresses** di config file → sistem gagal saat server migrasi.
- **Stale DNS cache** → client masih coba connect ke IP lama yang sudah tidak aktif.
- **Kubernetes pod restart** → service discovery gagal karena client masih cache IP lama.

**Solusi mitigasi:**
- **Service discovery** (Consul, etcd, Eureka, Kubernetes DNS)
- **Load balancer** sebagai single entry point
- **Dynamic configuration** (bukan hardcoded)
- **TTL yang tepat** untuk caching
- **Graceful shutdown** dan **connection draining**
- **Health check** untuk deteksi node yang gone

---

## **5. "Latency is zero" ❌**
*(Latensi itu nol)*

**Apa artinya asumsi ini:**
Komunikasi antar-node terjadi instan. Developer tulis kode synchronous yang blocking, seolah-olah response datang seketika.

**Kenapa keliru:**
Latensi **tidak pernah** nol karena batasan fisika:
- **Speed of light**: ~300.000 km/detik → Jakarta ke Singapura (~1000 km) minimal ~3.3 ms round-trip, realitanya 20-50 ms
- **Jakarta ke US**: ~150-250 ms round-trip
- **Propagation delay** di fiber optic
- **Processing delay** di router/switch
- **Queueing delay** saat kongesti
- **Serialization/deserialization** time

**Contoh kegagalan nyata:**
- **FoodGo**: Modul pesanan memanggil pembayaran secara synchronous → saat pembayaran lambat, seluruh thread blok → sistem hang.
- **Chatty applications**: Aplikasi yang buat ratusan RPC call untuk satu user action → latency terakumulasi jadi detik-detik.
- **Global applications**: User di Australia akses server di US → setiap page load butuh 200ms+ tambahan.

**Solusi mitigasi:**
- **Asynchronous communication** (message queue, event-driven)
- **Caching** di sisi client dan CDN
- **Batching** untuk kurangi round-trip
- **Edge computing** untuk proses dekat user
- **Connection pooling** untuk kurangi handshake overhead
- **Timeout yang tepat** agar tidak blocking selamanya

---

## **6. "Bandwidth is infinite" ❌**
*(Bandwidth itu tak terbatas)*

**Apa artinya asumsi ini:**
Jaringan bisa transfer data sebesar apapun secepat apapun. Developer kirim data besar tanpa optimasi.

**Kenapa keliru:**
Bandwidth **selalu terbatas**:
- **Physical limits**: Kabel fiber, spektrum wireless
- **Shared medium**: Banyak user pakai bandwidth yang sama
- **Cost**: Bandwidth mahal, terutama cross-region
- **Congestion**: Traffic spike bisa saturate link
- **Mobile networks**: 3G/4G bandwidth sangat terbatas dibanding fiber

**Contoh kegagalan nyata:**
- **Sending entire database** ke client untuk filter di frontend → timeout di mobile network.
- **Uncompressed images/videos** di app → user di jaringan lambat tidak bisa load.
- **N+1 query problem**: 1000 database call untuk 1 halaman → bandwidth DB habis.
- **Log shipping** tanpa compression → network saturated.

**Solusi mitigasi:**
- **Compression** (gzip, brotli, zstd)
- **Pagination** untuk data besar
- **Lazy loading** dan **infinite scroll**
- **CDN** untuk static assets
- **Protocol buffers** atau **MessagePack** untuk payload kecil
- **Rate limiting** untuk prevent abuse
- **Delta sync** (hanya kirim perubahan, bukan full data)

---

## **7. "Transport cost is zero" ❌**
*(Biaya transfer itu nol)*

**Apa artinya asumsi ini:**
Mengirim data lewat jaringan gratis. Developer tidak peduli berapa banyak data yang ditransfer atau berapa sering.

**Kenapa keliru:**
Transfer data **selalu ada biaya**:
- **Monetary cost**: AWS egress fees ($0.09/GB cross-region), CDN costs
- **Energy cost**: Datacenter pakai listrik besar untuk network gear
- **Time cost**: Latency = waktu user menunggu
- **Opportunity cost**: Bandwidth yang terpakai tidak bisa dipakai untuk request lain
- **Environmental cost**: Carbon footprint dari data transfer

**Contoh kegagalan nyata:**
- **Unoptimized mobile app**: 100MB per session → user kena kuota mahal → uninstall app.
- **Cross-region replication** tanpa pertimbangan cost → tagihan AWS membengkak.
- **Polling instead of push**: Client poll server tiap detik → biaya network bengkak.
- **Sending full objects** instead of deltas → bandwidth cost 10x lebih mahal.

**Solusi mitigasi:**
- **Cost-aware architecture**: Pilih region yang tepat, gunakan caching
- **Compression** untuk kurangi data transfer
- **Push notifications** atau **WebSocket** instead of polling
- **Delta updates** instead of full sync
- **Data locality**: Proses data dekat dengan sumbernya
- **Monitoring & alerting** untuk egress costs

---

## **8. "There is one administrator" ❌**
*(Hanya ada satu administrator)*

**Apa artinya asumsi ini:**
Satu orang/tim mengontrol seluruh sistem. Semua node punya policy yang sama, konfigurasi yang sama, timezone yang sama.

**Kenapa keliru:**
Sistem terdistribusi modern melibatkan **banyak stakeholder**:
- **Multiple teams**: Backend, frontend, mobile, DevOps, security
- **Multiple organizations**: Vendor, partner, third-party APIs
- **Multiple administrative domains**: Cloud provider, on-premise, edge
- **Conflicting policies**: Security vs performance, cost vs availability
- **Regulatory requirements**: GDPR di EU, PDPL di Indonesia, HIPAA di US
- **Different update schedules**: Tiap tim deploy kapan saja

**Contoh kegagalan nyata:**
- **Microservices tanpa governance**: Tiap tim pilih tech stack sendiri → nightmare untuk maintain.
- **Inconsistent security policies**: Satu service pakai TLS, yang lain tidak → vulnerability.
- **Breaking API changes**: Satu tim update API tanpa notify tim lain → client apps crash.
- **GDPR violation**: Data user EU di-store di US tanpa proper safeguards → fine miliaran.

**Solusi mitigasi:**
- **Platform team** untuk provide shared infrastructure
- **API contracts** dan **schema registry**
- **Policy as code** (Open Policy Agent, Terraform)
- **Service mesh** (Istio, Linkerd) untuk enforce policies
- **Centralized logging & monitoring**
- **Change management process** untuk breaking changes
- **Compliance automation** untuk regulatory requirements

---

##  **KESIMPULAN CHAPTER 1**

Chapter ini memberikan **fondasi konseptual** untuk memahami distributed systems:

1. **Definisi & Klasifikasi**: Memahami perbedaan distributed vs decentralized, dan berbagai jenis distributed systems
2. **Design Goals**: Sharing, transparency, openness, scalability - tapi dengan **trade-offs** yang jelas
3. **Quality Attributes**: Dependability (availability, reliability, safety) dan Security
4. **Scalability Challenges**: Size, geographical, administrative - masing-masing dengan masalah dan solusi sendiri
5. **Pitfalls**: 8 false assumptions yang harus dihindari

**Key Takeaway**: 
Distributed systems itu **inherently complex**. Tidak ada silver bullet. Setiap design decision punya **trade-offs**. Yang penting adalah **memahami konsekuensi** dari setiap pilihan dan **tidak membuat false assumptions**.
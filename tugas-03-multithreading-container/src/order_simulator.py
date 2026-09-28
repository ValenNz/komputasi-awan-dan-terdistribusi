"""
Tugas 3 - Simulasi Pesanan Masuk dengan Multithreading (FoodGo)
Kelompok: [Isi Nama Kelompok]
Author (logika multithreading): Nuevalen Refitra Alswanfo - 103072430008

Program ini menjalankan dua skenario secara berurutan:
  MODE 1 -> tanpa lock   : sengaja membiarkan race condition terjadi
  MODE 2 -> dengan lock  : menggunakan threading.Lock() agar counter akurat

Referensi teori: Distributed Systems (Tanenbaum & van Steen, 4th Ed.) Bab 03 - Processes
"""

import threading
import random
import time
import sys

NUM_ORDERS = 100        # jumlah pesanan simulasi yang masuk
NUM_WORKERS = 10        # jumlah thread pekerja

# Counter bersama untuk menghitung total pesanan yang berhasil diproses.
# Sengaja rawan race condition jika diakses tanpa proteksi.
processed_count = 0

# =============================================================================
# TODO 1: Buat objek Lock di sini untuk melindungi `processed_count`.
# =============================================================================
lock = threading.Lock()


# =============================================================================
# TODO 2: Increment `processed_count`
# =============================================================================
# Catatan desain:
# Di CPython, statement `processed_count += 1` secara teknis "hampir atomik"
# karena adanya GIL (Global Interpreter Lock). Agar race condition benar-benar
# TERLIHAT di output (sesuai tuntutan tugas: "buktikan dengan log/screenshot"),
# kita pecah operasi += menjadi tiga langkah eksplisit: READ -> YIELD -> WRITE.
# Pola read-modify-write yang dipisah ini adalah representasi paling jujur dari
# apa yang sebenarnya terjadi di level mesin (load -> add -> store), dan
# memperbesar "window of vulnerability" sehingga race condition hampir pasti
# muncul saat banyak thread berjalan konkuren.
# =============================================================================

def process_order(order_id: int, use_lock: bool = True) -> None:
    """
    Proses satu pesanan. Dipanggil oleh tiap thread pekerja.
    Parameter `use_lock` menentukan apakah increment dilindungi lock atau tidak.
    """
    global processed_count

    # Simulasikan kerja nyata (mis. validasi stok, hitung total harga, query DB)
    time.sleep(random.uniform(0.0005, 0.003))

    if use_lock:
        # ---------- MODE AMAN: bungkus increment dengan lock ----------
        with lock:
            current = processed_count          # READ
            time.sleep(0)                      # yield ke scheduler (perbesar window)
            processed_count = current + 1      # WRITE
    else:
        # ---------- MODE TIDAK AMAN: tanpa lock, race condition terjadi ----------
        current = processed_count              # READ
        time.sleep(0)                          # yield -> thread lain bisa masuk
        processed_count = current + 1          # WRITE (menimpa hasil thread lain)


def worker(order_ids: list, use_lock: bool) -> None:
    """Satu thread pekerja memproses sekumpulan order_id."""
    for order_id in order_ids:
        process_order(order_id, use_lock=use_lock)


# =============================================================================
# TODO 3: Bagi `order_ids` menjadi NUM_WORKERS bagian, buat satu
#         threading.Thread per bagian, start semua, lalu join semua.
# =============================================================================

def split_into_chunks(data: list, n_chunks: int) -> list:
    """Membagi list menjadi n_chunks bagian yang ukurannya hampir sama."""
    chunks = []
    base_size, remainder = divmod(len(data), n_chunks)
    start = 0
    for i in range(n_chunks):
        # Chunk pertama sebanyak `remainder` mendapat +1 elemen agar tidak ada yang tercecer
        size = base_size + (1 if i < remainder else 0)
        chunks.append(data[start:start + size])
        start += size
    return chunks


def run_simulation(use_lock: bool) -> int:
    """Jalankan satu siklus simulasi dan kembalikan nilai akhir processed_count."""
    global processed_count
    processed_count = 0  # reset counter untuk simulasi baru

    order_ids = list(range(1, NUM_ORDERS + 1))
    chunks = split_into_chunks(order_ids, NUM_WORKERS)

    threads = []
    for chunk in chunks:
        t = threading.Thread(target=worker, args=(chunk, use_lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return processed_count


def main() -> None:
    print("=" * 65)
    print("  FOODGO ORDER SIMULATOR - Multithreading Demo")
    print(f"  Pesanan: {NUM_ORDERS} | Thread worker: {NUM_WORKERS}")
    print("=" * 65)

    # ---------- MODE 1: TANPA LOCK (buktikan race condition) ----------
    print("\n[MODE 1] Menjalankan TANPA lock (rawan race condition)...")
    result_unsafe = run_simulation(use_lock=False)
    print(f"  -> Total pesanan tercatat: {result_unsafe} / {NUM_ORDERS}")
    if result_unsafe != NUM_ORDERS:
        lost = NUM_ORDERS - result_unsafe
        print(f"  RACE CONDITION TERDETEKSI! {lost} pesanan 'hilang' karena "
              f"thread saling menimpa hasil baca-tulis.")
    else:
        print("  (Kebetulan tidak ada collision di run ini — coba jalankan ulang.)")

    # ---------- MODE 2: DENGAN LOCK (buktikan perbaikan) ----------
    print("\n[MODE 2] Menjalankan DENGAN threading.Lock()...")
    result_safe = run_simulation(use_lock=True)
    print(f"  -> Total pesanan tercatat: {result_safe} / {NUM_ORDERS}")
    if result_safe == NUM_ORDERS:
        print("  Semua pesanan terhitung akurat berkat mutual exclusion dari Lock.")
    else:
        print("  Lock gagal — ada bug di implementasi.")

    # ---------- Ringkasan ----------
    print("\n" + "-" * 65)
    print("  RINGKASAN")
    print("-" * 65)
    print(f"  Tanpa lock : {result_unsafe:>4}  {'' if result_unsafe == NUM_ORDERS else 'RACE'}")
    print(f"  Dengan lock: {result_safe:>4}  {' AKURAT' if result_safe == NUM_ORDERS else ''}")
    print("=" * 65)

    # Exit code non-zero jika race terdeteksi (berguna untuk CI / validasi otomatis)
    if result_unsafe == NUM_ORDERS or result_safe != NUM_ORDERS:
        sys.exit(1)


if __name__ == "__main__":
    main()
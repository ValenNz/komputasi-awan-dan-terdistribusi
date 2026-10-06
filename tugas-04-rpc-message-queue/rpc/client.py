"""
Tugas 4 - Jalur A: RPC Client (simulasi modul Pesanan)
Jalankan server.py di terminal lain terlebih dahulu.
Dikerjakan oleh: Nuevalen Refitra Alswanfo (103072430008)
"""

import xmlrpc.client
import time


def main():
    # Buat ServerProxy ke http://localhost:8000
    # allow_none=True disinkronkan dengan server untuk keamanan parsing data
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)

    print("="*60)
    print("MEMULAI KOMUNIKASI RPC (SINKRON / BLOCKING)")
    print("="*60)

    # 1. Uji cek_saldo
    print("\n[1] Memanggil cek_saldo('user1') ... menunggu respons sinkron")
    start_time = time.time()
    
    # Client akan BLOCKING di baris ini sampai server membalas
    saldo = proxy.cek_saldo("user1")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"    ➔ Hasil: Saldo user1 adalah Rp {saldo:,.2f}")
    print(f"    ➔ Waktu tempuh (blocking): {elapsed_time:.4f} detik")
    print("    ➔ (Client TIDAK BISA mengerjakan hal lain selama waktu ini)")

    # 2. Uji proses_pembayaran (Skenario Sukses)
    print("\n[2] Memanggil proses_pembayaran('user1', 20000) ...")
    start_time = time.time()
    
    hasil_bayar = proxy.proses_pembayaran("user1", 20000)
    
    end_time = time.time()
    print(f"    ➔ Hasil: {hasil_bayar}")
    print(f"    ➔ Waktu tempuh (blocking): {end_time - start_time:.4f} detik")

    # 3. Uji proses_pembayaran (Skenario Gagal - Saldo Kurang)
    print("\n[3] Memanggil proses_pembayaran('user1', 50000) ... (Simulasi saldo kurang)")
    hasil_gagal = proxy.proses_pembayaran("user1", 50000)
    print(f"    ➔ Hasil: {hasil_gagal}")

    # 4. Uji user tidak ada
    print("\n[4] Memanggil cek_saldo('user99') ... (Simulasi user tidak ada)")
    saldo_tidak_ada = proxy.cek_saldo("user99")
    print(f"    ➔ Hasil: Saldo user99 adalah Rp {saldo_tidak_ada:,.2f}")
    
    print("\n" + "="*60)
    print("Semua pemanggilan RPC selesai.")
    print("="*60)


if __name__ == "__main__":
    main()
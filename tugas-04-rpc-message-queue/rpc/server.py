"""
Tugas 4 - Jalur A: RPC Server (simulasi modul Pembayaran)
Memakai xmlrpc.server dari Python standard library - tidak perlu install apa pun.
Dikerjakan oleh: Nuevalen Refitra Alswanfo (103072430008)
"""

from xmlrpc.server import SimpleXMLRPCServer
import logging

# Setup logging agar terlihat di terminal server jika ada anomali
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Simulasi "database" saldo user
saldo_user = {
    "user1": 50000,
    "user2": 120000,
}


def cek_saldo(user_id: str) -> float:
    """Kembalikan saldo user_id saat ini."""
    if user_id in saldo_user:
        return float(saldo_user[user_id])
    else:
        # Keputusan: Mengembalikan 0.0 dan log warning alih-alih raise error.
        # Alasan: Agar server RPC tidak crash (crash akan memutus koneksi semua client),
        # dan client tetap mendapat respons yang bisa ditangani (misal: "User tidak ditemukan").
        logging.warning(f"User '{user_id}' tidak ditemukan dalam database.")
        return 0.0


def proses_pembayaran(user_id: str, jumlah: float) -> dict:
    """Kurangi saldo user sejumlah `jumlah`. Kembalikan status hasil."""
    if user_id not in saldo_user:
        return {"status": "gagal", "pesan": "User tidak ditemukan", "saldo_akhir": 0.0}
    
    if saldo_user[user_id] >= jumlah:
        saldo_user[user_id] -= jumlah
        return {
            "status": "sukses", 
            "pesan": "Pembayaran berhasil diproses", 
            "saldo_akhir": float(saldo_user[user_id])
        }
    else:
        return {
            "status": "gagal", 
            "pesan": "Saldo tidak mencukupi", 
            "saldo_akhir": float(saldo_user[user_id])
        }


def main():
    # allow_none=True diperlukan agar server bisa mengembalikan tipe data kompleks (dict) atau None tanpa error
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    
    # Daftarkan fungsi agar bisa dipanggil lewat RPC
    server.register_function(cek_saldo, "cek_saldo")
    server.register_function(proses_pembayaran, "proses_pembayaran")
    
    print("RPC Server Modul Pembayaran berjalan di http://localhost:8000...")
    print("   (Tekan Ctrl+C untuk menghentikan server)")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")


if __name__ == "__main__":
    main()
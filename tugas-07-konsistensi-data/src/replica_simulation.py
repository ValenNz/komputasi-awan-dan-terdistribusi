"""
Tugas 7 (opsional) - Simulasi Replikasi Dua Server (Jakarta & Bandung)

Mensimulasikan delay replikasi dan masalah inconsistent read,
lalu memperbaikinya dengan mekanisme Read-Your-Writes sederhana.
"""

import time
import threading

REPLICATION_DELAY = 2.0


class Replica:
    def __init__(self, name: str):
        self.name = name
        self.saldo: dict[str, float] = {}
        self.last_write_version: dict[str, int] = {}

    def write(self, user_id: str, saldo_baru: float, version: int):
        self.saldo[user_id] = saldo_baru
        self.last_write_version[user_id] = version
        print(f"[{self.name}] WRITE saldo {user_id} = {saldo_baru} (versi {version})")

    def read(self, user_id: str) -> float:
        return self.saldo.get(user_id, 0.0)

    def get_version(self, user_id: str) -> int:
        return self.last_write_version.get(user_id, 0)


class ReplicationSystem:
    def __init__(self):
        self.jakarta = Replica("Jakarta")
        self.bandung = Replica("Bandung")
        self.version_counter = 0

    def top_up(self, user_id: str, jumlah: float):
        self.version_counter += 1
        version = self.version_counter
        saldo_baru = self.jakarta.read(user_id) + jumlah
        self.jakarta.write(user_id, saldo_baru, version)

        # TODO 1: replikasi ke Bandung TERTUNDA (simulasikan dengan
        # threading.Timer(REPLICATION_DELAY, ...) yang memanggil
        # self.bandung.write(user_id, saldo_baru, version) setelah delay.
        def _replicate():
            self.bandung.write(user_id, saldo_baru, version)

        timer = threading.Timer(REPLICATION_DELAY, _replicate)
        timer.daemon = True
        timer.start()

    def baca_saldo_naif(self, user_id: str, server: str) -> float:
        replica = self.jakarta if server == "Jakarta" else self.bandung
        return replica.read(user_id)

    def baca_saldo_read_your_writes(self, user_id: str, server: str, versi_minimal: int) -> float:
        replica = self.jakarta if server == "Jakarta" else self.bandung
        timeout = REPLICATION_DELAY * 3
        start = time.time()

        while replica.get_version(user_id) < versi_minimal:
            if time.time() - start > timeout:
                return self.jakarta.read(user_id)
            time.sleep(0.2)

        return replica.read(user_id)


def main():
    system = ReplicationSystem()
    user_id = "user1"

    print("=== Skenario NAIF (tanpa Read-Your-Writes) ===")
    system.top_up(user_id, 50000)
    time.sleep(0.5)
    print("Baca saldo dari Bandung (naif):", system.baca_saldo_naif(user_id, "Bandung"))

    time.sleep(REPLICATION_DELAY + 0.5)

    print("\n=== Skenario dengan Read-Your-Writes ===")
    system.top_up(user_id, 20000)
    versi_terakhir = system.version_counter
    
    saldo_ryw = system.baca_saldo_read_your_writes(
        user_id=user_id,
        server="Bandung",
        versi_minimal=versi_terakhir,
    )
    print("Baca saldo dari Bandung (RYW):", saldo_ryw)


if __name__ == "__main__":
    main()
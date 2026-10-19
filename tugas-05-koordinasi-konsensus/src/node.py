"""
Tugas 5 - Simulasi Node untuk Bully Algorithm
Dikerjakan oleh: Kelompok 1
Implementasi penuh oleh: Nuevalen, Haniel, Farrellino
"""

import argparse
import socket
import threading
import time

ELECTION_TIMEOUT = 2.0  # detik menunggu balasan OK sebelum menyatakan diri leader

class Node:
    def __init__(self, node_id: int, port: int, peers: dict):
        self.node_id = node_id
        self.port = port
        self.peers = peers
        self.leader_id = None
        self.lock = threading.Lock()
        # Event untuk sinkronisasi menunggu pesan OK (TODO 1 & 2)
        self.ok_event = threading.Event() 

    # ---------- Infrastruktur jaringan (SUDAH LENGKAP) ----------

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", self.port))
        server.listen()
        print(f"[Node {self.node_id}] Listening di port {self.port}")
        while True:
            conn, _ = server.accept()
            threading.Thread(target=self.handle_connection, args=(conn,), daemon=True).start()

    def handle_connection(self, conn: socket.socket):
        with conn:
            data = conn.recv(1024).decode()
            if not data:
                return
            sender_id, msg_type = data.split(":")
            self.on_message(int(sender_id), msg_type)

    def send_message(self, target_port: int, msg_type: str) -> bool:
        try:
            with socket.create_connection(("localhost", target_port), timeout=1.0) as s:
                s.sendall(f"{self.node_id}:{msg_type}".encode())
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False

    # ---------- Logika Bully Algorithm (LENGKAP) ----------

    def on_message(self, sender_id: int, msg_type: str):
        # TODO 1: Tangani pesan ELECTION, OK, COORDINATOR
        if msg_type == "ELECTION":
            if sender_id < self.node_id:
                # Balas OK ke node yang lebih rendah
                self.send_message(5000 + sender_id, "OK")
                # Mulai election sendiri karena kita lebih tinggi
                self.start_election()
        elif msg_type == "OK":
            # Tandai bahwa ada node lebih tinggi yang hidup
            self.ok_event.set()
        elif msg_type == "COORDINATOR":
            with self.lock:
                self.leader_id = sender_id
            print(f"[Node {self.node_id}] Menerima COORDINATOR. Leader baru adalah Node {sender_id}")
        elif msg_type == "PING":
            pass # Hanya untuk probing di monitor_leader

    def start_election(self):
        # TODO 2: Kirim ELECTION ke peer lebih tinggi, tunggu OK
        self.ok_event.clear()
        higher_peers = {pid: p for pid, p in self.peers.items() if pid > self.node_id}
        
        ada_yang_hidup = False
        for pid, port in higher_peers.items():
            if self.send_message(port, "ELECTION"):
                ada_yang_hidup = True
                
        if not ada_yang_hidup:
            # Tidak ada node lebih tinggi yang hidup
            self.declare_leader()
        else:
            # Tunggu balasan OK dengan timeout
            if not self.ok_event.wait(timeout=ELECTION_TIMEOUT):
                # Timeout tercapai, node lebih tinggi tidak merespons
                self.declare_leader()

    def declare_leader(self):
        # TODO 3: Set leader_id dan broadcast COORDINATOR
        with self.lock:
            self.leader_id = self.node_id
        print(f"[Node {self.node_id}] *** MENJADI LEADER! Broadcasting COORDINATOR... ***")
        for pid, port in self.peers.items():
            self.send_message(port, "COORDINATOR")

    def monitor_leader(self):
        # TODO 4: Cek periodik apakah leader masih hidup
        while True:
            time.sleep(3)
            with self.lock:
                current_leader = self.leader_id
                
            if current_leader is not None and current_leader != self.node_id:
                leader_port = 5000 + current_leader
                if not self.send_message(leader_port, "PING"):
                    print(f"[Node {self.node_id}] Leader {current_leader} terdeteksi mati! Memulai election...")
                    with self.lock:
                        self.leader_id = None
                    self.start_election()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--peers", type=str, required=True)
    args = parser.parse_args()

    peer_ports = [int(p) for p in args.peers.split(",")]
    peers = {port - 5000: port for port in peer_ports}

    node = Node(args.id, args.port, peers)

    threading.Thread(target=node.start_server, daemon=True).start()
    threading.Thread(target=node.monitor_leader, daemon=True).start()

    time.sleep(1)  # beri waktu semua node lain start
    node.start_election()

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
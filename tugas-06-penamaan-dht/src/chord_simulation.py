import hashlib

def hash_id(name: str) -> int:
    """Hash nama ke dalam ruang 8-bit (0-255) menggunakan SHA-1"""
    return int(hashlib.sha1(name.encode('utf-8')).hexdigest(), 16) % 256

class ChordRing:
    def __init__(self):
        self.nodes = {}  # node_id (int) -> node_name (str)
        self.data = {}   # key_hash (int) -> (kurir_id, ip_kurir, pemilik_node_id)

    # ================================
    # TODO FARRELLINO: join & leave
    # ================================
    def join(self, node_name: str, node_ip: str):
        node_id = hash_id(node_name)
        print(f"[Node] '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")
        
        if not self.nodes:
            self.nodes[node_id] = node_name
            print(f"[Node] '{node_name}' adalah node pertama dalam ring.")
            return

        # 1. Cari predecessor dari node_id di ring saat ini
        preds = [nid for nid in self.nodes.keys() if nid < node_id]
        if preds:
            predecessor_id = max(preds)
        else:
            predecessor_id = max(self.nodes.keys()) # wrap-around
            
        # 2. Tambahkan node baru ke ring
        self.nodes[node_id] = node_name
        
        # 3. Pindahkan data yang menjadi tanggung jawab node baru
        # Yaitu data dengan key_hash di range: predecessor_id < k <= node_id
        moved = False
        for k, (kurir_id, ip, owner_id) in list(self.data.items()):
            if predecessor_id < node_id:
                # Normal case: predecessor_id < k <= node_id
                if predecessor_id < k <= node_id:
                    old_succ_name = self.nodes[owner_id]
                    print(f"[Data] Key {k} ({kurir_id}) dipindahkan dari {old_succ_name} ke {node_name}")
                    self.data[k] = (kurir_id, ip, node_id)
                    moved = True
            else:
                # Wrap-around case: k > predecessor_id ATAU k <= node_id
                if k > predecessor_id or k <= node_id:
                    old_succ_name = self.nodes[owner_id]
                    print(f"[Data] Key {k} ({kurir_id}) dipindahkan dari {old_succ_name} ke {node_name}")
                    self.data[k] = (kurir_id, ip, node_id)
                    moved = True
                    
        if not moved:
            print(f"[Data] Tidak ada data yang perlu dipindahkan ke {node_name}.")

    def leave(self, node_name: str):
        node_id = hash_id(node_name)
        if node_id not in self.nodes:
            print(f"[Node] '{node_name}' tidak ditemukan di ring.")
            return
            
        print(f"[Node] '{node_name}' (id={node_id}) keluar dari ring")
        
        # 1. Cari data yang dipegang oleh node yang keluar
        keys_to_move = [k for k, (kurir_id, ip, owner_id) in self.data.items() if owner_id == node_id]
        
        # 2. Hapus node dari ring
        del self.nodes[node_id]
        
        if not self.nodes:
            print("[Node] Ring sekarang kosong.")
            self.data = {}
            return
            
        # 3. Pindahkan data ke successor baru
        for k in keys_to_move:
            kurir_id, ip, _ = self.data[k]
            # Cari successor baru
            candidates = [nid for nid in self.nodes.keys() if nid >= k]
            if candidates:
                new_succ_id = min(candidates)
            else:
                new_succ_id = min(self.nodes.keys()) # wrap-around
                
            new_succ_name = self.nodes[new_succ_id]
            print(f"[Data] Key {k} ({kurir_id}) dipindahkan dari {node_name} ke {new_succ_name}")
            self.data[k] = (kurir_id, ip, new_succ_id)

    # ================================
    # TODO HANIEL: find_successor
    # ================================
    def find_successor(self, key_hash: int) -> int:
        candidates = [nid for nid in self.nodes.keys() if nid >= key_hash]
        if candidates:
            return min(candidates)
        return min(self.nodes.keys())  # wrap-around

    # ================================
    # TODO NUEVALEN: register & lookup
    # ================================
    def register_kurir(self, kurir_id: str, ip_kurir: str):
        key_hash = hash_id(kurir_id)
        successor_id = self.find_successor(key_hash)
        successor_name = self.nodes[successor_id]
        self.data[key_hash] = (kurir_id, ip_kurir, successor_id)
        print(f"[Register] {kurir_id} (hash={key_hash}) disimpan di {successor_name} (id={successor_id})")

    def lookup(self, kurir_id: str) -> str | None:
        key_hash = hash_id(kurir_id)
        successor_id = self.find_successor(key_hash)
        successor_name = self.nodes[successor_id]
        if key_hash in self.data:
            print(f"[Lookup] {kurir_id} (hash={key_hash}) ditemukan di {successor_name} -> {self.data[key_hash][1]}")
            return self.data[key_hash][1]
        print(f"[Lookup] {kurir_id} (hash={key_hash}) tidak ditemukan.")
        return None

if __name__ == "__main__":
    ring = ChordRing()
    
    print("=== Skenario Awal: 4 Node Bergabung ===")
    ring.join("node-jakarta-1", "10.0.0.1")
    ring.join("node-jakarta-2", "10.0.0.2")
    ring.join("node-bandung-1", "10.0.0.3")
    ring.join("node-surabaya-1", "10.0.0.4")
    
    print("\n=== Register Kurir ===")
    # Hash teruji: kurir-000=183, kurir-001=50, kurir-002=28, kurir-003=132, kurir-012=116
    ring.register_kurir("kurir-000", "192.168.1.100") 
    ring.register_kurir("kurir-001", "192.168.1.10")  
    ring.register_kurir("kurir-002", "192.168.1.11")  
    ring.register_kurir("kurir-003", "192.168.1.12")  
    ring.register_kurir("kurir-012", "192.168.1.13")  # Akan dipindahkan saat node-medan-1 join
    
    print("\n--- Lookup sebelum perubahan topologi ---")
    ring.lookup("kurir-000")
    ring.lookup("kurir-001")
    ring.lookup("kurir-012")
    
    print("\n=== Skenario Join: Node Baru Bergabung ===")
    ring.join("node-medan-1", "10.0.0.5") # Hash 123
    
    print("\n--- Lookup setelah Join ---")
    ring.lookup("kurir-001")
    ring.lookup("kurir-012") # Sekarang dipegang node-medan-1
    
    print("\n=== Skenario Leave: Node Keluar ===")
    ring.leave("node-jakarta-1") # Hash 177
    
    print("\n--- Lookup setelah Leave ---")
    ring.lookup("kurir-000") # Akan di-wrap-around ke node-bandung-1
    ring.lookup("kurir-001")
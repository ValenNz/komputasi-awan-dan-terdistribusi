import hashlib

def hash_id(name: str) -> int:
    """Hash nama ke dalam ruang 8-bit (0-255) menggunakan SHA-1"""
    return int(hashlib.sha1(name.encode('utf-8')).hexdigest(), 16) % 256

class ChordRing:
    def __init__(self):
        self.nodes = {}  
        self.data = {}   

    def join(self, node_name: str, node_ip: str):
        node_id = hash_id(node_name)
        print(f"[Node] '{node_name}' (id={node_id}) bergabung, alamat {node_ip}")
        
        if not self.nodes:
            self.nodes[node_id] = node_name
            print(f"[Node] '{node_name}' adalah node pertama dalam ring.")
            return

        preds = [nid for nid in self.nodes.keys() if nid < node_id]
        if preds:
            predecessor_id = max(preds)
        else:
            predecessor_id = max(self.nodes.keys()) 
            
        self.nodes[node_id] = node_name

        moved = False
        for k, (kurir_id, ip, owner_id) in list(self.data.items()):
            if predecessor_id < node_id:
                if predecessor_id < k <= node_id:
                    old_succ_name = self.nodes[owner_id]
                    print(f"[Data] Key {k} ({kurir_id}) dipindahkan dari {old_succ_name} ke {node_name}")
                    self.data[k] = (kurir_id, ip, node_id)
                    moved = True
            else:
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
        
        keys_to_move = [k for k, (kurir_id, ip, owner_id) in self.data.items() if owner_id == node_id]
        
        del self.nodes[node_id]
        
        if not self.nodes:
            print("[Node] Ring sekarang kosong.")
            self.data = {}
            return
            
        for k in keys_to_move:
            kurir_id, ip, _ = self.data[k]
            candidates = [nid for nid in self.nodes.keys() if nid >= k]
            if candidates:
                new_succ_id = min(candidates)
            else:
                new_succ_id = min(self.nodes.keys()) 
                
            new_succ_name = self.nodes[new_succ_id]
            print(f"[Data] Key {k} ({kurir_id}) dipindahkan dari {node_name} ke {new_succ_name}")
            self.data[k] = (kurir_id, ip, new_succ_id)


    def find_successor(self, key_hash: int) -> int:
        candidates = [nid for nid in self.nodes.keys() if nid >= key_hash]
        if candidates:
            return min(candidates)
        return min(self.nodes.keys())
    
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
    ring.register_kurir("kurir-000", "192.168.1.100") 
    ring.register_kurir("kurir-001", "192.168.1.10")  
    ring.register_kurir("kurir-002", "192.168.1.11")  
    ring.register_kurir("kurir-003", "192.168.1.12")  
    ring.register_kurir("kurir-012", "192.168.1.13")  
    
    print("\n--- Lookup sebelum perubahan topologi ---")
    ring.lookup("kurir-000")
    ring.lookup("kurir-001")
    ring.lookup("kurir-012")
    
    print("\n=== Skenario Join: Node Baru Bergabung ===")
    ring.join("node-medan-1", "10.0.0.5") 
    
    print("\n--- Lookup setelah Join ---")
    ring.lookup("kurir-001")
    ring.lookup("kurir-012") 
    
    print("\n=== Skenario Leave: Node Keluar ===")
    ring.leave("node-jakarta-1") 
    
    print("\n--- Lookup setelah Leave ---")
    ring.lookup("kurir-000") 
    ring.lookup("kurir-001")
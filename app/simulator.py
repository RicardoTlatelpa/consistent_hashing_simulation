from app.node import Node
from app.hash_ring import HashRing
from app.key_store import KeyStore

class Simulator:
    def __init__(self, num_nodes=3):
        self.ring = Hashring()
        self.nodes = [Node(f"Node-{i}") for i in range(num_nodes)]
        self.store = KeyStore(self.ring)
        for node in self.nodes:
            self.ring.add_node(node)
    def add_node(self):
        new_node = Node(f"Node-{len(self.nodes)}")
        self.nodes.append(new_node)
        self.ring.add_node(new_node)
        print(f"Added {new_node}")
    def remove_node(self,node_index):
        node = self.nodes.pop(node_index)
        self.ring.remove_node(node)
        print(f"Removed {node}")
    def insert_keys(self, count=1000):
        import random
        for i in range(count):
            key = f"key-{random.randint(1,1_000_000)}"
            self.store.insert_key(key, f"value-{i}")
    def report_distribution(self):
        dist = self.store.get_distribution()
        for node, count in dist.items():
            print(f"{node}: {count} keys")
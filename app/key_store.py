class KeyStore:
    def __init__(self,ring):
        self.ring = ring
        self.store = dict()
    def insert_key(self,key,value):
        node = self.ring.get_node(key)
        self.store.setdefault(node.name, dict())[key] = value
        return node
    def get_distribution(self):
        return {node: len(keys) for node,keys in self.store.items()}
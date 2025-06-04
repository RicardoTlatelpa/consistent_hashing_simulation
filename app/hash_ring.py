import bisect
import hashlib
class HashRing:
    def __init__(self,virtual_nodes=3):
        self.ring = dict()
        self.sorted_keys = []
        self.nodes = set()
        self.virtual_nodes = virtual_nodes
    def _hash(self,key):        
        return int(hashlib.sha1(key.encode()).hexdigest(),16)
    def add_node(self,node):
        self.nodes.add(node)
        for i in range(self.virtual_nodes):
            vnode_key = f"{node.name}-vn{i}"
            vnode_hash = self._hash(vnode_key)
            self.ring[vnode_hash] = node
            bisect.insort(self.sorted_keys,vnode_hash)
    def remove_node(self,node):
        self.nodes.discard(node)
        for i in range(self.virtual_nodes):
            vnode_key = f"{node.name}-vn{i}"
            vnode_hash = self._hash(vnode_key)
            self.ring.pop(vnode_hash, None)
            self.sorted_keys.remove(vnode_hash)
    def get_node(self,key):
        key_hash = self._hash(key)
        idx = bisect.bisect(self.sorted_keys, key_hash)
        if idx == len(self.sorted_keys):
            idx = 0
        return self.ring[self.sorted_keys[idx]]
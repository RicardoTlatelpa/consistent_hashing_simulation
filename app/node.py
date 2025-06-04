import hashlib

class Node:
    def __init__(self,name):
        self.name = name
        self.hash = self.hash_node(name)

    def hash_node(self,name):
        return int(hashlib.sha1(name.encode()).hexdigest(),16)
    def __repr__(self):
        return f"Node({self.name})"

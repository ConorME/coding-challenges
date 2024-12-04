# Simple implementation using separate chaining
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in bucket:
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in bucket:
            if k == key:
                del bucket[i]
                return True
        
        return False

    def __str__(self):
        return str(self.table)
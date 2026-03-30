class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity
    
    def hash(self, key: int):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        val = self.map[index]
        while True:
            if self.map[index] is None:
                self.map[index] = [key, value]
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.map[index][0] == key:
                self.map[index][1] = value
                return
            
            index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)
        start_index = index
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                return self.map[index][1]
            index = (index + 1) % self.capacity
            if index == start_index: # Prevent infinite loop if full
                break
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        
        while self.map[index] is not None:
            if self.map[index][0] == key:
                # To keep the linear probing chain intact, 
                # we remove the item and re-insert the following block
                self.map[index] = None
                self.size -= 1
                
                # Rehash the following items in the cluster
                next_idx = (index + 1) % self.capacity
                while self.map[next_idx] is not None:
                    item_to_rehash = self.map[next_idx]
                    self.map[next_idx] = None
                    self.size -= 1
                    self.insert(item_to_rehash[0], item_to_rehash[1])
                    next_idx = (next_idx + 1) % self.capacity
                return True
            
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        old_map = self.map
        self.map = [None] * self.capacity
        self.size = 0
        for item in old_map:
            if item:
                self.insert(item[0], item[1])
            

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        next_node = self.head.next
        next_node.prev = new_node
        new_node.next = next_node
        self.head.next = new_node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        ret = self.tail.prev.val
        self.tail = self.tail.prev
        return ret

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        ret = self.head.next.val
        self.head = self.head.next
        return ret
        

class Node():
    def __init__(self, val, next_node = None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next_node
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next_node
        return -1  # Index out of bounds or list is empty
        
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node
        if not new_node.next_node:  # If list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next_node = Node(val)
        self.tail = self.tail.next_node       

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next_node
        
        # Remove the node ahead of curr
        if curr and curr.next_node:
            if curr.next_node == self.tail:
                self.tail = curr
            curr.next_node = curr.next_node.next_node
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next_node
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next_node
        return res

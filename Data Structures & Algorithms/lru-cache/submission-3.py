class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        node.next = self.right
        node.prev = self.right.prev
        prev_node.next = node
        next_node.prev = node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            this_node = self.cache[key]
            self.remove(this_node)
            self.insert(this_node)
            return this_node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)

            
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
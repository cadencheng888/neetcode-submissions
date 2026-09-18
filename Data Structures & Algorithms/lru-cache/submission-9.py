class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            nodeToRemove = self.cache[key]
            del self.cache[key]
            self.remove(nodeToRemove)
        
        newNode = Node(value, key)
        self.cache[key] = newNode
        self.insert(newNode)
        if len(self.cache) > self.capacity:
            nodeToRemove = self.cache[self.left.next.key]
            del self.cache[nodeToRemove.key]
            self.remove(nodeToRemove)
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insert(self, node):
        nextNode = self.right
        prevNode = self.right.prev
        node.next = nextNode
        node.prev = prevNode
        prevNode.next = node
        nextNode.prev = node


class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
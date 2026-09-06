"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = {None : None}
        current = head
        while current:
            old2new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            old2new[current].next = old2new[current.next]
            old2new[current].random = old2new[current.random]
            current = current.next
        return old2new[head]
            
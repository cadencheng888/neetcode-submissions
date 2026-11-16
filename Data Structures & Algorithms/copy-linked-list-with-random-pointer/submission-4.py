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
        curr1 = head
        copyHead = Node(0)
        returnHead = copyHead
        oldToNew = {None: None}
        while curr1:
            newNode = Node(curr1.val)
            copyHead.next = newNode
            oldToNew[curr1] = newNode
            copyHead = copyHead.next
            curr1 = curr1.next
        curr2 = head
        while curr2:
            oldToNew[curr2].random = oldToNew[curr2.random]
            curr2 = curr2.next
        return returnHead.next
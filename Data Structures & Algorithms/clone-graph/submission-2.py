"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        oldToNew = {}
        def clone(current):
            if not node:
                return
            copy = Node(current.val)
            oldToNew[current] = copy
            for nei in current.neighbors:
                if nei not in oldToNew:
                    clone(nei)
                copy.neighbors.append(oldToNew[nei])
        clone(node)
        return oldToNew[node]


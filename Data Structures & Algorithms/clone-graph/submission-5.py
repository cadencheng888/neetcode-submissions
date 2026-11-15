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
        def dfs(current):
            oldToNew[current] = Node(current.val)
            for nei in current.neighbors:
                if nei not in oldToNew:
                    dfs(nei)
                oldToNew[current].neighbors.append(oldToNew[nei])
        dfs(node)
        return oldToNew[node]
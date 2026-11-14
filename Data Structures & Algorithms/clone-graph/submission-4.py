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
        
        node_dict = {}

        def dfs(current):

            node_dict[current] = Node(current.val)
            for nei in current.neighbors:
                if nei not in node_dict:
                    dfs(nei)
                node_dict[current].neighbors.append(node_dict[nei])
        dfs(node)
        return node_dict[node]
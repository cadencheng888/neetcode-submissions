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
            return None
        
        node_dict = {}
        stack = [node]
        node_dict[node] = Node(node.val)
        while stack:
            current = stack.pop()

            for nei in current.neighbors:
                
                if nei not in node_dict:
                    node_dict[nei] = Node(nei.val)
                    stack.append(nei)
                node_dict[current].neighbors.append(node_dict[nei])
        return node_dict[node]

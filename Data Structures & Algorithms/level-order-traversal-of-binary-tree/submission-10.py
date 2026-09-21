# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        while len(q) != 0:
            height = len(q)
            levels = []
            for i in range(height):
                node = q.popleft()
                if node is not None:
                    levels.append(node.val)

                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            
            if levels:
                result.append(levels)
            
        return result
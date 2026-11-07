# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        right = None
        left = None
        def dfs(current):
            if not current:
                return
            if p.val <= current.val <= q.val or q.val <= current.val <= p.val:
                return current
            if p.val >= current.val and q.val >= current.val:
                return self.lowestCommonAncestor(current.right, p, q)
            if p.val <= current.val and q.val <= current.val:
                return self.lowestCommonAncestor(current.left, p, q)
            if left is not None:
                return left
            if right is not None:
                return right
        return dfs(root)

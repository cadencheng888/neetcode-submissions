# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(current):
            if not current:
                return
            if p.val <= current.val <= q.val or q.val <= current.val <= p.val:
                return root
            left= self.lowestCommonAncestor(current.left, p, q)
            right= self.lowestCommonAncestor(current.right, p, q)
            if left is not None:
                return left
            if right is not None:
                return right
        return dfs(root)

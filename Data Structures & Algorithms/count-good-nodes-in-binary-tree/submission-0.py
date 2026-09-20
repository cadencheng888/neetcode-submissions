# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, newmax):
            if not node:
                return 0
            if node.val >= newmax:
                isgood = 1
            else:
                isgood = 0
            newmax = max(node.val, newmax)
            left_count = dfs(node.left, newmax)
            right_count = dfs(node.right, newmax)
            return isgood + left_count + right_count

        return dfs(root, root.val)

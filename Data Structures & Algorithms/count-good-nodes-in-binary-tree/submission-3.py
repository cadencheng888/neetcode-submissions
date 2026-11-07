# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        goodNodesCount = 0

        def dfs(current, currentMax):
            nonlocal goodNodesCount
            if current is None:
                return
            
            if current.val >= currentMax:
                goodNodesCount += 1
            currentMax = max(currentMax, current.val)
            left = dfs(current.left, currentMax)
            right = dfs(current.right, currentMax)
        dfs(root, root.val)
        return goodNodesCount


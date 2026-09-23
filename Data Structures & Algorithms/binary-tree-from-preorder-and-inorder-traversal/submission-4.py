class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap to instantly find the index of any value in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # An iterator for preorder allows us to easily grab the next root
        preorder_iter = iter(preorder)
        
        def helper(left_bound, right_bound):
            # Base case: if there are no elements to construct the tree
            if left_bound > right_bound:
                return None
            
            # The next element in preorder is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find where the root splits the inorder array
            mid = inorder_map[root_val]
            
            # Build left and right subtrees
            root.left = helper(left_bound, mid - 1)
            root.right = helper(mid + 1, right_bound)
            
            return root
            
        return helper(0, len(inorder) - 1)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map values to their index in `inorder` for instant O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. Convert preorder to an iterator so we can cleanly grab the next root
        preorder_iter = iter(preorder)
        
        # 3. Use pointers (left, right) instead of slicing arrays
        def helper(left_bound, right_bound):
            # Base case: no elements left for this subtree
            if left_bound > right_bound:
                return None
            
            # The next element in our preorder traversal is the root
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find where this root is in the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees
            root.left = helper(left_bound, mid - 1)
            root.right = helper(mid + 1, right_bound)
            
            return root
            
        # Start the bounds with the entire inorder array
        return helper(0, len(inorder) - 1)
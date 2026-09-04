class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # 1. Put all nodes into an array
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
            
        # 2. Use two pointers to rewire the next pointers
        left, right = 0, len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            
            # Stop if we meet in the middle
            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        # 3. Terminate the last node to prevent cycles
        nodes[left].next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        current = head
        target_index = len(nodes) - n
        print(f"Index to remove: {n}")
        if target_index == 0:
            return head.next
        
        prev = nodes[target_index - 1]
        target_node = nodes[target_index]
        prev.next = target_node.next


        return head
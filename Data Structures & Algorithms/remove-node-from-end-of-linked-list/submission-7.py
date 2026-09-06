# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []
        current = head
        count = 0
        while current:
            nodes.append(current)
            current = current.next
            print(nodes[count].val)
            count += 1
        
        target_index = len(nodes) - n
        if target_index == 0:
            return head.next
        print(target_index)
        prev = nodes[target_index - 1]
        target_node = nodes[target_index]
        prev.next = target_node.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        total1 = ""
        while l1:
            total1 = str(l1.val) + total1
            l1 = l1.next
        total2 = ""
        while l2:
            total2 = str(l2.val) + total2
            l2 = l2.next
        total = int(total1) + int(total2)
        total_str = str(total)[::-1]
        print(total_str)
        for char in total_str:
            num = ListNode(int(char))
            current.next = num
            current = current.next
        return dummy.next
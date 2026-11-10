# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = False
        newCurr = ListNode(None)
        head = newCurr
        
        if not curr1 and not curr2:
            return
        while curr1 and curr2:
            currentSum = curr1.val + curr2.val

            if carry:
                currentSum += 1
                if currentSum > 9:
                    carry = True
                    onesDigit = int(str(currentSum)[1])
                    newNode = ListNode(onesDigit)
                    newCurr.next = newNode
                    newCurr = newCurr.next
                else:
                    carry = False
                    onesDigit = currentSum
                    newNode = ListNode(onesDigit)
                    newCurr.next = newNode
                    newCurr = newCurr.next
            else:
                if currentSum > 9:
                    carry = True
                    onesDigit = int(str(currentSum)[1])
                    newNode = ListNode(onesDigit)
                    newCurr.next = newNode
                    newCurr = newCurr.next
                else:
                    carry = False
                    onesDigit = currentSum
                    newNode = ListNode(onesDigit)
                    newCurr.next = newNode
                    newCurr = newCurr.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            if carry:
                currentSum = curr1.val + 1
            else:
                currentSum = curr1.val
            if currentSum > 9:
                currentSum = int(str(currentSum)[1])
                carry = True
            else:
                carry = False
            newNode = ListNode(currentSum)
            newCurr.next = newNode
            newCurr = newCurr.next
            curr1 = curr1.next
        while curr2:
            if carry:
                currentSum = curr2.val + 1
            else:
                currentSum = curr2.val
            if currentSum > 9:
                currentSum = int(str(currentSum)[1])
                carry = True
            else:
                carry = False
            newNode = ListNode(currentSum)
            newCurr.next = newNode
            newCurr = newCurr.next
            curr2 = curr2.next
        if carry:
            newCurr.next = ListNode(1)
            newCurr = newCurr.next
        return head.next
        
                

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        if head.next is None:
            return
        nodes = []
        current = head
        while current is not None:
            nodes.append(current)
            current = current.next
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None

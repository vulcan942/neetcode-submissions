# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First check if k nodes exist
        curr = head
        for _ in range(k):
            if curr is None:
                return head
            curr = curr.next

        # Reverse k nodes
        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head is now the tail of this reversed group
        head.next = self.reverseKGroup(curr, k)

        return prev
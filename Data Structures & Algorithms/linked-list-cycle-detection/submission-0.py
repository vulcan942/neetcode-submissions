# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        firstPointer = head
        secondPointer = head

        while secondPointer != None and secondPointer.next:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next.next
            if firstPointer == secondPointer:
                return True
        return False
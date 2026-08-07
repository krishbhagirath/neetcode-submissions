# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # l1 and l2: represent the current ListNode itself
        # dummy: empty node avoid edge cases, tail tracks the end
        
        dummy = ListNode()
        tail = dummy

        # iterate both lists while both are not empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # one list empty, one not
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

        
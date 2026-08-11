# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Option 1: reverse LL, traverse
        # Option 2: two pointers, L at start, R offset by n, increment until R is at NULL, leaving L at the node to be deleted, make dummy for start of left

        # init dummy
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right ptr n nodes fwd
        for i in range(n):
            right = right.next

        # move both fwd until right is null
        while right:
            left = left.next
            right = right.next

        # delete node (skip with left ptr)
        left.next = left.next.next
        return dummy.next # return everything after dummy

        

        
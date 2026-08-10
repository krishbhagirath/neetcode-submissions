# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # First: find middle of list using pointers

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next # jump by 1
            fast = fast.next.next # jump by 2

        secondHalf = slow.next # first node of second half
        slow.next = None # end of second half
        prevNode = None

        # Second: reverse second half of list
        while secondHalf:
            temp = secondHalf.next #store next ptr
            secondHalf.next = prevNode #move next to prev
            prevNode = secondHalf # set prev to current
            secondHalf = temp #move current forward

        # Third: merge two halves of list
        secondHalf = prevNode # end of loop, secondHalf = null, prev is last node
        first = head

        # second half shorter than first
        while secondHalf:

            # store temps
            temp1 = first.next
            temp2 = secondHalf.next

            # first points to end, second points to first's next node
            first.next = secondHalf
            secondHalf.next = temp1

            # shift ptrs
            first = temp1
            secondHalf = temp2




            
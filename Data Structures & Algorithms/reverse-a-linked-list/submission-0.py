# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # init previous node (none)
        curr = head # start current node at head

        while(curr != None): # run while list is not over
            nextNode = curr.next # save next node
            curr.next = prev # move pointer from current to previous (reverse pointer)
            prev = curr # move prev fwd
            curr = nextNode # move curr fwd

        head = prev

        return head

# Algorithm:
# - iterate while curr isn't Null
# - 1. store next node (curr.next)
# - 2. move current next to prev
# - 3. move prev up to curr
# - 4. move curr up to temp next
# - 5. after reversing all pointers, when curr IS none, head will be set to the prev node (the last touched real value)
        
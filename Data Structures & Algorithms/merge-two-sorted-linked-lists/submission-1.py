# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # steps:
        # 1) make dummy node for start, tail for moving end node (starts at dummy)
        # 2) loop while l1 and l2 still exist
            # 3) if l1 val < l2 val, append l1 to new LL, move l1 fwd
            #    same for other case, append l2 to new LL, move l2 fwd

        # 4) move tail fwd
        # 5) end of while loop, ONE LIST HAS ENDED
            # if l1 still exists, append rest of l1 to our list
            # elif l2, apppend rest of l2 to our list
        # return full list via dummy

        dummy = ListNode()
        tail = dummy # moving node tracking current node
        
        # 1, 2, 4
        # 3, 5
        # head, 1

        while l1 and l2: 

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next


        # loop exits, either l1 or l2 is now false (either only one list exist or both done)

        # append end of l1 or l2
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

















        # # l1 and l2: represent the current ListNode itself
        # # dummy: empty node avoid edge cases, tail tracks the end
        
        # dummy = ListNode()
        # tail = dummy

        # # iterate both lists while both are not empty
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next

        #     tail = tail.next

        # # one list empty, one not
        # if l1:
        #     tail.next = l1
        # elif l2:
        #     tail.next = l2

        # return dummy.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Method 1:
            # if no cycle, we end at a NULL
            # else, need a hashset to track what node we have visited
            # once either null or visited node is reached, we check


        # Method 2: Tortoise and Hare
            # fast pointer jumps by 2, slow jumps by 1
            # they'll meet again if it's cyclic, will not if it ends at NULL
            # Time: O(1) - compared to prev O(n)

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True # both pointers have met, cycle exists

        return False # fast reaches end before slow, if loop exits we have reached an end


        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        headl1 = l1
        headl2 = l2

        dummy = ListNode()
        prev = dummy
        carry = 0

        while headl1 or headl2 or carry:
            
            val1 = headl1.val if headl1 else 0
            val2 = headl2.val if headl2 else 0

            sum = val1 + val2 + carry

            carry = 1 if sum > 9 else 0

            newNode = ListNode(sum % 10)
            prev.next = newNode
            prev = newNode

            headl1 = headl1.next if headl1 else None
            headl2 = headl2.next if headl2 else None

        return dummy.next
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a dict, correspond old node to newly made nodes, then traverse again to fill values

        curr = head
        copies = {} # need to correspond original node with new node

        if head is None:
            return None

        while curr:
            newNode = Node(curr.val)
            copies[curr] = newNode # key: curr (old LL), value: newNode (new LL)
            curr = curr.next

        curr = head
        while curr:          
            if curr.next == None:
                copies[curr].next = None
            else:
                copies[curr].next = copies[curr.next] # correspond next ptrs
            
            if curr.random == None:
                copies[curr].random = None
            else:
                copies[curr].random = copies[curr.random] # correspond random ptrs

            curr = curr.next # move curr fwd

        return copies[head]

 



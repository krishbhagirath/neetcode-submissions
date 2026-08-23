# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use DFS

        # BASE CASES
        # ----------------------------
        # both null
        if not p and not q:
            return True

        # only one is null, one is not
        if not p or not q: 
            return False

        # non-matching values
        if p.val != q.val:
            return False
        
        # after base cases, call recursive function (check left and right sides)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
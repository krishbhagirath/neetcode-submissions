# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: what if root does not exist?
        if not root:
            return 0

        # Recursively determine the depth on each side
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        # Choose the appropriate side and count the current node
        return left_depth if left_depth > right_depth else right_depth
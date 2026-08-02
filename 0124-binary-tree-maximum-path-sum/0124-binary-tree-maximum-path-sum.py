# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def number(node):
            if node is None:
                return 0
            
            left = number(node.left)
            right = number(node.right)
            left = max(left , 0)
            right = max(right , 0)

            peak_val = node.val + right + left
            self.max_sum = max(self.max_sum , peak_val)
            return node.val + max(left , right)

        number(root)
        return self.max_sum
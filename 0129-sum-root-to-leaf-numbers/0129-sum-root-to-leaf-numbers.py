# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        def sum_root(node , number = 0):
            if node is None:
                return 
            number = number * 10 + node.val
            left = sum_root(node.left , number)
            right = sum_root(node.right , number)
            if node.left is None and node.right is None:
                self.total_sum += number
                return 
        sum_root(root)
        return self.total_sum 
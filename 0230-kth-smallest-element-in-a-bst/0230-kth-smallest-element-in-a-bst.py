# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x = 0
        num = 0
        def inorder(node):
            nonlocal x
            nonlocal num
            if node is None:
                return 
            inorder(node.left)
            x += 1
            if x == k:
                num = node.val
                return 
            inorder(node.right)
        inorder(root)
        return num
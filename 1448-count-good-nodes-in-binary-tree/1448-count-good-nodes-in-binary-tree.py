# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def check(node , value):
            nonlocal count
            if node is None :
                return 
            if value <= node.val:
                value = node.val
                count += 1
            check(node.left, value)
            check(node.right, value)
        
        check(root , float('-inf'))
        return count
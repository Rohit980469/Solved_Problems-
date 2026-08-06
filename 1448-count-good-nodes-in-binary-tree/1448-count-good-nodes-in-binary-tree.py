# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def check(node , value):
            if node is None :
                return 
            if value <= node.val:
                value = node.val
                self.count += 1
            check(node.left, value)
            check(node.right, value)
        
        check(root , float('-inf'))
        return self.count
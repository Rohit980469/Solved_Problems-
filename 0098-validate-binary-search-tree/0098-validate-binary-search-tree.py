# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isbst(node, low , high):
            if node is None :
                return True
            if (low < node.val < high):
                return isbst(node.left , low , node.val) and isbst(node.right , node.val , high)
            else:
                return False

        return isbst(root,float('-inf') , float('inf'))
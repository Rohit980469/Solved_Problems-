# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        r = []
        def inorder(node):
            if not node:
                return
            nonlocal r
            inorder(node.left)
            r.append(node.val)
            inorder(node.right)

        inorder(root)
        r.sort()
        
        self.x = 0
        def bst(node):
            if not node:
                return
            bst(node.left)
            node.val = r[self.x]
            self.x += 1
            bst(node.right)
        bst(root)

        return root
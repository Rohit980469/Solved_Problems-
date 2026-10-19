# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        self.prev = None
        def flat_list(node):
            if not node:
                return 
            flat_list(node.right)
            flat_list(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        flat_list(root)
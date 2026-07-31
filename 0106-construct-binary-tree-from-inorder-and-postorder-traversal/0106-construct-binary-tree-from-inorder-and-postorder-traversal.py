# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def tree(inord , postord):
            if not postord:
                return 
            x = postord[-1]
            x = inord.index(x)
            left_inorder = inord[:x]
            right_inorder = inord[x+1:]

            size = len(left_inorder)

            left_postord = postord[:size]
            right_postord = postord[size:-1]

            x = postord[-1] 
            root = TreeNode(x)
            root.left = tree(left_inorder , left_postord)
            root.right = tree(right_inorder , right_postord)

            return root
        return tree(inorder , postorder)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def tree(pre , ino):
            if not ino:
                return  
            root_value = pre[0]
            x = ino.index(root_value)
            left_inorder = ino[:x]
            right_inorder = ino[x+1:]


            left_preorder = pre[1:1+x]
            right_preorder = pre[x + 1 :]

            root = TreeNode(root_value)
            root.left = tree(left_preorder , left_inorder)
            root.right = tree(right_preorder , right_inorder)
            return root
        return tree(preorder , inorder)
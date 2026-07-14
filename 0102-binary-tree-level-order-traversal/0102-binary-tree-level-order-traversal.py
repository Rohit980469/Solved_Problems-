from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        curr =  deque([root])
        result  = []
        while curr:
            level = []
            for i in range(len(curr)):
                node = curr.popleft()
                level.append(node.val)
                if node.left != None:
                    curr.append(node.left)
                if node.right != None:
                    curr.append(node.right)
                
            result.append(level)
        return result
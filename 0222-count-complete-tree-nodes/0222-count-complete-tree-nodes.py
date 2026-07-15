from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 0
        node = deque([root])
        while node:
            curr = node.popleft()
            if curr.left != None:
                node.append(curr.left)
            if curr.right != None:
                node.append(curr.right)
            count += 1
        return count
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        node = deque([root])
        while node:
            x = len(node)
            for i in range(x):
                curr = node.popleft()
                if i == x - 1:
                    result.append(curr.val)
                if curr.left != None:
                    node.append(curr.left)
                if curr.right != None:
                    node.append(curr.right)
        return result
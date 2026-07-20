from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        node = deque([root])
        result = []
        level = 0
        while node :
            x = len(node)
            cl = []
            for i in range(x):
                curr = node.popleft()
                if curr.left != None:
                    node.append(curr.left)
                if curr.right != None:
                    node.append(curr.right)
                cl.append(curr.val)
            if level % 2 == 0:
                result.append(cl)
            else :
                result.append(cl[::-1])
            level += 1

        return result
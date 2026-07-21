from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        node = deque([(root,0 , 0)])
        d = {}
        while node:
            curr , hd , row = node.popleft()
            if hd not in d:
                d[hd] = []
            d[hd].append((row, curr.val))
            d[hd].sort()
            if curr.left != None:
                node.append((curr.left , hd - 1 , row + 1))
            if curr.right != None:
                node.append((curr.right , hd + 1 , row + 1))

        result = []
        for x in sorted(d.keys()):
            result.append([val for row , val in d[x]])
        return result
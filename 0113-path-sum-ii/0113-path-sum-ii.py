# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        current = []
        def r(node , rem):
            if node is None:
                return
            current.append(node.val)
            rem -= node.val
            if node.left is None and node.right is None and rem == 0:
                result.append(current[:])
            else :
                r(node.left , rem)
                r(node.right , rem)
            current.pop()
        r(root , targetSum)
        return result
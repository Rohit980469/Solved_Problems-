# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        x = len(nums)//2
        Root = TreeNode(nums[x])
        Root.left = self.sortedArrayToBST(nums[:x])
        Root.right = self.sortedArrayToBST(nums[x+1:])

        return Root 
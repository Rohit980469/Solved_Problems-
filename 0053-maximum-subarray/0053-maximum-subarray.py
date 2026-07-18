class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = nums[0]
        os = nums[0]
        for i in range(1,len(nums)):
            cs = max(nums[i],cs+nums[i])
            os = max(os,cs)
        return os
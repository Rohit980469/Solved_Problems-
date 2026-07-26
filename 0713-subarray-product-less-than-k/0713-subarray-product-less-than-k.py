class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 1:
            return 0
        count = 0
        left = 0
        cm = 1 
        for right in range(len(nums)):
            cm *= nums[right]
            while cm >= k and left <= right:
                cm /= nums[left]
                left += 1
            count += (right - left + 1)
        return count 
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        s = [False] * (n + 1)
        for x in nums:
            if 1 <= x <= n:
                s[x] = True

        for i in range(1,n+1):
            if not s[i]:
                return i
        # cyclic sort
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
        #         correct_index = nums[i] - 1
        #         nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1
        return n + 1
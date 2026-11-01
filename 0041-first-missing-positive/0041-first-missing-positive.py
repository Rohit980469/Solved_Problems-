class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        correct_index = 0
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                correct_index = nums[i] - 1
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
        for i in range(len(nums) ):
            if nums[i] != i + 1:
                return i + 1
        if 1 < nums[0]:
            return 1
        return len(nums) + 1
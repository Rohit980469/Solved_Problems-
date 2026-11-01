class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        n = len(nums)
        s = [False] * (n + 1)
        for i in nums:
            if not s[i]:
                s[i] = True
            else:
                result.append(i)
        return result
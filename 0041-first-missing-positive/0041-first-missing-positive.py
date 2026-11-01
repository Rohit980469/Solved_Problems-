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
        
        return n + 1
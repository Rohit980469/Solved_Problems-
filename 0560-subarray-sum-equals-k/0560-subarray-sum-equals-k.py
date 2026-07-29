from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cs = 0
        count = 0
        for i in range(len(nums)):
            cs += nums[i]
            if cs - k in d:
                count += d[cs- k]
            d[cs] += 1
        return count
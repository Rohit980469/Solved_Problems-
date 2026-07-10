class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        if not nums:
            return 0

        def get_digit_range(n: int) -> int:
            digits = [int(d) for d in str(abs(n))]
            return max(digits) - min(digits)

        ranges = [get_digit_range(num) for num in nums]
    
        max_range = max(ranges)
    
        total_sum = 0
        for num, r in zip(nums, ranges):
            if r == max_range:
                total_sum += num
            
        return total_sum
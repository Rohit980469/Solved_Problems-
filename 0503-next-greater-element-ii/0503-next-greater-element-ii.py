class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        mystack = []
        result = [-1] * len(nums)
        for i  in range(len(nums) * 2):
            x = i % len(nums)
            while mystack and nums[x] > nums[mystack[-1]]:
                prev = mystack.pop()
                result[prev] = nums[x]

            if i < len(nums):
                mystack.append(x)

        return result 
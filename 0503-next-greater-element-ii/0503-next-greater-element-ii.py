class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        mystack = []
        result = [-1] * len(nums)
        for x in range(len(nums) * 2):
            x %= len(nums)
            while mystack and nums[x] > nums[mystack[-1]]:
                prev = mystack.pop()
                result[prev] = nums[x]
            mystack.append(x)

        return result 
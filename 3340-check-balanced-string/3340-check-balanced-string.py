class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = int(num[0])
        odd_sum = int(num[1])
        for i in range(2,len(num)):
            if i % 2 == 0:
                even_sum += int(num[i])
            if i % 2 == 1:
                odd_sum += int(num[i])

        return True if even_sum == odd_sum else False
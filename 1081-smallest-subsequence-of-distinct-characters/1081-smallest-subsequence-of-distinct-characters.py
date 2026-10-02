class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i in s:
            count[i] -= 1
            if i not in stack:
                while stack and stack[-1] > i and count[stack[-1]] > 0 :
                    stack.pop()
                stack.append(i)
        return ''.join(stack)
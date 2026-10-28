class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result = 0
        d = 0
        for i , ch in enumerate(s):
            if ch == '(':
                d += 1
            else:
                d -= 1
                if s[i-1] == '(':
                    result += 1 << d

        return result
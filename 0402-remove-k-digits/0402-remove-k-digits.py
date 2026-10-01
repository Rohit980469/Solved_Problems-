class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for current in num:
            while stack and stack[-1] > current and k > 0:
                stack.pop()
                k -= 1
            stack.append(current)
        
        if k > 0:
            stack = stack[:-k]
            
        x = "".join(stack).lstrip("0")
        return x if x else "0"
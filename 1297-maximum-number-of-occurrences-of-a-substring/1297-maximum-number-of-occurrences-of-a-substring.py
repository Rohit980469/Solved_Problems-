from collections import defaultdict, Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = Counter()
        x = len(s)
        chars = defaultdict(int)
        left = 0

        for ch in range(minSize):
            chars[s[ch]] += 1 

        if len(chars) <= maxLetters:
            counter[s[left:minSize]] += 1
        
        for right in range(minSize,x):
            chars[s[right]] += 1
            chars[s[left]] -= 1
            if chars[s[left]] == 0:
                del chars[s[left]]
            left += 1
            if len(chars) <= maxLetters:
                counter[s[left:right+1]] += 1

        return max(counter.values() , default = 0)
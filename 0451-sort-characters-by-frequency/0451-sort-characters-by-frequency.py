from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_dict = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        new_list = [char*val for char , val in sorted_dict]
        new_s = ''.join(new_list)
        return new_s
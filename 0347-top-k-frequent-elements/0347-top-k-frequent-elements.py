from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        x = sorted(counter.items() , key = lambda x : x[1] , reverse= True)
        return [num for num , time in x[:k]]
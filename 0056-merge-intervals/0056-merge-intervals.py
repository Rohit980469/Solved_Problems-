class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x :x[0])
        result = [intervals[0]]
        for start , end in intervals[1:]:
            lst_str , lst_end = result[-1]
            if start <= lst_end:
                result[-1] = (min(lst_str,start) , max(lst_end , end))
            else :
                result.append([start,end])
        return result
            
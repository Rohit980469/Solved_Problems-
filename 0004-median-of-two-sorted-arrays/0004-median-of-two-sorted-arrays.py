class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mer_arr = sorted(nums1 + nums2)
        
        x = len(mer_arr)
        if x % 2 :
            return float(mer_arr[x // 2])

        return (mer_arr[x // 2] + mer_arr[x // 2 -1]) / 2.0
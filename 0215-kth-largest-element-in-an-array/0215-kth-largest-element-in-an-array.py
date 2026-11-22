class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def build_heap(arr,index):
            n = len(arr) 
            while True:
                left = index * 2 + 1
                right = index * 2 + 2
                largest = index
                if right < n and arr[right] > arr[largest]:
                    largest = right
                if left < n and arr[left] > arr[largest]:
                    largest = left

                if largest != index:
                    arr[largest] , arr[index] = arr[index] , arr[largest]
                    index = largest
                else:
                    break
            return arr

        self.x = 0
        def deletion():
            n = len(nums)
            if n < 1:
                return -1 
            a = nums[0]
            self.x += 1
            if self.x == k:
                return a
            nums[0] = nums[-1]
            nums.pop()
            index = 0
            while index * 2 + 1 < len(nums):
                left = index * 2 + 1
                right = index * 2 + 2
                largest = index
                if right < len(nums) and nums[right] > nums[largest]:
                    largest = right
                if left < len(nums) and nums[left] > nums[largest]:
                    largest = left
                if largest != index:
                    nums[largest] , nums[index] = nums[index] , nums[largest]
                    index = largest
                else:
                    break

        for i in range(len(nums)// 2 - 1 , -1 , -1):
            build_heap(nums,i)

        for i in range(k):
            r = deletion()

        return r
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        def build_heap(arr,index):
            n = len(arr)
            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                largest = index
                if right < n and arr[right] > arr[largest]:
                    largest = right
                if left < n and arr[left] > arr[largest]:
                    largest = left 
                if largest != index:
                    arr[index] , arr[largest] = arr[largest] , arr[index]
                    index = largest
                else:
                    break
            return arr

        def insert(number):
            stones.append(number)
            index = len(stones) - 1
            while index  > 0:
                parent_index = (index - 1) // 2 
                if stones[parent_index] < stones[index]: 
                    stones[index], stones[parent_index] = stones[parent_index], stones[index]
                    index = parent_index
                else:
                    break

        def deletion():
            x = stones[0]
            stones[0] = stones[-1]
            stones.pop()
            index = 0
            while index * 2 + 1 < len(stones):
                left = index * 2 + 1 
                right = index * 2 + 2 
                largest = left
                if right < len(stones) and stones[right] > stones[largest]:
                    largest = right
                if stones[index] < stones[largest]:
                    stones[index] , stones[largest] = stones[largest] , stones[index]
                    index = largest
                else:
                    break
            return x
        for i in range(len(stones) // 2 -1 , -1 , -1):
            build_heap(stones,i)

        while len(stones) > 1:
            a = deletion()
            b = deletion()
            if a!=b:
                insert(abs(a-b))
        return stones[0] if stones else 0
from typing import List
import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 0
            numMap[num] += 1

        mapKeys = list(numMap.keys())
        n = len(mapKeys)
        if k > n: 
            return mapKeys

        heap = []
        for i in range(k):
            j = len(heap)
            heap.append(mapKeys[i])
            l = math.floor((j-1)/2)
            while l > -1 and numMap[heap[l]] > numMap[heap[j]]:
                # we need to swap
                heap[j], heap[l] = heap[l], heap[j]
                j = l
                l = math.floor((j-1)/2)
        
        for i in range(k, n):
            if numMap[heap[0]] < numMap[mapKeys[i]]:
                # we need to swap the values
                heap[0] = mapKeys[i]
                j = 0
                while j*2+1 < len(heap):
                    left = numMap[heap[j*2+1]]
                    if j*2+2 < len(heap):
                        right = numMap[heap[j*2+2]]
                    else:
                        right = left + 1
                    if left < right:
                        if left < numMap[heap[j]]:
                            # we need to swap
                            heap[j], heap[j*2+1] = heap[j*2+1], heap[j]
                            j = j*2 + 1
                        else: 
                            break
                    else:
                        if right < numMap[heap[j]]:
                            # we need to swap
                            heap[j], heap[j*2+2] = heap[j*2+2], heap[j]
                            j = j*2 + 2
                        else: 
                            break

        return heap

            

sol = Solution()
print(sol.topKFrequent([4,1,-1,2,-1,2,3], 2))
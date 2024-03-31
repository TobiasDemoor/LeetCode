from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # parameters attributes
        n = len(nums)

        # process variables
        start = 0
        end = 0
        minNum = float('inf')
        maxNum = float('-inf')
        posMin = 0
        posMax = 0
        count = 0
        while end < n:
            if nums[end] <= minNum:
                if nums[end] < minK:
                    end += 1
                    start = end
                    minNum = float('inf')
                    maxNum = float('-inf')
                    continue
                minNum = nums[end]
                posMin = end
            if nums[end] >= maxNum:
                if nums[end] > maxK:
                    end += 1
                    start = end
                    minNum = float('inf')
                    maxNum = float('-inf')
                    continue
                maxNum = nums[end]
                posMax = end
            if minNum == minK and maxNum == maxK:
                count += 1 + min(posMin, posMax) - start
            end += 1

        return count
                    
                



sol = Solution()
print(sol.countSubarrays([1,3,5,2,7,5], 1,5))
print(sol.countSubarrays([1,1,1,1], 1,1))
print(sol.countSubarrays([2,1,3,5,2,7,5], 1,5))
print(sol.countSubarrays([934372,927845,479424,49441,17167,17167,65553,927845,17167,927845,17167,425106,17167,927845,17167,927845,251338,17167], 17167, 927845))
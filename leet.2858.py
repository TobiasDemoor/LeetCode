from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # parameters attributes
        n = len(nums)

        # process variables
        start = 0
        end = 0
        numberPos = {}
        maxLength = 0
        while end < n:
            if nums[end] not in numberPos:
                numberPos[nums[end]] = []
            else:
                if len(numberPos[nums[end]]) == k:
                    # store if this is the maximum length
                    maxLength = max(maxLength, end - start)
                    # remove the first occurence of the number and update count
                    oldStart = start
                    start = numberPos[nums[end]][0] + 1
                    for i in range(oldStart, start):
                        numberPos[nums[i]].pop(0)
                if nums[end] not in numberPos:
                    numberPos[nums[end]] = []
            numberPos[nums[end]].append(end)
            end += 1
        maxLength = max(maxLength, end - start)
        return maxLength
                    
                



sol = Solution()
print(sol.maxSubarrayLength([1], 1))
print(sol.maxSubarrayLength([1,1,1,1,1,3], 4))
print(sol.maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
print(sol.maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
print(sol.maxSubarrayLength([5,5,5,5,5,5,5], 4))
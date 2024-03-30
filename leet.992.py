from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # parameters attributes
        n = len(nums)

        # process variables
        start = 0
        end = 0
        numberPos = {}
        result = 0
        while end < n:
            if nums[end] not in numberPos:
                numberPos[nums[end]] = end
                if len(numberPos) == k:
                    result += 1 + min(numberPos.values()) - start
                    end += 1
                    while end < n and nums[end] in numberPos:
                        numberPos[nums[end]] = end
                        result += 1 + min(numberPos.values()) - start
                        end += 1
                    start = min(numberPos.values()) + 1
                    end -= 1
                    del numberPos[nums[start - 1]]
            else:
                numberPos[nums[end]] = end
            end += 1
        return result
                    
                



sol = Solution()
print(sol.subarraysWithKDistinct([1,2,1,2,3], 2))
print(sol.subarraysWithKDistinct([1,2,1,3,4], 3))
print(sol.subarraysWithKDistinct([1,2], 1))
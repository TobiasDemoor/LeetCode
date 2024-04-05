from typing import List

class Solution:
    # we are going to think of this as "the longest subarray that contains at most k zeroes"
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        zeroCount = 0
        while zeroCount < k and j < n:
            if nums[j] == 0:
                zeroCount += 1
            j += 1
        maxLength = j - i
        while j < n:
            if nums[j] == 0:
                # we've reached the limit
                if zeroCount == k:
                    # we search for a zero
                    while i < j and nums[i] != 0:
                        i += 1
                    i += 1
                else:
                    zeroCount += 1
                    maxLength = max(maxLength, j - i + 1)
            else:
                maxLength = max(maxLength, j - i + 1)
            j += 1

        return maxLength
        
sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(sol.longestOnes([0,0,0,1,1,1], 0))
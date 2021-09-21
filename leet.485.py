from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                maxOnes = max(maxOnes, count)
                count = 0
        return max(maxOnes, count)
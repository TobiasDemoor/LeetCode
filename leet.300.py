from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            auxMax = 0
            for i, v in enumerate(dp):
                if nums[i] < n and v > auxMax:
                    auxMax = v
            dp.append(auxMax+1)
        return max(dp)

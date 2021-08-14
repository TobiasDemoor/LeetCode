from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            compl = target-n
            if compl in hashMap:
                return [hashMap[compl], i]
            hashMap[n] = i
        raise Exception("No solution found")

from typing import List
import collections
from math import comb

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        sames = collections.Counter(nums)
        total = 0

        for k in sames.keys():
            total += pow(2, sames[k]) - 1 - sames[k] - comb(sames[k], 2)

        prev = []
        for i in range(n):
            current = {}
            for j in range(i):
                delta = nums[i] - nums[j]

                if delta == 0:
                    continue
                    
                if delta not in current:
                    current[delta] = [0,0]

                current[delta][0] += 1 # add new length 2 subsequence

                if delta in prev[j]:
                    current[delta][1] += prev[j][delta][0] + prev[j][delta][1]
                
            for delta in current.keys():
                total += current[delta][1]
            prev.append(current)
        return total



from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minM = m
        minN = n
        for op in ops:
            minM = min(minM, op[0])
            minN = min(minN, op[1])
        return minM*minN

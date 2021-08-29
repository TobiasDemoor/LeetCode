from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        counter = 0
        coverage = 0
        for i in nums:
            while coverage < n and i > coverage+1:
                counter += 1
                coverage += coverage + 1
            coverage += i
            if coverage >= n:
                break
        while coverage < n:
            counter += 1
            coverage += coverage + 1
        return counter
        
                
sol = Solution()
assert sol.minPatches([1,7,21,31,34,37,40,43,49,87,90,92,93,98,99],12) == 2
assert sol.minPatches([1,2,31,33],2147483647) == 28

from typing import List
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j: return 0

            count = 1
            l = i + 1
            while l <= j and boxes[l] == boxes[l-1]:
                l += 1
                count += 1
            
            ans = dp(l, j, 0) + (k+count)**2

            for m in range(l, j+1):
                if boxes[m] == boxes[i]:
                    ans = max(ans, dp(l, m-1, 0) + dp(m, j, k+count))
            return ans

        return dp(0, len(boxes)-1, 0)


sol = Solution()
assert sol.removeBoxes([1,3,2,2,2,3,4,3,1]) == 23,  "Failed with [1,3,2,2,2,3,4,3,1]"
assert sol.removeBoxes([1,1,1]) == 9,  "Failed with [1,1,1]"
assert sol.removeBoxes([1]) == 1,  "Failed with [1]"


from typing import List
from functools import lru_cache


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        minesSet = set((x, y) for x, y in mines)
        dpLeft = []
        dpRight = []
        dpUp = []
        dpDown = []
        for _ in range(n):
            dpLeft.append([0]*n)
            dpRight.append([0]*n)
            dpUp.append([0]*n)
            dpDown.append([0]*n)

        for i in range(n):
            for j in range(n):
                if (i,j) not in minesSet:
                    dpLeft[i][j] = 1 +  (dpLeft[i-1][j] if i > 0 else 0)
                    dpUp[i][j] = 1 +  (dpUp[i][j-1] if j > 0 else 0)

        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i,j) not in minesSet:
                    dpRight[i][j] = 1 +  (dpRight[i+1][j] if i < n-1 else 0)
                    dpDown[i][j] = 1 +  (dpDown[i][j+1] if j < n-1 else 0)
                    ans = max(ans, min(dpLeft[i][j], dpRight[i][j], dpUp[i][j], dpDown[i][j]))
        return ans

sol = Solution()
print(sol.orderOfLargestPlusSign(2, [[0,0],[0,1],[1,0]]))

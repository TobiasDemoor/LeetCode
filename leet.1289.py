from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(1,n):
            # find min
            minVal = grid[i-1][0]
            minPos = 0
            for j in range(1,n):
                if grid[i-1][j] < minVal:
                    minVal = grid[i-1][j]
                    minPos = j
            for j in range(minPos):
                grid[i][j] += minVal
            grid[i][minPos] += min(grid[i-1][:minPos] + grid[i-1][minPos+1:])
            for j in range(minPos + 1, n):
                grid[i][j] += minVal
        return min(grid[-1])

sol = Solution()
assert(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 13)
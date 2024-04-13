from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        height = [0] * (cols + 1)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            stack = []
            for i in range(cols + 1):
                while stack and height[stack[-1]] > height[i]:
                    j = stack.pop()
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, height[j] * width)
                stack.append(i)

        return maxArea

sol = Solution()
print(sol.maximalRectangle([["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]))
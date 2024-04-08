from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stackTop = stack.pop()
                result[stackTop] = i - stackTop
            stack.append(i)
        return result
    
sol = Solution()
print(sol.dailyTemperatures([99,73,74,75,71,69,72,76,73,73,74,75,71,69,72,76,73,73,74,75,71,69,72,76,73,73,74,75,71,69,72,76,73,73,74,75,71,69,72,76,73,100]))
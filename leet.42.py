from typing import List

class Solution:
    # monotonic stack
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and stack[-1][1] <= h:
                _, h2 = stack.pop()
                if stack:
                    j, h3 = stack[-1]
                    res += (i-j-1)*(min(h, h3)-h2)
            stack.append((i, h))
        return res

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([0,1,0,2,1,0,1,4,0,2,1,2,1])) # 8
print(sol.trap([4,2,0,3,2,5])) # 9
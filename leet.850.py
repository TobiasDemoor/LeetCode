from typing import List, Tuple
import bisect

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        events = []
        for x0, y0, x1, y1 in rectangles:
            bisect.insort(events, (x0, 0, y0, y1)) # insert open event ordered
            bisect.insort(events, (x1, 1, y0, y1)) # insert close event ordered
        
        def areaIncrement(openIntervals: List[Tuple[int, int]], inc: int) -> int:
            prev = float("-inf")

            length = 0
            for y0, y1 in openIntervals:
                if y1 > prev:
                    prev = max(prev, y0)
                    length += y1 - prev
                    prev = y1
            return length * inc

        area = 0
        prev = events[0][0]
        openIntervals = []
        for curr, eType, y0, y1 in events:
            area += areaIncrement(openIntervals, curr-prev)
            if eType == 1:
                openIntervals.remove((y0, y1))
            else:
                bisect.insort(openIntervals, (y0, y1))
            prev = curr
        return area % MOD

sol = Solution()
print(sol.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))

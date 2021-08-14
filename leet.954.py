from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        s = []
        arr.sort()
        for n in arr:
            if n < 0:
                target = n*2
            else:
                target = n/2.0
            if target in s:
                s.remove(target)
            else:
                s.append(n)
        
        return len(s) == 0

sol = Solution()
import time
init = time.time()
for i in range(10000):
    assert sol.canReorderDoubled([3,1,3,6]) == False
    assert sol.canReorderDoubled([2,1,2,6]) == False
    assert sol.canReorderDoubled([4,-2,2,-4]) == True
    assert sol.canReorderDoubled([2,2,4,4]) == True
    assert sol.canReorderDoubled([1,2,4,16,8,4]) == False
    assert sol.canReorderDoubled([1,2,4,16,8,32]) == True
print(time.time() - init)
print(sol.canReorderDoubled([3,1,3,6]))
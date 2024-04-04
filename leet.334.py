from typing import List
import time

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

sol = Solution()
print(sol.increasingTriplet([1,2,3,4,5]))
print(sol.increasingTriplet([2,1,5,0,4,6]))
print(sol.increasingTriplet([1,5,0,2,4,1,3]))
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = math.floor(math.sqrt(c))
        for i in range(limit+1):
            if math.sqrt(c-i**2).is_integer():
                return True
        return False


sol = Solution()
assert sol.judgeSquareSum(2) == True
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            if (a & 1) | (b & 1) != c & 1:
                if c & 1 == 1:
                    count += 1
                else: 
                    count += (a & 1) + (b & 1)
            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return count

sol = Solution()
print(sol.minFlips(256, 6, 5))
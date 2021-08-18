from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def recursive(s: str) -> int:
            if s.startswith("0"): return 0
            if len(s) <= 1: return 1

            result = 0
            for i in range(1, 3):
                if int(s[:i]) <= 26:
                    result += recursive(s[i:])

            return result

        return recursive(s)

sol = Solution()

assert sol.numDecodings("11106") == 2
assert sol.numDecodings("12") == 2
assert sol.numDecodings("226") == 3
assert sol.numDecodings("0") == 0
assert sol.numDecodings("06") == 0
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        maxLen = 1
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            for j in dp[max(0, curr-k):curr+k+1]:
                dp[curr] = max(dp[curr], j + 1)
            maxLen = max(maxLen, dp[curr])
        return maxLen

sol = Solution()
assert(sol.longestIdealString("acfgbd", 2) == 4)
assert(sol.longestIdealString("abcfghijkl", 1) == 7)
assert(sol.longestIdealString("eduktdb", 15) == 5)
assert(sol.longestIdealString("lkpkxcigcs", 6) == 7)
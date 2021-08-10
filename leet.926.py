class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip("0").rstrip("1")
        currentSum = s.count("0")
        minSum = currentSum
        for i in range(len(s)):
            if s[i] == "0":
                currentSum -= 1
            else:
                currentSum += 1
            minSum = min(minSum, currentSum)
        return minSum

sol = Solution()
assert sol.minFlipsMonoIncr("000111000111") == 3
assert sol.minFlipsMonoIncr("0") == 0
assert sol.minFlipsMonoIncr("1010001101") == 3
assert sol.minFlipsMonoIncr("1100010110") == 4
assert sol.minFlipsMonoIncr("0000100100") == 2

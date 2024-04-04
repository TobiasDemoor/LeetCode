class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        if n > m:
            str1, str2 = str2, str1
            n, m = m, n
        for i in range(n, 0, -1):
            if n % i == 0 and m % i == 0 and str1[:i] * (n // i) == str1 and  str1[:i] * (m // i) == str2:
                return str1[:i]
        return ''

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("ABABABAB", "ABAB"))
print(sol.gcdOfStrings("ABABCCC", "ABAB"))

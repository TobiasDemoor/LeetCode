from typing import Counter


class Solution:
    def containsAllChars(self, counterS: Counter, counterT: Counter) -> bool:
        for c in counterT:
            if c not in counterS or counterT[c] > counterS[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        i = 0 
        j = n
        minSubstr = ""
        counterS = Counter(s)
        counterT = Counter(t)

        while i >= 0:
            if self.containsAllChars(counterS, counterT):
                minSubstr = s[i:j]
                counterS[s[i]] -= 1
                i += 1
            else:
                i -= 1
                j -= 1
                counterS[s[i]] += 1
                counterS[s[j]] -= 1
                
        return minSubstr

sol = Solution()
assert sol.minWindow( s = "ADOBECODEBANC", t = "ABC") == "BANC"
assert sol.minWindow( s = "a", t = "a") == "a"
assert sol.minWindow( s = "a", t = "aa") == ""



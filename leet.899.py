class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            minS = s
            for i in range(len(s)):
                current = s[i:] + s[:i]
                if current < minS:
                    minS = current
            return minS
        return "".join(sorted(s))


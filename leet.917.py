class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst = []
        for c in s:
            if "a" <= c <= "z" or "A" <= c <= "Z":
                lst.append(c)
        
        for i, c in enumerate(s):
            if "a" <= c <= "z" or "A" <= c <= "Z":
                s = s[:i] + lst.pop() + s[i+1:]
        return s
        # n = len(s)
        # sList = list(s)
        # i, j = 0, n-1
        # while i < j:
        #     if "a" <= sList[i] <= "z" or "A" <= sList[i] <= "Z":
        #         while not("a" <= sList[j] <= "z" or "A" <= sList[j] <= "Z"):
        #             j -= 1
        #         sList[i], sList[j] = sList[j], sList[i]
        #         j -= 1
        #     i += 1
        # return "".join(sList)

sol = Solution()
print(sol.reverseOnlyLetters("ab-cd"))
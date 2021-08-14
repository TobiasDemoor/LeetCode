class Solution(object):
    
    def isPalindrome(self, s, i, j, auxDict):
        l = j - i
        if l == 1:
            return True
        if i in auxDict and j in auxDict[i]:
            return auxDict[i][j]
        else:
            val = s[i] == s[j-1]
            if l > 2 and val:
                val = self.isPalindrome(s, i+1, j-1, auxDict)
            if i not in auxDict:
                auxDict[i] = {}
            auxDict[i][j] = val
            return val

    def minCut(self, s: str) -> int:
        auxDict = {}

        n = len(s)
        aux = list(range(n))
        
        for j in range(2,n+1):
            if self.isPalindrome(s, 0, j, auxDict):
                aux[j-1] = 0
            else:
                for i in range(1,j):
                    if self.isPalindrome(s, i, j, auxDict):
                        aux[j-1] = min(aux[j-1], aux[i-1] + 1)

        return aux[-1]


sol = Solution()
print(sol.minCut("aab"))
print(sol.minCut("abb"))
print(sol.minCut("aaaaba"))
print(sol.minCut("a"))
print(sol.minCut("ab"))
print(sol.minCut("aaa"))
print(sol.minCut("abacdc"))
print(sol.minCut("abacdcbbb"))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        aux = s.rstrip()
        return len(aux) - aux.rfind(' ') - 1
    
sol = Solution()
print(sol.lengthOfLastWord("World"))
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   Hello   World moon  "))
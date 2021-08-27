from typing import List
import re


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def genRegexPattern(s:str) -> str:
            return ".*"+".*".join(s)+".*"
        strs.sort(key=len)
        dp = [[strs[0]]]
        for i in range(1, len(strs)):
            string = strs[i]
            lusList = []
            for s in dp[i-1]:
                if not bool(re.match(genRegexPattern(s), string)):
                    lusList.append(s)
            j = i-1
            l = len(string)
            regex = genRegexPattern(string)
            while j > -1 and len(strs[j]) == l and not bool(re.match(regex, strs[j])):
                j -= 1
            if j == -1 or len(strs[j]) < l:
                lusList.append(string)
            dp.append(lusList)
        
        print(dp)
        if len(dp[-1]) == 0:
            return -1
        
        return len(dp[-1][-1])
        
            

sol = Solution()
sol.findLUSlength(["abcd", "axxbxc"])
            

                

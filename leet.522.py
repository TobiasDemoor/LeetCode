from typing import List
import re


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len)
        lusList = [strs[0]]
        for i in range(1, len(strs)):
            string = strs[i]
            lusList = list(filter(lambda s: not bool(re.match(".*"+".*".join(s)+".*", string)), lusList))
            j = i-1
            l = len(string)
            while j > -1 and len(strs[j]) == l and not strs[j] == string:
                j -= 1
            if j == -1 or len(strs[j]) < l:
                lusList.append(string)

        if len(lusList) == 0:
            return -1

        return len(lusList[-1])


sol = Solution()
sol.findLUSlength(["abcd", "axxbxc"])

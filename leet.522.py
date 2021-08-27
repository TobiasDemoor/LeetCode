from typing import List
import re


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len)
        last = [strs[0]]
        for i in range(1, len(strs)):
            string = strs[i]
            lusList = []
            for s in last:
                if not bool(re.match(".*"+".*".join(s)+".*", string)):
                    lusList.append(s)
            j = i-1
            l = len(string)
            while j > -1 and len(strs[j]) == l and not strs[j] == string:
                j -= 1
            if j == -1 or len(strs[j]) < l:
                lusList.append(string)
            last = lusList

        if len(last) == 0:
            return -1

        return len(last[-1])


sol = Solution()
sol.findLUSlength(["abcd", "axxbxc"])

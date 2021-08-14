from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            representative = "".join(sorted(s))
            if representative not in groups:
                groups[representative] = []
            groups[representative].append(s)
            
        return list(groups.values())

sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])


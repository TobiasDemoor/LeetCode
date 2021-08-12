class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            representative = "".join(sorted(s))
            if representative not in groups:
                groups[representative] = []
            groups[representative].append(s)
            
        return list(groups.values())

sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])


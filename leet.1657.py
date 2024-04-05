class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        list1 = [ c for c in word1 ]
        list2 = [ c for c in word2 ]

        countMap1 = { }
        for c in list1:
            if c not in countMap1:
                countMap1[c] = 0
            countMap1[c] += 1

        countMap2 = { }
        for c in list2:
            if c not in countMap2:
                countMap2[c] = 0
            countMap2[c] += 1
        
        if countMap1.keys() != countMap2.keys(): return False
        countList1 = list(countMap1.values())
        countList2 = list(countMap2.values())
        countList1.sort()
        countList2.sort()
        if countList1 != countList2: return False

        return True

sol = Solution()
print
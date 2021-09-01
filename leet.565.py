from typing import List


# using DSU
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        rank = [1] * n
        parent = list(range(n))

        def find(x):
            if parent[x] == x: return x
            p = find(parent[x])
            parent[x] = p
            return p

        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                parent[y] = x
                rank[x] += rank[y]

        for i, n in enumerate(nums):
            union(i, n)
        return max(rank)


sol = Solution()
assert sol.arrayNesting([5,4,0,3,1,6,2]) == 4
assert sol.arrayNesting([0,1,2]) == 1

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n < 4:
            return trees

        def orient(p: List[int], q: List[int], r: List[int]) -> float:
            dif = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
            return dif

        def coLinear(p: List[int], q: List[int], r: List[int]):
            return q[0] >= min(p[0], r[0]) and q[0] <= max(p[0], r[0]) \
                and q[1] >= min(p[1], r[1]) and q[1] <= max(p[1], r[1])
        border = set()
        l = min(range(n), key=lambda i: trees[i][0])
        p = l
        while True:
            border.add(p)
            q = (p+1) % n
            for i in range(n):
                if orient(trees[p], trees[i], trees[q]) < 0:
                    q = i
            for i in range(n):
                if i != p and i != q and orient(trees[p], trees[i], trees[q]) == 0 \
                    and coLinear(trees[p], trees[i], trees[q]):
                    border.add(i)
            p = q
            if p == l:
                break
        
        return [trees[i] for i in border]

sol = Solution()
print(sol.outerTrees([[1,2],[2,2],[4,2],[5,2],[6,2]]))
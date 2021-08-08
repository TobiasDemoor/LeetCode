class Solution(object):
    def find(self, x, parent):
        if parent[x] == x: return x
        p = self.find(parent[x], parent)
        parent[x] = p
        return p

    def union(self, x, y, parent, rank):
        x = self.find(x, parent)
        y = self.find(y, parent)
        if rank[x] > rank[y]:
            parent[y] = x
            rank[x] += rank[y]
        else:
            parent[x] = y
            rank[y] += rank[x]

    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n+1))
        rank = [1] * (n+1)

        for i in range(threshold+1, n+1):
            for mul in range(i, n+1, i):
                self.union(i, mul, parent, rank)
        
        result = []
        for query in queries:
            [x, y] = query
            result.append(self.find(x, parent) == self.find(y, parent))
        return result


sol = Solution()
print(sol.areConnected(6, 2, [[1, 4], [2, 5], [3, 6]]))
print(sol.areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]))

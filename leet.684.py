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

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n+1)
        result = None
        for edge in edges:
            [x, y] = edge
            if self.find(x, parent) == self.find(y, parent):
                result = edge
            else:
                self.union(x, y, parent, rank)
        return result

sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

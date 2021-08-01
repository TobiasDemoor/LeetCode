class Solution(object):
    def defineIsland(self, grid, id, hashMap, i, j, n):
        if grid[i][j] == 1:
            hashMap[id] += 1
            grid[i][j] = id
            if i > 0:
                self.defineIsland(grid, id, hashMap, i-1, j, n)
            if i < n-1:
                self.defineIsland(grid, id, hashMap, i+1, j, n)
            if j > 0:
                self.defineIsland(grid, id, hashMap, i, j-1, n)
            if j < n-1:
                self.defineIsland(grid, id, hashMap, i, j+1, n)

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        # first define existing islands and their sizes
        initMax = 0
        last = 1
        hashMap = {0: 0}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    last += 1
                    hashMap[last] = 0
                    self.defineIsland(grid, last, hashMap, i, j, n)
                    initMax = max(initMax, hashMap[last])

        print(hashMap, grid)
        # then iterate over zeros and find max
        result = initMax
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    islands = []
                    if i > 0:
                        islands.append(grid[i-1][j])
                    if i < n-1:
                        islands.append(grid[i+1][j])
                    if j > 0:
                        islands.append(grid[i][j-1])
                    if j < n-1:
                        islands.append(grid[i][j+1])
                    local = 1 + sum([hashMap[id] for id in set(islands)])
                    result = max(result, local)
        return result


sol = Solution()
print(sol.largestIsland(
    [[0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 0, 1, 0]]))  # 7
print(sol.largestIsland(
    [[1,1],[1,1]])) # 4
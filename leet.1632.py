from typing import List


class Solution(object):
    def find(self, pair, parent):
        i, j = pair
        if parent[i][j] == pair:
            return pair
        p = self.find(parent[i][j], parent)
        parent[i][j] = p
        return p

    def union(self, x, y, parent, rank):
        x = self.find(x, parent)
        xi, xj = x
        y = self.find(y, parent)
        yi, yj = y
        if rank[xi][xj] > rank[yi][yj]:
            parent[yi][yj] = x
            rank[xi][xj] += rank[yi][yj]
        else:
            parent[xi][xj] = y
            rank[yi][yj] += rank[xi][xj]

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # init all required structures
        parent = []
        rank = []
        resultMat = []
        setMat = []
        for i in range(m):
            auxParent = []
            auxRank = []
            auxResultMat = []
            auxSetMat = []
            for j in range(n):
                auxParent.append((i,j))
                auxRank.append(1)
                auxResultMat.append(0)
                auxSetMat.append([])
            parent.append(auxParent)
            rank.append(auxRank)
            resultMat.append(auxResultMat)
            setMat.append(auxSetMat)

        # create DSU rows
        for i in range(m):
            hashMap = {}
            for j in range(n):
                val = matrix[i][j]
                if val in hashMap:
                    self.union((i,j), hashMap[val], parent, rank)
                else:
                    hashMap[val] = (i,j)
        
        # create DSU columns
        for j in range(n):
            hashMap = {}
            for i in range(m):
                val = matrix[i][j]
                if val in hashMap:
                    self.union((i,j), hashMap[val], parent, rank)
                else:
                    hashMap[val] = (i,j)
        
        cells = []
        for i in range(m):
            for j in range(n):
                xi, xj = self.find((i,j), parent)
                if (xi, xj) == (i, j):
                    cells.append((i,j))
                setMat[xi][xj].append((i,j))
        
        cells.sort(key=lambda cell: matrix[cell[0]][cell[1]])
        row = [0] * m
        col = [0] * n
        for cell in cells:
            rank = 1
            ci, cj = cell
            for i, j in setMat[ci][cj]:
                rank = max(rank, row[i]+1, col[j]+1)
            for i, j in setMat[ci][cj]:
                resultMat[i][j] = rank
                row[i] = rank
                col[j] = rank
        return resultMat


sol = Solution()
print(sol.matrixRankTransform([[1, 2], [3, 4]]))
print(sol.matrixRankTransform([[7, 7], [7, 7]]))
print(sol.matrixRankTransform(
    [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]))
print(sol.matrixRankTransform([[7, 3, 6], [1, 4, 5], [9, 8, 2]]))
print(sol.matrixRankTransform(
    [[-37, -50, -3, 44], [-37, 46, 13, -32], [47, -42, -3, -40], [-17, -22, -39, 24]]))

# [-37, -50, -3, 44]
# [-37, 46, 13, -32]
# [47, -42, -3, -40]
# [-17, -22, -39, 24]

# [2, 1, 3, 6]
# [2, 6, 5, 4]
# [5, 2, 4, 3]
# [4, 3, 1, 5]

# [2, 1, 4, 6]
# [2, 6, 5, 4]
# [5, 2, 4, 3]
# [4, 3, 1, 5]

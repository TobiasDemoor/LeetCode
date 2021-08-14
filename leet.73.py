from typing import List


# Solution 1: minimum memory attempt
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # position 0,0 has to encode more information than the other cells
        if matrix[0][0] == 0:
            matrix[0][0] = "HV"
        else:
            for j in range(1, n):
                if matrix[0][j] == 0:
                    matrix[0][0] = "H"
                    break
            for i in range(1, m):
                if matrix[i][0] == 0:
                    if matrix[0][0] == "H":
                        matrix[0][0] = "HV"
                    else:
                        matrix[0][0] = "V"
                    break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        val = matrix[0][0]
        print(matrix)
        if type(val) == str:
            if "V" in val:
                for i in range(m):
                    matrix[i][0] = 0
            if "H" in val:
                matrix[0] = [0]*n

# Solution 2: faster and simpler
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [False]*m
        cols = [False]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(m):
            if rows[i]:
                matrix[i] = [0]*n
        for j in range(n):
            if cols[j]:
                for i in range(m):
                    matrix[i][j] = 0



sol = Solution()
matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
sol.setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)

matrix = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]
sol.setZeroes(matrix)
print(matrix)
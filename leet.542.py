from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        rMat = []
        complete = True
        for i in range(m):
            aux = []
            for j in range(n):
                if mat[i][j] == 0:
                    aux.append(0)
                else:
                    aux.append(-1)
                    complete = False
            rMat.append(aux)
        count = 1
        lastCount = 0
        while not complete:
            complete = True
            for i in range(m):
                for j in range(n):
                    if rMat[i][j] == -1:
                        if (i > 0 and rMat[i-1][j] == lastCount) or (i < m-1 and rMat[i+1][j] == lastCount) or \
                            (j > 0 and rMat[i][j-1] == lastCount) or (j < n-1 and rMat[i][j+1] == lastCount):
                            rMat[i][j] = count
                        else:
                            complete = False
            count += 1
            lastCount = count-1
        return rMat


sol = Solution()
print(sol.updateMatrix([[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0]]))

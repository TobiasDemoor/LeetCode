from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        bottomM, topM = 0, len(matrix)-1
        bottomN, topN = 0, len(matrix[0])-1

        result = []
        while True:

            for j in range(bottomN, topN + 1):
                result.append(matrix[bottomM][j])
            
            bottomM += 1
            if bottomM > topM:
                break

            for i in range(bottomM, topM + 1):
                result.append(matrix[i][topN])
            
            topN -= 1
            if bottomN > topN:
                break

            for j in range(topN, bottomN - 1, -1):
                result.append(matrix[topM][j])
            
            topM -= 1
            if bottomM > topM:
                break

            for i in range(topM, bottomM - 1, -1):
                result.append(matrix[i][bottomN])
            
            bottomN += 1
            if bottomN > topN:
                break
        
        return result

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]
))
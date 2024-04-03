from typing import List

class Solution:
    def recursiveSol(self, board: List[List[str]], word: str, m: int, n: int, l: int, i: int, j: int, k: int, indexesP: List[int]) -> bool:
        indexes = indexesP.copy()
        indexes.append((i,j))
        if k == l:
            return True
        if i > 0 and board[i-1][j] == word[k]:
            if (i-1,j) not in indexes:
                sol = self.recursiveSol(board, word, m, n, l, i-1, j, k+1, indexes)
                if sol:
                    return True
        if i < m-1 and board[i+1][j] == word[k]:
            if (i+1,j) not in indexes:
                sol = self.recursiveSol(board, word, m, n, l, i+1, j, k+1, indexes)
                if sol:
                    return True
        if j > 0 and board[i][j-1] == word[k]:
            if (i,j-1) not in indexes:
                sol = self.recursiveSol(board, word, m, n, l, i, j-1, k+1, indexes)
                if sol:
                    return True
        if j < n-1 and board[i][j+1] == word[k]:
            if (i,j+1) not in indexes:
                sol = self.recursiveSol(board, word, m, n, l, i, j+1, k+1, indexes)
                if sol:
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        i = 0  # row pointer
        while i < m:
            j = 0  # column pointer
            while j < n:
                if board[i][j] == word[0]:
                    sol = self.recursiveSol(board, word, m, n, l, i, j, 1, [])
                    if sol:
                        return True
                j += 1
            i += 1

        return False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
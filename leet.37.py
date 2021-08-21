from typing import List


class Solution:
    def isPossible(self, board: List[List[str]], i: int, j: int, n: int):
        aux = str(n)
        for x in range(9):
            if aux == board[i][x] or aux == board[x][j]:
                return False
        i0 = (i//3)*3
        j0 = (j//3)*3
        for x in range(3):
            for y in range(3):
                if aux == board[i0+x][j0+y]:
                    return False
        return True

    def recursive(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for n in range(1, 10):
                        if self.isPossible(board, i, j, n):
                            board[i][j] = str(n)
                            self.recursive(board)
                            if self.solved:
                                return
                            board[i][j] = "."
                    return
        self.solved = True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solved = False
        self.recursive(board)


sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol.solveSudoku(board)
print(board)

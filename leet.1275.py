from typing import List
import collections

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["-"]*3, ["-"]*3, ["-"]*3]
        players = collections.deque(["A", "B"])
        for x, y in moves:
            board[x][y] = players[0]
            players.rotate()
        
        # check rows
        for i in range(3):
            if board[i][0] != "-" and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
        
        # check columns
        for j in range(3):
            if board[0][j] != "-" and board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
        
        # check diags
        if board[0][0] != "-" and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]

        if board[0][2] != "-" and board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

        return "Draw" if len(moves) == 9 else "Pending"
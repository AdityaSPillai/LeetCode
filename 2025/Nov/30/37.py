class Solution:
    def solveSudoku(self, board):
        rowUsed = [[False]*10 for _ in range(9)]
        colUsed = [[False]*10 for _ in range(9)]
        boxUsed = [[False]*10 for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    d = int(board[r][c])
                    rowUsed[r][d] = True
                    colUsed[c][d] = True
                    boxUsed[(r//3)*3 + (c//3)][d] = True

        def backtrack(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            b = (r//3)*3 + (c//3)
            for d in range(1, 10):
                if not rowUsed[r][d] and not colUsed[c][d] and not boxUsed[b][d]:
                    board[r][c] = str(d)
                    rowUsed[r][d] = colUsed[c][d] = boxUsed[b][d] = True
                    if backtrack(i + 1):
                        return True
                    board[r][c] = "."
                    rowUsed[r][d] = colUsed[c][d] = boxUsed[b][d] = False
            return False
        backtrack(0)
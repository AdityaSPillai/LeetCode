class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Row
        for row in board:
            seen=set()
            for i in row:
                if i==".":
                    continue
                elif i in seen:
                    return False
                seen.add(i)
        #Column
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        #Box
        for box in range(9):
            seen=set()
            for i in range(3):
                r=(box//3)*3+i
                for j in range(3):
                    c=(box%3)*3+j
                    if board[r][c]==".":
                        continue
                    elif board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True
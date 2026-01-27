class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx=[]
        n=len(board[0])
        m=len(board)
        self.found=0
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    idx.append([i,j])
        def backtracking(i,j,subset,indx):
            if not subset:
                self.found=1
                return
            if i+1<m and board[i+1][j]==subset[0] and [i+1,j] not in indx:
                indx.append([i,j])
                backtracking(i+1,j,subset[1:],indx)
                if self.found==1:
                    return
                indx.pop()
            if j+1<n and board[i][j+1]==subset[0] and [i,j+1] not in indx:
                indx.append([i,j])
                backtracking(i,j+1,subset[1:],indx)
                if self.found==1:
                    return
                indx.pop()
            if i-1>=0 and board[i-1][j]==subset[0] and [i-1,j] not in indx:
                indx.append([i,j])
                backtracking(i-1,j,subset[1:],indx)
                if self.found==1:
                    return
                indx.pop()
            if j-1>=0 and board[i][j-1]==subset[0] and [i,j-1] not in indx:
                indx.append([i,j])
                backtracking(i,j-1,subset[1:],indx)
                if self.found==1:
                    return
                indx.pop()
        for i,j in idx:
            backtracking(i,j,word[1:],[[i,j]])
            if self.found==1:
                return True
        return False

#using set
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = []
        n = len(board[0])
        m = len(board)
        self.found = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    idx.append([i, j])

        def backtracking(i, j, subset, indx):
            if not subset:
                self.found = 1
                return
            if i + 1 < m and board[i + 1][j] == subset[0] and (i + 1, j) not in indx:
                indx.add((i, j))
                backtracking(i + 1, j, subset[1:], indx)
                if self.found == 1:
                    return
                indx.remove((i, j))
            if j + 1 < n and board[i][j + 1] == subset[0] and (i, j + 1) not in indx:
                indx.add((i, j))
                backtracking(i, j + 1, subset[1:], indx)
                if self.found == 1:
                    return
                indx.remove((i, j))
            if i - 1 >= 0 and board[i - 1][j] == subset[0] and (i - 1, j) not in indx:
                indx.add((i, j))
                backtracking(i - 1, j, subset[1:], indx)
                if self.found == 1:
                    return
                indx.remove((i, j))
            if j - 1 >= 0 and board[i][j - 1] == subset[0] and (i, j - 1) not in indx:
                indx.add((i, j))
                backtracking(i, j - 1, subset[1:], indx)
                if self.found == 1:
                    return
                indx.remove((i, j))

        for i, j in idx:
            backtracking(i, j, word[1:], set((i, j)))
            if self.found == 1:
                return True
        return False

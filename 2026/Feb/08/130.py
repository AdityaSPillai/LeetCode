class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #Initializing all the needed values
        n,m=len(board),len(board[0])
        o=deque()
        change=set()
        seen=set()

        #Finding location of all the 'O' in the board
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    if i==0 or j==0 or i==n-1 or j==m-1:
                        o.append([i,j])
                    else:
                        change.add((i,j))
        def dfs(i,j):
            if i+1<n and (i+1,j) not in seen and board[i+1][j]=="O" and not (i+1==0 or j==0 or i+1==n-1 or j==m-1):
                seen.add((i+1,j))
                change.remove((i+1,j))
                dfs(i+1,j)
            if i-1>=0 and (i-1,j) not in seen and board[i-1][j]=="O" and not (i-1==0 or j==0 or i-1==n-1 or j==m-1):
                seen.add((i-1,j))
                change.remove((i-1,j))
                dfs(i-1,j)
            if j+1<m and (i,j+1) not in seen and board[i][j+1]=="O" and not (i==0 or j+1==0 or i==n-1 or j+1==m-1):
                seen.add((i,j+1))
                change.remove((i,j+1))
                dfs(i,j+1)
            if j-1>=0 and (i,j-1) not in seen and board[i][j-1]=="O" and not (i==0 or j-1==0 or i==n-1 or j-1==m-1):
                seen.add((i,j-1))
                change.remove((i,j-1))
                dfs(i,j-1)
        while o:
            a,b=o.popleft()
            seen.add((a,b))
            dfs(a,b)
        for i,j in change:
            board[i][j]="X"
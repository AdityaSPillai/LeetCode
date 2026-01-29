class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col,zero,time=len(grid),len(grid[0]),0,-1
        rot=0
        queue=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    zero+=1
                if grid[i][j]==2:
                    rot+=1
                    queue.append([i,j])
        if rot==0:
            return 0 if zero==row*col else -1
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                if r+1<row and grid[r+1][c]!=0 and grid[r+1][c]!=2:
                    grid[r+1][c]=2
                    rot+=1
                    queue.append([r+1,c])
                if r-1>=0 and grid[r-1][c]!=0 and grid[r-1][c]!=2:
                    grid[r-1][c]=2
                    rot+=1
                    queue.append([r-1,c])
                if c+1<col and grid[r][c+1]!=0 and grid[r][c+1]!=2:
                    grid[r][c+1]=2
                    rot+=1
                    queue.append([r,c+1])
                if c-1>=0 and grid[r][c-1]!=0 and grid[r][c-1]!=2:
                    grid[r][c-1]=2
                    rot+=1
                    queue.append([r,c-1])
            time+=1
        return time if zero+rot==row*col else -1
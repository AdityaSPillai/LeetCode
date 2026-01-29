class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row,col=len(isWater),len(isWater[0])
        queue=deque()
        for i in range(row):
            for j in range(col):
                if isWater[i][j]==1:
                    queue.append([i,j])
                else:
                    isWater[i][j]=-1
        d=0
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                isWater[r][c]=d
                if r+1<row and isWater[r+1][c]==-1:
                    queue.append([r+1,c])
                    isWater[r+1][c]=-2
                if r-1>=0 and isWater[r-1][c]==-1:
                    queue.append([r-1,c])
                    isWater[r-1][c]=-2
                if c+1<col and isWater[r][c+1]==-1:
                    queue.append([r,c+1])
                    isWater[r][c+1]=-2
                if c-1>=0 and isWater[r][c-1]==-1:
                    queue.append([r,c-1])
                    isWater[r][c-1]=-2
            d+=1
        return isWater
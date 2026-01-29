class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col=len(mat),len(mat[0])
        queue=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    queue.append([i,j])
                else:
                    mat[i][j]=-1
        d=0
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                mat[r][c]=d
                if r+1<row and mat[r+1][c]==-1:
                    queue.append([r+1,c])
                    mat[r+1][c]=-2
                if r-1>=0 and mat[r-1][c]==-1:
                    queue.append([r-1,c])
                    mat[r-1][c]=-2
                if c+1<col and mat[r][c+1]==-1:
                    queue.append([r,c+1])
                    mat[r][c+1]=-2
                if c-1>=0 and mat[r][c-1]==-1:
                    queue.append([r,c-1])
                    mat[r][c-1]=-2
            d+=1
        return mat
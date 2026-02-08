class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m=len(heights),len(heights[0])
        atlantic,pacific=set(),set()
        at,pa=deque(),deque()
        for i in range(n):
            if (i,m-1) not in atlantic:
                atlantic.add((i,m-1))
                at.append([i,m-1])
        for i in range(m):
            if (n-1,i) not in atlantic:
                atlantic.add((n-1,i))
                at.append([n-1,i])
        for j in range(n):
            if (j,0) not in pacific:
                pacific.add((j,0))
                pa.append([j,0])
        for j in range(m):
                if (0,j) not in pacific:
                    pacific.add((0,j))
                    pa.append([0,j])
        while at:
            i,j=at.popleft()
            if i-1>=0 and heights[i][j]<=heights[i-1][j] and (i-1,j) not in atlantic:
                atlantic.add((i-1,j))
                at.append([i-1,j])
            if i+1<n and heights[i][j]<=heights[i+1][j] and (i+1,j) not in atlantic:
                atlantic.add((i+1,j))
                at.append([i+1,j])
            if j-1>=0 and heights[i][j]<=heights[i][j-1] and (i,j-1) not in atlantic:
                atlantic.add((i,j-1))
                at.append([i,j-1])
            if j+1<m and heights[i][j]<=heights[i][j+1] and (i,j+1) not in atlantic:
                atlantic.add((i,j+1))
                at.append([i,j+1])
        while pa:
            i,j=pa.popleft()
            if i-1>=0 and heights[i][j]<=heights[i-1][j] and (i-1,j) not in pacific:
                pacific.add((i-1,j))
                pa.append([i-1,j])
            if i+1<n and heights[i][j]<=heights[i+1][j] and (i+1,j) not in pacific:
                pacific.add((i+1,j))
                pa.append([i+1,j])
            if j-1>=0 and heights[i][j]<=heights[i][j-1] and (i,j-1) not in pacific:
                pacific.add((i,j-1))
                pa.append([i,j-1])
            if j+1<m and heights[i][j]<=heights[i][j+1] and (i,j+1) not in pacific:
                pacific.add((i,j+1))
                pa.append([i,j+1])
        res=[]
        for i,j in pacific:
            if (i,j) in atlantic:
                res.append([i,j])
        return res
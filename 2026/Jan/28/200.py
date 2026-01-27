class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        visited=set()
        i=0

        def bfs(r,c):
            queue=deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                ro,co=queue.popleft()
                direction=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in direction:
                    r=ro+dr
                    c=co+dc
                    if (c<col and r<row and c>=0 and r>=0 and
                    grid[r][c]=='1' and (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    i+=1
        return i
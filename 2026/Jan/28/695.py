class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rown,coln=len(grid),len(grid[0])
        visited=set()
        maxi=0
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            visited.add((r,c))
            length=1
            while queue:
                ro,co=queue.popleft()
                for dr,dc in direction:
                    row,col=ro+dr,co+dc
                    if (
                        row<rown and
                        col<coln and
                        row>=0 and
                        col>=0 and
                        grid[row][col]==1 and
                        (row,col) not in visited
                    ):
                        queue.append((row,col))
                        visited.add((row,col))
                        length+=1
            return length
        for r in range(rown):
            for c in range(coln):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxi=max(bfs(r,c),maxi)
        return maxi
from typing import List
from collections import deque
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        row,col=len(rooms),len(rooms[0])
        visited=set()
        queue=deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j]==0:
                    visited.add((i,j))
                    queue.append([i,j])
        def addCell(r,c):
            if r<0 or c<0 or r==row or c==col or rooms[r][c]==-1 or (r,c) in visited:
                return
            visited.add((r,c))
            queue.append([r,c])
        d=0
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                rooms[r][c]=d
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            d+=1
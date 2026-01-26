class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        prerotated=mat
        count=0
        while prerotated!=target and count<4:
            rotated=[[0]*n for _ in range(n)]
            col=n-1
            for i in range(n):
                for j in range(n):
                    rotated[j][col]=prerotated[i][j]
                col-=1
            count+=1
            prerotated=rotated
        return True if count<4 else False
                
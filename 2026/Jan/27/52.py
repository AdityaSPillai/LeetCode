class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(i,j,x,y):
            di,dj=i,j
            if i>x:
                while i>x:
                    i-=1
                    j-=1
                    if i==x and j==y:
                        return False
                i,j=di,dj
                while i>x:
                    i-=1
                    j+=1
                    if i==x and j==y:
                        return False
                i,j=di,dj
            else:
                while i<x:
                    i+=1
                    j-=1
                    if i==x and j==y:
                        return False
                i,j=di,dj
                while i<x:
                    i+=1
                    j+=1
                    if i==x and j==y:
                        return False
                i,j=di,dj
            return True
        res=[]
        arr=[i for i in range(n)]
        def backtrack(p,curr):
            if p==n:
                res.append(curr.copy())
                return
            for i in range(n):
                if i in curr:
                    continue
                addi=1
                for j in range(len(curr)):
                    if not check(j,curr[j],p,i):
                        addi=0
                        break
                if addi==1:
                    curr.append(i)
                    backtrack(p+1,curr)
                    curr.pop()
        backtrack(0,[])
        return len(res)
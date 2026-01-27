class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtracking(o,c,subset):
            if o==n and c==n:
                res.append(subset)
                return
            elif o==c:
                subset+='('
                backtracking(o+1,c,subset)
                return
            elif o==n:
                subset+=')'
                backtracking(o,c+1,subset)
                return
            else:
                subset+='('
                backtracking(o+1,c,subset)
                subset=subset[:-1]
                subset+=')'
                backtracking(o,c+1,subset)
                return
        backtracking(1,0,"(")
        return res
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        dtoa={
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
        def backtrack(i,substring):
            if i==-1:
                res.append(substring)
                return
            digit=d[i]
            for j in dtoa[digit]:
                substring+=j
                backtrack(i-1,substring)
                substring=substring[:-1]
        d=[]
        digits=int(digits)
        while digits>0:
            r=digits%10
            digits=digits//10
            d.append(r)
        backtrack(len(d)-1,"")
        return res
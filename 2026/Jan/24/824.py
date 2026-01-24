class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split()
        res=""
        n=len(s)
        for i in range(n):
            a="a"*(i+1)
            if i!=n-1:
                if s[i][0] in "aeiouAEIOU":
                    res=res+(s[i]+"ma"+a+" ")
                else:
                    res=res+(s[i][1:]+s[i][0]+"ma"+a+" ")
            else:
                if s[i][0] in "aeiouAEIOU":
                    res=res+(s[i]+"ma"+a)
                else:
                    res=res+(s[i][1:]+s[i][0]+"ma"+a)
        return res
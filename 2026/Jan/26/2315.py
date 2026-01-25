class Solution:
    def countAsterisks(self, s: str) -> int:
        count=res=0
        for i in s:
            if i=="|":
                if count==0:
                    count=1
                else:
                    count=0
            elif i=="*":
                if count==0:
                    res+=1
        return res
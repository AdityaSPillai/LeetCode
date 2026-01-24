class Solution:
    def maxPower(self, s: str) -> int:
        i=0
        maxi=0
        lens=len(s)
        while i<lens:
            count=1
            while i+1<lens and s[i]==s[i+1]:
                count+=1
                i+=1
            maxi=max(maxi,count)
            i+=1
        return maxi
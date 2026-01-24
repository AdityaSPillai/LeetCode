class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ssum=0
        tsum=0
        for i in s:
            ssum+=ord(i)
        for i in t:
            tsum+=ord(i)
        return chr(tsum-ssum)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)
        nb=count['b']
        na=count['a']
        nl=count['l']//2
        no=count['o']//2
        nn=count['n']
        return min(nb,na,nl,no,nn)
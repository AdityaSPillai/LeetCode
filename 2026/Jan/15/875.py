class Solution:
    def checkRate(self, rate:int, piles:List[int], h:int)->bool:
        t=0
        for i in piles:
            t+=(i+rate-1)//rate
        if t>h:
            return False
        else:
            return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        if h==len(piles):
            return m
        l,r=1,m
        rate=0
        while l<=r:
            mid=l+((r-l)//2)
            if self.checkRate(mid,piles,h):
                rate=mid
                r=mid-1
            else:
                l=mid+1
        return rate
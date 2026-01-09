class Solution(object):
    def countTrapezoids(self, points):
        level={}
        for i in points:
            level[i[1]]=level.get(i[1],0)+1
        l=[]
        mod=10**9+7
        for c in level.values():
            if c >= 2:
                l.append((c*(c-1)//2)%mod)
        if len(l)<=1:
            return 0
        total=0
        running=0
        for p in l:
            total =(total + (p*running)) %mod
            running = (running + p) %mod
        return total
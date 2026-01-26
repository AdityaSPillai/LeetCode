class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=[]
        n=len(score)
        res=[""]*n
        for i in range(n):
            heapq.heappush(s,[-score[i],i])
        v,i=heapq.heappop(s)
        res[i]="Gold Medal"
        if s:
            v,i=heapq.heappop(s)
            res[i]="Silver Medal"
        if s:
            v,i=heapq.heappop(s)
            res[i]="Bronze Medal"
        count=4
        while s:
            v,i=heapq.heappop(s)
            res[i]=str(count)
            count+=1
        return res
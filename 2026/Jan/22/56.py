class Solution:
    def merge(self, intervals: List[List[int]])     :
        heapq.heapify(intervals)
        s,e=heapq.heappop(intervals)
        res=[]
        while intervals:
            i,j=heapq.heappop(intervals)
            if (s<=i and e>=i) or (s<=j and e>=j):
                s=min(s,i)
                e=max(e,j)
            elif e>i:
                res.append([i,j])
            else:
                res.append([s,e])
                s,e=i,j
        res.append([s,e])
        return res
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        res=[]
        heapq.heapify(dist)
        for i in points:
            x,y=i
            d=(x*x)+(y*y)
            heapq.heappush(dist,(d,x,y))
        for i in range(k):
            m=heapq.heappop(dist)
            res.append([m[1],m[2]])
        return res
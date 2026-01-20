class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while stones:
            n=-heapq.heappop(stones)
            if stones:
                m=-heapq.heappop(stones)
                if n==m:
                    continue
                elif n>m:
                    heapq.heappush(stones,m-n)
                else:
                    heapq.heappush(stones,n-m)
            else:
                return n
        return 0
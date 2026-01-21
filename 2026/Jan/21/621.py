class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=[0]*26
        for i in tasks:
            c[ord(i)-ord('A')]+=1
        c = [-x for x in c if x != 0]
        queue=deque()
        heapq.heapify(c)
        time=0
        while queue or c:
            time+=1
            if not c:
                time=queue[0][1]
            if queue and queue[0][1]==time:
                node,temp=queue.popleft()
                heapq.heappush(c,-node)
            if c:
                num=heapq.heappop(c)
                if (-num)-1>0:
                    queue.append([(-num)-1,time+n+1])
        return time
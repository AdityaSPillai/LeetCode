import math
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dist=[]
        selected=[]
        count=0

        for i in range(len(points)):
            x,y=points[i]
            if x<0 and y<0:
                sqsize=-1*min(x,y)
            elif x<0:
                sqsize=max(-x,y)
            elif y<0:
                sqsize=max(x,-y)
            else:
                sqsize=max(x,y)
            heapq.heappush(dist,[sqsize,[x,y],s[i]])
        while dist:
            d,p,a=heapq.heappop(dist)
            x,y=p
            if a not in selected:
                selected.append(a)
                count+=1
                maxdist=d
                currcount=1
                reduces=0
                while dist:
                    if dist[0][0]<=maxdist:
                        if dist[0][2] not in selected:
                            d,p,a=heapq.heappop(dist)
                            selected.append(a)
                            currcount+=1
                            count+=1
                        else:
                            count=count-currcount
                            reduces=1
                            break
                    else:
                        break
                if reduces==1:
                    for i in range(currcount):
                        m=selected.pop()
                    break
            else:
                break
        return len(selected)
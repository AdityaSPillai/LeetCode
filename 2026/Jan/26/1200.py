class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        heapq.heapify(arr)
        s=[]
        res=[]
        mini=10**18
        while arr:
            n=heapq.heappop(arr)
            s.append(n)
            if arr:
                mini=min(mini,(arr[0]-n))
        for i in range(len(s)-1):
            if s[i+1]-s[i]==mini:
                res.append([s[i],s[i+1]])
        return res
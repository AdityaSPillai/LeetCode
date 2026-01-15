class TimeMap:

    def __init__(self):
        self.arr={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key]=[]
        self.arr[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.arr.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            mid=l+((r-l)//2)
            if values[mid][1]<=timestamp:
                res=values[mid][0]
            if timestamp==values[mid][1]:
                return values[mid][0]
            
            if timestamp>values[mid][1]:
                l=mid+1
            else:
                r=mid-1
        return res

#Leetcode Submission
class TimeMap:
    def __init__(self):
        self.arr={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key]=[]
        self.arr[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.arr.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            mid=l+((r-l)//2)
            vn=values[mid][1]
            vv=values[mid][0]
            if vn==timestamp:
                return vv
            if vn<=timestamp:
                res=vv
            if vn>timestamp:
                r=mid-1
            else:
                l=mid+1
        return res
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1,l2={},{}
        for i,v in enumerate(list1):
            l1[v]=i
        mini=10**18
        res=[]
        for i,v in enumerate(list2):
            if v in l1:
                if mini>l1[v]+i:
                    mini=l1[v]+i
                    res=[list2[i]]
                elif mini==l1[v]+i:
                    res.append(list2[i])
        return res
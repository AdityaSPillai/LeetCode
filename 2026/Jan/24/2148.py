class Solution:
    def countElements(self, nums: List[int]) -> int:
        count={}
        mini,maxi=10**18,-10**18
        for i in nums:
            mini=min(mini,i)
            maxi=max(maxi,i)
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        del count[maxi]
        if maxi!=mini:
            del count[mini]
        return sum(count.values())
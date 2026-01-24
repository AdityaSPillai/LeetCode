class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxi=0
        maxe=-1
        for i in count:
            if i%2==0:
                if maxi<count[i]:
                    maxi=count[i]
                    maxe=i
                if maxi==count[i]:
                    if maxe>i:
                        maxe=i
        return maxe
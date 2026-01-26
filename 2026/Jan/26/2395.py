class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumv=set()
        for i in range(len(nums)-1):
            t=nums[i]+nums[i+1]
            if t not in sumv:
                sumv.add(t)
            else:
                return True
        return False
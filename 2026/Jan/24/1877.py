class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        for i in range(int(len(nums)/2)):
            m=nums[i]+nums[-(1+i)]
            maxi=max(maxi,m)
        return maxi
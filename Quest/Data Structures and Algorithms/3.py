class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        maxi=0
        while i<len(nums):
            count=0
            s=nums[i]
            if s==1:
                count=1
                while i+1<len(nums) and nums[i+1]==1:
                    count+=1
                    i+=1
            maxi=max(maxi,count)
            i+=1
        return maxi
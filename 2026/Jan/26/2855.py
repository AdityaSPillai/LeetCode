class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count=0
        n=sorted(nums)
        while nums[0]>nums[-1]:
            nums=nums[-1:]+nums[:-1]
            count+=1
        if n==nums:
            return count
        return -1
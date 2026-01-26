class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        m=1
        maxi=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==maxi:
                continue
            else:
                m+=1
                maxi=nums[i]
                if m==3:
                    return maxi
        return nums[-1]
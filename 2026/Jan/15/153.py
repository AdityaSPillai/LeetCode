class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        m=10**18
        while l<=r:
            mid=l+((r-l)//2)
            if nums[mid]>=nums[l]:
                m=min(m,nums[l])
                l=mid+1
            else:
                m=min(m,nums[mid])
                r=mid-1
        return m
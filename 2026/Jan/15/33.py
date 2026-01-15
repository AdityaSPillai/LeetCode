class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=l+((r-l)//2)
            if nums[mid]==target:
                return mid
            elif nums[l]==target:
                return l
            elif nums[r]==target:
                return r
            
            
            if nums[mid]>=nums[l]:
                #Left Side
                if nums[mid]<target:
                    l=mid+1
                elif nums[l]>target:
                    l=mid+1
                else:
                    r=mid-1
            else:
                #Right Side
                if nums[mid]>target:
                    r=mid-1
                elif nums[r]<target:
                    r=mid-1
                else:
                    l=mid+1
            
        return -1
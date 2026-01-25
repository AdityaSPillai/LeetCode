class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]>nums[i-1]:
                continue
            else:
                return i
                break
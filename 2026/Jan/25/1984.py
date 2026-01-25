class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        lenn=len(nums)
        if lenn==1:
            return 0
        nums.sort()
        mini=10**18
        for i in range(lenn-k+1):
            diff=nums[i+k-1]-nums[i]
            mini=min(mini,diff)
        return mini
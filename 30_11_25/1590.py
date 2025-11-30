class Solution(object):
    def minSubarray(self, nums, p):
        total=sum(nums)
        target=total%p
        if target==0:
            return 0
        prefix=0
        seen={0:-1}
        ans=len(nums)
        for i,num in enumerate(nums):
            prefix=(prefix+num)%p
            want=(prefix-target)%p
            if want in seen:
                ans=min(ans,i-seen[want])
            seen[prefix]=i
        return ans if ans < len(nums) else -1
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)
        premaxodd,nextmaxodd=nums[-1],nums[-3]+nums[-1]
        maxodd=1
        premaxeven,nextmaxeven=nums[-2],nums[-2]
        maxeven=0
        if n==3:
            return max(nextmaxodd,nextmaxeven)
        nextmaxeven=nums[-4]+max(nextmaxeven,premaxodd)
        for i in range(n-5,-1,-1):
            if maxodd:
                maxodd=0
                maxeven=1
                temp=max(nextmaxodd,premaxeven)
                premaxodd=nextmaxodd
                nextmaxodd=temp+nums[i]
            else:
                maxeven=0
                maxodd=1
                temp=max(nextmaxeven,premaxodd)
                premaxeven=nextmaxeven
                nextmaxeven=temp+nums[i]
        return max(nextmaxodd,nextmaxeven)
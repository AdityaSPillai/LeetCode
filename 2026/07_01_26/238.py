class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,pre,post=[],[],[0 for i in range(len(nums))]
        prod=1
        for i in range(len(nums)):
            prod=prod*nums[i]
            pre.append(prod)
        prod=1
        for i in range(len(nums)-1,-1,-1):
            prod=prod*nums[i]
            post[i]=prod
        for i in range(len(nums)):
            if i==0:
                res.append(post[1])
            elif i==len(nums)-1:
                res.append(pre[len(nums)-2])
            else:
                res.append(pre[i-1]*post[i+1])
        return res
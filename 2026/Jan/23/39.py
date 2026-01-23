class Solution:
    def __init__(self):
        self.res=[]
    def dfs(self,currset,s,n,nums,target):
        if s>target:
            return -1
        elif s==target:
            self.res.append(currset.copy())
            return -1
        for i in range(n,len(nums)):
            currset.append(nums[i])
            s+=nums[i]
            x=self.dfs(currset,s,i,nums,target)
            currset.pop()
            if x==-1:
                x=0
                s-=nums[i]
                break
            s-=nums[i]
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currset=[]
        nums.sort()
        self.dfs(currset,0,0,nums,target)
        return self.res
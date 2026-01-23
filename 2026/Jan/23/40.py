class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        candidates.sort()
        def dfs(i,total):
            if total==target:
                res.append(subset.copy())
                return
            if total>target or i>=len(candidates):
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                subset.append(candidates[j])
                dfs(j+1,total+candidates[j])
                subset.pop()
        dfs(0,0)
        return res
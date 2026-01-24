class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs.pop()
        while strs:
            curr=strs.pop()
            for i in range(len(prefix)-1,-1,-1):
                if i<len(curr) and prefix[i]==curr[i]:
                    continue
                else:
                    prefix=prefix[:i]
        return prefix
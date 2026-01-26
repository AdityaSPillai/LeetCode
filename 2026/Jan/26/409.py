class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        total=0
        totalodd=0
        oddcount=0
        maxodd=0
        odd=0
        for i in count.values():
            if i%2==0:
                total+=i
            else:
                odd=1
                totalodd+=i
                oddcount+=1
                maxodd=max(maxodd,i)
        if odd==1:
            total=total+maxodd+(totalodd-maxodd-oddcount+1)
        return total
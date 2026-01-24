class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        m=0
        while n>0:
            m=(10*m)+(n%10)
            n=n//10
        if x==m:
            return True
        else:
            return False
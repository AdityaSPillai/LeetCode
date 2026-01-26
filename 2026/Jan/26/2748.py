class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n=list(combinations(nums,2))
        count=0
        for a,b in n:
            while a:
                x=a%10
                a=a//10
            y=b%10
            if gcd(x,y)==1:
                count+=1
        return count
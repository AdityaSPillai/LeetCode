class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp,price=prices[0],0
        for i in range(len(prices)):
            minp,price=min(minp,prices[i]),max(price,prices[i]-minp)
        return max(0,price)
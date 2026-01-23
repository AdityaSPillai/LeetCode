class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        total=1
        for i in range(k):
            n=heapq.heappop(nums)
            heapq.heappush(nums,n+1)
        for i in nums:
            total*=i
            total=total%((10**9)+7)
        return total%((10**9)+7)
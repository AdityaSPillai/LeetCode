class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,slow1,fast=0,0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        while True:
            slow=nums[slow]
            slow1=nums[slow1]
            if slow1==slow:
                break
        return slow
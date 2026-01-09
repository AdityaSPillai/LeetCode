class Solution(object):
    def twoSum(self, nums, target):
        h={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in h:
                return [h[diff],i]
            h[n]=i
        return []
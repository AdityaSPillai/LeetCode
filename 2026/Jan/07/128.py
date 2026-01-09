class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        nums1=set(nums)
        for n in nums1:
            if n-1 not in nums1:
                temp=1
                m=n
                while m+1 in nums1:
                    temp=temp+1
                    m=m+1
                if temp>longest:
                    longest=temp
        return longest
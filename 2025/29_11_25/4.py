class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged=sorted(nums1+nums2)
        n=len(merged)
        mid=n//2
        if n%2==1:
            median=merged[mid]
        else:
            median=((merged[mid]+merged[mid-1])/2.0)
        return median
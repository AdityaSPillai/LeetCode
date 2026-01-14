class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        l=0
        r=(len(matrix)*len(matrix[0]))-1
        while l<=r:
            mid1,mid2=(l+((r-l)//2))//len(matrix[0]),(l+((r-l)//2))%len(matrix[0])
            if matrix[mid1][mid2]==target:
                return True
            elif matrix[mid1][mid2]>target:
                mid=(mid1*len(matrix[0]))+mid2
                r=mid-1
            else:
                mid=(mid1*len(matrix[0]))+mid2
                l=mid+1
        return False

#Leetcode Submission
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        c=len(matrix[0])
        l,r=0,(len(matrix)*c)-1
        while l<=r:
            mid=(l+(r-l)//2)
            mid1,mid2=mid//c,mid%c
            if matrix[mid1][mid2]==target:
                return True
            elif matrix[mid1][mid2]>target:
                r=mid-1
            else:
                l=mid+1
        return False
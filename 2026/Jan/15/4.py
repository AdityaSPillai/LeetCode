class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1,len2=len(nums1),len(nums2)
        l1,l2,r1,r2=0,0,len1-1,len2-1
        if (len1+len2)%2==0:
            want=2
        else:
            want=1
        if len1>0 and len2>0:
            while (r1-l1+1)+(r2-l2+1)>want:
                if nums1[l1]<nums2[l2]:
                    l1+=1
                else:
                    l2+=1
                if nums1[r1]<nums2[r2]:
                    r2-=1
                else:
                    r1-=1
            if want==2:
                if r1-l1==1:
                    return (nums1[r1]+nums1[l1])/2
                elif r2-l2:
                    return (nums2[r2]+nums2[l2])/2
                else:
                    return (nums1[r1]+nums2[r2])/2
            else:
                if r1==l1:
                    return float(nums1[r1])
                else:
                    return float(nums2[r2])
        if len1>0:
            mid=(len1-1)//2
            return float(nums1[mid]) if want==1 else (nums1[mid]+nums1[mid+1])/2
        else:
            mid=(len2-1)//2
            return float(nums2[mid]) if want==1 else (nums2[mid]+nums2[mid+1])/2


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l,r=0,0
        q=deque()

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            
            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
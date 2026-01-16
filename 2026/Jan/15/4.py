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


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        lena,lenb=len(A),len(B)
        total=lena+lenb
        half=total//2

        if lena>lenb:
            A,B=B,A
            lena,lenb=lenb,lena
        
        l,r=0,lena-1
        while True:
            mid=l+((r-l)//2)
            mid2=half-mid-2

            al=A[mid] if mid>=0 else float("-infinity")
            ar=A[mid+1] if mid+1<lena else float("infinity")
            bl=B[mid2] if mid2>=0 else float("-infinity")
            br=B[mid2+1] if mid2+1<lenb else float("infinity")

            if al>br:
                r=mid-1
            elif ar<bl:
                l=mid+1
            else:
                if total%2==0:
                    return (min(ar,br)+max(al,bl))/2
                return float(min(ar,br))
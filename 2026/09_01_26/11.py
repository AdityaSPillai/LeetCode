class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        m=0
        while l<r:
            h=heights[r] if heights[r]<heights[l] else heights[l]
            ln=r-l
            a=h*ln
            if m<a:
                m=a
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return m
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[[0,heights[0]]]
        area=0
        for i in range(1,len(heights)):
            #print("In: ",i,heights[i],stack)
            if heights[i]>stack[-1][1]:
                stack.append([i,heights[i]])
            elif heights[i]==stack[-1][1]:
                stack.append([stack[-1][0],heights[i]])
            else:
                popped=stack.pop()
                area=max(area,((popped[1])*(i-popped[0])))
                index=popped[0]
                while stack and heights[i]<stack[-1][1]:
                    popped=stack.pop()
                    area=max(area,((popped[1])*(i-popped[0])))
                    index=popped[0]
                stack.append([index,heights[i]])
                #print("Area: ",area)
            #print("Out: ",i,heights[i],stack,"\n")
        while stack:
            popped=stack.pop()
            #print(popped,area,(popped[1]*(len(heights)-popped[0])),"Calculation: ",popped[1],len(heights),popped[0])
            area=max(area,(popped[1]*((len(heights))-popped[0])))
        return area
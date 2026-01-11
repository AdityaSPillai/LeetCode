class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0]*len(temp)
        stack=[0]
        for i in range(1,len(temp)):
            if temp[i]>temp[stack[len(stack)-1]]:
                while len(stack)!=0 and temp[i]>temp[stack[len(stack)-1]]:
                    p=stack.pop()
                    res[p]=i-p
                stack.append(i)
            else:
                stack.append(i)
        return res
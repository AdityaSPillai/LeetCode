#Approach 1
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack=[abs(nums[0])]
        res=[]
        i=1
        while stack and i<len(nums):
            if stack[len(stack)-1]>=abs(nums[i]):
                stack.append(abs(nums[i]))
                i+=1
            else:
                while stack and stack[len(stack)-1]<abs(nums[i]):
                    n=stack.pop()
                    res.append(n*n)
                stack.append(abs(nums[i]))
                i+=1
        while stack:
            n=stack.pop()
            res.append(n*n)
        return res
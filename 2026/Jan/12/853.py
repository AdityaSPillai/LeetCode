#Solution 1
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position,speed=zip(*sorted(zip(position,speed)))
        time=[(target-position[i])/speed[i] for i in range(len(position))]
        stack=[]
        for i in range(len(time)-1,-1,-1):
            if stack and time[i]<=stack[len(stack)-1]:
                continue
            else:
                stack.append(time[i])
        return len(stack)

#Solution 2
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position,speed=zip(*sorted(zip(position,speed)))
        stack=[]
        for i in range(len(position)-1,-1,-1):
            time=(target-position[i])/speed[i]
            if stack and time<=stack[len(stack)-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
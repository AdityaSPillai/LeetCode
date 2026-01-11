#Solution 1
class MinStack:

    def __init__(self):
        self.stack={}

    def push(self, val: int) -> None:
        self.stack[len(self.stack)]=val

    def pop(self) -> None:
        del self.stack[len(self.stack)-1]

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack.values())

#Solution 2
class MinStack:

    def __init__(self):
        self.stack={}
        self.mini=10**18

    def push(self, val: int) -> None:
        self.mini=min(self.mini,val)
        self.stack[len(self.stack)]=[val,self.mini]

    def pop(self) -> None:
        del self.stack[len(self.stack)-1]
        if len(self.stack)==0:
            self.mini=10**18
        else:
            self.mini=self.stack[len(self.stack)-1][1]

    def top(self) -> int:
        return self.stack[len(self.stack)-1][0]

    def getMin(self) -> int:
        return self.mini
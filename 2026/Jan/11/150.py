#solution 1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator=set(["+","-","/","*"])
        for i in tokens:
            if i in operator:
                temp2=stack.pop()
                temp1=stack.pop()
                if i=="+":
                    stack.append(temp1+temp2)
                elif i=="-":
                    stack.append(temp1-temp2)
                elif i=="*":
                    stack.append(temp1*temp2)
                else:
                    stack.append(int(temp1/temp2))
            else:
                stack.append(int(i))
            print(stack,"\n")
        return stack.pop()

#solution 2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in "+-/*":
                if i=="+":
                    stack.append(stack.pop()+stack.pop())
                elif i=="-":
                    a,b=stack.pop(),stack.pop()
                    stack.append(b-a)
                elif i=="*":
                    stack.append(stack.pop()*stack.pop())
                elif i=="/":
                    a,b=stack.pop(),stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack.pop()
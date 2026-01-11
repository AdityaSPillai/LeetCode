#Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openb=set(["(","[","{"])
        closeb={")":"(","}":"{","]":"["}
        for i in s:
            if i in openb:
                stack.append(i)
            elif i in closeb:
                if len(stack)!=0:
                    if closeb[i]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                continue
            print(stack)
        if len(stack)==0:
            return True
        return False

#Solution 2
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        brackets={")":"(","]":"[","}":"{"}
        for i in s:
            if i in brackets:
                if st and st[-1]==brackets[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return True if not st else False
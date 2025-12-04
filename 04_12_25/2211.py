class Solution(object):
    def countCollisions(self, directions):
        result=0
        flag=-1
        for c in directions:
            if c=="L":
                if flag>=0:
                    result+=flag+1
                    flag=0
            elif c=="S":
                if flag>0:
                    result+=flag
                flag=0
            else:
                if flag>=0:
                    flag+=1
                else:
                    flag=1
        return result
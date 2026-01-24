class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        tocheck=[]
        lenh=len(haystack)
        if len(needle)>lenh:
            return -1
        for i in range(lenh):
            if haystack[i]==needle[0]:
                tocheck.append(i)
        print(tocheck)
        for i in tocheck:
            no=0
            for j in range(len(needle)):
                if i+j<lenh:
                    if haystack[i+j]!=needle[j]:
                        no=1
                        break
                else:
                    no=1
                    break
            if no==0 and j>=len(needle)-1:
                return i
        return -1

#Better Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1
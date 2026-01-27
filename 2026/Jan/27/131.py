class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def palindrome(string):
            l,r=0,len(string)-1
            while l<=r:
                if string[l]!=string[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        def backtrack(substring,subres):
            if not substring:
                res.append(subres.copy())
                return
            st=""
            while substring:
                st+=substring[0]
                substring=substring[1:]
                if palindrome(st):
                    subres.append(st)
                    backtrack(substring,subres)
                    subres.pop()
        backtrack(s,[])
        return res
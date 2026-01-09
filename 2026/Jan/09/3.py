class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        anchor,pointer,longest=0,1,0
        temp=set()
        temp.add(s[anchor])
        while pointer<len(s):
            if s[pointer] in temp:
                if s[pointer]==s[anchor]:
                    anchor+=1
                    pointer+=1
                else:
                    longest=max(longest,len(temp))
                    while s[anchor]!=s[pointer]:
                        anchor+=1
                    anchor+=1
                    pointer=anchor+1
                    temp=set()
                    temp.add(s[anchor])
            else:
                temp.add(s[pointer])
                pointer+=1
        return max(longest,len(temp))
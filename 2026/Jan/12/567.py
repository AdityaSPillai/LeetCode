class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1s,s2s=[0]*26,[0]*26
        match=0
        for i in range(len(s1)):
            s1s[ord(s1[i])-ord('a')]+=1
            s2s[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if s1s[i]==s2s[i]:
                match+=1
        for i in range(1,len(s2)-len(s1)+1):
            if match==26:
                return True

            if s2s[ord(s2[i-1])-ord('a')]==s1s[ord(s2[i-1])-ord('a')]:
                match-=1
            elif s2s[ord(s2[i-1])-ord('a')]>s1s[ord(s2[i-1])-ord('a')]:
                match+=1
            s2s[ord(s2[i-1])-ord('a')]-=1

            if s2s[ord(s2[i+len(s1)-1])-ord('a')]==s1s[ord(s2[i+len(s1)-1])-ord('a')]:
                match-=1
            elif s2s[ord(s2[i+len(s1)-1])-ord('a')]<s1s[ord(s2[i+len(s1)-1])-ord('a')]:
                match+=1
            s2s[ord(s2[i+len(s1)-1])-ord('a')]+=1
        return match==26

#Correct Solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1s,s2s=[0]*26,[0]*26
        matches=0
        for i in range(len(s1)):
            s1s[ord(s1[i])-ord('a')]+=1
            s2s[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            if s1s[i]==s2s[i]:
                matches+=1
        
        for i in range(1,len(s2)-len(s1)+1):
            if matches==26:
                return True
                
            if s2s[ord(s2[i-1])-ord('a')]==s1s[ord(s2[i-1])-ord('a')]:
                matches-=1
                s2s[ord(s2[i-1])-ord('a')]-=1
            elif s2s[ord(s2[i-1])-ord('a')]>s1s[ord(s2[i-1])-ord('a')]:
                s2s[ord(s2[i-1])-ord('a')]-=1
                if s2s[ord(s2[i-1])-ord('a')]==s1s[ord(s2[i-1])-ord('a')]:
                    matches+=1
            else:
                s2s[ord(s2[i-1])-ord('a')]-=1
            if s2s[ord(s2[i+len(s1)-1])-ord('a')]==s1s[ord(s2[i+len(s1)-1])-ord('a')]:
                s2s[ord(s2[i+len(s1)-1])-ord('a')]+=1
                matches-=1
            elif s2s[ord(s2[i+len(s1)-1])-ord('a')]<s1s[ord(s2[i+len(s1)-1])-ord('a')]:
                s2s[ord(s2[i+len(s1)-1])-ord('a')]+=1
                if s2s[ord(s2[i+len(s1)-1])-ord('a')]==s1s[ord(s2[i+len(s1)-1])-ord('a')]:
                    matches+=1
            else:
                s2s[ord(s2[i+len(s1)-1])-ord('a')]+=1

        return matches==26
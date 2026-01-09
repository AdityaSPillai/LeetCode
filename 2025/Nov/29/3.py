class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet=set()
        left=0
        longest=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            longest=max(longest,right-left+1)
        return longest
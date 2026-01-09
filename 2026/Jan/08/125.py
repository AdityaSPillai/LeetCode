class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        right=0
        left=len(s)-1
        for i in range(len(s)):
            if right==left:
                return True
            elif right>left:
                return True

            if s[right].lower()==s[left].lower():
                right=right+1
                left=left-1
                continue
            elif s[right] not in alph:
                right=right+1
            elif s[left] not in alph:
                left=left-1
            else:
                return False
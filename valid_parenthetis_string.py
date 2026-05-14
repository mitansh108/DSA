class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = 0
        closed = 0
        j = len(s)-1
        for i in range(len(s)):
            if s[i] == '(' or s[i] == "*":
                opened+=1
            else:
                opened-=1
            if s[j-i] == ')' or s[j-i] == "*":
                closed+=1
            else:
                closed-=1
            
            if opened < 0 or closed <0:
                return False
        return True
            
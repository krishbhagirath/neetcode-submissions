class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        newString = ""

        for i in range (len(s)-1, -1, -1):
            if((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9')):
                newS += s[i].lower()
        
        for i in range(len(newS)-1, -1, -1):
            newString += newS[i]

        return newS == newString

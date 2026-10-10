class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        s = str.lower(s)

        while i < j:
            if str.isalnum(s[i]) == False and str.isalnum(s[j]) == False:
                i += 1
                j -= 1
            elif str.isalnum(s[i]) == False:
                i += 1
            elif str.isalnum(s[j]) == False:
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True
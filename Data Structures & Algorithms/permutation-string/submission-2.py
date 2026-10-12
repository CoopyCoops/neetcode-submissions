class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i,j = 0,0
        
        while j < len(s2):
            if s2[j] not in s1:
                j += 1
                i += 1
            
            while j < len(s2) and j-i+1 < len(s1) and s2[j] in s1:
                j += 1
            
            if j-i+1 == len(s1) and ''.join(sorted(s2[i:j+1])) == ''.join(sorted(s1)):
                return True
            else:
                i += 1
                j += 1
            
        
        return False
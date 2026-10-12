class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        
        cs = {}
        ct = {}
        for i in range(len(s)):
            if s[i] not in cs:
                cs[s[i]] = 1
            else:
                cs[s[i]] += 1
            
            if t[i] not in ct:
                ct[t[i]] = 1
            else:
                ct[t[i]] += 1

        return cs == ct
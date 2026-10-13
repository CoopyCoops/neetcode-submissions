class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        if len(s) == len(t):
            if sorted(s) != sorted(t):
                return ""
            else:
                return s

        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        
        if s == t or s[0:len(t)] == t:
            return t

        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        smap = {}
        i,j = 0,0
        have = 0
        need = len(tmap)
        substring = []
        while j < len(s):
            if s[j] not in tmap:
                j += 1
            else:
                i = j
                while j < len(s):
                    if s[j] in tmap:
                        smap[s[j]] = 1 + smap.get(s[j], 0)
                        if smap[s[j]] == tmap[s[j]]:
                            have += 1
                    while have == need:
                        heapq.heappush(substring, (j-i+1, i))
                        smap[s[i]] -= 1
                        if smap[s[i]] < tmap[s[i]]:
                            have -= 1
                        i += 1
                        while i < len(s) and s[i] not in smap and i <= j:
                            i += 1
                    j += 1
        
        if len(substring) == 0:
            return ""
        else:
            start = substring[0][1]
            length = substring[0][0]
            return s[start:start+length]
            
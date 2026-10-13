class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        smap = {}
        i,j = 0,0
        have = 0
        need = len(tmap)
        best_len, best_start = float("inf"),0

        for end in range(len(s)):
            if s[end] in tmap:
                i = end
                j = end
                break
        
        while j < len(s):
            if s[j] in tmap:
                smap[s[j]] = 1 + smap.get(s[j], 0)
                if smap[s[j]] == tmap[s[j]]:
                    have += 1
            while have == need:
                if j-i+1 < best_len:
                    best_len, best_start = j-i+1, i
                smap[s[i]] -= 1
                if smap[s[i]] < tmap[s[i]]:
                    have -= 1
                i += 1
                while i < len(s) and s[i] not in tmap and i <= j:
                    i += 1
            j += 1
        
        if best_len == float("inf"):
            return ""
        else:
            return s[best_start:best_start+best_len]
            
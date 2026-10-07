class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wd = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                freq[idx] += 1

            if tuple(freq) in wd:
                wd[tuple(freq)].append(s)
            else:
                wd[tuple(freq)] = [s]
        
        ans = []
        for k, v in wd.items():
            ans.append(v)

        return ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                n = ord(c) - ord("a")
                freq[n] += 1
            
            if tuple(freq) in word:
                word[tuple(freq)].append(s)
            else:
                word[tuple(freq)] = [s]
        
        res = []
        for key, value in word.items():
            res.append(value)

        return res

            
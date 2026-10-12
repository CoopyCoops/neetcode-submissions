class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        length = 0
        i,j = 0,0

        while j < len(s):
            while s[j] in word:
                word.remove(s[i])
                i += 1
            word.add(s[j])
            length = max(length, j - i + 1)
            j += 1
        
        return length
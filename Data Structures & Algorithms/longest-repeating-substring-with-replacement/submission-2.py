class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j,ans,substring_len = 0,0,0,0
        count = {}

        while j < len(s):
            count[s[j]] = 1 + count.get(s[j], 0)
            substring_len = j - i + 1
            most_freq = max(count.values())
            if substring_len - most_freq <= k:
                ans = max(ans, substring_len)
            else:
                count[s[i]] = count.get(s[i], 0) - 1
                i += 1
            j += 1

        return ans
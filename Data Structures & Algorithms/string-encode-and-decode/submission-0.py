class Solution:

    def encode(self, strs: List[str]) -> str:
        length, res = [], []
        for s in strs:
            length.append(len(s))
        for l in length:
            res.append(str(l))
            res.append(",")
        res.append("#")
        for s in strs:
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        size, res, i = [], [], 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            size.append(int(s[i:j]))
            i = j + 1
        
        i += 1
        for l in size:
            res.append(s[i:i+l])
            i += l
        
        return res
        
        

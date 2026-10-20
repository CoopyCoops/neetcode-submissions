class TimeMap:

    def __init__(self):
        self.TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.TimeMap:
            self.TimeMap[key].append((timestamp, value))
        else:
            self.TimeMap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        
        l,r = 0,len(self.TimeMap[key])-1
        while l <= r:
            m = l + (r-l)//2
            if self.TimeMap[key][m][0] == timestamp:
                return self.TimeMap[key][m][1]
            elif self.TimeMap[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return self.TimeMap[key][r][1] if self.TimeMap[key][r][0] < timestamp else ""
        

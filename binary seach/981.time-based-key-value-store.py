class TimeMap:
    
    def __init__(self):
        self.d=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value,timestamp])
        #print(self.d[key])

    def get(self, key: str, timestamp: int) -> str:
        ret=''
        l=0
        dd=self.d[key]
        r=len(dd)-1
        
        while l<=r:
            mid=(r-l)//2+l
            if timestamp<dd[mid][1]:
                r=mid-1
            else:
                ret=dd[mid][0]
                l=mid+1
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
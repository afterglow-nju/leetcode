class HitCounter:
    
    def __init__(self):
        self.d=defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.d[timestamp]+=1

    def getHits(self, timestamp: int) -> int:
        ret=0
        for i in range(max(1,timestamp-299),timestamp+1):
            ret+=self.d[i]
        return ret


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


class HitCounter:
    
    def __init__(self):
        self.s=[]

    def hit(self, timestamp: int) -> None:
        self.s.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.s:
            if self.s[0]<timestamp-299:
                self.s.pop(0)
            else:
                break
        return len(self.s)
        

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
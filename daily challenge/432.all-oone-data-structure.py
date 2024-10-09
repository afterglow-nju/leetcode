# wrong!
class AllOne:
    
    def __init__(self):
        self.d=defaultdict(int)
        self.max=0
        self.max_key=""
        self.min=-1
        self.min_key=defaultdict(lambda:defaultdict(int))
        self.min_key[-1][""]=1

    def inc(self, key: str) -> None:
        self.d[key]+=1
        if key in self.min_key[self.d[key]-1]:
            del self.min_key[self.d[key]-1][key]


        if self.d[key]>self.max:
            self.max=self.d[key]
            self.max_key=key
        if len(self.d)==1:
            self.min=self.max
            self.min_key[self.min][self.max_key]=1

        if self.d[key]<self.min:
            self.min=self.d[key]
            self.min_key[self.min][key]=1
            
        print(key,self.max_key,self.min_key,self.min,self.max,self.d)

    def dec(self, key: str) -> None:
        self.d[key]-=1
        
        if self.d[key]<self.min:
            self.min=self.d[key]
            self.min_key=key
            if self.min_key[self.d[key]+1]==1 and self.min_key[self.d[key]+1][key]==1:
                del self.min_key[self.d[key]+1][key]
            self.min_key[self.min][key]=1

        if self.max_key==self.min_key:
            self.max=self.min
            self.max_key=key
        print(key,self.max_key,self.min_key,self.min,self.max,self.d)


    def getMaxKey(self) -> str:
        return self.max_key

    def getMinKey(self) -> str:
        return list(self.min_key[self.min].keys())[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
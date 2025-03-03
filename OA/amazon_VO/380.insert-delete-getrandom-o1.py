class RandomizedSet:
    
    def __init__(self):
        self.d=dict()
        self.l=[]

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.l.append(val)
        self.d[val]=len(self.l)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False

        index=self.d[val]
        last=self.l[-1]
        self.d[last]=index
        self.l[index]=last
        
        self.l.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return self.l[random.randint(0,len(self.l)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
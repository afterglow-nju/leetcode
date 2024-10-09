class MyCircularDeque:
    
    def __init__(self, k: int):
        self.q=[0]*k
        self.valid=[0]*k
        self.front=0
        self.end=0
        self.k=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front=(self.front-1+self.k)%self.k
        self.q[self.front]=value
        self.valid[self.front]=1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.end]=value
        self.valid[self.end]=1
        self.end=(self.end+1)%self.k
        
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.valid[self.front]=0
        self.front=(self.front+1)%self.k
        return True
        
            


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.end=(self.end-1+self.k)%self.k
        self.valid[self.end]=0
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
       
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.end-1+self.k)%self.k]
        

    def isEmpty(self) -> bool:
        return sum(self.valid)==0

    def isFull(self) -> bool:
        return sum(self.valid)==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(self.k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
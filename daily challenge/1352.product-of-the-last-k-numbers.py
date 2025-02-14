class ProductOfNumbers:
    
    def __init__(self):
        self.p=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.p=[1]
        else:
            self.p.append(num*self.p[-1])
    def getProduct(self, k: int) -> int:
        if k>=len(self.p):
            return 0
        else:
            return self.p[-1]//self.p[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
class MinStack:
    
    def __init__(self):
        self.stack=[]
        self.stack_min=[]
        self.min='1#'

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min=min(self.min if self.min!='1#'  else val,val)
        self.stack_min.append(self.min)
        #self.stack_min.append(min(self.stack_min[-1] if self.stack_min else val,val))

    def pop(self) -> None:
        try:
            self.stack.pop()
            self.stack_min.pop()
        except:
            assert(0)

    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            assert(0)

    def getMin(self) -> int:
        return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
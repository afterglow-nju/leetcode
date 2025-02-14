class NumberContainers:
    
    def __init__(self):
        #索引-数字,记录最新的对应关系
        self.idx={}
        # 存储 数字->[索引堆] 的映射，每个堆是个最小堆,堆里存的索引
        self.h = defaultdict(list)    
        

    def change(self, index: int, number: int) -> None:
        self.idx[index]=number
        heappush(self.h[number],index)
        

    def find(self, number: int) -> int:
        heap=self.h[number] #当前元素对应的堆
        while heap and self.idx[heap[0]]!=number:
            heappop(heap)
        return heap[0] if heap else -1


        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
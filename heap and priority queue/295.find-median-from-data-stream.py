更妙的方法
from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = [] # smaller half of the list, max heap
        self.large = [] # larger half of the list, min heap
        

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()









class MedianFinder:
    
    def __init__(self):
        self.max=[]
        self.min=[]
        heapq.heapify(self.max)
        heapq.heapify(self.min)

        
    def addNum(self, num: int) -> None:
        if self.max and self.min:
            if num<self.min[0]:
                heapq.heappush(self.max,-num)
            else:
                heapq.heappush(self.min,num)
        else:
            heapq.heappush(self.min,num)
        
        if len(self.max)>len(self.min):
            heapq.heappush(self.min,-heapq.heappop(self.max))
        elif len(self.max)+1<len(self.min):
            heapq.heappush(self.max,-heapq.heappop(self.min))

    def findMedian(self) -> float:
        l1=len(self.max)
        l2=len(self.min)
        #print(l1,l2,self.max[0],self.min[0])
        if l1==l2:
            return (-self.max[0]+self.min[0])/2
        else:
            return self.min[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
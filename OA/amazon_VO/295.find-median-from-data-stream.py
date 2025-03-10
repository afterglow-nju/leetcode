class MedianFinder:
    
    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if not self.left or not self.right:
            heapq.heappush(self.left,-num)
            
        else:
            if num<self.right[0]:
                heapq.heappush(self.left,-num)
            else:
                heapq.heappush(self.right,num)
        if len(self.left)-len(self.right)>1:
            heappush(self.right,-heapq.heappop(self.left))
        if len(self.right)-len(self.left)>1:
            heappush(self.left,-heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        m,n=len(self.left),len(self.right)
        #print(self.left,self.right)
        if (m+n)&1==1:
            if m>n:
                return -self.left[0]
            else:
                return self.right[0]
        else:
            return (-self.left[0]+self.right[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
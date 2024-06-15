class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        new=[[-profits[i],capital[i]] for i in range(len(profits))]
        new.sort(key=lambda x:x[1])
        index=0
        h=[]
        heapq.heapify(h)
        
        while k>0:
            while index<len(new):
                if new[index][1]<=w:
                    heapq.heappush(h,new[index][0])
                    index+=1
                else:
                    break

            if h:      
                w-=heapq.heappop(h)
                k-=1
            else:
                break
        return w
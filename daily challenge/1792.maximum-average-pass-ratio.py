class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        ratio=0
        h=[]

        for i in classes:
            if i[1]==i[0]:
                ratio+=1
            else:
                h.append([ -(i[1]-i[0])/(i[1]*(i[1]+1)), i[0],i[1]])
        heapq.heapify(h)

        while h and extraStudents>0:
            i=heapq.heappop(h)
            i[1]+=1
            i[2]+=1
            i[0]=-(i[2]-i[1])/(i[2]*(i[2]+1))
            extraStudents-=1
            heapq.heappush(h,i)
            #print(h)
        for i in h:
            ratio+=i[1]/i[2]
        return ratio/len(classes)
        
        '''
        4/6 5/6 4/10 2/10
        '''
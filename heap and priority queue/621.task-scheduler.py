class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        from collections import Counter
        x=Counter(tasks)
        t1=list(x.keys())
        t2=list(x.values())
        h=[[-t2[i],t1[i]] for i in range(len(t1))]
        heapq.heapify(h)
        ret=0
        pop=[0]*(n+1)
        index=0 #index就是在n个interval中轮转
        have=0
        #要最大堆
        while len(h)>0 or have>0:
        
            if pop[index]!=0:
                #print(pop[index],h[0])
                #一个轮回后，把一个轮回前跑的任务A再放进堆中
                
                heapq.heappush(h,pop[index])
                pop[index]=0
                have-=1
            if len(h)>0:
                t=heapq.heappop(h)
                
                t[0]+=1
                if t[0]<0:
                    pop[index]=t
                    have+=1
            index+=1
            index=index%(n+1)
            ret+=1
        return ret
f
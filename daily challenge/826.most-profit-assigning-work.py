class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        p,d=zip(*sorted(list(zip(profit,difficulty)),reverse=True,key=lambda x:x[0]))
        p=list(p)
        d=list(d)
        worker.sort(reverse=True)
        ret=0
        tem,index=0,0
        for i in worker:
            for j in range(index,len(profit)):
                if d[j]<=i:
                    ret+=p[j]
                    break
                tem=j
            index=tem
        return ret
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        pre=[0]*len(customers)
        for i in range(len(customers)):
            pre[i]=pre[i-1]
            if grumpy[i]==0:
                pre[i]+=customers[i]

        con=[0]*len(customers)
        con[0]=sum(customers[0:minutes])
        for i in range(1,len(customers)-minutes+1):
            con[i]=con[i-1]-customers[i-1]+customers[i+minutes-1]

        ret=0
        for i in range(len(customers)-minutes+1):
            #i~i+minutes-1
            now=con[i]
            if i>0:
                now+=pre[i-1]
            if i+minutes<len(customers):
                now+=pre[len(customers)-1]-pre[i+minutes-1]
            ret=max(ret,now)
        return ret
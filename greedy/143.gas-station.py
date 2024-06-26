class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dis=[gas[i]-cost[i] for i in range(len(gas))]
        if sum(dis)<0:
            return -1
        
        s=[0]*len(dis)
        i=0
        for j in range(len(dis)):
            if dis[j]>0:
                i=j
                break
        c,now,ret=0,0,i
        n=len(dis)
        #print(dis)
        i=i-1
        while c < n:
            i=(i+1)%n 
            now+=dis[i]
            #print(i,now)
            if now<0:
                now=0
                ret=(i+1)%n
            c+=1
        return ret

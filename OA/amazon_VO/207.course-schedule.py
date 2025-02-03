class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        ind=[0]*n
        e=defaultdict(list)
        for x,y in p:
            ind[y]+=1
            e[x].append(y)
        q=[]
        cnt=0
        for i in range(n):
            if ind[i]==0:
                q.append(i)
                cnt+=1
        while q:
            tem=[]
            for i in q:
                for j in e[i]:
                    ind[j]-=1
                    if ind[j]==0:
                        tem.append(j)
                        cnt+=1

            q=tem
        return cnt==n


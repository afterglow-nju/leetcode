class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ind=[0]*n
        e=defaultdict(list)
        level=0
        d=defaultdict(set)
        for x,y in prerequisites:
            e[y].append(x)
            ind[x]+=1
        q=deque()
        for i in range(n):
            if ind[i]==0:
                q.append(i)
            d[i].add(i)
        while q:
            tem=deque()
            while q:
                t=q.popleft()
                for i in e[t]:
                    ind[i]-=1
                    d[i]|=d[t]
                    if ind[i]==0:
                        tem.append(i)
                        #print(i)
                        
            q=tem
        ret=[]
        #print(d)
        for i in queries:
            if i[1] in d[i[0]]:
                ret.append(True)
            else:
                ret.append(False)
        return ret
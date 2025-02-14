#重要的是，拓扑排序的意义，DAG的某种顺序class Solution:
class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        e=defaultdict(list)
        ind=[0]*num
        for i in pre:
            e[i[1]].append(i[0])
            ind[i[0]]+=1
        q=deque()
        for i in range(num):
            if ind[i]==0:
                q.append(i)
        ret=[]
        while q:
            n=q.popleft()
            ret.append(n)
            for i in e[n]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        if len(ret)==num:
            return ret
        else:
            return []
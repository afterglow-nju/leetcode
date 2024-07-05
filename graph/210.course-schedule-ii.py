class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        #重要的是，拓扑排序的意义，DAG的某种顺序
        g=defaultdict(list)
        In=[0]*numCourses
        
        
        for i in range(len(pre)):
            g[pre[i][0]].append(pre[i][1])
            In[pre[i][1]]+=1
        

        order=list()
        q=deque()

        for i in range(numCourses):
            if In[i]==0:
                q.append(i)
        
        while q:
            t=q.popleft()
            order.append(t)
            for i in g[t]:
                In[i]-=1
                if In[i]==0:
                    q.append(i)
        if len(order)==numCourses:
            return order[::-1]
        else:
            return []
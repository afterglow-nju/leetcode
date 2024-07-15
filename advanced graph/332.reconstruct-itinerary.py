class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g=defaultdict(list)
        #In=defaultdict(int)
        #Out=defaultdict(int)
        tickets.sort(key=lambda x:x[1])
        for i in tickets:
            g[i[0]].append(i[1])
            #Out[i[0]]+=1
            #In[i[1]]+=1
        #for i in g.keys():
            #g[i].sort()
        stack=['JFK']
        ret=[]
        while stack:
            node=stack[-1]
            if g[node]!=[]:
                stack.append(g[node][0])
                del g[node][0]
            else:
                ret.append(stack.pop())
        return ret[::-1]
        
        
        

            
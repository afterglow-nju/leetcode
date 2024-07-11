class Solution:
    def averageWaitingTime(self, cus: List[List[int]]) -> float:
        

        ret=cus[0][1]
        finish=cus[0][0]+cus[0][1]
        for i in range(1,len(cus)):
            if cus[i][0]>=finish:
                ret+=cus[i][1]
                finish=cus[i][0]+cus[i][1]
            else:
                ret+=finish-cus[i][0]+cus[i][1]
                finish=finish+cus[i][1]
            #print(ret[i])
        return ret/len(cus)

        '''
        ret=[0]*len(cus)
        ret[0]=cus[0][1]
        finish=cus[0][0]+cus[0][1]
        for i in range(1,len(cus)):
            if cus[i][0]>=finish:
                ret[i]=cus[i][1]
                finish=cus[i][0]+cus[i][1]
            else:
                ret[i]=finish-cus[i][0]+cus[i][1]
                finish=finish+cus[i][1]
            #print(ret[i])
        return sum(ret)/len(cus)
        '''
        
        
        class Solution:
        def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g=defaultdict(list)
        In=defaultdict(int)
        Out=defaultdict(int)
        for i in tickets:
            Out[i[0]]+=1
            In[i[1]]+=1

        end=""
        for i in In.keys():
            print(i,Out[i],In[i])
            if Out[i]<In[i]:
                end=i

        g=defaultdict(list)
        for i in tickets:
            if i[0]==end:
                i[0]="Z"
            if i[1]==end:
                i[1]="Z"
            g[i[0]].append(i[1])

        for i in g.keys():
            g[i].sort()
            print(end,i,g[i])



        stack=['JFK']
        ret=['JFK']
        while stack:
            v=stack[-1]
            if g[v]!=[]:
                
                #print(g[stack[-1]],g[stack[-1]][0])
                stack.append(g[v][0])
                ret.append(g[v][0])
                g[v].remove(g[v][0])
                
                
            else:
                stack.pop()
        for i in range(len(ret)):
            if ret[i]=="Z":
                ret[i]=end
        return ret
        
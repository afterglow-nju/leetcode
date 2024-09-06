class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d=defaultdict(int)
        for i in obstacles:
            d[(i[0],i[1])]=1

        x,y=0,0
        ret=0
        dire=[[0,1],[1,0],[0,-1],[-1,0]]
        index=0
        for i in commands:
            if i==-1:
                index=(index+1)%4
            elif i==-2:
                index=(index-1)
                if index==-1:
                    index=3
            else:
                #if [x,y] in obstacles:
                #    continue
                #print(dire[index],x,y)
                for j in range(i):
                    newx,newy=x+dire[index][0],y+dire[index][1]
                    if (newx,newy) not in d:
                        x,y=newx,newy
                        #print(x,y)
                    else:
                        break
                ret=max(ret,x**2+y**2)

        return ret
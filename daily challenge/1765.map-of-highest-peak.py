class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=[]
        m,n=len(isWater),len(isWater[0])
        h=[[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    q.append([i,j])
                    h[i][j]=0
        
        ret=1
        
        while q:
            tem=[]
            for node in q:
                for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nx,ny=node[0]+x,node[1]+y
                    if 0<=nx<m and 0<=ny<n:
                        if h[nx][ny]==-1:
                            #print(nx,ny,ret)
                            h[nx][ny]=ret
                            tem.append([nx,ny])
            #print(tem,ret)
            if tem==[]:
                return h
            ret+=1
            q=tem
        assert(0)

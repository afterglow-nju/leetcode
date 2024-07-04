class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po,ao=set(),set()
        m,n=len(heights),len(heights[0])
        def bfs1(s1,s2,a,b): #zuo shang 
            s1,s2=a,b

            if a*b==0:
                po.add((a,b))
                #return

            if a+1<len(heights):
                if (a+1,b) not in po:
                    if heights[s1][s2]<=heights[a+1][b]:
                        po.add((a+1,b))
                        bfs1(s1,s2,a+1,b)
            if b+1<len(heights[0]):
                if (a,b+1) not in po:
                    if heights[s1][s2]<=heights[a][b+1]:
                        po.add((a,b+1)) 
                        bfs1(s1,s2,a,b+1)
            if a-1>=0:
                if (a-1,b) not in po:
                    if heights[s1][s2]<=heights[a-1][b]:
                        po.add((a-1,b))
                        bfs1(s1,s2,a-1,b)
            if b-1>=0:
                if (a,b-1) not in po:
                    if heights[s1][s2]<=heights[a][b-1]:
                        po.add((a,b-1)) 
                        bfs1(s1,s2,a,b-1)
                        
        def bfs2(s1,s2,a,b): #zuo shang 
            s1,s2=a,b

            if a==len(heights)-1 or b==len(heights[0])-1:
                ao.add((a,b))
                #return

            if a+1<len(heights):
                if (a+1,b) not in ao:
                    if heights[s1][s2]<=heights[a+1][b]:
                        ao.add((a+1,b))
                        bfs2(s1,s2,a+1,b)
            if b+1<len(heights[0]):
                if (a,b+1) not in ao:
                    if heights[s1][s2]<=heights[a][b+1]:
                        ao.add((a,b+1)) 
                        bfs2(s1,s2,a,b+1)

            if a-1>=0:
                if (a-1,b) not in ao:
                    if heights[s1][s2]<=heights[a-1][b]:
                        ao.add((a-1,b))
                        bfs2(s1,s2,a-1,b)
            if b-1>=0:
                if (a,b-1) not in ao:
                    if heights[s1][s2]<=heights[a][b-1]:
                        ao.add((a,b-1)) 
                        bfs2(s1,s2,a,b-1)
                        
        for i in range(n):
            bfs1(0,i,0,i)
        for i in range(m):
            bfs1(i,0,i,0)
        for i in range(n):
            bfs2(m-1,i,m-1,i)
        for i in range(m):
            bfs2(i,n-1,i,n-1)
        #print(po)
        #print(ao)
        return list(po&ao)
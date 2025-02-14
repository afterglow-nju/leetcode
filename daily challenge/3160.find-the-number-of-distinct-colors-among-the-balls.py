class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        c=defaultdict(int) # color
        b=defaultdict(lambda :0) # ball
        ret=[]
        cnt=0
        for x,y in queries:

            if x in b:
                color=b[x]
                c[color]-=1
                if c[color]==0:
                    del c[color]
            b[x]=y
            c[y]+=1
            ret.append(len(c))
        return ret

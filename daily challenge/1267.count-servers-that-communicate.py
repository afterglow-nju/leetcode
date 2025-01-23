class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        s=set()
        m,n=len(grid),len(grid[0])
        ret=0
        for i in range(m):
            if sum(grid[i])>=2:
                for j in range(n):
                    if grid[i][j]==1:
                        s.add((i,j))
                        ret+=1
        #print(s,ret)
        for i in range(n):
            cnt=0
            t=set()
            for j in range(m):
                if grid[j][i]==1:
                    cnt+=1
                    if (j,i) not in s:
                        t.add((j,i))
            #print(cnt,t)
            if cnt>=2:
                ret+=len(t)
                s|=t
        return ret
    
    
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = Counter(), Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1
        
        return ans

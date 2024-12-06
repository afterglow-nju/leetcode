class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n=len(box),len(box[0])
        ret=[[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                #print(i,j,j,n-i-1)
                ret[j][m-i-1]=box[i][j]
        #print(ret)
        for i in range(m):
            pos=deque()
            for j in range(n-1,-1,-1):
                #print(i,j)
                if ret[j][i]=='.':
                    pos.append([j,i])
                if ret[j][i]=='*':
                    pos=deque()
                if ret[j][i]=='#':
                    if len(pos)!=0:
                        tem=pos.popleft()
                        #print(tem)
                        ret[tem[0]][tem[1]]='#'
                        ret[j][i]='.'
                        pos.append([j,i])
        return ret

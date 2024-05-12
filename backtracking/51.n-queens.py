class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret=[]

        def back(ans,s,now):
            if s==n:
                ret.append(ans[:])
                return 
            for i in range(1,n+1):
                locate=(s,i)
                
                label=1
                for j in now:
                    if j[0]==locate[0] or j[1]==locate[1] or abs(j[0]-locate[0])==abs(j[1]-locate[1]):
                        label=0
                        break
                if label:
                    t=(i-1)*'.'+'Q'+(n-i)*'.'
                    now.append(locate)
                    ans.append(t)
                    back(ans,s+1,now)
                    now.pop()
                    ans.pop()
                
            return 

        back([],0,[])
        return ret
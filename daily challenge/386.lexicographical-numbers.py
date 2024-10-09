class Solution:
    def lexicalOrder(self, num: int) -> List[int]:
        ret=[]

        def dfs(n):
            if n<=num:
                ret.append(n)
            else:
                return False

            flag=True
            for i in range(10):
                flag=dfs(n*10+i)
                
            return True
        
        for i in range(1,10):
            if i<=num:
                dfs(i)
            else:
                break
        return ret
                   
        
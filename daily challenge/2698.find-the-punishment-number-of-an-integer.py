class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(c,index,t,s):
            if c==t and index==len(s):
                return True
            x=0
            for i in range(index,len(s)):
                x=x*10+int(s[i])
                if dfs(c+x,i+1,t,s):
                    return True
            return False
        ret=0
        for i in range(1,n+1):
            if dfs(0,0,i,str(i*i)):
                #print(i)
                ret+=i*i
        return ret
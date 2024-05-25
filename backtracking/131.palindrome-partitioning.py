class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret=[]
        import copy
        n=len(s)
        f=[[True]*n for _ in range(n)] #开二维数组
        #因为这公式，所以从n开始递减
        for i in range(n-1,-1,-1):
            for j in range(i+1,n): #不是很理解为什么从i+1开始
                f[i][j]=f[i+1][j-1] and s[i]==s[j]
#update in 2024.5.23
#秒啊，这个遍历顺序，保证用到的一定是遍历过的

        def back(ans,index):
            if index==len(s):
                ret.append(ans[:])#copy.deepcopy(ans))
            l,r=index,index
            for i in range(index,n):
                if f[l][r]:
                    ans.append(s[l:r+1])
                    back(ans,r+1)
                    ans.pop()
                r+=1
                
        back([],0)
        return ret
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret=[]
        import copy

        def isp(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True


        def back(ans,index):
            if index==len(s):
                ret.append(ans[:])#copy.deepcopy(ans))
            l,r=index,index
            for i in range(index,len(s)):
                if isp(l,r):
                    ans.append(s[l:r+1])
                    back(ans,r+1)
                    ans.pop()
                r+=1
                
        back([],0)
        return ret
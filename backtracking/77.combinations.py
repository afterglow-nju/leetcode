class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    #C_n^k
        ret=[]
        def back(ans,l,index):
            if l==k:
                ret.append(ans[:])
                return
            for i in range(index,n+1):
                ans.append(i)
                back(ans,l+1,i+1)#避免重复，不是index+1，而是i+1
                ans.pop()
        
        back([],0,1)
        return ret
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret=[]
        def combine(index,cnt,now):
            if cnt==k:
                ret.append(now)
                return 
            for i in range(index,n+1):
                combine(i+1,cnt+1,now+[i])
        combine(1,0,[])
        return ret
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre=[0]*(1+len(arr))
        pre[0]=arr[0]
        for i in range(1,len(arr)):
            pre[i]=pre[i-1]^arr[i]
        ret=[]
        for i in queries:
            ret.append(pre[i[0]-1]^pre[i[1]])
        return ret
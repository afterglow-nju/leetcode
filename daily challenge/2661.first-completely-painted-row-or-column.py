class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        r=[n]*m
        c=[m]*n
        d=defaultdict(lambda:[])
        for i in range(m):
            for j in range(n):
                d[mat[i][j]]=[i,j]
        for i in range(len(arr)):
            t=d[arr[i]]
            r[t[0]]-=1
            c[t[1]]-=1
            if r[t[0]]==0 or c[t[1]]==0:
                return i
        assert(0)
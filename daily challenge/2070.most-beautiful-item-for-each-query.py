class Solution:
    def maximumBeauty(self, A, queries):
        A.sort(key=lambda x:(x[0],-x[1]))
        d=defaultdict(int)
        ret=[]
        prev=""
        tem=[]
        for i in range(len(A)):
            if A[i][0]!=prev:
                d[A[i][0]]=max(A[i][1],d[prev])
                prev=A[i][0]
                tem.append(A[i][0])
        for i in queries:
            index=bisect.bisect_right(tem,i)-1
            if index>=0:
                ret.append(d[tem[index]])
            else:
                ret.append(0)
        return ret

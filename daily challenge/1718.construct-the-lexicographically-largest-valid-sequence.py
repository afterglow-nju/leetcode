class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        used=[False]*(n+1)
        ret=[]
        cnt=[0]*(2*n-1)
        def find(cnt,index):
            if index==2*n-1:
                ret=cnt
                return True
            for i in range(n,0,-1):
                if used[i]:
                    continue
                else:
                    if index+i>=len(cnt) ot cnt[index+1]!=0:
                        continue
                    else:
                        used[i]=True
                        cnt[index]=i
                        cnt[index+i]=i
                        find()
                        uesd[i]=False
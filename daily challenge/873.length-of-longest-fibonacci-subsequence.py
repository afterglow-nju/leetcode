class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ret=0
        s=set(arr)
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                n1,n2=arr[i],arr[j]
                cnt=2
                while n1+n2 in s:
                    cnt+=1
                    n1,n2=n2,n1+n2
                ret=max(ret,cnt)
        return ret if ret!=2 else 0
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def get_count(pre,n):
            cnt=0
            b=pre+1
            while pre<=n:
                cnt+=min(n+1,b)-pre
                pre*=10
                b*=10
            return cnt

        pre,cnt=1,1
        while cnt<k:
            tem=get_count(pre,n)
            if tem+cnt>k:
                pre*=10
                cnt+=1
            elif tem+cnt<=k:
                pre+=1
                cnt+=tem
        return pre
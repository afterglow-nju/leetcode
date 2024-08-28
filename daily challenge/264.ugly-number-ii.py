class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]*n
        i=0
        i1,i2,i3=0,0,0
        while True:
            if i==n-1:
                return dp[n-1]
            two,three,five=dp[i1]*2,dp[i2]*3,dp[i3]*5
            nxt=min(two,three,five)
            dp[i+1]=nxt
            i1=i1 if nxt!=two else i1+1
            i2=i2 if nxt!=three else i2+1
            i3=i3 if nxt!=five else i3+1
            
            i+=1
        '''
        h=[1]
        if n==1:
            return 1
        size=0
        heapq.heapify(h)
        while size<=n:
            t=heapq.heappop(h)
            size+=3
            heapq.heappush(h,t*2)
            heapq.heappush(h,t*3)
            heapq.heappush(h,t*5)
            print(size,h)
        return h[size-n]
        '''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n=len(books)
        dp=[inf]*(n+1)
        dp[0]=0
        for i in range(n):
            w,h=0,0
            j=i
            while j>=0:
                w+=books[j][0]
                if w>shelfWidth:
                    break
                h=max(h,books[j][1])
                dp[i+1]=min(dp[i+1],dp[j]+h)
                j-=1
        return dp[n]
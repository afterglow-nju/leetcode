class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        ret=0
        m=0
        i=0
        coins.sort()
        while i<len(coins):
            if m+1<coins[i]:
                ret+=1
                m+=m+1
            else:
                m+=coins[i]
                i+=1
            if m>=target:
                break
        #print(m,ret)
        while m<target:
            m+=m+1
            ret+=1
        return ret
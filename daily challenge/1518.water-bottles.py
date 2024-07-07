class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles+(numBottles-numExchange)//(numExchange-1)+1 if numBottles > numExchange  else numBottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret,n,t=0,numBottles,0
        while n+t>=numExchange:
            ret+=n
            empty=n+t
            nxt=(empty)//numExchange
            t=empty%numExchange
            n=nxt
            #print(nxt,n,t)
            
        return ret+n
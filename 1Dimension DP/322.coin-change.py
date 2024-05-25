class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        
        f=[float('inf')]*(1+amount)
        for i in coins:
            if i>amount:
                continue
            f[i]=1
        f[0]=0
        for i in range(1,amount+1):
            ret=float('inf')
            for j in coins:
                ret=min(ret,1+f[i-j] if i-j>=0 else float('inf')) #重点在于枚举硬币，我之前是枚举dp。枚举dp其实是没用好dp的信息，是我傻逼了
            
            f[i]=ret 
        
        #for i in range(1,amount+1):
        #    print(i,f[i])
        
        return f[amount] if f[amount]!=float('inf') else -1

        
        
        '''
        ret=[float('inf')]
        def back(now,a,index):
            if now==amount:
                ret[0]=min(ret[0],a)
                return 
            if now>amount:
                return
            for i in range(index,len(coins)):
                back(now+coins[i],a+1,i)
        back(0,0,0)
        return ret[0] if ret[0]!=float('inf') else -1
        '''
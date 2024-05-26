class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #这样更快，这样不是n^2
        
        
        
        #可以有别的组合，不能贪心
        d=Counter(wordDict)
 
        dp=[False] * (len(s)+1)
        dp[0]=True

        for i in range(1,len(s)+1):
            for word in d.keys():
                if i-len(word)>=0 and dp[i-len(word)] and s[i-len(word):i] in d:
                    dp[i]=True 
        #print(dp)
        return dp[len(s)]








class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        
        
        
        #可以有别的组合，不能贪心
        d=Counter(wordDict)
 
        dp=[False] * (len(s)+1)
        dp[0]=True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in d:
                    dp[i]=True 
        return dp[len(s)]
        '''
        def back(current,memo={}):
            if current in memo:
                return memo[current]
            
            if not current:
                return True

            n=len(current)
            #print(current)
            for i in range(1,n+1):
                if current[:i] in d:
                    memo[current[:i]]=True
                    if back(current[i:n+1],memo):
                        memo[current]=True
                        return True
            memo[current]=False
            return False
        return back(s)
        '''
        
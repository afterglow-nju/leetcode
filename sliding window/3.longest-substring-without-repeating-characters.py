class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=dict()
        ret=0
        left=0
        for i,n in enumerate(s):
            
            if n in d:
                index=d[n]
                #print(i,n,left,ret)
                ret=max(ret,i-1-left+1)
                left=max(left,index+1)
                d[n]=i
            else:
                d[n]=i
        #print(ret)
        t=0
        for i in d:
            if d[i]>=left:
                t+=1
        ret=max(ret,t)
        return ret
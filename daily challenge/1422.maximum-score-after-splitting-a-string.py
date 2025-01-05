class Solution:
    def maxScore(self, s: str) -> int:
        left,right=0,0
        if s[0]=='0':
            left+=1
        for i in range(1,len(s)):
            if s[i]=='1':
                right+=1
        ret=right+left
        for i in range(1,len(s)-1):
            if s[i]=='0':
                left+=1
            else:
                right-=1
            ret=max(ret,left+right)
        return ret
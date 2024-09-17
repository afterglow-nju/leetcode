class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        status=0
        pos=[float('inf')]*32
        pos[0]=-1
        ret=0
        for i in range(len(s)):
            if s[i]=='a':
                status^=(1<<0)
            elif s[i]=='e':
                status^=(1<<1)
            elif s[i]=='i':
                status^=(1<<2)
            elif s[i]=='o':
                status^=(1<<3)
            elif s[i]=='u':
                status^=(1<<4)
            if pos[status]!=float('inf'):
                #print(i,status,pos[status])
                ret=max(ret,i-pos[status])
            else:
                pos[status]=i
        return ret
            
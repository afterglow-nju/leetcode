class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        f=[[True]*n for i in range(n)]
        
        ret=0
        r=(0,0)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                f[i][j]=f[i+1][j-1] and s[i]==s[j]
                #print(f[i][j])
                if f[i][j]:
                    if j-i+1>ret:
                        ret=j-i+1
                        r=(i,j)
        
        return s[r[0]:r[1]+1]
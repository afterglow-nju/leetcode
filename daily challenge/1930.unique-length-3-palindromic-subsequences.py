class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ret=0
        for i in range(26):
            c=chr(ord('a')+i)
            left,right=0,len(s)-1
            while left<len(s):
                if s[left]==c:
                    break
                else:
                    left+=1
            if left>=len(s):
                continue
            else:
                while right>=0:
                    if s[right]==c:
                        break
                    else:
                        right-=1
                m=set(list(s[left+1:right]))
                ret+=len(m)
        return ret
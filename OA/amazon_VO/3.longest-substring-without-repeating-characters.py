class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        cur=set()
        ret=0
        while right<len(s):
            while s[right] in cur:
                cur.remove(s[left])
                left+=1
            cur.add(s[right])
            ret=max(ret,right-left+1)
            right+=1
        return ret


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        ret=1
        d=set()
        left=0
        d.add(s[0])
        for i in range(1,len(s)):
            if s[i] in d:
                ret=max(ret,i-1-left+1)
                while s[left]!=s[i]:
                    d.remove(s[left])
                    left+=1
                left+=1
            else:
                d.add(s[i])
        ret=max(ret,len(s)-1-left+1)
        return ret
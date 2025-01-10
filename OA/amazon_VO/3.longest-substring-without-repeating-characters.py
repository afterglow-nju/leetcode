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
            
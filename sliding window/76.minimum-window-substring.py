class Solution:
    def minWindow(self, s: str, t: str) -> str:

#不知道怎么快速比较

        if len(t)>len(s):
            return ""
        
        target=dict()
        now=dict()
        for i in t:
            target[i]=target.get(i,0)+1
        left,right=0,0
        minn=float('inf')
        ret=""
        meet=0
        while right<len(s):
            #print(left,right)
            c=s[right]
            now[c]=now.get(c,0)+1

            if c in target and now[c]<=target[c]:
                meet+=1
            #print(left,right,meet)
            while meet==len(t):
                l=right-left+1
                if minn>l:
                    minn=l
                    ret=s[left:right+1]
                if s[left] in target and now[s[left]]==target[s[left]]:
                    meet-=1
                now[s[left]]-=1
                left+=1
            right+=1
        return ret
        
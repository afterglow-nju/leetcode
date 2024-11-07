class Solution:
    def minWindow(self, s: str, T: str) -> str:

#不知道怎么快速比较
        if len(T)>len(s):
            return ""

        t=defaultdict(int)
        n=defaultdict(int)
        for i in T:
            t[i]+=1
        left=0
        right=0
        ret=float('inf')
        meet=0
        ans=''
        while right<len(s):
            if s[right] in t:
                n[s[right]]+=1
            else:
                right+=1
                continue
            
            if n[s[right]]==t[s[right]]:
                meet+=1
            while meet==len(t):
                L=right-left+1
                if L<ret:
                    ret=L
                    ans=s[left:right+1]
                if s[left] in t:
                    n[s[left]]-=1
                    if n[s[left]]<t[s[left]]:
                        meet-=1
                left+=1
                
            right+=1
        return ans








        '''
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
        '''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def sn(s:str):
            return ord(s)-ord('A')

            
        left,right=0,0
        alpha=[0]*26
        ret=0
        Sum=0
        #Max=0
        while right<len(s):
            # add righat pointer
            alpha[sn(s[right])]+=1
            maxn=max(alpha)
            if right-left+1-max(alpha)<=k:
                ret=max(ret,right-left+1)
            else:
                while right-left+1-maxn>k:

                    alpha[sn(s[left])]-=1
                    
                    left+=1
            right+=1
        return ret

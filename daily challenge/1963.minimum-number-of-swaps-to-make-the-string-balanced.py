class Solution:
    def minSwaps(self, s: str) -> int:
        close,openn=0,0
        left,right=0,len(s)-1
        ret=0
        s=list(s)
        while left<right:
            if s[left]=='[':
                openn+=1
                left+=1
            else:
                close+=1
                if close<=openn:
                    left+=1
                else:
                    tem=close-openn
                    ret+=tem
                    for i in range(tem):
                        while s[right]!='[':
                            right-=1
                        close-=1
                        openn+=1
                        s[left],s[right]=s[right],s[left]
                        left+=1
        return ret
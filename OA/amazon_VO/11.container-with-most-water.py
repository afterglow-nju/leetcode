class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        left,right=0,n-1
        ret=0
        while left!=right:
            ret=max(ret,min(h[left],h[right])*(right-left))
            if h[left]<h[right]:
                left+=1
            else:
                right-=1
        return ret

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)-1
        left=0
        right=n
        ret=0
        while left<right:
            if height[left]<height[right]:
                m=height[left]
                s=m*(right-left)
                left+=1
            else:
                m=height[right]
                s=m*(right-left)
                right-=1
            ret=max(ret,s)
        return ret
class Solution:
    def trap(self, height: List[int]) -> int:
        ret=0
        stack=[]
        left,right=0,1
        while right<len(height):
            if height[right]<height[left]:
                stack.append(height[right])
                right+=1
            else:
                while stack:
                    ret+=height[left]-stack.pop()
                left=right
                right+=1
        right_wall=height[-1]
        for i in range(len(stack)-1,-1,-1):
            if stack[i]<right_wall:
                ret+=right_wall-stack[i]
            else:
                right_wall=stack[i]
        return ret
                    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack,index=[],[]
        heights.append(0)
        ret=0
        for i,n in enumerate(heights):
            far_left=i
            while stack and n<stack[-1]:
                h=stack.pop()
                w=index.pop()
                far_left=w
                size=h*(i-w)
                ret=max(ret,size)
            stack.append(n)
            index.append(far_left)
        return ret
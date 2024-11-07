class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack=[]
        for i,x in enumerate(nums):
            if not stack or nums[stack[-1]]>x:
                stack.append(i)
        j=len(nums)-1
        ret=0
        while stack and j>=0:
            while j>=0 and nums[j]<nums[stack[-1]]:
                j-=1
            while stack and nums[j]>=nums[stack[-1]]:
                ret=max(ret,j-stack[-1])
                stack.pop()
        return ret
        













        '''
        stack, ans = [], 0
        for i, x in enumerate(nums):
            if not stack or nums[stack[-1]] > x:
                stack.append(i)
        j = len(nums) - 1
        while stack and j >= 0:
            while j >= 0 and nums[j] < nums[stack[-1]]:
                j -= 1
            if j >= 0:
                ans = max(ans, j - stack.pop())
        return ans
        '''

'''
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ret=0
        t=[[nums[i],i] for i in range(len(nums))]
        t.sort()
        stack=[]
        for i in t:
            if not stack:
                stack.append(i)
            else:
                while stack and  i[1]<stack[-1][1]:
                    tem=stack.pop()
                    ret=max(ret,tem[1]-i[1])
                stack.append(i)
        return ret
'''
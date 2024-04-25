class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        ret=0
        lmax=nums[0]
        rmax=nums[n-1]
        while left<right:
            if lmax<rmax:
                ret+=max(0,lmax-nums[left])
                left+=1
                lmax=max(lmax,nums[left])
            else:
                ret+=max(0,rmax-nums[right])
                right-=1
                rmax=max(rmax,nums[right])
        return ret 
    
#我的方法竟然会快一点,:joy:
class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=1
        ret=0
        stack=[]
        while right<n:
            left_wall=nums[left]
            right_wall=nums[right]
            if right_wall<left_wall:
                h=left_wall-right_wall
                stack.append([left_wall,right_wall,right]) #只要大于right_wall，就可
                right+=1
            else:
                left=right
                right+=1
                while stack:
                    #print(left_wall,stack[-1][1])
                    ret+=left_wall-stack[-1][1]
                    #print(ret)
                    stack.pop()
        #print(ret)
        #print(stack)
        s=stack[::-1]
    
        #for i,n in reversed(stack): #说明右边没有更高的了，没有比left_wall高的了
        m=0
        for i in range(len(s)-1):
          

            #print(m,s[i][1],s[i+1][1])
            m=max(m,s[i][1])        
            ret+=max(0,m-s[i+1][1])
            #print(m-s[i+1][1])
        
        return ret
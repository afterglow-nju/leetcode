class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ret=-11
        fmax=[1]*len(nums)
        fmin=[1]*len(nums)
        for i in range(len(nums)):
            fmax[i]=max(fmax[i-1]*nums[i],fmin[i-1]*nums[i],nums[i])
            fmin[i]=min(fmax[i-1]*nums[i],fmin[i-1]*nums[i],nums[i])
            ret=max(ret,fmax[i])
        return ret
    

#纯数学
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        #f=[[0]*n for i in range(n)]
        ret=float('-inf')
        left,right=0,0
        m=[]
        t=[]
        tem=1
        #p=1 #positibe
        #n=1 #negative
        for i in nums:
            if i==1:
                ret=1
                del i

        while right<len(nums):
            if nums[right]<0:
                m.append(right)
                tem*=nums[right]
                t.append(tem)
            elif nums[right]>0:
                tem*=nums[right]
                t.append(tem)
            else:
                #print(nums[right],m[-1],t[-1],t[0],t[m[-1]-1])
                if t and t[-1]<0:
                    first=m[0]
                    last=m[-1]
                    #print(t,m,left,first-left,last-left)
                    ret=max(0,ret,t[last-1-left],t[-1]/t[first-left] if t[-1]!=t[first-left] else t[-1])
                elif t:
                    ret=max(ret,t[-1])
                else:
                    ret=max(0,ret)
                m,t=[],[]
                tem=1
                left=right+1
            right+=1
        
        #
        if t and t[-1]<0:
            
            first=m[0]
            last=m[-1]
            #print(t,m,left,first-left,last-left)
            ret=max(ret,t[last-left-1],t[-1]/t[first-left] if t[-1]!=t[first-left] else t[-1]) #last之前，第一个负的之前
        elif t:
            ret=max(ret,t[-1])
        return int(ret)
        '''
        for i in range(n):
            t=nums[i]
            ret=max(ret,t)
            for j in range(i+1,n):
                t*=nums[j]
                ret=max(ret,t)
        return ret
        '''
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        #nums.append(nums[0])
        size=nums.count(1)
        left,right=0,size-1
        if size==0:
            return 0
        
        
        count=nums[left:right+1].count(0)
        ret=count
        left+=1
        right+=1
        nums=nums+nums
        while right<len(nums)//2+size:
            
            #if nums[right-1]==0 and nums[right]==0:
            #    pass
            #if nums[right-1]==0 and nums[right]==1:
            #    count-=1
            #elif nums[right-1]==1 and nums[right]==0:
            #    count+=1
            if nums[right]==0:
                count+=1
            if nums[left-1]==0:# and nums[left]==1:
                count-=1
            #elif nums[left-1]==1 and nums[left]==0:
            #    count+=1
            '''
            if nums[left-1]==0:
                if nums[left]==1:
                    count-=1
            else:
                if nums[left]!=1:
                    count+=1
            
            '''
            #count=nums[left:right+1].count(0)
            #print(ret,count)
            ret=min(ret,count)
            left+=1
            right+=1
        return ret


        '''
        if len(nums)==1:
            return 0

        arr=[]
        left,right=0,0
        while right<len(nums):
            if nums[right]==1:
                right+=1
            else:
                if left!=right:
                    arr.append((right-1-left+1,left,right-1))
                left=right+1
                right+=1
        if len(arr)==0:
            return 0
        ret=0   
        if nums[-1]==0 or nums[0]==0:
            if nums[-1]==0:
                if arr[1][0]==1:
                    del arr[1]
                    arr[-1]
            arr.sort(reverse=True)
            L,R=arr[0][1],arr[0][2]
            #print(L,R)
            for i in range(1,len(arr)):
                l,r=arr[i][1],arr[i][2]
                if r<L:
                    ret+=L-r-1
                elif l>R:
                    ret+=l-R-1
                else:
                    assert(0)     
        else:

            l1,r1=arr[0][1],arr[0][2]
            l2,r2=arr[-1][1],arr[-1][2]
            arr[0]=(arr[0][0]+arr[-1][0],l2,r1)
            for i in range(1,len(arr)):
                l,r=arr[i][1],arr[i][2]
                ret+=min(L-r-1,l-R-1)
        return ret
        '''
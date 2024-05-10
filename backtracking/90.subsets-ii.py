class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        used=[0]*n
        ret=[]
        nums.sort()
        
        def back(ans,index,n):
            ret.append(ans[:])
            #print(ret,index)
            if index==n:
                return 
            for i in range(index,n):
                if not used[i]:
                    if i>0 and nums[i-1]==nums[i] and used[i-1]==0:
                        continue
                    used[i]=1
                    ans.append(nums[i])
                    back(ans,i+1,n) #应该是i+1，又忘了
                    ans.pop()
                    used[i]=0
        back([],0,n)
        return ret
#这样也行，不需要used数组
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #不重复的类的，一般是要排序的
        ret=[]
        nums.sort()

        def back(ans,index):
            ret.append(ans[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                ans.append(nums[i])
                back(ans,i+1)
                ans.pop()
        
        back([],0)
        return ret





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
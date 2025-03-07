class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret=[]
        def back(ans,index):
            #if index>=len(nums):
            #    return 

            ret.append(ans[:])

            for i in range(index,len(nums)):
                ans.append(nums[i])
                back(ans,i+1)
                ans.pop()
            
        back([],0)
        return ret
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ret=[]
        path=[]
        n=len(nums)
        def dfs(i):
            if i==n:
                ret.append(path[:])
                return 
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            return 
        dfs(0)
        return ret
        
        
        
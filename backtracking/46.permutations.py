class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret=[]
        used=[0]*len(nums)
        def back(depth,ans):
            if depth==len(nums):
                ret.append(ans[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=1
                    ans.append(nums[i])
                    back(depth+1,ans)
                    ans.pop()
                    used[i]=0
        back(0,[])
        return ret

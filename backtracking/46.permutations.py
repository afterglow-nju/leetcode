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


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret=[]
#想起来之前怎么做了，是新开一个bool数组，用来指示这个数字有无用过
        
        def permu(nmd,ans,d):
            if d==len(nums):
                ret.append(ans[:])
            for i in range(len(nums)):
                if not nmd[i]:
                    nmd[i]=1
                    ans.append(nums[i])
                    permu(nmd,ans,d+1)
                    ans.pop()
                    nmd[i]=0
            return

        nmd=[0]*len(nums)
        permu(nmd,[],0)
        return ret
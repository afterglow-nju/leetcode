class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        used=[0]*len(nums)
        nums.sort()

        def back(d,ans):
            if d==len(nums):
                ret.append(ans[:])
                return 

            for i in range(len(nums)):
                if not used[i]:
                    #print(i,used[i-1],ans)
                    if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                        #是continue而不是return的原因是，我之前return，是担心返回不全的ans，但其实不用，因为直接continue，它depth不会满，所以不会append，始终少一个
                        continue
                    used[i]=1
                    ans.append(nums[i])
                    back(d+1,ans)
                    ans.pop()
                    used[i]=0

        
        back(0,[])
        return ret
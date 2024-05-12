class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()#其实可以不用
        ret=[]

        def back(ans,now,index):
            if now==target:
                ret.append(ans[:])
                return
            if now>target:
                return 
            #print(now)
            for i in range(index,len(candidates)):
                ans.append(candidates[i])
                back(ans,now+candidates[i],i)#不是i+1，因为可以重复取
                ans.pop()

        back([],0,0)
        return ret
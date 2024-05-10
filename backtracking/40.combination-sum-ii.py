class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret=[]
        used=[0]*len(candidates)
        def back(ans,now,index):
            if now==target:
                ret.append(ans[:])
                return
            if now>target:
                return 
            #print(now)
            for i in range(index+1,len(candidates)):
                if i>0 and candidates[i]==candidates[i-1] and used[i-1]==0:
                    continue
                ans.append(candidates[i])
                used[i]=1
                back(ans,now+candidates[i],i)
                ans.pop()
                used[i]=0
        back([],0,-1)
        return ret

#不按顺序的，需要used回溯，应该排在前面的元素会出现在后面。比如排列
#按顺序的，就不需要往前看，直接一个for往当前值后面看就行 。比如求和
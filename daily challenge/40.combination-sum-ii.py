class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        candidates.sort()
        used=[0]*len(candidates)
        def back(ans,s,index):
            if s==target:
                ret.append(ans[:])
                return 
            if s>target:
                return 
            for i in range(index,len(candidates)):
                
                if i>0 and candidates[i-1]==candidates[i] and used[i-1]==0:# and ans and ans[-1]!=candidates[i]:
                    continue
                ans.append(candidates[i])
                used[i]=1
                back(ans,s+candidates[i],i+1) 
                ans.pop()
                used[i]=0
      
                
        back([],0,0)
        return ret
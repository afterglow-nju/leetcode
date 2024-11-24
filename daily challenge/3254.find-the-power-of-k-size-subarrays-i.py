class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ret=[]
        flag=False
        n=len(nums)
        nums=nums+nums
        for i in range(n-k+1):
            if not flag:
      
                f=True
                prev=nums[i]
                for j in range(i+1,i+k):
                    if nums[j]==prev+1:
                        prev=nums[j]
                        continue
                    else:
                        f=False
                        break
                if f:
                
                    ret.append(nums[i+k-1])
                    flag=True
                else:
                    ret.append(-1)
            else:
               
                if k>1 and nums[i+k-1]!=nums[i+k-2]+1:
                    flag=False
                    ret.append(-1)
                else:
                    ret.append(nums[i+k-1])
        return ret

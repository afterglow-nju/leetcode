class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        ret=[0]
        cnt = [0] * (max(nums) + k * 2) 
        def back(i):
            if i==len(nums):
                #print(cnt)
                ret[0]+=1
                return 

            t=nums[i]
            back(i+1)
            if cnt[t-k]==0 and cnt[t+k]==0:
                cnt[t]+=1
                back(i+1)
                cnt[t]-=1

      

        back(0)
        return ret[0]-1
    
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        ret=[0]
        nums=[i+k for i in nums]
        nums.sort()
        d=[0]*(max(nums)+k+1)
        def back(index):
            if index==len(nums):
                #print(d)
                ret[0]+=1
                return 
            back(index+1)
            #不要
            if d[nums[index]-k]==0 and d[nums[index]+k]==0:
                #要
                d[nums[index]]=1
                back(index+1)
                d[nums[index]]=0
                
            #else:
            #    back(index+1)


        back(0)
        return ret[0]-1
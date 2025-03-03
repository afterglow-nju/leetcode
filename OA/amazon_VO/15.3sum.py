class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        nums.sort()
        n=len(nums)
        #print(nums)
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            id1,id2=i+1,n-1
            #print(ret)
            while id1<id2:
                t=nums[i]+nums[id1]+nums[id2]
                if t==0:
                    ret.append([nums[i],nums[id1],nums[id2]])
                    id1+=1
                    id2-=1
                    while id1<id2 and nums[id1-1]==nums[id1]:
                        id1+=1
                    while id2>id1 and nums[id2+1]==nums[id2]:
                        id2-=1
                    
                elif t<0:
                    id1+=1
                else:
                    id2-=1
        return ret
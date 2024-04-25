class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret=[]
        for i,n in enumerate(nums):
            if n==nums[i-1] and i>=1:
                continue

            l=i+1
            r=len(nums)-1
            while l<r: #因为有这个条件限制，所以不用对i做限制防止越界
                #print(n,nums[l],nums[r])
                if n+nums[l]+nums[r]>0:
                    r-=1
                elif n+nums[l]+nums[r]<0:
                    l+=1
                else:
                    ret.append([n,nums[l],nums[r]])
                    tem=nums[l]
                    while nums[l]==tem and l<r:
                        l+=1
        return ret
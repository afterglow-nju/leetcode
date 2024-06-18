class Solution:
    def jump(self, nums: List[int]) -> int:
        dis=[i+nums[i] for i in range(len(nums))]

        ret=0
        i=0


        if len(nums)==1:
            return 0



        while i<len(nums):
            now=nums[i]
            tem,index=0,0
            for j in range(i+1,now+1+i):
                if j>=len(nums)-1:
                    ret+=1
                    return ret
                if dis[j]>=tem:
                    tem=dis[j]
                    index=j
            #print(i,index,tem)
            
            i=index
            ret+=1
        return ret
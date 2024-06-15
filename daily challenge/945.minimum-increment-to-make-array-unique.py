class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        ret=0
        #
        #print(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                t=nums[i-1]-nums[i]+1
                nums[i]=nums[i-1]+1
                ret+=t
                #print(i,t)
#nums[i]变成的值和t没有关系，因为增长那个都一样
        return ret

        '''
        s=set(nums)
        l=[i for i in range(min(nums),max(nums)+len(nums))]
        l=[i for i in l if i not in s]
        ret=0
        new=[]
        for i in nums:
            if i not in s:
                new.append(i)
            else:
                s.remove(i)
        j=0
        for i in range(0,len(new)):
            while l[j]-new[i]<=0:
                j+=1
            ret+=l[j]-new[i]
            j+=1
        return ret
        '''
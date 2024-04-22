class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic=dict() # value : index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in dic:
                return [dic[diff],i]
            dic[n]=i
        assert(0)
        #便遍历便寻找，不用考虑重复

        '''
        57 17.81
        dic=dict()
        for i in nums:
            dic[i]=dic.get(i,0)+1
        index1=[]
        tem=0
        for i in nums:
            t=target-i
            if dic.get(t,None) is not None :
                if t==i and dic[i]==1:
                    tem+=1
                    continue
                index1.append(tem)
            tem+=1
        return index1
        '''
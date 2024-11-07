class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        maxValue=max(i[0] for i in nums)
        q=[(x[0],i,0) for i,x in enumerate(nums)]
        heapq.heapify(q)
        ret=[-10**5,10**5]
        while True:
            minValue,row,index=heapq.heappop(q)
            if maxValue-minValue<ret[1]-ret[0]:
                ret[0],ret[1]=minValue,maxValue
            if index==len(nums[row])-1:
                break
            maxValue=max(maxValue,nums[row][index+1])
            heapq.heappush(q,(nums[row][index+1],row,index+1))
        return ret
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        for i in range(n):
            arr.append(nums[i])
            tem=nums[i]
            for j in range(i+1,n):
                tem+=nums[j]
                arr.append(tem)
                
        arr.sort()
        ret=0
        mod=1e9+7
        #print(len(arr))
        #assert(0)
        for i in range(left-1,right):
            ret+=arr[i]
            ret%=mod
        return int(ret)
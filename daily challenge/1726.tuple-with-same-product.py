class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        c=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                c[nums[i]*nums[j]]+=1
        ret=0
        for k,v in c.items():
            if v>=2:
                #print(k,v)
                ret+=v*(v-1)//2*8
        return ret
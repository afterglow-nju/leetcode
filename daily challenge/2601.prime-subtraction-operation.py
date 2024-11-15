class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        valid = [True] * 1001
        valid[0] = valid[1] = False
        for i in range(2, len(valid)):
            if valid[i]:
                for j in range(i * i, len(valid), i):
                    valid[j] = False
        primes = [i for i in range(len(valid)) if valid[i]]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                tem=bisect_right(primes,nums[i]-nums[i+1])
                if tem<len(primes):
                    nums[i]-=primes[tem]
                #print(tem,len(primes),primes[-1],nums[i],nums[i+1])
                if nums[i]<=0 or nums[i]>=nums[i+1]:
                    return False
        return True

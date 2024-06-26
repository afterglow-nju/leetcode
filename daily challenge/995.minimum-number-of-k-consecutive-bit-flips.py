class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ret=0
        #print(len(nums))
        
        n=len(nums)
        d=[0]*(n+1)
        cnt=0
        for i in range(n):
            cnt^=d[i]
            #print(cnt,nums[i],i)
            if cnt^nums[i]==0:
                d[i]^=1
                cnt^=1
                if i+k>n:
                    return -1
                d[i+k]^=1
                ret+=1

            
        return ret

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ret=0
        #print(len(nums))
        q=collections.deque()
        n=0
        for i in range(len(nums)):
            while q and q[0]+k-1<i:
                q.popleft()
                n-=1
            if (n%2==0 and nums[i]==1) or (n%2==1 and nums[i]==0):
                continue
            else:
                if i>len(nums)-k:
                    return -1
                ret+=1
                q.append(i)
                n+=1
                #print(i)
        #if q and q[0]+k>len(nums):
        #    print(q[0])
        #    return -1
        return ret
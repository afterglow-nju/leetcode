class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        d=defaultdict(set)
        pre=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2==1:
                pre[i]=pre[i-1]+1
            else:
                pre[i]=pre[i-1]
            d[pre[i]].add(i)
            
        ret=0
        #print(pre)
        for i in range(len(nums)):#begin with i, find j after i
            now=pre[i-1] if i>0 else 0
            target=k+now
            s=d[target]
            #print(now,target)
            for j in s:
                if j>=i:
                    ret+=1
        return ret
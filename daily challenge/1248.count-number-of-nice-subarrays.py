class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd=[0]*(len(nums)+1)
        ret=0
        O=0
        odd[0]=1
        #odd[i] stands for i odd number
        for i in range(len(nums)):
            if nums[i]%2==1:
                O+=1
            #print(O,odd)
            odd[O]+=1
            if O>=k:
                ret+=odd[O-k]
            
        #print(odd)
        return ret


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
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        d=defaultdict(dict)
        e=defaultdict(int)
        
        def get(x):
            ret=0
            for i in x:
                if x[i]!=0:
                    ret|=(1<<i)
            return ret

        for i in range(len(nums)):
            b=bin(nums[i])[2:][::-1]
            for j in range(len(b)):
                if b[j]=='1':
                    d[i][j]=1
        left,right=0,0
        ret=float('inf')
        
        while right<len(nums):
            #print(d[right],right)
            for j in d[right].keys():
                e[j]+=1

            if get(e)>=k:
                #ret=min(ret,right-left+1)
                while left<=right and get(e)>=k: 
                    #print(left,right,e,get(e))
                    ret=min(ret,right-left+1)   
                    for j in d[left].keys():
                        e[j]-=1
                    left+=1
                
            right+=1
        return ret if ret!=float('inf') else -1
            

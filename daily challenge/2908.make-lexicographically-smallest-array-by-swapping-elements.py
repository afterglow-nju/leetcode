class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        origin=nums[::]
        group=defaultdict(int)
        cnt=0
        nums.sort()
        group[nums[0]]=0
        num_group=defaultdict(lambda:[])
        num_group[0].append(nums[0])
        #print(num_group[0],type(num_group[0]))
        for i in range(1,len(nums)):
            if abs(nums[i]-nums[i-1])>limit:
                cnt+=1
            group[nums[i]]=cnt
            num_group[cnt].append(nums[i])
        for key,value in num_group.items():
            num_group[key]=deque(sorted(value))
        #print(origin)
        for i,x in enumerate(origin):
            g=num_group[group[x]]
            #print(x,g)
            origin[i]=g.popleft()
        return origin

        

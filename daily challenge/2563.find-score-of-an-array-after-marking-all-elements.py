class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            i0 = i
            while i + 1 < n and nums[i] > nums[i + 1]:  # 找到下坡的坡底
                i += 1
            for j in range(i, i0 - 1, -2):  # 从坡底 i 到坡顶 i0，每隔一个累加
                ans += nums[j]
            i += 2  # i 选了 i+1 不能选
        return ans


class Solution:
    def findScore(self, nums: List[int]) -> int:
        h=[]
        d=defaultdict(int)
        ret=0
        for i,x in enumerate(nums):
            h.append([x,i])
            d[i]=1
        heapq.heapify(h)
        while h:
            v=heapq.heappop(h)
            if d[v[1]]==1:
                #print(v[1])
                d[v[1]]=0
                ret+=v[0]
                d[max(0,v[1]-1)]=0
                d[min(len(nums)-1,v[1]+1)]=0
        return ret

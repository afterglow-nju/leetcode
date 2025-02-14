class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ret=0
        h=nums
        heapq.heapify(h)
        while h:
            #print(ret,h)
            a=heapq.heappop(h)
            if a>=k:
                break
            b=heapq.heappop(h)
            
            heapq.heappush(h,a*2+b)
            ret+=1
        return ret

        
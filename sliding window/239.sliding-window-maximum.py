class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #维护一个单调队列, 将index而不是value放进去
        #q=[]
        q=collections.deque()
        ret=[]
        for i in range(len(nums)):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
                #q.pop(-1)
            q.append(i)
            while q and q[0]+k<=i:
                q.popleft()
                #q.pop(0)
            ret.append(nums[q[0]])
        return ret[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret=[]
        queue=[] ###为了把窗口外的元素拿进来，queue放的是index
        for i in range(len(nums)):
            
            while queue and nums[i]>=nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i) 
            while queue and queue[0]<i-k+1:
                queue.pop(0)
                         
            ret.append(nums[queue[0]])
        return ret[k-1:]
            
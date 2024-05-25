class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #according to the master theorm, the time complexity is theta n
        n=len(nums)
        left,right=0,n-2
        total=n-1

        while True:
            print(left)
            while left < right and nums[left] == nums[left+1]: left += 1
            while right>left and nums[right]==nums[right-1]: right-=1
            total=right+1
            p=nums[total]
            while left<=right:
                if nums[left]<=p:
                    left+=1
                else:
                    nums[left],nums[right]=nums[right],nums[left]
                    right-=1
            #print(left,right,total,nums,p)
            #[0,rigth] [right+1,p-1] p
            res=total-right
            if res==k:
                return p
            elif res>k:
                right=total-2
                total=right+1
            else: #res<k
                left=0
                right-=1
                total=right+1
                k=k-res

        

        
        
        '''
        method 1
        heap=nums
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return heap[0]
        '''
        '''
        method 2
        heap=[]
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        
        return heap[0]
        '''
        '''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #according to the master theorm, the time complexity is theta n
        n=len(nums)
        left,right=0,n-1
        k=n-k
        while True:
            while left < right and left < right and nums[left] == nums[left+1]: left += 1
            p=nums[right]
            while left<right:
                while left<right and nums[left]<=p:
                    left+=1
                nums[right]=nums[left] #之前nums[right]=pviot，所以丢掉的是pviot
                while left<right and nums[right]>p:
                    right-=1
                nums[left]=nums[right]
            
            #[0,rigth] [right+1,p-1] p
            nums[left]=p
            #print(left,right,nums,p)
            if right==k:
                return p
            elif right<k:
                left+=1
                right=n-1
            else: #right>k
                left=0
                right-=1
        '''  

        
        
        '''
        method 1
        heap=nums
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return heap[0]
        '''
        '''
        method 2
        heap=[]
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        
        return heap[0]
        '''
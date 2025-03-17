class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]==0 and nums[-1]==0:
            return 0
        left,right=0,n-1
        ret=0
        id1,id2=0,n-1
        while left<=right:
            mid=(right-left)//2+left
            if mid+1<n:
                #print(mid,mid+1,nums[mid],nums[mid+1])
                if nums[mid]<0 and nums[mid+1]>=0:
                    id1=mid
                    break
                elif nums[mid]>=0:
                    right=mid-1
                elif nums[mid+1]<0:
                    left=mid+1
                else:
                    assert(0)
            else:
                #print(mid,'!')
                if nums[mid]<0:
                    id1=n-1
                else:
                    id1=0
                break

        left,right=0,n-1
        ret=0
        while left<=right:
            mid=(right-left)//2+left
            #print(mid-1,mid,nums[mid-1],nums[mid])
            if mid-1>=0:
                if nums[mid]>0 and nums[mid-1]<=0:
                    id2=mid
                    break
                elif nums[mid]<=0:
                    left=mid+1
                elif nums[mid-1]>0:
                    right=mid-1
                else:
                    #print(nums[mid],nums[mid-1])
                    assert(0)
            else:
                if nums[mid]<0:
                    id2=n-1
                else:
                    id2=0
                break
        #print(id1,id2)
        return max(id1+1,n-1-id2+1)
        

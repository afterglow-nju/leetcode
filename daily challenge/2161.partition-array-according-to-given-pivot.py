class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        ans=[pivot]*n
        left,right=0,n-1
        for i in nums:
            if i<pivot:
                ans[left]=i
                left+=1
            elif i>pivot:
                ans[right]=i
                right-=1
    
        ans=ans[:left]+ans[left:right+1]+ans[right+1:][::-1]
        return ans


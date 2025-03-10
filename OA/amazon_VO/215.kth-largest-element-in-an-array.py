class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left,right=0,n-1
        
        while True:
            #print(nums,k)
            pivot=random.choice(nums)
            small,equal,big=[],[],[]
            for i in nums:
                if i<pivot:
                    small.append(i)
                elif i>pivot:
                    big.append(i)
                else:
                    equal.append(i)
            #print(small,equal,big,pivot,k,len(equal)+len(big))
            if k<=len(big):
                nums=big
            elif k>len(equal)+len(big):
                nums=small
                k=k-len(equal)-len(big)
            else:
                return pivot
        assert(0)
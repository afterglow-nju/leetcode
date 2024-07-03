class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)&set(nums2)
        ret=[]
        d1,d2=defaultdict(int),defaultdict(int)
        for i in nums1:
            d1[i]+=1
        for i in nums2:
            d2[i]+=1
        for i in s:
            t=[i]*min(d1[i],d2[i])
            ret+=t
        return ret
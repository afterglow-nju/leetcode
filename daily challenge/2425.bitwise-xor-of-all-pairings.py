class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ret=0
        if len(nums1)%2==1:
            for i in nums2:
                ret^=i
        if len(nums2)%2==1:
            for i in nums1:
                ret^=i
        return ret
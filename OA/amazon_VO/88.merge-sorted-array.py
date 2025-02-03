class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1,index2=m-1,n-1
        index=m+n-1
        for i in range(m+n-1,-1,-1):
            if index1==-1 or (index2!=-1 and nums1[index1]<nums2[index2]):
                nums1[i]=nums2[index2]
                index2-=1
            else:
                nums1[i]=nums1[index1]
                index1-=1
    
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ret=[]
        id1,id2=0,0
        while id1<len(nums1) and id2<len(nums2):
            #print(id1,id2)
            if nums1[id1][0]==nums2[id2][0]:
                ret.append([nums1[id1][0],nums1[id1][1]+nums2[id2][1]])
                id1+=1
                id2+=1
            elif nums1[id1][0]<nums2[id2][0]:
                ret.append(nums1[id1])
                id1+=1
            else:
                ret.append(nums2[id2])
                id2+=1
        while id1<len(nums1):
            ret.append(nums1[id1])
            id1+=1
        while id2<len(nums2):
            ret.append(nums2[id2])
            id2+=1
        return ret
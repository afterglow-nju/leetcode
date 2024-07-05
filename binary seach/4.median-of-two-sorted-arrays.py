class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        #nums1 short, nums2 long
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin<=imax:
            i=(imin+imax)//2
            j=half_len-i
            if i<m and nums1[i]<nums2[j-1]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m+n)%2==1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                return (max_of_left+min_of_right)/2

        
        
        '''
        if len(nums1)<len(nums2):
            nusm1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        k=(m+n)//2
        left=0
        right=n1-1
        while left<right:
            t=k-left
            a=nums1[left+1]
            b=nums2[t]
            if a<b:
        '''
        '''
        def findk(k):
            target=k
            l1,r1=0,m-1
            l2,r2=0,n-1
            index=0
            while True:
                m1=min(l1+k//2-1,m-1)
                m2=min(l2+k//2-1,n-1)
                print(index,m1,m2,l1,l2,target)
                if index==target-1:
                    return min(nums1[m1],nums2[m2])

                
                if nums1[m1]<=nums2[m2]:
                    
                    index+=m1+1-l1
                    l1=m1+1
                    r2=m2
                else:
                    index+=m2+1-l2
                    l2=m2+1
                    r1=m1
        if (m+n)//2==(m+n)/2:
            return (findk((m+n)//2)+findk((m+n)//2-1))/2
        else:
            return findk((m+n)//2) 

        '''
class Solution:
    def minimizeXor(self, nums1: int, nums2: int) -> int:
        n1=nums1.bit_count()
        n2=nums2.bit_count()
        s=[]
        print(n2,bin(nums1))
        nums1=bin(nums1)[2:]
        diff=len(nums1)-n1
        tem=n2
        for i in range(len(nums1)):
            if tem>0 and nums1[i]=='1':
                s.append('1')
                tem-=1
            else:
                s.append('0')
        if tem>0:
            for i in range(len(s)-1,-1,-1):
                if s[i]=='0':
                    s[i]='1'
                    tem-=1
                if tem==0:
                    break
        if tem>0:
            for i in range(tem):
                s.append('1')
        #s=s[::-1]
        print(s)
        return int("".join(s),2)      
            
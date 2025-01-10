class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        c=Counter(nums)
        S=sum(nums)
        nums.sort(reverse=True)
        ret=0
        for i in nums:
            t=S-i
            #print(t)
            if t%2==0 and t//2 in c:
                if (i==t//2 and c[t//2]>=2) or (i!=t//2):
                    return i
        assert(0)








        
        
        '''
        total = sum(nums)
        counts = Counter(nums)

        outlier = float('-inf')

        for num in counts:
            p_outlier = total - 2 * num
            if p_outlier in counts:
                if counts[num] > 1 or p_outlier != num:
                    outlier = max(outlier, p_outlier)
        return outlier
        '''
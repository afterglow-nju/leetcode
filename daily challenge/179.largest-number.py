class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs=list(map(str,nums))
        def cmp(a,b):
            if a+b==b+a:
                return 0
            elif a+b<b+a:
                return -1
            else:
                return 1
        strs=sorted(strs,reverse=True, key=functools.cmp_to_key(cmp))
        return "".join(strs) if strs[0]!='0' else '0'
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        integer=[[] for _ in range(9)]
        for i in nums:
            if 0<=i<10:
                integer[0].append(i)
            elif 10<=i<100:
                integer[1].append(i)
            elif 100<=i<1000:
                integer[2].append(i)
            elif 1000<=i<10000:
                integer[3].append(i)
            elif 10000<=i<100000:
                integer[4].append(i)
            elif 100000<=i<1000000:
                integer[5].append(i)
            elif 1000000<=i<10000000:
                integer[6].append(i)
            elif 10000000<=i<100000000:
                integer[7].append(i)
            elif 100000000<=i<1000000000:
                integer[8].append(i)
        ret=""
        status=0
        for i in range(9):
            if integer[i]!=[]:
                status&=1<<i
        while status:
            tem=-1
            index=-1
            for i in range(9):
                if integer[i]!=[]:
                    if integer[i][-1]>tem:
                        tem=integer[i][-1]   
                        index=i
'''
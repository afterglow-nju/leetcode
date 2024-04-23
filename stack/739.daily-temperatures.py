class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        day=[]
        ret=[0]*len(temperatures)
        for i,n in enumerate(temperatures):
            while stack and stack[-1]<n:
                d=day.pop()
                stack.pop()
                ret[d]=i-d#+diff[d]
                #index+=ret[d]
                #diff[day[-1]]=index
            
            stack.append(n)
            day.append(i)

        return ret
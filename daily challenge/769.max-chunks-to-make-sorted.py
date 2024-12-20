class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        ret=0
        Max=-1
        
        pre=-1
        count=0
        for i in range(n):
            value=arr[i]
            #print(value,Max,count,pre,ret)
            if value<Max:
                count+=1
            else:
                
                Max=value
                count+=1
                max_index=i
            if count==Max-(pre+1)+1:
                ret+=1
                count=0
                pre=Max
                Max=-1
                
        if Max!=-1:
            ret+=1
        return ret
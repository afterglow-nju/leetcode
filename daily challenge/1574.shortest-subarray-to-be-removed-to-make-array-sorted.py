class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        prev=-1
        cur=arr[0]
        pre_idx=0
        prefix=[]
        while prev<=cur:
            prev=cur
            prefix.append(cur)
            #print(prefix,pre_idx)
            if pre_idx+1<len(arr):
                cur=arr[pre_idx+1]
                pre_idx+=1
            else:
                pre_idx+=1
                break
        pre_idx-=1
        #print(pre_idx,prefix)
        assert(pre_idx+1==len(prefix))
            
        prev=10**9+1
        cur=arr[-1]
        suf_idx=len(arr)-1
        suffix=[]
        #print(cur,prev)
        while prev>=cur:
            prev=cur
            suffix.append(cur)
            if suf_idx-1>=0:
                cur=arr[suf_idx-1]
                suf_idx-=1
            else:
                suf_idx-=1
                break
        suf_idx+=1
        suffix=suffix[::-1]
        ret=min(len(arr)-1-(pre_idx+1)+1,suf_idx-1-0+1)
        #print(len(suffix),len(prefix),suffix)
        for i in range(pre_idx+1):
            index=bisect.bisect_left(suffix,prefix[i])
            #print(prefix[i],suf_idx-1+index,index)
            if index<len(suffix):   
            #    print('!')
                ret=min(ret,suf_idx-1+index-(i+1)+1)
        return ret if ret>=0 else 0
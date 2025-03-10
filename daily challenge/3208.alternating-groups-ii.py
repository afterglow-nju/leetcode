class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        colors=colors+colors
        ret=0
        left,right=0,1
        while right<k+n-1:
            #print(right)
            if colors[right]!=colors[right-1]:
                right+=1
            else:
                #print('!')
                if right-left+1>=k:
                    ret+=right-(left+k-1)+1-1
                left=right
                right+=1
        if right-left+1>=k:
            ret+=right-(left+k-1)+1-1
        return ret

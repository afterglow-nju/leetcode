class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[0]
        for i in range(1,n+1):
            ret.append(ret[i>>1]+(i&1))
        return ret
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[0,1,1,2]
        index=2
        l=2
        while len(ret)<n+1:
            #print(ret,index,l)
            ret=ret+ret[index:index+l+1]+[i+1 for i in ret[index:index+l+1] ]
            
            index=index+l
            l<<=1
        return ret[:n+1]
'''
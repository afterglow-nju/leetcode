class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2==1:
            return -1
        if sum(skill)%(len(skill)//2)!=0:
            return -1
        target=sum(skill)//(len(skill)//2)
        d=defaultdict(int)
        for i in skill:
            d[i]+=1
        ret=0
        for i in d:
            if d[i]==0:
                continue
            
            if d[target-i]==d[i]:
                #print(d[i],i,target-i)
                if target-i!=i:
                    ret+=d[i]*((target-i)*i)
                    d[target-i]=0
                    d[i]=0
                else:
                    if d[i]%2==0:
                        ret+=(d[i]//2)*(i**2)
                        d[i]=0
                    else:
                        return -1
            
            else:
                #print(tem,i,target-i,d[target-i])
                return -1
        return ret
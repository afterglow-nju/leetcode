class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        d=defaultdict(int)
        h=defaultdict(int)
        direction=defaultdict(int)
        for i in range(len(positions)):
            d[positions[i]]=i
            h[positions[i]]=healths[i]
            direction[positions[i]]=-1 if directions[i]=='L' else 1
        s=[]
        positions.sort()
        for i in range(len(positions)):
            now=positions[i]
            if not s or (direction[now]*direction[s[-1]]>0 or direction[s[-1]]<0):
                s.append(now)
            else:
                #print("here")
                while s:
                    if direction[now]*direction[s[-1]]>0:
                        s.append(now)
                        break
                    elif h[s[-1]]>h[now]:
                        h[s[-1]]-=1
                        break
                    elif h[s[-1]]==h[now]:
                        s.pop()
                        break
                    else:
                        s.pop()
                        h[now]-=1
                        if not s:
                            #print("here")
                            s.append(now)
                            break
        remain=[(d[i],i) for i in s]
        remain.sort()
        #print(remain)
        return [h[i[1]] for i in remain]
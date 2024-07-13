class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s=[a[0]]
        for i in range(1,len(a)):
            now=a[i]
            if not s or (s and (s[-1]*now>0 or s[-1]<0 )):
                #print("!")
                s.append(now)
            else:
                flag=False
                while s:
                    if s[-1]*now>0:
                        s.append(now)
                        flag=False
                        break
                    elif s[-1]>-now:
                        flag=False
                        break
                    elif s[-1]==-now:
                        s.pop()
                        flag=False
                        break
                    else:
                        s.pop()
                        flag=True
                #print(s)
                if flag:
                #    print(now)
                    s.append(now)
        return s
                
            


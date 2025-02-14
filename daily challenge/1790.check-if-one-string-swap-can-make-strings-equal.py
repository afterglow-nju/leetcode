class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        r1,r2=[],[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
                if diff==1:
                    r1=[s1[i],s2[i]]
                elif diff==2:
                    r2=[s1[i],s2[i]]
                    if r1[0]==r2[1] and r2[0]==r1[1]:
                        continue
                    else:
                        return False
                else:
                    return False
        return diff in [0,2]
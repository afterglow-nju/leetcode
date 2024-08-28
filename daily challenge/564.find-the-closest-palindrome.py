class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)
        l = len(n)
        half, v, ov = n[:l//2], int(n[:(l+1)//2]), int(n)
        res = set()
        s1, s2 = str(v-1), str(v + 1)
        res.add("9" * (l - 1))
        res.add("1" + "0" * (l - 1) + "1")
        if l % 2:
            res.add(s1[:-1] + s1[-1] + s1[:-1][::-1])
            res.add(s2[:-1] + s2[-1] + s2[:-1][::-1])
        else:
            res.add(s1 + s1[::-1])
            res.add(s2 + s2[::-1])
        if n[::-1] != n:
            res.add(half + n[l//2] + half[::-1] if l % 2 else half + half[::-1])
        if n in res:
            res.remove(n)
        return min(res, key = lambda x:(abs((k:=int(x)) - ov), k))


'''
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        left,right=0,len(n)-1
        flag=True
        while left<right:
            if left==right:
                left+=1
                right-=1
            else:
                flag=False
                break
        if flag:
            n=n[:len(n)-1:]+str(int(n[-1])-1)

        

        if len(n)%2==1:
            #print(n[:len(n)//2],n[:len(n)//2:-1])
            return n[:len(n)//2+1]+"".join(reversed(n[:len(n)//2]))
        else:
            return n[:len(n)//2]+"".join(reversed(n[:len(n)//2]))
'''
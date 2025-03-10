class Solution:
    def f(self, word: str, k: int) -> int:
        cnt1 = defaultdict(int)  # 每种元音的个数
        ans = cnt2 = left = 0  # cnt2 维护辅音个数
        for b in word:
            if b in "aeiou":
                cnt1[b] += 1
            else:
                cnt2 += 1
            while len(cnt1) == 5 and cnt2 >= k:
                out = word[left]
                if out in "aeiou":
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        del cnt1[out]
                else:
                    cnt2 -= 1
                left += 1
            ans += left
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word, k) - self.f(word, k + 1)


'''
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ret=0
        flag=False
        cnt=0
        v=['a','e','i','o','u']
        d=defaultdict(int)
        left,right=0,0
        for i in range(len(word)):
            if word[i] in v:
                d[word[i]]+=1
                if len(d.keys())==5:
                    flag=True
            else:
                cnt+=1
            if flag and cnt==k:
                #print(left,i)
                ret+=1
            elif cnt>k:
                while cnt>k and left<=i:
                    if word[left] in v:
                        d[word[left]]-=1
                        if d[word[left]]==0:
                            del d[word[left]]
                            flag=False
                    else:
                        cnt-=1
                    left+=1
        while left<len(word) and flag and cnt==k:
            ret+=1
            if word[left] in v:
                d[word[left]]-=1
                if d[word[left]]==0:
                    break
            else:
                cnt-=1
                break
            left+=1
            

        return ret
'''
                
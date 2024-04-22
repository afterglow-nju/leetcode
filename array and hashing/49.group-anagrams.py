class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=dict()
        for i in strs:
            tem="".join(sorted(i))
            #print(tem,i)
            if tem in dic:
                dic[tem].append(i)
            else:
                dic[tem]=[i]
        #print(dic)
        return dic.values()
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=dict()
        for i in nums:
            dic[i]=dic.get(i,0)+1
        return list(dict(sorted(dic.items(), key=lambda item:item[1], reverse=True)).keys())[:k]
        dict(sorted(x.items(), key=lambda item: item[1]))
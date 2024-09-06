class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        dice=(len(rolls)+n)*mean-sum(rolls)
        if dice<n or dice>n*6:
            return []
        else:
            now=dice%n
            v=dice//n
            return now*[v+1]+(n-now)*[v]
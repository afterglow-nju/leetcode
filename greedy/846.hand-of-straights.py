用counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False
        hand.sort()
        d=Counter(hand)
        #for i in range(len(hand)):
        #    d[hand[i]]+=1
        for i in d.keys():
            if d[i]!=0:
                for j in range(i+groupSize-1,i-1,-1):
                    if d[j]>=d[i]:#d.get(j,None) and 
                        d[j]-=d[i]
                    else:
                        return False
        return  True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False
        hand.sort()
        d=defaultdict(int)
        for i in range(len(hand)):
            d[hand[i]]+=1
        for i in d.keys():
            if d[i]!=0:
                for j in range(i+groupSize-1,i-1,-1):
                    if d.get(j,None) and d[j]>=d[i]:
                        d[j]-=d[i]
                    else:
                        return False
        return  True
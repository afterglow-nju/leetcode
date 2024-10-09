class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s1)<len(s2):
            s1,s2=s2,s1
        l1=s1.split(" ")
        l2=s2.split(" ")

        #print(l2,l1[0:len(l2)],l1[len(l1)-len(l2):len(l1)])
        if l2==l1[0:len(l2)] or l2==l1[len(l1)-len(l2):len(l1)]:
            return True

        
        for i in range(len(l2)):
            if l2[i]==l1[i]:
                if l2[i+1:len(l2)]==l1[len(l1)-(len(l2)-i-1):len(l1)]:
                    return True
            else:
                return False
      
class Solution:
    def isArraySpecial(self , A , Q):
        q=[0]*len(A)
        left=0
        index=0
        for right in range(1,len(A)):
            #print(right,index,A[right] , A[index],(A[right]&1) + (A[index]&1))
            if (A[right]&1) + (A[index]&1)==1:
                index=right
                continue
            else:
                while left<=right-1:
                    q[left]=right-1
                    left+=1
                index=right
        #print(left,q)
        while left<len(A):
            q[left]=len(A)-1
            left+=1
        #print(q)
        ret=[]
        for i in Q:
            if i[1]<=q[i[0]]:
                ret.append(True)
            else:
                ret.append(False)
        return ret
class Solution:
    def averageWaitingTime(self, cus: List[List[int]]) -> float:
        

        ret=cus[0][1]
        finish=cus[0][0]+cus[0][1]
        for i in range(1,len(cus)):
            if cus[i][0]>=finish:
                ret+=cus[i][1]
                finish=cus[i][0]+cus[i][1]
            else:
                ret+=finish-cus[i][0]+cus[i][1]
                finish=finish+cus[i][1]
            #print(ret[i])
        return ret/len(cus)

        '''
        ret=[0]*len(cus)
        ret[0]=cus[0][1]
        finish=cus[0][0]+cus[0][1]
        for i in range(1,len(cus)):
            if cus[i][0]>=finish:
                ret[i]=cus[i][1]
                finish=cus[i][0]+cus[i][1]
            else:
                ret[i]=finish-cus[i][0]+cus[i][1]
                finish=finish+cus[i][1]
            #print(ret[i])
        return sum(ret)/len(cus)
        '''
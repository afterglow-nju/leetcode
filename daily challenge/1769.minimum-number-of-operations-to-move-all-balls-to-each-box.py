class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ret=[]
        left,right=0,0
        lc,rc=0,0
        index=0
        for i in range(len(boxes)):
            if boxes[i]=='1':
                right+=i
                rc+=1
        
        
        while index<len(boxes):
            #print(index,left,right,rc)
            ret.append(left+right)
            left+=lc
            
            if boxes[index]=='1':
                left+=1
                #right-=1
                lc+=1
                rc-=1
            right-=rc
            
            index+=1
        return ret
        '''
        ret=[]
        for i in range(len(boxes)):
            left,right=i-1,i+1
            tem=0
            for j in range(left+1):
                if boxes[j]=='1':
                    tem+=i-j
            for j in range(right,len(boxes)):
                if boxes[j]=='1':
                    tem+=j-i
            ret.append(tem)
        return ret
        '''
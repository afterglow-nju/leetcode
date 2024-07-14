class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d=defaultdict(int)
        s=[]
        i=0
        while i < len(formula):
            word=formula[i]
            if 'A'<=word<='Z':
                index=i
                while index+1<len(formula) and 'a'<=formula[index+1]<='z':
                    index+=1
                s.append([formula[i:index+1],1])
                i=index+1

            elif '0'<=word<='9':
                index=i
                while index+1<len(formula) and '0'<=formula[index+1]<='9':
                    index+=1
                num=int(formula[i:index+1])
                i=index+1
                if s[-1][0]==')':
                    s.pop()
                    tem_stack=[]
                    while s[-1][0]!='(':
                        tem=s.pop()
                        tem_stack.append([tem[0],tem[1]*num])
                        #d[tem[0]]+=tem[1]*num
                    s.pop()
                    s+=tem_stack
                else:
                    s[-1][1]=num
            else:
                assert(word=='(' or word==')')
                s.append((word,float('inf')))
                i+=1
        while s:
            tem=s.pop()
            #print(tem)
            d[tem[0]]+=tem[1]
        d.pop('(',None)
        d.pop(')',None)
        ret=''
        #print(d,d.items())
        for i in sorted(d.items()):
            ret+=i[0]
            if i[1]!=1:
                ret+=str(i[1])
        return ret

class Solution:
    def minimumDeletions(self, s: str) -> int:
        f,cnt_b=0,0
        for i in s:
            if i=='b':
                cnt_b+=1
            else:
                f=min(f+1,cnt_b)
        return f
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        d=[[0,0,0,0]]*len(s)
        # 前a 后b 前b 后a
        
        ret=0
        if s[0]=='a':
            d[0][0]=1
            for i in s:
                if i=='b':
                    d[0][1]+=1
                if i=='a':
                    d[0][3]+=1
            d[0][3]-=1
            ret=min(d[0][2]+d[0][3],d[0][2]+d[0][1],d[0][0]+d[0][3])
        else:
            d[0][2]=1
            for i in s:
                if i=='b':
                    d[0][1]+=1
                if i=='a':
                    d[0][3]+=1
            d[0][1]-=1
            ret=min(d[0][2]-1+d[0][3],d[0][2]+d[0][1],d[0][0]+d[0][3])
        for i in range(1,len(s)):
            if s[i]=='a':
                #d[i][0]=d[i-1][0]+1
                #d[i][1]=d[i-1][1]
                d[i][2]=d[i-1][2]
                d[i][3]=d[i-1][3]-1
                ret=min(ret,d[i][2]+d[i][3])#,d[i][2]+d[i][1],d[i][0]+d[i][3])
            else:
                #d[i][0]=d[i-1][0]
                #d[i][1]=d[i-1][1]-1
                d[i][2]=d[i-1][2]+1
                d[i][3]=d[i-1][3]
                ret=min(ret,d[i][2]-1+d[i][3])#,d[i][2]+d[i][1],d[i][0]+d[i][3])
            #print(s[i],d[i],ret)
        return ret
'''
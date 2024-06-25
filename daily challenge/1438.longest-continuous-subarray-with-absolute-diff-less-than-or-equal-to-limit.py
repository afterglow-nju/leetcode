class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ret=0
        n=len(nums)
        t=limit

        qmax=collections.deque()
        qmin=collections.deque()
        left=0
        #qmax.append(0)
        #qmin.append(0)
        i=0
        while i < n:
            #print("?",nums[i],qmax[-1],qmin[-1])
            while qmax and nums[qmax[-1]]<nums[i]: #这里注意，不能小于等于！！
                qmax.pop()
            while qmin and nums[qmin[-1]]>nums[i]: #
                qmin.pop()
            
            qmin.append(i)
            qmax.append(i)
            while qmax and qmin and nums[qmax[0]]-nums[qmin[0]]>limit:
                if nums[qmax[0]]==nums[left]:
                    qmax.popleft()
                if nums[qmin[0]]==nums[left]:
                    qmin.popleft()
                left+=1
            ret=max(ret,i-left+1)
            i+=1
        
        return ret

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ret=1
        n=len(nums)

        def divide(t):
            qmax=collections.deque()
            qmin=collections.deque()
            left=0
            qmax.append(0)
            qmin.append(0)
            for i in range(1,n):
                #print("?",nums[i],qmax[-1],qmin[-1])
                while qmax and nums[qmax[-1]]<=nums[i]:
                    qmax.pop()
                qmax.append(i)
                while qmax and qmax[0]+t<=i:
                    qmax.popleft()

                while qmin and nums[qmin[-1]]>=nums[i]:
                    qmin.pop()
                qmin.append(i)
                while qmin and qmin[0]+t<=i:
                    qmin.popleft()
                #print(qmax[0],qmin[0],t)
                if nums[qmax[0]]-nums[qmin[0]]<=limit:
                    if i>=t-1:
                        return True
            return False
        
        l,r=1,n
        Flag=False
        while l<=r:

            mid=(r-l)//2+l
            #print("here",l,r,mid)
            
            if divide(mid):
                l=mid+1
                ret=mid
                Flag=False
                #print("yes")
            else:
                r=mid-1
                Flag=True
                #print("no")
        #if Flag:
        #    ret-=1
        return ret
                
                    
        '''
        left,right=0,1
        heapmax,heapmin=[(-nums[0],0)],[(nums[0],0)]
        heapq.heapify(heapmax)
        heapq.heapify(heapmin)
        trash1,trash2=float('inf'),float('inf')
        length=1
        while right<n:
            #print(right)
            while True and heapmax and heapmin:
                Max=max(-heapmax[0][0],nums[right])
                Min=min(heapmin[0][0],nums[right])
                print(Max,Min,right,heapmax[0][1],heapmin[0][1])
                if Max-Min<=limit and heapmax[0][1]>=trash1 and heapmin[0][1]>=trash2:
                    trash1=min(trash1,heapmax[0][1])
                    trash2=min(trash2,heapmin[0][1])
                    heapq.heappush(heapmax,(-nums[right],right))
                    heapq.heappush(heapmin,(nums[right],right))
                    ret=max(ret,right-min(trash1,trash2)+1)
                    right+=1
                    break
                else:
                    if Max-Min>limit:
                        if heapmax[0][1]<=heapmin[0][1]:
                            heapq.heappop(heapmax)
                            trash1=heapmax[0][1] if heapmax else 0
                        else:
                            heapq.heappop(heapmin)
                            trash2=heapmin[0][1] if heapmin else 0
                    else:
                        trash1=max(trash1,heapmax[0][1])
                        trash2=max(trash2,heapmin[0][1])

                        if heapmax[0][1]<trash1:
                            heapq.heappop(heapmax)
                        elif heapmin[0][1]<trash2:
                            heapq.heappop(heapmin)
                        else:
                            assert(0)
            if not heapmax or not heapmin:
                heapmax,heapmin=[(-nums[right],right)],[(nums[right],right)]
                heapq.heapify(heapmax)
                heapq.heapify(heapmin)
                trash1,trash2=right,right
        return ret
        '''         
        '''
        dp=[[[0,0,0]]*n for _ in range(n)]
        for i in range(n):
            dp[i][i][0]=0
            dp[i][i][1]=nums[i]-limit
            dp[i][i][2]=nums[i]+limit
        
        for i in range(n):
            for j in range(i+1,n):
                t=dp[i][j-1]
                if t[1]<=nums[j]<=t[2]:
                    dp[i][j]=[1,max(t[1],nums[j]-limit),min(t[2],nums[j]+limit)]
                    ret=max(ret,j-i+1)
                else:
                    break
        return ret
        '''
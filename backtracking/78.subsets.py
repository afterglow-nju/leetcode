class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        import copy

        for i in range(0,len(nums)):
            #print(ans)
            t=copy.deepcopy(ans) #t是没有i的
            for j in ans:
                j.append(nums[i])
            #ans.append([nums[i]])
            ans+=t #因为 ans t的元素是list，直接拼接即可
            #地位一样，就是+；地位一个是list一个是element，就是append

                

        return ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret=[]
        def back(ans,index):
            #if index>=len(nums):
            #    return 

            ret.append(ans[:])

            for i in range(index,len(nums)):
                ans.append(nums[i])
                back(ans,i+1)
                ans.pop()
            
        back([],0)
        return ret


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        import copy

        for i in range(0,len(nums)):
            #print(ans)
            t=copy.deepcopy(ans) #t是没有i的
            for j in ans:
                j.append(nums[i])
            #ans.append([nums[i]])
            ans+=t #因为 ans t的元素是list，直接拼接即可
            #地位一样，就是+；地位一个是list一个是element，就是append

                

        return ans

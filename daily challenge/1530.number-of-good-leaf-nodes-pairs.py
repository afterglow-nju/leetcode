# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        leaf=[]
        parent=defaultdict(TreeNode)
        ans=[0]
        def dfs(node):
            dis=[0]*(distance+1)
            if not node:
                return dis
            if not node.left and not node.right:
                dis[0]=1
                return dis
            leftDepths, rightDepths = [0] * (distance + 1), [0] * (distance + 1)
            if node.left:
                leftDepths=dfs(node.left)
            if node.right:
                rightDepths=dfs(node.right)
            for i in range(distance):
                dis[i+1]+=leftDepths[i]
                dis[i+1]+=rightDepths[i]
                
            for i in range(distance+1):
                for j in range(distance-i-1):
                    ans[0]+=leftDepths[i]*rightDepths[j]

            return dis
        dfs(root)
        return ans[0]

        
        '''
        path=defaultdict(list)
        nums=[0]

        def dfs(node,p):
            if not node:
                return 
            if not node.left and not node.right:
                #print(node.val)
                path[nums[0]]=p
                nums[0]+=1
                return
            #print(p)
            dfs(node.left,p+['L'])
            #p.pop()
            dfs(node.right,p+['R'])
            #p.pop()
        
        dfs(root,[])
        ans=0

        #path=dict(sorted(path.items(),key=lambda y: y[1]))
        #print(path.keys(),nums[0])
        for i in range(nums[0]):
            for j in range(i+1,nums[0]):
                index=0
                while index<min(len(path[i]),len(path[j])):
                    if path[i][index]==path[j][index]:
                        index+=1
                    else:
                        break
                if len(path[i])+len(path[j])-2*index<=distance:
                    #print(index,i,j,path[i],path[j],distance,len(path[i])+len(path[j])-2*index)
                    ans+=1
                
        return ans
            
        '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        path=defaultdict(list)
        nums=[0]

        def dfs(node,p):
            if not node:
                return 
            if not node.left and not node.right:
                #print(node.val)
                path[nums[0]]=p
                nums[0]+=1
                return
            #print(p)
            dfs(node.left,p+['L'])
            #p.pop()
            dfs(node.right,p+['R'])
            #p.pop()
        
        dfs(root,[])
        ans=0

        #path=dict(sorted(path.items(),key=lambda y: y[1]))
        #print(path.keys(),nums[0])
        for i in range(nums[0]):
            for j in range(i+1,nums[0]):
                index=0
                while index<min(len(path[i]),len(path[j])):
                    if path[i][index]==path[j][index]:
                        index+=1
                    else:
                        break
                if len(path[i])+len(path[j])-2*index<=distance:
                    #print(index,i,j,path[i],path[j],distance,len(path[i])+len(path[j])-2*index)
                    ans+=1
                
        return ans
            

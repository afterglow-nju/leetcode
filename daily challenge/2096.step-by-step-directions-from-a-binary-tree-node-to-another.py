# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find(node,target,s):
            if node.val==target:
                return True
            if node.left and find(node.left,target,s):
                s+='L'
            elif node.right and find(node.right,target,s):
                s+='R'
            return s
            
        s1,s2=[],[]
        find(root,startValue,s1)
        find(root,destValue,s2)
        index=0
        print("?",s1,s2)
        
        while s1 and s2 and s1[-1]==s2[-1]:
            s1.pop()
            s2.pop()
        s="U"*(len(s1))+"".join(reversed(s2))
        return s
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, node: Optional[TreeNode], startValue: int, destValue: int) -> str:
        find=[0]
        path1,path2=[],[]
        def bfs(node,path,value):
            global path1
            if node.val==value:
                return True,path
            f1,f2=False,False
            p1,p2=[],[]

            if not node.left and not node.right:
                return False,[]
            if node.left:
                f1,p1=bfs(node.left,path+['L'],value)
            if node.right:
                f2,p2=bfs(node.right,path+['R'],value)
            if find[0]==1:
                #print('12',path1)
                return True,path1
            if f1:
                find[0]=1
                path1=p1
                #print('!',p1)
                return True,p1
            if f2:
                find[0]=1
                path1=p2
                #print("?")
                return True,p2
            return False,[]

        _,path1=bfs(node,[],startValue)
        #print('!!')
        find[0]=0
        _,path2=bfs(node,[],destValue)
        print(path1,path2)
        index=0
        path1=path1[::-1]
        path2=path2[::-1]
        while path1 and path2:
            if path1[-1]==path2[-1]:
                path1.pop()
                path2.pop()
            else:
                break
            
        return "".join(['U']*len(path1)+path2[::-1])
        assert(0)

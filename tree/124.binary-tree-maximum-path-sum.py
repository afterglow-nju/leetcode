# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         self.len=val # stand for the max path that pass this node
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret=[root.val]
        def path(node):
            l=node.left
            r=node.right
            if not l and not r:
                return node.val
            if l and r:
                m1=path(l)
                m2=path(r)
                n=node.val
                ret[0]=max(ret[0],m1,m2,m1+n,m2+n,m1+m2+n,n) #6种可能
                node.len=max(m1+n,m2+n,n)
                return node.len
            else:
                if not r:
                    m1=path(l)
                if not l:
                    m1=path(r)
                n=node.val
                ret[0]=max(ret[0],m1,m1+n,n)
                node.len=max(m1+n,n)
                return node.len
        path(root)
        return ret[0]
    
这样更简单
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         self.len=val # stand for the max path that pass this node
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret=[float('-inf')]
        def path(node):
            if not node:
                return 0
            l=node.left
            r=node.right
            m1=max(0,path(l))
            m2=max(0,path(r))
            n=node.val
            ret[0]=max(ret[0],m1+m2+n) #6种可能
            node.len=max(m1+n,m2+n,n) #返回单边最大
            return node.len
            
        path(root)
        return ret[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        f=dict()
        f[root.val]=None
        def dfs(node):
            if not node:
                return 
            if node.left:
                f[node.left.val]=node
                dfs(node.left)
            if node.right:
                f[node.right.val]=node
                dfs(node.right)
            return 
        dfs(root)
        vis=dict()
        while p:
            vis[p.val]=True
            p=f[p.val]
        while q:
            if q.val in vis:
                return q
            q=f[q.val]
        assert(0)
        
        
        
        
        
        
        
        
        
        
        
        '''
        p1,p2=[],[]
        def find(n,now,p,r):
            if not now:
                return 
            if now.val==n.val:
                p=p+[now]
                r.extend(p)
                return
            find(n,now.left,p+[now],r)
            find(n,now.right,p+[now],r)
        find(p,root,[],p1)
        cnt=
        
        assert(0)
        '''


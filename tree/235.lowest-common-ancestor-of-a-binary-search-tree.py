# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #因为保证一定存在，所以不用考虑为None的情况
        #BST 二叉搜索树的性质就是，左节点<父节点<右节点
        def lca(p,q,r):
            if p.val<=r.val<=q.val:
                return r
            elif p.val<q.val<r.val:
                return lca(p,q,r.left)
            else:
                return lca(p,q,r.right)
        if p.val>q.val:
            p,q=q,p
        return lca(p,q,root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(n1,n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            
            l1,r1=n1.left,n1.right
            l2,r2=n2.left,n2.right
            b1=same(l1,l2)
            b2=same(r1,r2)

            return b1 and b2 and n1.val==n2.val
        
        def subtree(root,s):
            if not root and not s:
                return True
            elif not root or not s:
                return False
            l=root.left
            r=root.right
            b1=same(root,s)
            b2=subtree(l,s)
            b3=subtree(r,s)
            
            return b1 or b2 or b3
        return subtree(root,subRoot)
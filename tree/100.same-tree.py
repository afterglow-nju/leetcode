# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
        return same(p,q)
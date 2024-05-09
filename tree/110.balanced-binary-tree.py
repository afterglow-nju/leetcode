# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret=1
        def depth(node,d):
            nonlocal ret
            if not node :
                return d
            left=node.left
            right=node.right
            t1=depth(left,d+1)
            t2=depth(right,d+1)
            #print(t1,t2)
            if abs(t1-t2)>1:
                ret=0

            return max(t1,t2)
        depth(root,0)
        if ret:
            return True
        else:
            return False

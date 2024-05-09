# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret=0
        def depth(node,d,index):
            if not node :
                return d
            left=node.left
            right=node.right
            t1=depth(left,d+1,index+1)
            t2=depth(right,d+1,index+1)
            nonlocal ret
            #print(t1,t2,index,t1-1+t2-1-index,ret)
            ret=max(ret,t1-1+t2-1-2*index)
            return max(t1,t2)
        depth(root,0,0)
        return ret
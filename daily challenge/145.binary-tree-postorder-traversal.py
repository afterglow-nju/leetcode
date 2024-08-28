# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret=[]
        def back(root):
            if not root:
                return 
            back(root.left)
            back(root.right)
            ret.append(root.val)
            
        back(root)
        return ret
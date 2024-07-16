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
        
        
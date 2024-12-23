# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root
        
        q1,q2=[root],[root.left,root.right]
        level=0
        while q1:
            if level&1==0:
                q2=q2[::-1]
                for i in range(len(q1)):
                    q1[i].left=q2[i*2]
                    q1[i].right=q2[i*2+1]
                q2=q2[::-1]
            else:
                q1=q1[::-1]
                for i in range(len(q1)):
                    q1[i].left=q2[i*2]
                    q1[i].right=q2[i*2+1]
            level+=1
            q1=q2
            q2=[]
            for i in q1:
                if not i.left:
                    return root
                q2.append(i.left)
                q2.append(i.right)
            
        assert(0)
        return root

            
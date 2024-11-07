# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        else:
            if root1 and root2:
                if root1.val==root2.val:
                    return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))
                else:
                    return False
            
            else:
                return False

        '''
        q1=[root1] if root1 else []
        q2=[root2] if root2 else []
        if root1 and root2:
            if root1.val!=root2.val:
                return False
        while q1 and q2:
            t1,t2=[],[]
            for i in q1:
                if i.left:
                    t1.append(i.left)
                if i.right:
                    t1.append(i.right)
            for i in q2:
                if i.left:
                    t2.append(i.left)
                if i.right:
                    t2.append(i.right)
            q1=t1
            q2=t2
            q1.sort(key=lambda x:x.val)
            q2.sort(key=lambda x:x.val)
            #print(q1,q2)
            if len(q1)==len(q2):
                for i in range(len(q1)):
                    if q1[i].val==q2[i].val:
                        continue
                    else:
                        return False
            else:
                return False
        return q1==q2
        
        '''
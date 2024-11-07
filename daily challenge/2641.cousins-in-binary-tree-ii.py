# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Sum=[]
        q=[root]
        depth=1
        while q:
            tem=[]
            t=0
            while q:
                t+=q[-1].val
                if q[-1].left:
                    tem.append(q[-1].left)
                if q[-1].right:
                    tem.append(q[-1].right)
                q.pop()
            Sum.append(t)
            q=tem
        root.val=0
        q=[root]
        #print(Sum)
        while q:
            tem=[]
            while q:
                p=q.pop()
                if p.left and p.right:
                    p.left.val=Sum[depth]-p.left.val-p.right.val
                    p.right.val=p.left.val
                    tem.append(p.left)
                    tem.append(p.right)
                    
                else:
                    if p.left:
                        p.left.val=Sum[depth]-p.left.val
                        tem.append(p.left)
                    if p.right:
                        p.right.val=Sum[depth]-p.right.val 
                        tem.append(p.right)   
            q=tem
            depth+=1
            
        return root
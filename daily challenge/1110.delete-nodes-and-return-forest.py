# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        ret=[]
        q=deque()
        q.append(root)

        def delete(node):
            if not node:
                return
            if node.left and node.left.val in to_delete:
                q.append(node.left.left)
                q.append(node.left.right)
                node.left=None
            else:
                delete(node.left)
            if node.right and node.right.val in to_delete:
                q.append(node.right.left)
                q.append(node.right.right)
                node.right=None
            else:
                delete(node.right)

        
        while q:
            node=q.pop()
            if not node:
                continue
            if node.val in to_delete:
                q.append(node.left)
                q.append(node.right)
            else:
                ret.append(node)
                delete(node)
                
        return ret
                

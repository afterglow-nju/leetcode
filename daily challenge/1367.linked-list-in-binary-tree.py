# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        ret=[0]
        def dfs(node,cur):
            
            if not cur:
                ret[0]=1
                return True
            if not node:
                return False
                
            if node.val==cur.val:
                return dfs(node.left,cur.next) or dfs(node.right,cur.next)
            else:
                return False
            
        def is_sub(node,cur):
            if not node:
                return False
            if not head:
                return True
            return dfs(node,cur) or is_sub(node.right,cur) or is_sub(node.left,cur)
        
        
        return is_sub(root,head)
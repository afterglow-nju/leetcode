# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q=deque()
        q.append(root)
        ret=[]
        while q:
            l=len(q)
            for i in range(l):
        #如果要记录层数，就把q清空。如果不需要记录层数，直接while q，就行
                t=q.popleft()
                if not t:
                    ret.append(None)
                else:
                    ret.append(t.val)
                    #if t.left: 
                    q.append(t.left) 
                    #if t.right: 
                    q.append(t.right)
        #print(ret)
        return str(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ret=eval(data)
        q=deque()
        index=0
        root=TreeNode(ret[0])
        if ret[0]==None:
            return []
        q.append(root)
        total_len=len(ret)
        #print(ret)
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if index==total_len-1:
                    #print(root)
                    return root
                left=ret[index+1]
                right=ret[index+2]
                index=index+2
                if left!=None:
                    n1=TreeNode(left)
                    node.left=n1
                    q.append(n1)
                if right!=None:
                    n2=TreeNode(right)
                    node.right=n2
                    q.append(n2)
        
        return root
                
                
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))










# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
没成功，想用前序中序复原的，但是str转换不回去list
import ast

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre,ino=[],[]
        def dfs(node):
            if not node:
                return 
            pre.append(node)#.val)
            dfs(node.left)
            ino.append(node)#.val)
            dfs(node.right)
        dfs(root)
        return str(pre)+'#'+str(ino)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        t=data.split('#')
        preorder=ast.literal_eval(t[0])
        inorder=ast.literal_eval(t[1])
        #print(preorder[0],"!!!!!!")
        def dfs(preorder,inorder):
            if not preorder:
                return None
            root=TreeNode(preorder[0])
            index=inorder.index(preorder[0])
            root.left=dfs(preorder[1:index+1],inorder[0:index])
            root.right=dfs(preorder[index+1:],inorder[index+1:])
            return root
        
        return dfs(preorder,inorder)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
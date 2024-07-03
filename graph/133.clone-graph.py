"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #就给一个节点，因为是连通图
        d=defaultdict(int)
        def bfs(node):
            if not node or not node.val:
                return False
            elif d[node.val]!=0:
                return d[node.val]
            else:
                t=Node(node.val)
                d[node.val]=t

                for i in node.neighbors:
                    tem=bfs(i)
                    if not tem:
                        continue
                    else:
                        d[node.val].neighbors.append(tem)
                return t
        if not node:
            return node
        return bfs(node)
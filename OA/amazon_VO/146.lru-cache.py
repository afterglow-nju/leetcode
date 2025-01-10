class Node:
    def __init__(self,key=None,value=None,prev=None,nxt=None):
        self.key=key
        self.val=value
        self.prev=prev
        self.nxt=nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        self.nowc=0
        self.d=defaultdict(Node)
        self.head=Node()
        self.tail=Node()
        self.head.nxt=self.tail
        self.tail.prev=self.head
    
    def move_to_left(self,node):
        node.prev.nxt=node.nxt
        node.nxt.prev=node.prev
        self.tail.prev.nxt=node
        node.prev=self.tail.prev
        node.nxt=self.tail
        self.tail.prev=node

    def print_list(self):
        cur=self.head
        while cur:
            print(cur.key)
            cur=cur.nxt

    def get(self, key: int) -> int:
        if key in self.d:
            node=self.d[key]
            self.move_to_left(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node=self.d[key]
            node.val=value
            self.move_to_left(node)
        else:
            if self.nowc<self.c:
                self.nowc+=1
            else:
                #self.print_list()
                
                dnode=self.head.nxt
                self.head.nxt=dnode.nxt
                dnode.nxt.prev=self.head
                #print(dnode.key)
                del self.d[dnode.key]
            
            node=Node(key,value)
            node.prev=self.tail.prev
            node.nxt=self.tail
            self.tail.prev.nxt=node
            self.tail.prev=node
            self.d[key]=node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
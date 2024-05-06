class Node:
    def __init__(self, key=None,value=None):
        self.key = key
        self.value=value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.d=dict() 
        self.l=[]
        self.total=0
        self.capacity=capacity
        self.head=Node()
        self.tail=Node()
        self.tail.prev=self.head
        self.head.next=self.tail

    def move_back(self,key:int):
        node=self.d[key]
        node.prev.next=node.next
        node.next.prev=node.prev
        self.tail.prev.next=node
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev=node
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.move_back(key)
            return self.d[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        
        a=self.d.get(key,None)
        if key in self.d:
            self.d[key].value=value
            self.move_back(key)
            self.total-=1
        else:
            newnode=Node(key,value)
            newnode.prev=self.tail.prev
            self.tail.prev.next=newnode
            newnode.next=self.tail
            newnode.prev=self.tail.prev
            self.tail.prev=newnode
            
            self.d[key]=newnode
        #print(self.head.next.key,self.head.next.next.key)
        if self.total>=self.capacity:
            #print("here")
            k=self.head.next.key
            self.d.pop(k)
            self.head.next=self.head.next.next
            self.head.next.prev=self.head
            self.total-=1
        self.total+=1
        
        

        
        
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
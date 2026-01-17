class Node:
    def __init__(self,key,value):
        self.val=value
        self.key=key
        self.next=self.prev=None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.right=Node(0,0)
        self.left=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def insert(self, node):
        right=self.right
        left=self.right.prev
        node.next=right
        node.prev=left
        left.next=node
        right.prev=node
    
    def remove(self, Node):
        p=Node.prev
        n=Node.next
        p.next=n
        n.prev=p

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node=Node(key,value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
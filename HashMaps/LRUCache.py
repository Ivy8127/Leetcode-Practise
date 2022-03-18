#Create Node class
# key , val , prev, next
class Node:
    
    def __init__(self,key,val):
        self.key, self.val = key,val
        self.prev, self.next = None, None
    
class LRUCache:

    def __init__(self, capacity: int):
        #dummy nodes - LRU -left and MRU -right
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next , self.right.prev = self.right,self.left 
    
    def remove(self,node):
        prev, nxt = node.prev , node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self,node):
        #inseting just before the right pointer, which is the MRU
        prev, right = self.right.prev , self.right
        prev.next = right.prev = node
        node.next = right
        node.prev = prev
        
    def get(self, key: int) -> int:
        #check whether whether the key exists:
        if key in self.cache:
             #remove it from the dll
                self.remove(self.cache[key])
             #insert it at the right - MRU
                self.insert(self.cache[key])
            #return this val -which is the node
                return self.cache[key].val
        return -1     
            
    def put(self, key: int, value: int) -> None:
        #if the key is in the hashmap
         # we have to remove the node from the list
         #create a new node with the key value pair - add it this to the hashmap
        #check that whether the length of the cache is over the capacity
         #evict the LRU - the node that is after the left- remove it from the dll
            #delete key from the hashmap
            if key in self.cache:
                self.remove(self.cache[key])
            self.cache[key]= Node(key,value)
             #insert this new node to our linked list
            self.insert(self.cache[key])
            if len(self.cache) > self.capacity:
                #evict the LRU - which is the next after the left
                LRU = self.left.next
                self.remove(LRU)
                del self.cache[LRU.key]
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
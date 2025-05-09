class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map of nodes
        self.mapofnodes = {}
        # dummy nodes
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        # Connect nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, otherwise return -1
        if key not in self.mapofnodes:
            return -1
        node = self.mapofnodes[key]
        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # if key already exist remove
        if key in self.mapofnodes:
            oldnode = self.mapofnodes[key]
            self.remove(oldnode)
        # else we add the key to our map and nodelist
        newNode = ListNode(key, value)
        self.mapofnodes[key] = newNode
        self.add(newNode)

        # check if we gone over capacity
        if len(self.mapofnodes) > self.capacity:
            # last recently used is the next from the head dummy node
            lru = self.head.next
            self.remove(lru)
            # delete the key from the map
            del self.mapofnodes[lru.key]


    def add(self, node):
        # add node to the end just before tail
        prevlast = self.tail.prev

        prevlast.next = node
        node.prev = prevlast
        node.next = self.tail
        self.tail.prev = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
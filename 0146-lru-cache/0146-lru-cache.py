class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic ={}
        self.arr = []

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            if self.arr.index([key,self.dic[key]]) !=(len(self.arr)-1):
                self.arr.pop(self.arr.index([key,self.dic[key]]))
                self.arr.append([key,self.dic[key]])
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            self.dic[key] = value
            if len(self.arr) < self.capacity:
                self.arr.append([key,value])
            else:
                del self.dic[self.arr[0][0]]
                self.arr.pop(0)
                self.arr.append([key,value])
        else:
            self.arr.pop(self.arr.index([key,self.dic[key]]))
            self.dic[key] = value
            self.arr.append([key,value])
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
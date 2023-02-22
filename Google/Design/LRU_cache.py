class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.c = capacity
        self.l = []
        

    def get(self, key: int) -> int:
        if key in self.d:
            self.l.append(key)
            return self.d[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.l.append(key)
        self.d[key] = value
        if len(self.d.keys()) > self.c:
            last = self.l.pop(0)
            while last in self.l:
                last = self.l.pop(0)
            self.d.pop(last)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
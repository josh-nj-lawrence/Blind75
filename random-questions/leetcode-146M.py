from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keys():
            self.move_to_end(key)
            return self[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self:
            # Update no problem
            self.move_to_end(key)
        self[key] = value
        # Check if capcity is reached
        if len(self) > self.capacity:
            self.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

# Results: 89.8% (762ms) 71.66% space (75.2MB)
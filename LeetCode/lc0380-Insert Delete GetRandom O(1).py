import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = dict() # {val:index}
        self.arr = [] # val

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            last_num = self.arr[-1]
            index = self.hashmap[val]
            
            # swap and pop
            self.arr[index] = last_num
            self.hashmap[last_num] = index
            self.arr.pop()
            
            # remove it from hashmap
            del self.hashmap[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

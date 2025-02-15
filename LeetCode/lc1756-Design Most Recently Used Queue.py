# time:O(n), space:O(n)
class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.arr = [i for i in range(1, self.n+1)]
        

    def fetch(self, k: int) -> int:
        value = self.arr.pop(k-1)
        self.arr.append(value)
        return value
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

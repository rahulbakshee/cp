# bruteforce
# time:O(n^2), space:O(1)
class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        index = len(self.arr)-2

        while index >= 0 and self.arr[index] <= price:
            index -= 1
        return len(self.arr) - index - 1



# monotonic stack
# time:O(n), space:O(n)
class StockSpanner:

    def __init__(self):
        self.stack = [] # pair:[price, span]
        
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append([price, span])
        return span

# time - set:O(1), get:O(logn)
# space - O(n)
class TimeMap:

    def __init__(self):
        self.hashmap = {} # {key:[[value, timestamp], [value, timestamp]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.hashmap.get(key, []) # [["bar", 1], ["bar", 2], ["bar", 2], ["bar", 4]]

        # binary search
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right)//2
            if values[mid][1]<=timestamp:
                result = values[mid][0]
                left = mid+1
            else:
                right = mid-1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

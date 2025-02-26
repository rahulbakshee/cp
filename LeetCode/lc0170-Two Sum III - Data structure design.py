# time:O(1)-add, O(n)-find
# space:O(n)
class TwoSum:

    def __init__(self):
        self.hashmap = {} # num:count        

    def add(self, number: int) -> None:
        if number in self.hashmap:
            self.hashmap[number] += 1
        else:
            self.hashmap[number] = 1        

    def find(self, value: int) -> bool:
        for key in self.hashmap.keys():
            complement = value - key
            if key != complement:
                if complement in self.hashmap:
                    return True
            else:
                if self.hashmap[key] >1:
                    return True

        return False       


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

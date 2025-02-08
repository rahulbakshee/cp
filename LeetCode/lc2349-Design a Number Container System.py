# Time complexity: O(logn) per change operation and O(1) per find operation.,  space:O(n)
class NumberContainers:

    def __init__(self):
        self.index_to_number = dict()
        self.number_to_index = defaultdict(SortedSet)


    def change(self, index: int, number: int) -> None:
        # update number_to_index
        if index in self.index_to_number:
            prev_number = self.index_to_number[index]
            self.number_to_index[prev_number].remove(index)
            if not self.number_to_index[prev_number]:
                del self.number_to_index[prev_number]

        self.number_to_index[number].add(index)

        # update the index to number
        self.index_to_number[index] = number
        
    def find(self, number: int) -> int:
        if number in self.number_to_index:
            return self.number_to_index[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

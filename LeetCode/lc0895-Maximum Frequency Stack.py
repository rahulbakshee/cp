"""Using Frequency Map + Grouped Stacks
Use a frequency map cnt to track how many times each 
element appears. Use a dictionary of stacks stacks[f] 
to store all elements with frequency f in a stack
(LIFO order).
Keep track of the current maximum frequency maxCnt."""
class FreqStack:

    def __init__(self):
        self.cnt = {}         # Maps value -> frequency count
        self.maxCnt = 0       # Tracks current maximum frequency
        self.stacks = {}      # Maps frequency -> stack of elements with that frequency

    def push(self, val: int) -> None:
        # Increment the frequency count of the value
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt

        # Update the max frequency seen so far
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []  # Initialize stack for new frequency

        # Push the value onto the stack corresponding to its frequency
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        # Pop from the stack of current max frequency
        res = self.stacks[self.maxCnt].pop()

        # Decrease the frequency count of that value
        self.cnt[res] -= 1

        # If the stack for the max frequency is now empty, reduce maxCnt
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1

        return res
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

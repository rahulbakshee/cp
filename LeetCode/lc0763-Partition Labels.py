""" using hashmap
 - Build a map (hashmap) of each character to its last index in the string.
 - Iterate through the string and for each character:
     - Expand the current partition's end to the farthest last occurrence 
     of any character seen so far.
 - When the current index i reaches end, it means:
     - All characters in this partition don’t appear later.
     - Finalize the partition and start a new one."""

# time:O(n), space:O(1)26 char of english
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # hashmap to store {num:last_occurance}
        hashmap = {}
        for i, char in enumerate(s):
            hashmap[char] = i

        result = []
        size, end = 0,0
        # enumerate over s, to deteremine size and partition(end index)
        for i, char in enumerate(s):
            size += 1
            end = max(end, hashmap[char])
            
            if i == end:
                result.append(size)
                size = 0

        return result

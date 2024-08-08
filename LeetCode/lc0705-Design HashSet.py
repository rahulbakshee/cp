# # using list
# # time: add:O(n), contains:O(n), remove:O(n)
# # Your MyHashSet object will be instantiated and called as such:
# # obj = MyHashSet()
# # obj.add(key)
# # obj.remove(key)
# # param_3 = obj.contains(key)


class MyHashSet:
    def __init__(self):
        self.my_set = []
    
    def add(self, key:int)->None:
        """Inserts the value key into the HashSet."""
        if not self.contains(key):
            self.my_set.append(key)
    
    def contains(self, key:int)->bool:
        """Returns whether the value key exists in the HashSet or not."""
        return True if key in self.my_set else False

    def remove(self, key:int)->None:
        """Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing."""
        if self.contains(key):
            self.my_set.remove(key)

################################################################################################################

# using hashing and linkedlist
# time: avg-O(1), worst:O(n)
# space: O(n) - n is number of keys in hashset
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range (10**4)]

    
    def add(self, key:int)-> None:
        """Inserts the value key into the HashSet."""
        # hash function
        index = key % len(self.set)

        # get the head of linkedlist at this index
        curr = self.set[index]

        while curr.next:
            if curr.next.data == key:
                return
            curr = curr.next
        curr.next = ListNode(key)
    
    def contains(self, key:int)->bool:
        """Returns whether the value key exists in the HashSet or not."""

        index = key % len(self.set)                
        curr = self.set[index]

        while curr.next:
            if curr.next.data == key:
                return True
            curr = curr.next
        return False

    def remove(self, key:int)->None:
        """Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing."""
        index = key % len(self.set)
        curr = self.set[index]

        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            curr = curr.next

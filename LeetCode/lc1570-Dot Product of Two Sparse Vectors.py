#EDITORIAL

# 1- not efficient storing of sparse vectors
# time:O(n), space:O(1)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for v1, v2 in zip(self.nums, vec.nums):
            result += v1*v2

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)



# 2- efficient storing of vectors using hashmap
# time:O(n), space:O(L)
# Let n be the length of the input array and L be the number of non-zero elements.
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.storage = {}
        for i, n in enumerate(self.nums):
            if n!=0:
                self.storage[i] = n


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        if len(self.storage) < len(vec.storage):
            v1, v2 = self.storage, vec.storage
        else:
            v2, v1 = self.storage, vec.storage

        for key, value in v1.items():
            if key in v2:
                result += value * v2[key]

        return result


# 3 - index - value pairs
# time:O(n), space:O(L)
# Let n be the length of the input array and L be the number of non-zero elements.
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = [] # [index,value]
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0,0

        while p<len(self.pairs) and q<len(vec.pairs):
            if self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            elif self.pairs[p][0] > vec.pairs[q][0]:
                q += 1
            else: #=
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1

        return result


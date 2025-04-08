# time:O(n+m), space:O(n+m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))


# time:O(n+m), space:O(n+m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)

        return result


# time:O(nlong+mlogm), space:O(min(n,m))
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        one, two = 0,0
        result = set()

        while one<len(nums1) and two< len(nums2):
            if nums1[one] < nums2[two]:
                one += 1
            elif nums1[one] > nums2[two]:
                two += 1
            else: # bothe equal
                result.add(nums1[one])
                one += 1
                two += 1

        return list(result)

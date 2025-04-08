class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def intersect(nums1, nums2):
            if not nums1 or not nums2:
                return []

            one, two = 0,0
            result = set()

            while one<len(nums1) and two<len(nums2):
                if nums1[one] < nums2[two]:
                    one += 1
                elif nums1[one] > nums2[two]:
                    two += 1
                else: # intersection
                    result.add(nums1[one])
                    one += 1
                    two += 1

            return sorted(list(result))

        arr2 = intersect(arr1, arr2)
        return intersect(arr2, arr3)

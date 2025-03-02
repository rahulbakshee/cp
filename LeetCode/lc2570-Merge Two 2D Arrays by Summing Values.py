class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        left, right = 0,0

        result = []
        while left<len(nums1) and right<len(nums2):
            if nums1[left][0] < nums2[right][0]:
                value = nums1[left]
                result.append(value)
                left += 1

            elif nums1[left][0] > nums2[right][0]:
                value = nums2[right]
                result.append(value)
                right += 1

            else: # both equal
                value = [nums1[left][0], nums1[left][1]+nums2[right][1]]
                result.append(value)
                left += 1
                right += 1


        while left<len(nums1):
            result.append(nums1[left])
            left += 1

        while right<len(nums2):
            result.append(nums2[right])
            right += 1
        return result

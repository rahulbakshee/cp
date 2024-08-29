# time:O(n**2)n - len of nums2, space:O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_to_greater = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    nums_to_greater[nums2[i]] = nums2[j]
                    break

        result = []
        for num in nums1:
            if num in nums_to_greater:
                result.append(nums_to_greater[num])
            else:
                result.append(-1)
        return result



# using stack - time:O(n+m), space:O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_to_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                nums_to_greater[stack.pop()] = num
            
            if num in nums1:
                stack.append(num)

        result = []
        for num in nums1:
            if num in nums_to_greater:
                result.append(nums_to_greater[num])
            else:
                result.append(-1)
        return result


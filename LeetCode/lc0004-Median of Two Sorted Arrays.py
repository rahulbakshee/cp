# time:O(n+m logn+m), space:O(n+m)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        
        nums1 = sorted(nums1)
        print(nums1)
        
        total_len = len(nums1) 
        if total_len %2 == 0:
            return (nums1[total_len//2] + nums1[total_len//2 - 1]) /2
        else:
            return nums1[total_len//2]  


# copied from neetcode
# using binary search
# time:O(log(min(m, n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total //2

        if len(A) > len(B): # A is smaller
            A, B = B, A

        left, right = 0, len(A) -1
        while True:
            midA = (left + right)//2 
            midB = half - midA - 2

            a_left = A[midA] if midA >=0 else float("-inf")
            a_right = A[midA+1] if midA+1 < len(A) else float("inf")
            b_left = B[midB] if midB >= 0 else float("-inf")
            b_right = B[midB+1] if midB+1 < len(B) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right))/2
            elif a_left > b_left:
                right = midA -1
            else:
                left = midA + 1




                

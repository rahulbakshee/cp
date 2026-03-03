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
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        # binary search on A (smaller)
        left, right = 0, len(A)-1
        while True:
            midA = (left + right) // 2 
            midB = half - midA - 2
            
            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if (midA+1) < len(A) else float("inf")

            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if (midB+1) < len(B) else float("inf")

            # compare both the ends from two sublists
            if leftA <= rightB and leftB <= rightA:
                # odd  
                if total %2:
                    return min(rightA, rightB)

                # even
                else:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
            elif leftA > rightB:
                right = midA - 1

            else:
                left = midA + 1

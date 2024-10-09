class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        result = 0
        window_sum = 0

        for right in range(len(arr)):
            window_sum += arr[right]
            avg = window_sum / k
            if right-left+1 == k:
                if avg >= threshold:
                    result += 1
                window_sum -= arr[left]
                left += 1
        return result

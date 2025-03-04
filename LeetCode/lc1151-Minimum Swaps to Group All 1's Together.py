# time:O(n), space:O(1)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        window_len = total_ones = sum(data)
        curr_ones = max_ones = 0

        left, right = 0, 0
        while right < len(data):
            # add the right index num to the curr_ones
            # it could be eityher 1/0
            # and increment right(extend window)
            curr_ones += data[right]
            right += 1

            # always check if the window size is correct
            # if it is more, move the left pointer
            if right - left > window_len:
                curr_ones -= data[left]
                left += 1

            # keep checking the max of ones we can find in a window
            max_ones = max(max_ones, curr_ones)
        
        # return the total number of ones minus the ones in the current window
        # which is equal to the  number of zeroes in a window
        return total_ones - max_ones

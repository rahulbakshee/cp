# from editorial page

# time:O(n**2), space:O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums_str = str(num)
        max_nums = num

        for i in range(len(nums_str)):
            for j in range(i+1, len(nums_str)):
                nums_list = list(nums_str)
                nums_list[i], nums_list[j] = nums_list[j], nums_list[i]

                max_nums = max(max_nums, int("".join(nums_list)))

        return max_nums



# time:O(n), space:O(n)
# two pass
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        
        # find the max right index from right to left
        max_right_index = [0] * n
        max_right_index[n-1] = n-1
        
        for i in range(n-2, -1, -1):
            if nums[i] > nums[max_right_index[i+1]]:
                max_right_index[i] = i
            else:
                max_right_index[i] = max_right_index[i+1]


        # check for first opportuinity to swap
        for i in range(n):
            if nums[i] < nums[max_right_index[i]]:
                nums[i], nums[max_right_index[i]] = nums[max_right_index[i]], nums[i]
                return int("".join(nums))

        return num

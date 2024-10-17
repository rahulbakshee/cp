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
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_right_index = [0] * n

        max_right_index[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            max_right_index[i] = (
                i
                if num_str[i] > num_str[max_right_index[i + 1]]
                else max_right_index[i + 1]
            )

        for i in range(n):
            if num_str[i] < num_str[max_right_index[i]]:
                num_str[i], num_str[max_right_index[i]] = (
                    num_str[max_right_index[i]],
                    num_str[i],
                )
                return int("".join(num_str))

        return num

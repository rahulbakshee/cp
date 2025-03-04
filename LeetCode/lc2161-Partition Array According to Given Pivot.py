class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallers = []
        equals = []
        largers = []

        for num in nums:
            if num < pivot:
                smallers.append(num)
            elif num > pivot:
                largers.append(num)
            else:
                equals.append(num)

        return smallers + equals+ largers






class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallers = 0
        equals = 0

        for num in nums:
            if num < pivot:
                smallers += 1
            elif num == pivot:
                equals += 1

        # time to assign indexes
        smallers_index = 0
        equals_index = smallers
        largers_index = smallers + equals

        # iterate again on nums and assign repective num with indexes
        result = [0] * len(nums)
        for i, num in enumerate(nums):
            if num < pivot:
                result[smallers_index] = num
                smallers_index += 1

            elif num > pivot:
                result[largers_index] = num
                largers_index += 1

            else:
                result[equals_index] = num
                equals_index += 1

        return result





class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)

        less_index = 0
        greater_index = len(nums)-1

        for i, j in zip(range(len(nums)), range(len(nums)-1,-1,-1)):
            if nums[i] < pivot:
                result[less_index] = nums[i]
                less_index += 1

            if nums[j] > pivot:
                result[greater_index] = nums[j]
                greater_index -= 1

        while less_index <= greater_index:
            result[less_index] = pivot
            less_index += 1

        return result


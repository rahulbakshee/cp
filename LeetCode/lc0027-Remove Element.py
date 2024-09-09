# time:O(n), space:O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_index = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else: # nums[i] != val
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index

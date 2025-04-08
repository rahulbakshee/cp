class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        seen = set()
        i = 0

        while i < len(nums) and len(nums) != len(set(nums)):
            if nums[i] in seen:
                nums = nums[3:]
                result += 1
                seen = set()
                i = 0
            else:
                seen.add(nums[i])
            
            
            if len(nums) < 3:
                break

            i += 1
            # print(nums)
        return result if len(nums) == len(set(nums)) else result+1
            



class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def check(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)

            return True


        result = 0
        for i in range(0, len(nums), 3):
            if check(i):
                return result
            result += 1

        return result

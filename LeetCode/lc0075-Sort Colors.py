class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1-bruteforce - time:O(nlogn), space:O(n)
        nums.sort()

        
        # 2-counter -time:O(n), space:O(n)
        hashmap = Counter(nums)
        for i in range(hashmap[0]):
            nums[i] = 0
        for i in range(hashmap[0], hashmap[0]+hashmap[1]):
            nums[i] = 1
        for i in range(hashmap[0]+hashmap[1], hashmap[0]+hashmap[1]+hashmap[2]):
            nums[i] = 2


        # 3-optimal - three pointers - time:O(n), space:O(1)
        low, mid, high = 0,0,len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

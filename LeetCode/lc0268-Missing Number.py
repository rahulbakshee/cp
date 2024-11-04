# https://leetcode.com/problems/missing-number/solutions/2563887/eight-different-approaches-in-python3/?orderBy=most_votes

class Solution:
    def brute_force(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N*N)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)
    
    def sorting(self, nums: List[int]) -> int:
        """
        Time Complexity: O(Nlog(N))
        Space Complexity: O(N)
        """
        nums.sort()
        
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
    
    def binary_search(self, nums: List[int]) -> int:
        """
        Time Complexity:
            O(Nlog(N)) if nums not sorted
            O(log(N)) if nums already sorted
        
        Space Complexity:
            O(N) if nums not sorted
            O(1) if nums sorted
        """
        nums.sort()
        left, right = 0, len(nums)
        mid = (left+right)//2
        while left < right:
            if nums[mid] == mid:
                left = mid+1
            else:
                right = mid - 1
            
            mid = (left + right)//2
        
        return mid + 1
    
    def hashing(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        nums_set = set(nums)
        N = len(nums)
        for i in range(N):
            if i not in nums_set:
                return i
        
        return len(nums)
        
    def gauss_formula(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        N = len(nums)
        return N*(N + 1)//2 - sum(nums)
    
    def xor(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        result = len(nums)
        for i, v in enumerate(nums):
            result ^= i^v
        
        return result
    
    def cyclic_swapping(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        current = 0
        N = len(nums)
        count = 0
        while current < N:
            count+= 1
            if nums[current] == N:
                current += 1
                continue
            
            if nums[current] == nums[nums[current]]:
                current += 1
            else:
                temp = nums[current]
                nums[current] = nums[nums[current]]
                nums[temp] = temp
        
        for i, v in enumerate(nums):
            if i != v:
                return i
        
        return N
    
    def value_inversion(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        
        Advantages:
            - Original Input array can be restored
        """
        
        for i, _ in enumerate(nums):
            nums[i] += 1
        
        for i, v in enumerate(nums):
            if abs(v) > len(nums):
                continue
        
            nums[abs(v)-1] = -abs(nums[abs(v)-1])
        
        for i, v in enumerate(nums):
            if v > 0:
                return i
        
        return len(nums)
                
    
    def missingNumber(self, nums: List[int]) -> int:
        # return self.brute_force(nums)
        # return self.sorting(nums)
        # return self.hashing(nums)
        # return self.gauss_formula(nums)
        # return self.xor(nums)
        # return self.cyclic_swapping(nums)
        # return self.binary_search(nums)
        return self.value_inversion(nums)

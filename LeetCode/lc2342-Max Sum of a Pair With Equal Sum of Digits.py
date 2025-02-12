class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def get_sum(number:int)->int:
            return sum(list(map(int, list(str(number)))))

        hashmap = defaultdict(list) # {sum1:[index1, index2...]}
        for i, num in enumerate(nums):
            hashmap[get_sum(num)].append(nums[i])

        maxSum = 0
        for key, value in hashmap.items():
            if len(value)>1:
                sorted_values = list(sorted(value))
                
                maxSum = max(maxSum, sum(sorted_values[-2:]))

        return maxSum if maxSum else -1             

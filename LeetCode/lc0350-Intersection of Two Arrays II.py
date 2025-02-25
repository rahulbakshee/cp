class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        
        counter2 = dict()
        for num in nums2:
            if num in counter2:
                counter2[num] += 1
            else:
                counter2[num] = 1
                
        result = []
        # optimizations for iteration over smaller len of counter
        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1
            
        # iterate over smaller length counter(counter1)
        # look for keys which are common
        # get their min value and add it to result array
        
        for key, value in counter1.items():
            if key in counter2:
                val = min(value, counter2[key])
                for _ in range(val):
                    result.append(key)
            
        return result
        
        
        

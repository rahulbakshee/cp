class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                st.add(num)

        return len(st)

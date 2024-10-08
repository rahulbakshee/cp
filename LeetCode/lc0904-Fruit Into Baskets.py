# time:O(n), space:O(n)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_trees = 0
        window = dict()
        k = 2

        for right in range(len(fruits)):
            curr = fruits[right]
            if curr in window:
                window[curr] += 1
            else:
                window[curr] = 1

            # check for unique type of fruits in window OR len of window
            if len(window) > k:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1

            max_trees = max(max_trees, right-left+1)

        
        return max_trees

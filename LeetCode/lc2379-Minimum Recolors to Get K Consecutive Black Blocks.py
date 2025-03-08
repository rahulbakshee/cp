# two pointers - time:O(n), space:O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        min_whites = len(blocks)

        left, right = 0,0
        while right < len(blocks):
            if blocks[right] == "W":
                whites += 1
            
            # reduce the window
            if right-left+1 > k:
                if blocks[left] == "W":
                    whites -= 1
                left += 1
            
            # calculate the min_whites if window length is k
            if right-left+1 == k:
                min_whites = min(min_whites, whites)
            
            
            right += 1

        return min_whites



# time:O(blocks), space:O(k)
from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        window_dict = Counter(window)
        # window_dict = {"B":k, "W":k-1}

        result = window_dict["W"]
        min_result = result

        for i in range(k, len(blocks)):
            # add the next element and remove the first element
            if blocks[i] == "W":
                result += 1
            if blocks[i-k] == "W":
                result -= 1

            min_result = min(min_result, result)

        return min_result
      

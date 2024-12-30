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
      

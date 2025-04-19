# bruteforce
# time:O(n^2), space:O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        result = 0

        for i in range(n):
            max_count = 0
            counter = dict()
            for j in range(i, n):
                counter[s[j]] = 1+counter.get(s[j], 0)
                max_count = max(max_count, counter[s[j]])

                # check k condition
                if (j-i+1) - max_count <= k:
                    result = max(result, j-i+1)        


        return result




# time:O(n), space:O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_count = 0
        result = 0

        for end in range(len(s)):
            if s[end] in count:
                count[s[end]] += 1
            else:
                count[s[end]] = 1
            
            max_count = max(max_count, count[s[end]])
    
            if end-start+1-max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        max_count = 0
        left, right = 0,0
        max_len = 0

        while right < len(s):
            char = s[right]

            # add to the running dictionary/counter
            counter[char] = 1+ counter.get(char, 0)
            
            # update the max_counter
            max_count = max(max_count, counter[char])

            # check K condition
            # when curr_window_size minus max_counter is greater than k
            while (right-left+1) - max_count > k:
                counter[s[left]] -= 1
                left += 1
            
            # update the max_len
            max_len = max(max_len, right-left+1)

            right += 1

        return max_len

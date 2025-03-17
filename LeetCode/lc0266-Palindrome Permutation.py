class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        single_count = 0
        for key, value in counter.items():
            counter[key]  = counter[key]%2
            if counter[key] == 1:
                single_count += 1

        return True if single_count in [0,1] else False

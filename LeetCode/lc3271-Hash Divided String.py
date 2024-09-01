class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alphabets = {
                    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
                    8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p',
                    16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
                    24: 'y', 25: 'z'
                }

        result = ""
        for i in range(0, len(s), k):
            subresult = 0
            for char in s[i:i+k]:
                subresult += ord(char) - ord("a")

            subresult = subresult % 26
            result += alphabets[subresult]

        return result
            

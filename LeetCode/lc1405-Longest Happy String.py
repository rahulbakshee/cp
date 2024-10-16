# time:O(a+b+c), space:O(1) not counting string builder
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        curr_a = curr_b = curr_c = 0
        total_chars = a+b+c
        result = []

        for _ in range(total_chars):
            if (a>=b and a>=c and curr_a!=2) or (a>0 and (curr_b==2 or curr_c==2)):
                result.append("a")
                a -= 1
                curr_a += 1
                curr_b = 0
                curr_c = 0

            elif (b>=c and b>=a and curr_b!=2) or (b>0 and (curr_a==2 or curr_c==2)):
                result.append("b")
                b -= 1
                curr_b += 1
                curr_a = 0
                curr_c = 0

            elif (c>=a and c>=b and curr_c!=2) or (c>0 and (curr_a==2 or curr_b==2)):
                result.append("c")
                c -= 1
                curr_c += 1
                curr_a = 0
                curr_b = 0

        return "".join(result)

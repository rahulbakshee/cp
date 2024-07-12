# https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2024-07-12

# copied from editorial - need to revisit
# time:O(n) - two passes on the input string each for "ab" and "ba"
# space:O(n) - for creating a separate list
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_points = 0
        s = list(s)

        if x> y:
            total_points += self.remove_substring(s, "ab", x)
            total_points += self.remove_substring(s, "ba", y)
        else:
            total_points += self.remove_substring(s, "ba", y)
            total_points += self.remove_substring(s, "ab", x)
            
        return total_points

    def remove_substring(self, input_string, target_substring, points):
        total_points = 0
        write_index = 0

        # iterate through the string
        for read_index in range(len(input_string)):
            # add the current character
            input_string[write_index] = input_string[read_index]
            write_index += 1

            # at least two elements 
            if (write_index >1 
            and input_string[write_index-1] == target_substring[1] 
            and input_string[write_index-2] == target_substring[0]):
                total_points += points
                write_index -= 2

        del input_string[write_index:]
        return total_points

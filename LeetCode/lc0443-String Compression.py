# time:O(n), space:O(1), n is len of chars
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0

        while i < len(chars):
            curr_char = chars[i]
            count = 0
            # calculate the length of repeating char
            while i < len(chars) and chars[i] == curr_char:
                i += 1
                count += 1
            
            # write the char
            chars[write] = curr_char
            write += 1

            # write the len
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write

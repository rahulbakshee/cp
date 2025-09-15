class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not s:
            return ""
        if not order:
            return s

        # build a freq/counter from s
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        
        # use order to build final output
        result = []
        for char in order:
            if char in freq:
                result.append(char * freq[char])
                del freq[char]


        # see if remaining characters in s
        # append them to final result
        for key, val in freq.items():
            result.append(key * val)

        return "".join(result)

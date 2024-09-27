class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""
        vowels = {"a","e","i","o", "u", "A", "E", "I", "O", "U"}
        result = []
        words = sentence.split()
        count = 1
        for word in words:
            if word[0] in vowels:
                curr = word + "ma" + count *"a"
            else:
                curr = word[1:] + word[0] + "ma" + count *"a"
            count += 1
            result.append(curr)

        return " ".join(result)

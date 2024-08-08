class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # create a dict of chars
        # loop over words
            # for each word, create a dict of letters
            # while creating the dict, if I see occurance of that letter is mjkore than given chars- break
            # if it could be formed using chars from char_dict, then add the len(word) to the final result

        # time:O(c) where c is len(chars)
        # time:O(n*m) where n is len(words) and m is average/worst case len(individual word)
        # total - O(c + n*m)

        # space:O(1) as max 26 letter 
        
        def is_good_word(word:str, chars_dict:dict) -> bool:
            """ given a word, returns if the word is good or not"""
            word_dict = {}
            for w in word:
                if w in word_dict:
                    word_dict[w] += 1
                else:
                    word_dict[w] = 1

            for key, value in word_dict.items():
                if key not in chars_dict or chars_dict[key] < word_dict[key]:
                    return False

            return True

        
        result = 0

        # create dict from chars
        chars_dict = {}
        for char in chars:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        # loop over each word to find if it is good
        for word in words:
            if is_good_word(word, chars_dict):
                result += len(word)

        return result

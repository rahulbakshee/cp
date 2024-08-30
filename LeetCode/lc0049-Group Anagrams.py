# https://leetcode.com/problems/group-anagrams/description/
# time:O(n*mlogm) - n is the total number of words in strs, m is the avg len of each word in strs
# space:O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        return anagram_dict.values()




# time - O(n * mlogm), space - O(n)
# n is the length of input string, m is the average lenght of each word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for s in strs:
            if "".join(sorted(s)) in dic:
                dic["".join(sorted(s))].append(s)
            else:
                dic["".join(sorted(s))] = [s]
        return dic.values()

# using hashmap/dict - optimized runtime
# time - O(n * m), space - O(n)
# n is the length of input string, m is the average lenght of each word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for s in strs: #eat
            count = [0] *26
            for c in s: #e #4
                count[ord(c) - ord("a")] +=1
            
            dic[tuple(count)].append(s)
            print(dic)
        return dic.values()


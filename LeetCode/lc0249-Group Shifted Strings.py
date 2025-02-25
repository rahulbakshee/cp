Let N be the length of strings and K be the maximum length of a string in strings.

Time complexity: O(N∗K)

We iterate over all N strings and for each string, we iterate over all the characters to generate the Hash value, which takes O(K) time. To sum up, the overall time complexity is O(N∗K).

Space complexity: O(N∗K)

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strings:
            # strings with one chars
            if len(s) == 1:
                hashmap["one"].append(s)
                continue
                
            # stirngs with more than one chars
            key = []
            for i in range(1, len(s)):
                val = ord(s[i]) - ord(s[i-1])
                if val <0:
                    val = val + 26
                key.append(val)
                
            hashmap[tuple(key)].append(s)
            
        return list(hashmap.values())
                

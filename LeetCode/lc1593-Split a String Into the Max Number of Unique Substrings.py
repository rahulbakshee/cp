########################## EDITORIAL
# backtracking
# time:O(n.2^n), space:O(n)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def backtrack(s, start, seen):
            if start == len(s):
                return 0

            max_count = 0

            for end in range(start+1, len(s)+1):
                sub_string = s[start:end]
                if sub_string not in seen:
                    # take it
                    seen.add(sub_string)
                    # update max_count
                    max_count = max(max_count, 1+backtrack(s, end, seen))
                    # don't take it
                    seen.remove(sub_string)                    
            return max_count

        return backtrack(s, 0, seen)




# backtracking with pruning
# time:O(n.2^n), space:O(n)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        max_count = [0]

        def backtrack(s, start, seen, count, max_count):
            if count + len(s) - start <= max_count[0]:
                return 

            if start == len(s):
                max_count[0] = max(max_count[0], count)
                return 
            
            for end in range(start+1, len(s)+1):
                sub_string = s[start:end]
                if sub_string not in seen:
                    seen.add(sub_string)
                    backtrack(s, end, seen, count+1, max_count)
                    seen.remove(sub_string)
            return

        backtrack(s, 0, seen, 0, max_count)
        return max_count[0]

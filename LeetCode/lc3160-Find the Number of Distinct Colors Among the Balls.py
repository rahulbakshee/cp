# time:O(n) - n-len of queries
# space:O(n)
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hashmap = dict() # ball1:color1, ball2:color2....
        rev_hashmap = defaultdict(list) # color1:[ball1, ball2...]
        result = []

        for query in queries:
            #print(query, hashmap, rev_hashmap)
            ball, color = query
            if ball in hashmap:
                prev_color = hashmap[ball]
                rev_hashmap[prev_color].remove(ball)

                # delete key if no values
                if len(rev_hashmap[prev_color]) == 0:
                    del rev_hashmap[prev_color]
            hashmap[ball] = color
            rev_hashmap[color].append(ball)

            # append the distinct values from hashmap into result
            result.append(len(rev_hashmap.keys()))

        return result

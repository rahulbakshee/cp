# time:O(ST), space:O(1)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_freq = set(source)
        
        for t in target:
            if t not in source_freq:
                return -1


        result = 0        
        source_index = 0
        m = len(source)

        for target_index in range(len(target)):
            if source_index == 0:
                result += 1

            while target[target_index] != source[source_index]:
                source_index = (source_index +1) % m

                if source_index == 0:
                    result += 1

                
            source_index = (source_index + 1) %m


        return result

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        counter1, counter2 = dict(), dict() # {string: index}
        min_sum = len(list1)+len(list2)
        min_sum_str = []

        for i in range(len(list1)):
            counter1[list1[i]] = i

        for i in range(len(list2)):
            counter2[list2[i]] = i

        # counter1 - len = 10
        # counter2 - len = 900        
        print(counter1)

        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1


        for key, value in counter1.items():
            if key in counter2:
                if min_sum > value+counter2[key]:
                    min_sum = min(min_sum, value+counter2[key])
                    min_sum_str = [key]
                elif min_sum == value+counter2[key]:
                    min_sum_str.append(key)

        # iterate ove list1 and store all strings in a dict with string:index
        # check for a string if it is present inboth dicts, and compare the sum of indexes
        # return max index sum
        return min_sum_str

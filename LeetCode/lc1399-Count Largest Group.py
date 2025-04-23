class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = dict()

        for i in range(1, n+1):
            num = i
            num_sum = 0

            while num:
                num_sum += num % 10
                num = num//10


            counter[num_sum] = 1+counter.get(num_sum, 0)

        freq = Counter(counter.values())
        
        return freq[max(freq.keys())]

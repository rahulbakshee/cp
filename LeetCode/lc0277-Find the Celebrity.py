# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# bruteforce
# time:O(n^2), space:O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        # step2
        # func to check if i is celeb
        def is_celeb(i)->bool:
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j) or not knows(j,i):
                    return False

            return True

        # step1 
        # outer loop to iterate over n
        for i in range(n):
            if is_celeb(i):
                return i

        return -1

"""Find the Candidate (1 pass):
Start with candidate = 0, iterate from 1 to n-1:
If candidate knows i, 
    then candidate is not the celebrity → update candidate = i.
Validate the Candidate (1 pass):
For all j ≠ candidate, check:
    candidate must not know j
    j must know candidate
If any condition fails, return -1."""
# optimal  - time:O(n), space:O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        # step2
        # func to check if i is celeb
        def is_celeb(i)->bool:
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j) or not knows(j,i):
                    return False

            return True

        # step1 
        # one loop to iterate over n
        # to find who is the celeb candidate
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        # another loop to confirm celeb
        if is_celeb(candidate):
            return candidate

        return -1

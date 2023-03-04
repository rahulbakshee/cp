# https://leetcode.com/problems/corporate-flight-bookings/description/


# brute force : time limit exceeded
# space: O(1) if we don't consider answer else O(n), time:O(n**2)
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for booking in bookings:
            first, last, seats = booking
            for index in range(first-1, last):
                answer[index] += seats
            #print(answer)
        return answer

# using cumulative sum
# space: O(1) if we don't consider answer else O(n), time:O(n)
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n+1)

        for booking in bookings:
            first, last, seats = booking
            answer[first-1] += seats
            answer[last] -= seats

        # cum sum
        for i in range(n):
            answer[i+1] += answer[i]
        return answer[:n]
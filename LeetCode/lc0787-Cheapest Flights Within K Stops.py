# Bellman-Ford algorithm to find cheapest price with at most k stops
# time:O(k*E), space:O(n), e-edges/flights,k&n input
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # min_prices[i] will hold the minimum cost to reach city i 
        # from src with at most current # of stops
        min_prices = [float("inf") for i in range(n)]
        min_prices[src] = 0  # Cost to reach src from src is 0

        # Do at most k+1 rounds of relaxation (corresponds to k stops, 
        # i.e., k+1 edges)
        for i in range(k+1):
            # Make a copy to ensure we only use results from the previous 
            # iteration (avoids over-relaxing in same round)
            temp = min_prices.copy()

            # For every flight, try to relax the edge (if it leads to a cheaper price)
            for s, d, p in flights:  # s = source city, d = destination city, p = price
                if min_prices[s] == float("inf"):
                    continue  # Cannot reach s yet; skip

                # If cost via s is lower, update temp price for d
                if min_prices[s] + p < temp[d]:
                    temp[d] = min_prices[s] + p

            # Prepare for the next round (next level of stops)
            min_prices = temp

        # If destination is still unreachable, return -1
        return min_prices[dst] if min_prices[dst] != float("inf") else -1



# # shortest path - djikstra + BFS- time:O(nk), space:O(n+m)
# # n-cities,m-flights,k-stops
from collections import defaultdict, deque
from typing import List

# Find the cheapest price from src to dst within at most k stops using BFS + cost tracking
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. Build an adjacency list to represent the flight graph
        graph = defaultdict(list)  # graph[u] = [(v, price_to_v), ...]
        for u, v, p in flights:
            graph[u].append((v, p))

        # 2. Track the minimum price found so far to each node
        min_prices = {node: float("inf") for node in range(n)}
        min_prices[src] = 0  # The cost to reach the source from itself is zero

        # 3. BFS queue: each entry is (total_price, current_city, stops_made)
        q = deque([(0, src, 0)])

        while q:
            price, node, curr_k = q.popleft()  # Get the next city and travel cost

            # If we've used more than k stops, skip this path
            if curr_k > k:
                continue

            # Explore all outgoing flights from `node`
            for nei_d, nei_p in graph[node]:
                new_price = price + nei_p
                # If this path is cheaper, update and continue exploring it
                if min_prices[nei_d] > new_price:
                    min_prices[nei_d] = new_price
                    q.append((new_price, nei_d, curr_k + 1))

        # Return the result: -1 if unreachable
        return -1 if min_prices[dst] == float("inf") else min_prices[dst]

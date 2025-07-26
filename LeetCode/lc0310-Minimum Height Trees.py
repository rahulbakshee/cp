# Brute Force BFS / DFS from Each Node
# For each node, perform BFS/DFS to find the height of the 
# tree rooted at that node. Track the minimum height and the
# nodes achieving it.This is straightforward but inefficient 
# (O(n²)) for large graphs.

"""Topological Sorting / Leaf Trimming
for the tree-alike graph, the number of centroids is no more than 2.
The roots of the Minimum Height Trees (MHTs) must be the graph’s centers 
(1 or 2 nodes). We can find them by iteratively trimming leaves (nodes with
only one connection) until 1 or 2 nodes remain. 
Algorithm Steps:
 - Build an adjacency list of the graph.
 - Initialize a queue with all leaf nodes (nodes with only 1 edge).
 - While more than 2 nodes remain:
     - Remove current leaves from the graph.
     - Update the degree (number of edges) of their neighbors.
     - Add new leaves to the queue.
 - Return the remaining 1 or 2 nodes as the MHT roots."""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # If there's only one node, it is the root of the MHT.
        if n == 1:
            return [0]

        # Build adjacency list of the undirected graph.
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Dictionary to record the number of edges (degree) for each node.
        edge_cnt = {}

        # Queue for leaf nodes.
        leaves = deque()

        # Initialize degrees and find initial leaves.
        for src, neighbors in adj.items():
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)

        # Trim leaves layer-by-layer until <= 2 nodes remain.
        while leaves:
            # Once <= 2 nodes remain, these are the centroids (roots of MHTs).
            if n <= 2:
                return list(leaves)

            # Number of leaves to process in this layer
            leaves_count = len(leaves)

            for _ in range(leaves_count):
                node = leaves.popleft()
                n -= 1  # Remove the leaf from the total node count

                # For each neighbor, reduce their degree by 1 since leaf is removed.
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    # If neighbor becomes a leaf, add it to the queue.
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

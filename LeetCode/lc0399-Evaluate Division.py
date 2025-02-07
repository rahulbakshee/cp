# from editorial
# time:O(m*n) - N be the number of input equations and M be the number of queries.
# space:O(n)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 3- define backtrack function
        def backtrack(A, B, product, visited):
            """
                check if there is a path between A and B
                return the weights of the path i.e. A/B

                @params
                (from_node, target_node, curr_product, visited set)
                
            """
            # base case
            visited.add(A)
            ret = -1.
            neighbors = graph[A]
            if B in neighbors:
                ret = product*graph[A][B]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack(neighbor, B, value*product, visited)
                    if ret != -1.0:
                        break
            
            visited.remove(A)
            return ret
        
        # 1 - build the graph
        graph = defaultdict(defaultdict)
        for equation, value in zip(equations, values):
            A, B = equation
            graph[A][B] = value
            graph[B][A] = 1/value


        # 2- evaluate each query and check if there is a path 
        # between query[0] to query[1]
        result = []
        for query in queries:
            A, B = query
            if A not in graph or B not in graph:
                ret = -1.
            elif A == B:
                ret = 1.
            else:
                visited = set()
                ret = backtrack(A,B,1,visited) # from_node, target_node, curr_product, visited set

            result.append(ret)

        return result

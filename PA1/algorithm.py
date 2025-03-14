import heapq
"""
using Dijkstra’s algorithm to return the length of the shortest cycle in the graph

Algorithm:
    1:implement a procedure based on  Dijkstra’s algorithm to find the shortest path from one vertex to the vertex it self, if there is a path, it is the shortest cycle for this vertex.
    2: iterate on all the vertex in the graph to get the min value. 
"""
def find_shortest_cycle(graph):
    shortest_cycle = float('inf')
    
    for start in graph:  # Iterate over all vertices as potential start points
        pq = []  # Min-heap priority queue for Dijkstra's algorithm
        heapq.heappush(pq, (0, start))  # Push (distance, vertex)
        distances = {v: float('inf') for v in graph}  # Initialize distances to infinity
        distances[start] = 0  # Distance to the start node is 0
        
        while pq:
            dist, node = heapq.heappop(pq)  # Extract the node with the smallest distance
            for neighbor, weight in graph[node]:  # Explore neighbors
                new_dist = dist + weight
                if neighbor not in distances: #Ignore neighbor that is an endpoint 
                    continue
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist  # Update shortest distance
                    heapq.heappush(pq, (new_dist, neighbor))  # Push updated distance to priority queue
                # Check for cycle: if we return to the start node, update shortest cycle length
                if neighbor == start:
                    shortest_cycle = min(shortest_cycle, new_dist)
                    
    return shortest_cycle if shortest_cycle != float('inf') else 0 



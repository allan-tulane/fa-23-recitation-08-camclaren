from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    visited = {}
    frontier = [(0, 0, source)]
    
    # checks if frontier is empty; if not, then removes next node in queue from frontier
    while len(frontier) != 0:
        weight, edges, node = heappop(frontier)
        # if node hasn't been visited, adds to visited
        if node not in visited:
            visited[node] = (weight, edges)
            # adds neighboring nodes to frontier
            for neighbor, weight_neighbor in graph[node]:
                heappush(frontier, (weight + weight_neighbor, edges + 1, neighbor))

    return visited

    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    visited = {}
    frontier = [(0, 0, source)]
    # initializes it with no value for key bc first node has no parents
    parents = {source: None}

    # checks if frontier is empty; if not, adds node to visited set
    while len(frontier) != 0:
        node = frontier.popleft()
        visited.add(node)
        # checks the neighboring nodes and adds to frontier
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in frontier:
                parents[neighbor] = node
                frontier.append(neighbor)

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    # checks if the destination node is a parent node
    if destination in parents:
      return get_path(parents, parents[destination]) + parents[destination]
    else:
    # if not, returns empty string since you're already at the node
      return ''


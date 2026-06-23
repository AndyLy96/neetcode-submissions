from typing import Dict, List, Tuple, Optional
import heapq


class Graph:
    """Simple weighted directed graph with Dijkstra utilities.

    The constructor accepts either an adjacency dict mapping node -> {neighbor: weight}
    or a list of edges in the form [(u, v, w), ...].
    """

    def __init__(self, graph=None):
        self.graph: Dict[object, Dict[object, float]] = {}
        if graph is None:
            return
        # if graph looks like a list of edges
        if isinstance(graph, list):
            for u, v, w in graph:
                self.add_edge(u, v, w)
        elif isinstance(graph, dict):
            # shallow copy to ensure dict-of-dict shape
            for u, nbrs in graph.items():
                self.graph[u] = dict(nbrs)
        else:
            raise TypeError("Graph must be a list of edges or an adjacency dict")

    def add_edge(self, node1, node2, weight: float):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        # ensure node2 exists in graph keys so distances include it
        if node2 not in self.graph:
            self.graph[node2] = {}

    def shortest_distances(self, source) -> Dict[object, float]:
        """Return a mapping node -> shortest distance from source."""
        distances: Dict[object, float] = {node: float("inf") for node in self.graph}
        distances[source] = 0

        pq: List[Tuple[float, object]] = [(0, source)]

        visited = set()

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph.get(current_node, {}).items():
                tentative_distance = current_distance + weight

                if tentative_distance < distances.get(neighbor, float("inf")):
                    distances[neighbor] = tentative_distance
                    heapq.heappush(pq, (tentative_distance, neighbor))
        return distances
    def shortest_distance(self, source) -> Dict[object, float]:
        """Alias for shortest_distances — keeps a single public method name.

        Returns a mapping node -> shortest distance from source.
        """
        return self.shortest_distances(source)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times is a list of edges [u, v, w]
        g = Graph(times)
        # ensure nodes 1..n exist in graph keys
        for node in range(1, n + 1):
            if node not in g.graph:
                g.graph[node] = {}

        distances = g.shortest_distance(k)
        # if any node unreachable, return -1
        maxd = 0
        for node in range(1, n + 1):
            d = distances.get(node, float("inf"))
            if d == float("inf"):
                return -1
            maxd = max(maxd, d)
        return maxd


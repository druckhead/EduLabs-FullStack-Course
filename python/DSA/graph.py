from os import link
from pprint import pprint
from typing import Any


class Graph:
    def __init__(self, directed=False) -> None:
        self._directed = directed

        self._edges: dict[Any, list[dict[Any, Any]]] = {}

    def _validate_nodes_exist(self, *args):
        for node in args:
            if node not in self._edges.keys():
                raise Exception("Vertex does not exist in the graph")

    def add_node(self, v: Any):
        self._edges[v] = []

    def add_edge(self, from_v, to_v, weight=0):
        self._validate_nodes_exist(from_v, to_v)

        self._edges[from_v].append({"vertex": to_v, "weight": weight})
        if not self._directed:
            self._edges[to_v].append({"vertex": from_v, "weight": weight})

    def is_adjacent(self, v1, v2):
        self._validate_nodes_exist(v1, v2)
        if v2 in self._edges[v1]:
            return -1
        elif v1 in self._edges[v2]:
            return 1
        else:
            return 0

    def _min_dist(self, distance, unvisited):
        min = float("inf")
        min_key = None
        for v in unvisited:
            if distance[v] < min:
                min = distance[v]
                min_key = v

        return min_key

    def dfs(self, from_node, to_node) -> bool:
        return self._dfs_rec(from_node, to_node, set())

    def _dfs_rec(self, from_node, to_node, visited) -> bool:

        if from_node == to_node:
            return True

        visited.add(from_node)
        for node in self._edges[from_node]:
            if node not in visited:
                if self._dfs_rec(node, to_node, visited):
                    return True
        return False

    # iterative #
    def _dfs1(self, from_v, to_v, unvisited: list, distance, previous):
        while len(unvisited) > 0:
            u = self._min_dist(distance, unvisited)
            if not u:
                return None
            unvisited.pop(unvisited.index(u))

            for node in self._edges[u]:
                if node["vertex"] in unvisited:
                    alt = distance[u] + node["weight"]
                    if alt < distance[node["vertex"]]:
                        distance[node["vertex"]] = alt
                        previous[node["vertex"]] = u

        return distance[to_v]

    def dfs1(self, from_v, to_v):
        distance = {}
        previous = {}
        unvisited = []
        for node in self._edges:
            distance[node] = float("inf")
            previous[node] = None
            unvisited.append(node)
        distance[from_v] = 0

        return self._dfs1(from_v, to_v, unvisited, distance, previous)

    # end #

    def is_friend_of_friend(self, m1, m2):
        for friend in self._edges[m1]:
            for f in self._edges[friend["vertex"]]:
                if self.is_adjacent(friend["vertex"], m2) == (1 or -1):
                    return True
        return False

    def distance(self, m1, m2):
        self._validate_nodes_exist(m1, m2)
        return self._distance(m1, m2, set(), list())

    def _distance(self, m1, m2, visited, path):
        if m1 == m2:
            if m1 not in path:
                path.append(m1)
            return len(path) - 1

        visited.add(m1)
        path.append(m1)
        for node in self._edges[m1]:
            if node["vertex"] not in visited:
                if self._path(node["vertex"], m2, visited, path):
                    return len(path) - 1
        return float("inf")

    def get_path(self, m1, m2):
        return self._path(m1, m2, set(), list())

    def _path(self, m1, m2, visited, path):
        if m1 == m2:
            if m1 not in path:
                path.append(m1)
            return " -> ".join(path) or None

        visited.add(m1)
        path.append(m1)
        for node in self._edges[m1]:
            if node["vertex"] not in visited:
                if self._path(node["vertex"], m2, visited, path):
                    return " -> ".join(path)
        return None


if __name__ == "__main__":
    # g = Graph(directed=True)
    # for city in (
    #     "Brussels",
    #     "Kyoto",
    #     "Amsterdam",
    #     "Tokyo",
    #     "Tel Aviv",
    #     "Paris",
    #     "London",
    #     "Hong Kong",
    # ):
    #     g.add_node(city)

    # g.add_edge("Brussels", "Tel Aviv", 7)
    # g.add_edge("Brussels", "Tokyo", 5)

    # g.add_edge("Tokyo", "Kyoto", 1)
    # g.add_edge("Tokyo", "Hong Kong", 3)

    # g.add_edge("Paris", "Tel Aviv", 4)
    # g.add_edge("Paris", "London", 2)
    # g.add_edge("Paris", "Amsterdam", 1)

    # g.add_edge("Tel Aviv", "Paris", 2)

    # g.add_edge("Hong Kong", "Tel Aviv", 10)

    # pprint(g._edges)
    # print(f"Path from Brussels to Amsterdam: {g.dfs1('Brussels', 'Amsterdam')}")
    # # brussel -(7)> telaviv -(2)> paris -(1)> amsterdam == 10
    # # brussel -(5)> tokyo -(3)> hongkong -(10)> telaviv -(2)> paris -(1)> amsterdam == 21
    # print(f"Path from Tokyo to Brussels: {g.dfs1('Tokyo', 'Brussels')}")
    # # no path

    # print(f"Path from Tokyo to Brussels: {g.dfs1('Brussels', 'London')}")
    # # brussel -(7)> telaviv -(2)> paris -(2)> london == 11
    # # brussel -(5)> tokyo -(3)> hongkong -(10)> telaviv -(2)> paris -(2)> london == 21

    linkedin = Graph()
    for name in ("David", "Julia", "Nathan", "Ron", "James", "Mor", "Dor", "Jim"):
        linkedin.add_node(name)

    linkedin.add_edge("David", "James")
    linkedin.add_edge("James", "Jim")
    linkedin.add_edge("Jim", "Mor")
    linkedin.add_edge("Jim", "Dor")
    linkedin.add_edge("Mor", "Julia")
    linkedin.add_edge("Mor", "Nathan")
    linkedin.add_edge("Julia", "Ron")

    print(linkedin.is_friend_of_friend("Ron", "David"))
    print(linkedin.get_path("Ron", "David"))
    print(linkedin.distance("Ron", "David"))

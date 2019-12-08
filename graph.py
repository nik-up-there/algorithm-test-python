import numpy as np


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.struct = {}

    def add_node(self, node):
        self.nodes.append(node)
        self.struct[node] = {}

    def add_edge(self, node1, node2, weight=1):
        self.edges.append((node1, node2))
        self.struct[node1][node2] = weight

    def dijkstra(self, start, end):
        # Parameters verification
        if start not in self.nodes or end not in self.nodes:
            raise ValueError

        # Initialisation
        parents = {}
        distances = {}
        for node in self.struct.keys():
            parents[node] = ""
            distances[node] = np.inf
        distances[start] = 0
        to_visit = [start]

        # Dijkstra loop
        while len(to_visit) > 0:
            # Find minimal node
            min_value, min_index = np.inf, -1
            for index, node in enumerate(to_visit):
                if distances[node] < min_value:
                    min_index = index
                    min_value = distances[node]
            current_point = to_visit.pop(min_index)
            # Update parents and distance
            current_distance = distances[current_point]
            for neighbor, distance in self.struct[current_point].items():
                if parents[neighbor] == "":
                    to_visit.append(neighbor)
                new_distance = distance + current_distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parents[neighbor] = current_point

        # Returning the path
        path = [end]
        node = end
        while node != start:
            node = parents[node]
            path.insert(0, node)

        return path

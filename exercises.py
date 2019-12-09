########################################################################################################################
#                                                      IMPORTS
########################################################################################################################
from graph import Graph
# import networkx as nx


########################################################################################################################
#                                                  GLOBAL VARIABLES
########################################################################################################################
MOVES = [("RIGHT", 1, 0), ("LEFT", -1, 0), ("UP", 0, 1), ("DOWN", 0, -1)]


########################################################################################################################
#                                                    EXERCISE Nº1
########################################################################################################################
def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """
    if len(s1) != len(s2):
        return False

    hash_map = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for letter in s1:
        hash_map[letter] += 1

    for letter in s2:
        hash_map[letter] -= 1

    for letter in hash_map.keys():
        if hash_map[letter] != 0:
            return False

    return True


########################################################################################################################
#                                                    EXERCISE Nº2
########################################################################################################################
def preprocess_string(string):
    """
    A function that preprocess the input string to remove all character that are not "(" or ")"
    Not useful here as every tested string are only made with "(" and ")" but we never know ;-)
    :param string: the string to preprocess
    :return: string: the preprocessed string
    """
    new_string = ""
    for x in string:
        if x == "(" or x == ")":
            new_string += x
    return new_string


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """
    string = preprocess_string(string)
    stack = []
    for x in string:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return not stack


########################################################################################################################
#                                                    EXERCISE Nº3
########################################################################################################################
def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """
    # Transform the given maze into a graph object
    # Create graph object
    maze_graph = Graph()
    # Add nodes to the graph
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                maze_graph.add_node((i, j))
    # Add edges to the graph
    for node in maze_graph.nodes:
        i, j = node
        for move in MOVES:
            new_node = (i + move[1], j + move[2])
            if new_node in maze_graph.nodes:
                maze_graph.add_edge(node, new_node)
    # Finding the shortest path using Dijkstra algorithm
    try:
        return maze_graph.dijkstra(start, end)
    except ValueError:
        # Either source or target not in graph nodes
        return False
    except KeyError:
        # No path from source to target
        return False


# def shortest_path_with_library(start, end, maze):
#     """
#     Write an algorithm that finds the shortest path in a maze from start to end
#     The maze is represented by a list of lists containing 0s and 1s:
#     0s are walls, paths cannot go through them
#     The only movements allowed are UP/DOWN/LEFT/RIGHT
#     :param start: tuple (x_start, y_start) - the starting point
#     :param end: tuple (x_end, y_end) - the ending point
#     :param maze: list of lists - the maze
#     :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
#     """
#     # Transform the given maze into a graph object
#     # Create graph object
#     maze_graph = nx.MultiDiGraph()
#     # Add nodes to the graph
#     for i in range(len(maze)):
#         for j in range(len(maze[i])):
#             if maze[i][j] == 1:
#                 maze_graph.add_node((i, j))
#     # Add edges to the graph
#     for node in maze_graph.nodes():
#         i, j = node
#         for move in MOVES:
#             new_node = (i + move[1], j + move[2])
#             if new_node in maze_graph.nodes():
#                 maze_graph.add_edge(node, new_node)
#     # Find the shortest path using Dijkstra algorithm
#     try:
#         path = nx.shortest_path(maze_graph, source=start, target=end, method='dijkstra')
#         return path
#     except nx.exception.NodeNotFound:
#         # Either source or target not in graph nodes
#         return False
#     except nx.exception.NetworkXNoPath:
#         # No path from source to target
#         return False

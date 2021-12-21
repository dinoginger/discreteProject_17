"""
This module contains functions to work with graphs.
Functions are able to analyse graphs' connected components,
strongly connected components, briges and connection points.
"""
import func_strongly_connected
import func_find_bridges
import func_cut_vertices
import func_connected_components
import func_read_write


def read(path: str) -> list:
    """
    Reads graph from file

    Args:
        path (str): path to the file

    Returns:
        list: graph as list of tuples
    """
    return func_read_write.read_graph(path)


def write(path: str, graph: list) -> None:
    """
    Writes graph from list of tuples to file.

    Args:
        path (str): path to file
        graph (list): graph as list of tuples
    """
    return func_read_write.write_graph(path, graph)


def strongly_connected_components(graph: list) -> list:
    """
    Function which uses Tarjan's alogrithm to find
    strongly connected components of the given oriented graph.

    Args:
        graph (list): Directed graph as a list of edges,
        here a list of (int, int) tuples.
    Returns:
        list: list of all the SCC's of the graph, which are also lists.

    >>> strongly_connected_components([("NUMBER OF NODES", "NUMBER OF EDGES"\
    ),(0, 1), (1, 2), (2, 3), (3, 0), (2, 4), (4, 5), (5, 6), (6, 4), (6, 7)])
    [[7], [4, 5, 6], [0, 1, 2, 3]]
    >>> strongly_connected_components([("NUMBER OF NODES", "NUMBER OF EDGES"\
    ), (0, 2), (2, 1), (1, 0), (0, 3), (3, 4)])
    [[4], [3], [0, 1, 2]]
    """
    return func_strongly_connected.find_SCC(graph)


def cut_vertices(graph: list) -> list:
    """
    A function that finds cut vertices in O(n+m)

    Args:
        graph (list): Adjacency matrix of a graph

    Returns:
        list: numbers of points, whose removal disconnects graph

    >>> cut_vertices([("NUMBER OF NODES", "NUMBER OF EDGES"), (1, 4), \
    (2, 4), (2, 3), (3, 4), (3, 6), (3, 8), (6, 5), (6, 7), (5, 7), (3, 7)])
    [3, 4]
    """
    return func_cut_vertices.cut_vertices(graph)


def find_bridges(graph: list) -> list:
    """
    Returns a list containing bridges on given undirected
    graph.

    Args:
        graph (list): list of edges

    Returns:
        list: list of bridges

    >>> find_bridgess([("NUMBER OF NODES", "NUMBER OF EDGES"), (0, 1), (1, \
    2), (2, 3), (3, 4), (3, 5), (5, 1), (2, 6), (6, 7), (7, 8), (6, 8)])
    [(3, 4), (2, 6), (0, 1)]
    >>> find_bridgess([("NUMBER OF NODES", "NUMBER OF EDGES"),(1, 2), \
    (2, 3), (3, 1), (2, 4), (4, 5), (5, 6), (4, 6)])
    [(2, 4)]
    """
    return func_find_bridges.find_bridges(graph)


def connected_components(graph: list) -> list:
    """Returns connected components of undirected graph

    Args:
        graph (list): graph as list of tuples

    Returns:
        list: list of connected components
    >>> connected_components([("NUMBER OF NODES", "NUMBER OF EDGES"), (1, 3\
    ), (2, 3), (3, 5), (5, 6), (5, 4), (7, 8), \
    (7, 9), (14, 12), (12, 11), (12, 13), (11, 13)])
    [[1, 2, 3, 4, 5, 6], [8, 9, 7], [11, 12, 13, 14]]
    """
    return func_connected_components.connected_components(graph)

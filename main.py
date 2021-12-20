"""
This module contains functions to work with graphs.
Functions are able to analyse graphs' connected components,
strongly connected components, briges and connection points.
"""
import strongly_connected
import find_bridges
import func_cut_vertices
import csv


def read_graph(path: str) -> list:
    """Return a graph, read from file,
    as a list of tuples. Each tuple
    represents an edge.

    Args:
        path (str): Path to csv file with graph

    Returns:
        list: Graph, read from file
    """

    graph = list()

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        for line in reader:
            graph.append((int(line[0]), int(line[1])))

    return graph
  
  
def write_graph(path: str, graph: list) -> None:
    """Writes graph represented as
    list of tuples, where tuple is an edge,
    in a csv file.

    Args:
        path (str): Path to csv file
        graph (list): Graph, represented by list
    """

    with open(path, 'w') as file:
        writer = csv.writer(file, delimiter=' ')
        for edge in graph:
            writer.writerow(edge)


def create_adj_matrix(graph: list, directed: bool=False) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (list): Graph as a list of edges
        directed (bool): Sets if the graph is directed or not

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()

    for node1, node2 in graph:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)

        if not directed:
            if node2 not in adj_matrix:
                adj_matrix[node2] = {node1}
            else:
                adj_matrix[node2].add(node1)

    return adj_matrix


def dfs(graph: dict, start: int) -> set:
    """Return a sequence of nodes after dfs.

    Args:
        graph (dict): Adjacency matrix of a graph
        start (int): Starting node

    Returns:
        set: Nodes visited after dfs
    """

    stack, visited = [start], set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        for neighbour in graph[node]:
            stack.append(neighbour)

        visited.add(node)

    return visited


def connected_components(graph: list) -> list:
    """Return a list containing connected components.
    Connected component is identified by the node with least number
    that belongs to a the component.

    Args:
        graph (list): Graph as a list of edges

    Returns:
        list: Connected components
    """

    matrix_graph = create_adj_matrix(graph[1:])
    nodesleft = set(matrix_graph.keys())
    components = []

    while nodesleft:
        con_component = dfs(matrix_graph, nodesleft.pop())
        nodesleft.difference_update(con_component)
        components.append(list(con_component))

    return components


def strongly_connected_components(graph):
    """
    Documentation here
    """
    return strongly_connected.find_SCC(graph)


def cut_vertices(graph):
    """
    Documentation here.
    """
    return func_cut_vertices.cut_vertices(graph)


def bridges(graph):
    """
    Documentation here
    """
    return find_bridges.find_bridges(graph)




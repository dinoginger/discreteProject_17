"""
This module contains functions required to find bridges
"""


def create_adj_matrix(graph: list, directed: bool = False) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (list): Graph as a list of edges
        directed (bool): Sets if the graph is directed or not

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()

    for node1, node2 in graph[1:]:
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


def rec_find_bridges(graph_dict: dict, vertices: list, u: int, visited: list,
                     parent: list, low: list, disc: list,
                     time: int, bridges: list) -> list:
    """Helping recursive function for find_bridges that checks if
    edge is a bridge and adds it to a list.

    Args:
        graph_dict (dict): matrix of graph as a dict
        vertices (list): list of vertices
        u (int): vertice
        visited (list): list of bool of the vertice
        parent (list): list of vertices(parents)
        low (list): list of numbers
        disc (list): list of numbers
        time (int): time of discovery
        bridges (list): list of bridges as tuples

    Returns:
        List: list of bridges as tuples
    """

    idx = vertices.index(u)
    visited[idx] = True
    disc[idx] = time
    low[idx] = time
    time += 1

    for ver in graph_dict[u]: # iter for each connected vertex
        idx_1 = vertices.index(ver)
        if visited[idx_1] is False: 
            parent[idx_1] = u
            rec_find_bridges(graph_dict, vertices, ver, visited, # recur for each unvisited vertex
                             parent, low, disc, time, bridges)
            low[idx] = min(low[idx], low[idx_1]) # set the lowest possible low for vertex
            if low[idx_1] > disc[idx]: # check whether an edge is a bridge
                bridge = (u, ver)
                bridges.append(bridge)
        elif ver != parent[idx]:
            low[idx] = min(low[idx], disc[idx_1]) # set lowest low if vertex has a back edge

    return bridges


def find_bridges(graph: list) -> list:
    """Returns a list containing bridges

    Args:
        graph (list): list of edges

    Returns:
        list: list of bridges
    """

    graph_dict = create_adj_matrix(graph) # dictionary of adjacency matrix
    vertices = list(graph_dict.keys()) # list of vertices
    vertices_num = len(graph_dict) # quantity of vertices
    bridges = [] # list of bridges in graph
    time = 0 
    visited = [False] * vertices_num # list which tells whether vertex is visited or not
    disc = [0] * vertices_num # list which indicates when vetex was discovered 
    low = [0] * vertices_num # list of disc of lowest vertex that can be visited in subtree
    parent = [0] * vertices_num # list of parent vertices for each vertex

    for i in graph_dict:
        if visited[vertices.index(i)] is False: #recur for each unvisited vertex
            return rec_find_bridges(graph_dict, vertices, i, visited, parent,
                                    low, disc, time, bridges)

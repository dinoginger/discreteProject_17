"""
Module for findning cut vertices by Roman Mutel
"""


def create_adj_matrix(graph: list) -> dict:
    """Return adjacency matrix of a graph,
    given the list of it's edges.

    Args:
        graph (list): Graph as a list of edges

    Returns:
        dict: Adjacency matrix
    """

    adj_matrix = dict()


    for node1, node2 in graph[1:]:
        if node1 not in adj_matrix:
            adj_matrix[node1] = {node2}
        else:
            adj_matrix[node1].add(node2)

        if node2 not in adj_matrix:
            adj_matrix[node2] = {node1}
        else:
            adj_matrix[node2].add(node1)

    return adj_matrix


def cut_vertices(graph: list):
    """
    A function that finds cut vertices in O(n+m)

    Args:
        graph (list): Adjacency matrix of a graph

    Returns:
        list: numbers of points, whose removal disconnects graph
    """
    graph = create_adj_matrix(graph)

    def cut_vertices_dfs(vertex: int, root, d, h,
                         used, order, graph: dict, cut_v):
        """
        Helper function for cut_vertices
        """

        used[vertex] = 1
        d[vertex] = h[vertex] = order
        children = 0

        for u in graph[vertex]:
            if u == root:
                continue
            elif used[u]:
                # коли ребро зворотнє
                h[vertex] = min(h[vertex], d[u])
            else:
                # коли ребро пряме
                cut_vertices_dfs(u, vertex, d, h, used,
                                 order + 1, graph, cut_v)
                h[vertex] = min(h[vertex], h[u])
                children += 1
                if h[u] >= d[vertex] and root != -1:
                    cut_v[vertex] = 1

        # спеціальний випадок, якщо вершина є коренем (якщо root == -1)
        if root == -1 and children > 1:
            cut_v[vertex] = 1

    n = len(graph.keys()) + 1
    used, d, h, cut_v = [0] * n, [0] * n, [0] * n, [0] * n
    for i in range(1, n):
        if i in graph.keys():
            cut_vertices_dfs(i, -1, d, h, used, 1, graph, cut_v)
            break

    cut_v_names = []
    for i in range(n):
        if cut_v[i]:
            cut_v_names.append(i)

    return cut_v_names

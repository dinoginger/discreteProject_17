"""
module documentation here
"""

import csv
# from random import randint
# import time


# def generate_file(path):
#     with open(path, 'w') as file:
#         for i in range(100000):
#             file.write(str(randint(1, 1000))+','+str(randint(1, 1000))+'\n')


def read_graph(path: str) -> set:
    """Return a graph, read from file,
    as a set of tuples. Each tuple
    represents an edge.

    Args:
        path (str): Path to csv file with graph

    Returns:
        set: Graph, read from file
    """

    graph = set()
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            graph.add((int(line[0]), int(line[1])))

    return graph


def write_graph(path: str, graph: set) -> None:
    """Writes graph represented as
    set of tuples, where tuple is an edge,
    in a csv file.

    Args:
        path (str): Path to csv file
        graph (set): Graph, represented by set
    """

    with open(path, 'w') as file:
        writer = csv.writer(file)
        for edge in graph:
            writer.writerow(edge)


def connected_components():
    """
    Documentation here
    """
    pass


def strongly_connected_components():
    """
    Documentation here
    """
    pass


def connection_points():
    """
    Documentation here
    """
    pass


def bridges():
    """
    Documentation here
    """
    pass


if __name__ == "__main__":
    # start = time.perf_counter()
    # generate_file('existing.csv')
    # write_graph('new.csv', read_graph('existing.csv'))
    # print(time.perf_counter()-start)
    pass

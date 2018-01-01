import networkx as nx
import matplotlib.pyplot as plt


def digit_sum(number, base):
    """
    Takes a number and its associated base and calculated the digit sum (quersumme) of the number
    :param number: number
    :param base: number base
    :return: digit sum
    """
    n = number
    q = 0

    while n > 0:
        q += n % base
        n //= base

    return q


class VortexGraph:
    """
    Holds a vortex graph to display the symmetry of numbers in any base
    """
    graph = None
    base = None
    layout = None

    def __init__(self, base=10):
        # Init graph
        self.base = base
        self.graph = nx.DiGraph()
        nodes = reversed(range(1, base, 1))
        self.graph.add_nodes_from(nodes)
        # self.layout = nx.circular_layout(self.graph)
        self.layout = nx.shell_layout(self.graph)

    def add_node(self, node):
        """
        Adds a node to the graph
        :param node: Node to add
        """
        self.graph.add_node(node)

    def connect_nodes(self):
        """Initiates recursive connecting of nodes"""
        for node in self.graph.nodes():
            self._recursive_connect(node)

    def _recursive_connect(self, node):
        """
        Recursively connect the nodes, internal function
        :param node: Current node to work with
        """
        next_node = node + node
        # If node number exceeds base
        while next_node >= self.base:
            # calculate digit sum depending on base
            next_node = digit_sum(next_node, self.base)

        print('( ' + str(node) + ' -> ' + str(next_node) + ' )')

        # Done if edge exists
        if self.graph.has_edge(node, next_node):
            return

        # Otherwise set edge
        self.graph.add_edge(node, next_node)
        # and continue recursive connect
        self._recursive_connect(next_node)

    def draw_graph(self):
        """
        Draw graph
        """
        nx.draw(self.graph, pos=self.layout, with_labels=True, node_color='orange', node_size=600, edge_color='black', linewidths=1, font_size=15)
        plt.show()

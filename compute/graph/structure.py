class Graph:

    def __init__(self):
        self.nodes = []
        self.firstNode = None
        self.previousNode = None        

    def add(self, node):

        if None == self.firstNode:
            self.firstNode = node

        if None != self.previousNode:
            self.previousNode.add(Synapse().add(node))

        self.previousNode = node
        self.nodes.append(node)
        return node

    def connect(self, subgraph):
        self.add(subgraph.first())

    def first(self):
        return self.firstNode

    def write(self, data):
        self.firstNode.write(data)

class Node:

    def __init__(self):
        self.__arguments = []
        self.__synapses = []

    def add(self, synapse):
        self.__synapses.append(synapse)
        return self

    def arguments(self, value):
        self.__arguments = value

    def read(self):
        result = self.__arguments
        self.__arguments = []
        return result

    def write(self, data):
        if None != data:
            self.__arguments += data

    def initialize(self):
        return

    def activate(self):
        self.process()
        data = self.read()
        if None != data:
            for i in range(len(self.__synapses)):
                synapse = self.__synapses[i]
                synapse.write(data)
    
    def process(self):
        return
    
    def synapses(self):
        return self.__synapses
        
class Synapse:

    __node: None

    def add(self, node):
        self.__node = node
        return self

    def node(self):
        return self.__node
    
    def write(self, data):
        self.__node.write(data)

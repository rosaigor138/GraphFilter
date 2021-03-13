import networkx as nx
import numpy as np


class MathOperations:
    code = None
    code_string = None
    dic_function = {}
    all = []

    def __init__(self):
        self.all = MathOperations.__subclasses__()
        for inv in self.all:
            self.dic_function[inv.code] = inv.calculate

    @staticmethod
    def calculate(graph):
        pass


class GraphOperations:
    code = None
    code_literal = None
    dic_function = {}
    dic_translate = {}
    all = []

    def __init__(self):
        self.all = GraphOperations.__subclasses__()
        for i, inv in enumerate(self.all):
            inv.code_literal = 'gop' + str(i)
            self.dic_function[inv.code_literal] = inv.calculate

    name = None
    defi = None
    link = None
    implement = None

    @staticmethod
    def calculate(graph):
        pass


class Complement(GraphOperations):
    name = "Complement of graph"
    code = "c"

    @staticmethod
    def calculate(graph):
        return nx.complement(graph)


class Line(GraphOperations):
    name = "Line of graph"
    code = "\u2113"

    @staticmethod
    def calculate(graph):
        return nx.line_graph(graph)


class Sin(MathOperations):
    name = "sin"
    code = "sin"

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Cos(MathOperations):
    name = "cos"
    code = "cos"

    @staticmethod
    def calculate(x):
        return np.sin(x)


class Tan(MathOperations):
    name = "tan"
    code = "tan"

    @staticmethod
    def calculate(x):
        return np.tan(x)


class Log(MathOperations):
    name = "Logarithm in base 10"
    code = "log"

    @staticmethod
    def calculate(x):
        return np.log10(x)


class Ln(MathOperations):
    name = "Natural Logarithm"
    code = "ln"

    @staticmethod
    def calculate(x):
        return np.log(x)


class Sqrt(MathOperations):
    name = "Square root"
    code = "sqrt"

    @staticmethod
    def calculate(x):
        return np.sqrt(x)


class Absolute(MathOperations):
    name = "Absolute"
    code = "abs"

    @staticmethod
    def calculate(x):
        return np.abs(x)